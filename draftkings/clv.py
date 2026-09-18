#!/usr/bin/env python3
"""Closing line value (CLV) tracker.

Fetches fresh DraftKings + Pinnacle lines, then for every ticket leg in draftkings/card.json whose game
kicks off within the window (default: 15 minutes ago to 75 minutes ahead; --all grades every ungraded leg)
records the DraftKings closing number and computes:
  point_clv  : points gained vs the close (positive = we got the better number)
  price_clv  : closing implied probability minus our implied probability (positive = we beat the close)
  clv        : price_clv + 0.04 * point_clv  (a half point is worth about 2 probability points on average)
  pin_clv    : Pinnacle no-vig closing probability minus our implied probability (the sharpest yardstick)
Writes the results back into card.json (leg.close, leg.clv, ticket.clv) and appends to draftkings/clv-log.json.
Usage: python3 draftkings/clv.py [--all] [--dry-run]
"""
import json, subprocess, sys, datetime, pathlib, statistics

here = pathlib.Path(__file__).parent
ALL = "--all" in sys.argv; DRY = "--dry-run" in sys.argv
r = subprocess.run([sys.executable, str(here / "fetch_dk_lines.py")], capture_output=True, text=True)
if not r.stdout.startswith("VERIFIED"):
    print("CLV: could not fetch closing lines:", r.stdout.strip().splitlines()[0] if r.stdout.strip() else r.stderr.strip()[:200]); sys.exit(1)
lines = json.loads((here / "lines" / "latest.json").read_text())
card = json.loads((here / "card.json").read_text())
now = datetime.datetime.now(datetime.timezone.utc)

def implied(price):
    return 100 / (price + 100) if price > 0 else -price / (-price + 100)
def find_game(leg):
    for g in lines["games"]:
        if leg.get("home") == g["home"] and leg.get("away") == g["away"]:
            return g
    return None

log = json.loads((here / "clv-log.json").read_text()) if (here / "clv-log.json").exists() else []
graded, rows = 0, []
for t in card["tickets"]:
    legs = t.get("legs") or []
    if not legs:
        continue
    for leg in legs:
        if leg.get("clv") is not None or not leg.get("market"):
            continue
        g = find_game(leg)
        if not g:
            rows.append((t["id"], leg.get("label", "?"), "game not found in feed")); continue
        ko = datetime.datetime.fromisoformat(g["commence_time"].replace("Z", "+00:00"))
        mins = (ko - now).total_seconds() / 60
        if not ALL and not (-15 <= mins <= 75):
            continue
        mkt, side = leg["market"], leg["side"]
        dk = g["dk"].get(mkt, {}).get(side); pin = g["pinnacle"].get(mkt, {}).get(side)
        if not dk:
            rows.append((t["id"], leg.get("label", "?"), "no DK close for this side")); continue
        point_clv = 0.0
        if mkt == "spreads":
            point_clv = (leg["point"] - dk["point"])
        elif mkt == "totals":
            point_clv = (leg["point"] - dk["point"]) if side == "Under" else (dk["point"] - leg["point"])
        price_clv = round(implied(dk["price"]) - implied(leg["price"]), 4)
        clv = round(price_clv + 0.04 * point_clv, 4)
        pin_clv = round(pin["fair_prob"] - implied(leg["price"]), 4) if pin else None
        leg["close"] = {"point": dk.get("point"), "price": dk["price"], "pin_fair_prob": pin["fair_prob"] if pin else None,
                        "at": now.strftime("%Y-%m-%dT%H:%MZ")}
        leg["point_clv"], leg["price_clv"], leg["clv"], leg["pin_clv"] = point_clv, price_clv, clv, pin_clv
        log.append({"week": card.get("week"), "ticket": t["id"], "label": leg.get("label"), "market": mkt, "side": side,
                    "bet_point": leg.get("point"), "bet_price": leg["price"], "close_point": dk.get("point"), "close_price": dk["price"],
                    "point_clv": point_clv, "price_clv": price_clv, "clv": clv, "pin_clv": pin_clv, "at": leg["close"]["at"]})
        rows.append((t["id"], leg.get("label", "?"), f"bet {leg.get('point', '')} {leg['price']:+d} | close {dk.get('point', '')} {dk['price']:+d} | CLV {clv:+.3f} | vs Pinnacle {pin_clv if pin_clv is None else format(pin_clv, '+.3f')}"))
        graded += 1
    done = [l["clv"] for l in legs if l.get("clv") is not None]
    if done and len(done) == len(legs):
        t["clv"] = round(statistics.mean(done), 4)

wk = [t["clv"] for t in card["tickets"] if t.get("clv") is not None]
card.setdefault("season", {})["clv_week"] = round(statistics.mean(wk), 4) if wk else None
allc = [e["clv"] for e in log if e.get("clv") is not None]
card["season"]["clv_season"] = round(statistics.mean(allc), 4) if allc else None
card["clv_updated_at"] = now.strftime("%Y-%m-%dT%H:%MZ")
if not DRY:
    (here / "card.json").write_text(json.dumps(card, indent=1))
    (here / "clv-log.json").write_text(json.dumps(log, indent=1))
print(f"CLV run {now.strftime('%Y-%m-%d %H:%M UTC')}: graded {graded} leg(s){' (dry run)' if DRY else ''}. Week avg CLV: {card['season']['clv_week']}. Season avg CLV: {card['season']['clv_season']}.")
for rrow in rows:
    print(" | ".join(str(x) for x in rrow))
