#!/usr/bin/env python3
"""Fetch DraftKings NFL lines via The Odds API and print a markdown table.

Requires:
  ODDS_API_KEY  environment variable (free key from https://the-odds-api.com)
  api.the-odds-api.com allowed in the environment's network policy

Usage:
  python3 draftkings/fetch_dk_lines.py            # markdown table to stdout, JSON to draftkings/lines/latest.json
  python3 draftkings/fetch_dk_lines.py --book fanduel   # another book for line shopping
"""
import json, os, sys, time, urllib.request, urllib.parse, datetime, pathlib

book = "draftkings"
if "--book" in sys.argv:
    book = sys.argv[sys.argv.index("--book") + 1]
key = os.environ.get("ODDS_API_KEY", "").strip()
if not key:
    print("UNVERIFIED: ODDS_API_KEY is not set. Fall back to screenshot protocol.")
    sys.exit(2)

params = {
    "regions": "us", "markets": "h2h,spreads,totals", "bookmakers": book,
    "oddsFormat": "american", "dateFormat": "iso", "apiKey": key,
}
url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?" + urllib.parse.urlencode(params)
req = urllib.request.Request(url, headers={"User-Agent": "dk-picks/1.0"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
        remaining = r.headers.get("x-requests-remaining")
except Exception as e:
    print(f"UNVERIFIED: fetch failed ({e}). Fall back to screenshot protocol.")
    sys.exit(1)

fetched = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
out = pathlib.Path(__file__).parent / "lines"
out.mkdir(exist_ok=True)
(out / "latest.json").write_text(json.dumps({"fetched_utc": fetched, "book": book, "events": data}, indent=1))

def fmt(p):
    return f"{p:+d}" if isinstance(p, int) else str(p)

print(f"VERIFIED {book.upper()} NFL lines via The Odds API, fetched {fetched}. Requests remaining this month: {remaining}\n")
print("| Kickoff (ET) | Game | Spread | Total | Moneyline |")
print("|---|---|---|---|---|")
et = datetime.timezone(datetime.timedelta(hours=-4))  # EDT; switch to -5 after Nov 1
for ev in data:
    home, away = ev["home_team"], ev["away_team"]
    ko = datetime.datetime.fromisoformat(ev["commence_time"].replace("Z", "+00:00")).astimezone(et).strftime("%a %m/%d %I:%M %p")
    spread = total = ml = "n/a"
    for bm in ev.get("bookmakers", []):
        if bm["key"] != book:
            continue
        for m in bm["markets"]:
            o = {x["name"]: x for x in m["outcomes"]}
            if m["key"] == "spreads" and away in o and home in o:
                spread = f"{away} {o[away]['point']:+g} ({fmt(o[away]['price'])}) / {home} {o[home]['point']:+g} ({fmt(o[home]['price'])})"
            elif m["key"] == "totals" and "Over" in o:
                total = f"{o['Over']['point']:g} (O {fmt(o['Over']['price'])} / U {fmt(o['Under']['price'])})"
            elif m["key"] == "h2h" and away in o and home in o:
                ml = f"{away} {fmt(o[away]['price'])} / {home} {fmt(o[home]['price'])}"
    print(f"| {ko} | {away} at {home} | {spread} | {total} | {ml} |")
