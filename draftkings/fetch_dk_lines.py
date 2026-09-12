#!/usr/bin/env python3
"""Fetch NFL lines via The Odds API: DraftKings plus Pinnacle (the sharp reference) in one call.

Prints (1) the DraftKings board, (2) an "edge vs Pinnacle" table: for every DraftKings side, the
no-vig Pinnacle fair probability minus DraftKings' implied probability, and any half-point gap.
Writes draftkings/lines/latest.json with both books and the computed edges.

Requires ODDS_API_KEY in the environment and api.the-odds-api.com allowed by the network policy.
Usage: python3 draftkings/fetch_dk_lines.py [--book fanduel]   (the named book replaces DraftKings)
"""
import json, os, sys, urllib.request, urllib.parse, datetime, pathlib
from zoneinfo import ZoneInfo

book = "draftkings"
if "--book" in sys.argv:
    book = sys.argv[sys.argv.index("--book") + 1]
key = os.environ.get("ODDS_API_KEY", "").strip()
if not key:
    print("UNVERIFIED: ODDS_API_KEY is not set. Fall back to screenshot protocol.")
    sys.exit(2)

params = {"regions": "us,eu", "markets": "h2h,spreads,totals", "bookmakers": f"{book},pinnacle",
          "oddsFormat": "american", "dateFormat": "iso", "apiKey": key}
url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?" + urllib.parse.urlencode(params)
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "dk-picks/1.1"}), timeout=30) as r:
        data = json.loads(r.read().decode()); remaining = r.headers.get("x-requests-remaining")
except Exception as e:
    print(f"UNVERIFIED: fetch failed ({str(e).replace(key, 'REDACTED')}). Fall back to screenshot protocol.")
    sys.exit(1)

def implied(price):
    return 100 / (price + 100) if price > 0 else -price / (-price + 100)
def american(prob):
    return round(-100 * prob / (1 - prob)) if prob >= 0.5 else round(100 * (1 - prob) / prob)
def fmt(p):
    return f"{p:+d}"

et = ZoneInfo("America/New_York")
fetched = datetime.datetime.now(datetime.timezone.utc)
games, edges = [], []
for ev in data:
    home, away = ev["home_team"], ev["away_team"]
    ko = datetime.datetime.fromisoformat(ev["commence_time"].replace("Z", "+00:00"))
    books = {bm["key"]: {m["key"]: {o["name"]: o for o in m["outcomes"]} for m in bm["markets"]} for bm in ev.get("bookmakers", [])}
    dk, pin = books.get(book, {}), books.get("pinnacle", {})
    g = {"id": ev["id"], "commence_time": ev["commence_time"], "kickoff_et": ko.astimezone(et).strftime("%a %m/%d %I:%M %p"),
         "home": home, "away": away, "dk": {}, "pinnacle": {}, "edges": []}
    for mkt, sides in (("spreads", (away, home)), ("totals", ("Over", "Under")), ("h2h", (away, home))):
        d, p = dk.get(mkt), pin.get(mkt)
        if d and all(s in d for s in sides):
            g["dk"][mkt] = {s: {"point": d[s].get("point"), "price": d[s]["price"]} for s in sides}
        if p and all(s in p for s in sides):
            p1, p2 = implied(p[sides[0]]["price"]), implied(p[sides[1]]["price"])
            g["pinnacle"][mkt] = {s: {"point": p[s].get("point"), "price": p[s]["price"], "fair_prob": round(pr / (p1 + p2), 4)}
                                  for s, pr in zip(sides, (p1, p2))}
        if mkt in g["dk"] and mkt in g["pinnacle"]:
            for s in sides:
                dkp, pp = g["dk"][mkt][s], g["pinnacle"][mkt][s]
                point_gap = None
                if mkt != "h2h" and dkp["point"] is not None and pp["point"] is not None:
                    # positive = DK gives this side more points (spread) or a friendlier number (totals)
                    point_gap = (dkp["point"] - pp["point"]) if mkt == "spreads" else ((pp["point"] - dkp["point"]) if s == "Over" else (dkp["point"] - pp["point"]))
                prob_edge = round(pp["fair_prob"] - implied(dkp["price"]), 4)
                # combined edge folds a half point in at ~2 percentage points (more on 3 and 7, less elsewhere; this is the average)
                combined = round(prob_edge + 0.02 * (point_gap or 0) * 2, 4)
                e = {"market": mkt, "side": s, "dk_point": dkp["point"], "dk_price": dkp["price"], "dk_implied": round(implied(dkp["price"]), 4),
                     "pin_point": pp["point"], "pin_fair_price": american(pp["fair_prob"]), "pin_fair_prob": pp["fair_prob"],
                     "prob_edge": prob_edge, "point_gap": point_gap, "combined_edge": combined}
                g["edges"].append(e); edges.append((g, e))
    games.append(g)

out = pathlib.Path(__file__).parent / "lines"; out.mkdir(exist_ok=True)
(out / "latest.json").write_text(json.dumps({"fetched_utc": fetched.strftime("%Y-%m-%d %H:%M UTC"), "book": book, "games": games}, indent=1))

print(f"VERIFIED {book.upper()} NFL lines via The Odds API, fetched {fetched.strftime('%Y-%m-%d %H:%M UTC')}. Requests remaining this month: {remaining}\n")
print("| Kickoff (ET) | Game | Spread | Total | Moneyline |\n|---|---|---|---|---|")
for g in games:
    d = g["dk"]; a, h = g["away"], g["home"]
    sp = f"{a} {d['spreads'][a]['point']:+g} ({fmt(d['spreads'][a]['price'])}) / {h} {d['spreads'][h]['point']:+g} ({fmt(d['spreads'][h]['price'])})" if "spreads" in d else "n/a"
    to = f"{d['totals']['Over']['point']:g} (O {fmt(d['totals']['Over']['price'])} / U {fmt(d['totals']['Under']['price'])})" if "totals" in d else "n/a"
    ml = f"{a} {fmt(d['h2h'][a]['price'])} / {h} {fmt(d['h2h'][h]['price'])}" if "h2h" in d else "n/a"
    print(f"| {g['kickoff_et']} | {a} at {h} | {sp} | {to} | {ml} |")

print(f"\nEDGE VS PINNACLE (no-vig). Pinnacle fair prob is the sharpest public estimate of the true probability. Combined edge = (Pinnacle fair prob - {book} implied prob) + half-point gaps at about 2 points each; positive means {book} is better than fair.")
print("Rules: (A) combined_edge >= +0.015 qualifies on price alone, take these first. (B) Otherwise a leg needs your own estimate above the DK implied prob AND within 6 points of Pinnacle fair prob, or a documented reason the market has not priced (QB change, weather, late injury). Never bet a leg with combined_edge below -0.05.")
print("| Kickoff (ET) | Game | Side | DK | DK implied | Pinnacle fair | Point gap | Combined edge |\n|---|---|---|---|---|---|---|---|")
ranked = sorted(edges, key=lambda ge: ge[1]["combined_edge"], reverse=True)
shown = 0
for g, e in ranked:
    if e["combined_edge"] < -0.02: continue
    pt = f"{e['dk_point']:+g}" if e["market"] == "spreads" else (f"{e['dk_point']:g}" if e["market"] == "totals" else "")
    pinpt = (' @ ' + (format(e['pin_point'], '+g') if e['market']=='spreads' else format(e['pin_point'], 'g'))) if e['pin_point'] is not None else ''
    print(f"| {g['kickoff_et']} | {g['away']} at {g['home']} | {e['side']} {pt} | {fmt(e['dk_price'])} | {e['dk_implied']:.3f} | {fmt(e['pin_fair_price'])} ({e['pin_fair_prob']:.3f}){pinpt} | {('%+g' % e['point_gap']) if e['point_gap'] is not None else ''} | {e['combined_edge']:+.3f} |")
    shown += 1
    if shown >= 30: break
if not shown: print("| (no side with a positive edge right now) | | | | | | |")
