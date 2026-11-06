#!/usr/bin/env python3
"""Line movement since the opening snapshot.

Compares draftkings/lines/latest.json against an opening snapshot (default: the newest
draftkings/lines/open-week-*.json) and prints every DraftKings spread, total, and moneyline
that moved, with Pinnacle's move alongside. Positive "move" on a spread means the listed
side is now getting MORE points (the market moved toward the other side).
Usage: python3 draftkings/moves.py [open-snapshot.json] [--min 0.5]
"""
import json, sys, glob, pathlib

here = pathlib.Path(__file__).parent
min_move = 0.0
argv = sys.argv[1:]
if "--min" in argv:
    i = argv.index("--min"); min_move = float(argv[i + 1]); del argv[i:i + 2]
args = [a for a in argv if not a.startswith("--")]
if args:
    open_path = pathlib.Path(args[0])
else:
    snaps = sorted(glob.glob(str(here / "lines" / "open-week-*.json")))
    if not snaps:
        print("MOVES: no opening snapshot found (run fetch_dk_lines.py --snapshot open-week-NN on Tuesday)."); sys.exit(2)
    open_path = pathlib.Path(snaps[-1])
opened = json.loads(open_path.read_text()); latest = json.loads((here / "lines" / "latest.json").read_text())
by_id = {g["id"]: g for g in opened["games"]}

def implied(price):
    return 100 / (price + 100) if price > 0 else -price / (-price + 100)
def fmt_side(mkt, pt, price):
    if mkt == "h2h": return f"{price:+d}"
    return f"{pt:+g} ({price:+d})" if mkt == "spreads" else f"{pt:g} ({price:+d})"

rows = []
for g in latest["games"]:
    o = by_id.get(g["id"])
    if not o: continue
    for mkt in ("spreads", "totals", "h2h"):
        if mkt not in g["dk"] or mkt not in o["dk"]: continue
        for side in g["dk"][mkt]:
            now, was = g["dk"][mkt][side], o["dk"][mkt].get(side)
            if not was: continue
            if mkt == "h2h":
                move = round(implied(was["price"]) - implied(now["price"]), 3)  # positive = price got better for this side
                size = abs(move) * 10
            else:
                move = round(now["point"] - was["point"], 1)
                if mkt == "totals" and side == "Over": move = -move  # positive = friendlier number for this side
                size = abs(move)
                if move == 0 and now["price"] != was["price"]:
                    move_price = round(implied(was["price"]) - implied(now["price"]), 3)
                    size = abs(move_price) * 10; move = move_price
            pin_now = g["pinnacle"].get(mkt, {}).get(side); pin_was = o["pinnacle"].get(mkt, {}).get(side)
            pin = ""
            if pin_now and pin_was:
                pin = f"{fmt_side(mkt, pin_was.get('point'), pin_was['price'])} -> {fmt_side(mkt, pin_now.get('point'), pin_now['price'])}"
            if size >= min_move and move != 0:
                rows.append((size, g["kickoff_et"], f"{g['away']} at {g['home']}", mkt, side,
                             fmt_side(mkt, was.get("point"), was["price"]), fmt_side(mkt, now.get("point"), now["price"]), move, pin))

rows.sort(key=lambda r: -r[0])
print(f"LINE MOVES since {opened['fetched_utc']} (open) -> {latest['fetched_utc']} (now). Positive move = friendlier number or price for the listed side.")
print("| Kickoff (ET) | Game | Market | Side | Open | Now | Move | Pinnacle open -> now |\n|---|---|---|---|---|---|---|---|")
for r in rows:
    mv = f"{r[7]:+g}" if r[3] != "h2h" and isinstance(r[7], float) and abs(r[7]) >= 0.5 else f"{r[7]:+.3f} prob"
    print(f"| {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {mv} | {r[8]} |")
if not rows: print("| (no moves) | | | | | | | |")
