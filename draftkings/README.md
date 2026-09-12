# DraftKings NFL Picks Log

Weekly research cards and results for Luke's DraftKings NFL plays.
One file per week: `2026-week-NN.md`. Each file has the card (parlays, leans, watch list)
and a **Results** section filled in after the games.

## Cadence (America/New_York)

| Update   | When              | Covers                                   |
|----------|-------------------|------------------------------------------|
| Sunday   | 11:00 AM ET       | Final Sunday card after Saturday news    |
| Monday   | 5:00 PM ET        | Monday Night Football                    |
| Thursday | 5:00 PM ET        | Thursday Night Football (next week)      |

Each update is produced by a scheduled Claude routine that researches lines, injuries,
weather, and betting splits, then rewrites the week's file and pushes it here.

## Method (Luke's standing instruction: own analysis, not consensus)

1. Price the leg, not the story. A leg makes the card only if the estimated win rate beats the
   breakeven implied by the price (52.4 percent at -110). State the estimate on every ticket.
2. Shop the number. Compare DraftKings to the market. A point off consensus through a key number
   (3, 7, 10) is the edge.
3. Respect situational history (early-season big dogs, big favorites covering under 50 percent,
   unders with backup QBs and weather, short-week unders) but regress it.
4. Put parlay money where DK's hold is smallest: spreads, totals, moneylines in cross-game parlays.
   Props and same game parlays get at most one quarter-unit ticket per card.
5. Correlate on purpose (dog plus under, favorite plus over).
6. Fade the crowd where it is loudest (80 percent plus of tickets on one side).
7. Every ticket gets a kill switch: the line or inactive that turns it off.

## Unit sizing

- Luke's weekly budget is exactly $100, spent in full every week. 1u = $20.
- Standing split: Thursday $15, Sunday $70, Monday $15. If a kill switch removes a ticket, move that money
  to the next-best ticket on the same day so the week still spends $100. Never carry forward, never add after a loss.
- Every card shows one dollar amount per ticket, not columns.
- Everything is structured for DraftKings only: DK lines, DK parlay and Same Game Parlay mechanics, DK promos.
- Core plays: 1u. Parlays: 0.5u. Long shots and TD ladders: 0.25u.
- Weekly total: $100 exactly. No chasing after a losing Sunday.

## Grading

Results are graded against the line at the time the card was written.
Track: record by ticket type (core, parlay, long shot) and net units.

## Line verification (added after the Week 1 screenshot check)

This environment cannot reach DraftKings or any live odds site. Search-engine summaries are hours to days
stale and were wrong by a full point on two Week 1 games. Rules:
1. A line is VERIFIED only if it comes from a DraftKings screenshot Luke sent, or from a live odds source the
   environment can actually fetch (The Odds API since Sep 12, 2026; see below).
2. Every other line is labeled UNVERIFIED and must carry the threshold Luke applies in the app before placing.
3. Never present a search-sourced line as DK's line. Say "DK line as of <source time>, verify in app".
4. Durable fix: allow sportsbook.draftkings.com (or site.api.espn.com) in the environment's network policy at
   claude.ai/code environment settings. Then the routines can pull live lines.

## Live DraftKings lines (The Odds API)

`draftkings/fetch_dk_lines.py` pulls DraftKings' exact NFL spreads, totals, and moneylines from The Odds API
(licensed aggregator, free tier 500 requests per month, bookmaker key `draftkings`). Every routine runs it first.
If it prints VERIFIED, those lines are the source of truth. If it prints UNVERIFIED, fall back to Luke's screenshots.

One-time setup (Luke):
1. Create a free account at https://the-odds-api.com and copy the API key.
2. In the Claude Code environment settings: add `api.the-odds-api.com` to Allowed domains, and add an
   environment variable `ODDS_API_KEY` with the key.
3. Start a new session or wait for the next routine. Running sessions do not pick up the change.

## Pushing from routine sessions

Routine-fired sessions can read the repo but have no push credential of their own. `draftkings/push.sh`
pushes the current branch using a `GITHUB_TOKEN` environment variable when one is set (fine-grained
personal access token, Contents: read and write, this repo only), and falls back to a plain push otherwise.
Setup (Luke): create the token at github.com > Settings > Developer settings > Fine-grained tokens, then add
it in the Claude Code environment settings as an environment variable named GITHUB_TOKEN.

## Dashboard (phone view)

`draftkings/dashboard/index.html` is a mobile-first page that renders `draftkings/card.json` (fetched live from the
picks branch, with the last card bundled as a fallback). Every routine writes `card.json` alongside the week's
markdown, so the dashboard updates itself on every run. Hosted through GitHub Pages at
`/draftkings/dashboard/` once that folder is on the Pages branch. Add it to the phone home screen for an app icon.

`card.json` shape: week, title, year, built_at, lines_verified_at, verification (verified|unverified),
verification_note, budget {total, sunday, monday, thursday}, tickets [ {id, type (single|parlay|sgp), day,
name, game, kickoff, stake, price, payout, estimate, breakeven, placed (bool), legs [...], why, kill_switch,
result (null|win|loss|push), net, clv} ], watch [strings], board [{kickoff, game, spread, total, ml, read}],
season {record, net, weeks [{week, net}], clv_week, clv_season}, clv_updated_at. Stakes must sum to the day's budget.

Every leg is structured so `clv.py` can grade it: {label, pick, game, away, home, commence_time, market
(spreads|totals|h2h), side (the team name exactly as The Odds API prints it, or Over|Under for totals), point
(null for h2h), price (American, integer), why}. `away`, `home`, and `commence_time` are copied from
`draftkings/lines/latest.json`. After the close routine runs, a leg also carries close {point, price,
pin_fair_prob, at}, point_clv, price_clv, clv, and pin_clv.

## Level 1 rules (added Sep 12, 2026)

### Pinnacle fair-price rule
`fetch_dk_lines.py` pulls Pinnacle next to DraftKings and strips Pinnacle's vig to a fair probability for every
side. It prints an EDGE VS PINNACLE table: prob_edge = Pinnacle fair probability minus DK implied probability;
point_gap = points DK gives beyond Pinnacle (positive is good for us); combined_edge = prob_edge + 0.04 x point_gap.
1. Rule A. A leg qualifies on price alone when combined_edge is +0.015 or better.
2. Rule B. A leg with combined_edge between -0.05 and +0.015 qualifies only if the card states an own estimate above
   DK's implied probability AND that estimate is within 6 points of Pinnacle's fair probability, or the card documents
   news Pinnacle has not priced yet (an inactive posted after the fetch, a weather change).
3. Never bet a leg with combined_edge below -0.05. If Pinnacle says DK's number is that far off, DK is right and we are wrong.
4. State combined_edge next to every leg on the card.

### Concentration limits
1. No leg appears in more than one ticket (a single and a parlay may not share a leg).
2. No single game carries more than 30 percent of that day's budget across all tickets.
3. A day's tickets share at most one correlated pair (dog plus under, favorite plus over) per game.

### Placed tickets
Tickets already in `card.json` for the current week are treated as placed (`placed: true`). A later routine
may only (a) apply a kill switch, which sets the ticket's stake to what Luke should keep and moves the freed
money to a new ticket, or (b) fill unplaced budget. It never silently rewrites a placed ticket. When a kill
switch trips, the card says what to do if the original ticket was already placed.

### Closing line value (CLV)
`draftkings/clv.py` runs at close time (Sunday 12:55 PM, 4:20 PM, 8:15 PM ET; Monday and Thursday 8:10 PM ET,
one routine each), fetches the current DK and Pinnacle numbers, and for every leg kicking off in the window
records the close and computes point_clv, price_clv, clv (price_clv + 0.04 x point_clv) and pin_clv (against
Pinnacle's no-vig close). Ticket CLV is the mean of its legs; `season.clv_week` and `season.clv_season` roll up.
Every graded leg is appended to `draftkings/clv-log.json`. The dashboard shows CLV per ticket and per week.
Reading it: a season average above zero means the picks beat the market; above +1.0 percent is strong.
A negative season average after 6 weeks means the method, not the luck, needs fixing.
`python3 draftkings/clv.py --all` grades every ungraded leg regardless of kickoff; `--dry-run` writes nothing.

### Inactives alert
A routine fires at 11:35 AM ET Sunday and 6:50 PM ET Monday and Thursday, reads the kill switches and watch
list in `card.json`, checks the posted inactives and DK's current numbers, and notifies Luke only with the
tickets that changed and the exact action (keep, cut to $X, swap to Y).

## Routine git flow
Every routine starts with `git fetch origin claude/draftkings-nfl-picks-4aiuoj && git checkout -B
claude/draftkings-nfl-picks-4aiuoj FETCH_HEAD` so it works on the picks branch with the latest scripts, and ends
with `sh draftkings/push.sh`, which pushes HEAD to the picks branch using GITHUB_TOKEN. The dashboard reads
`card.json` from that branch, so nothing has to reach `main` for the phone view to update; `main` only hosts
`dashboard/index.html` through GitHub Pages and needs a PR when the page itself changes.
