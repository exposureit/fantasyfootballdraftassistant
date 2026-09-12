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
   environment can actually fetch (none as of Sep 12, 2026).
2. Every other line is labeled UNVERIFIED and must carry the threshold Luke applies in the app before placing.
3. Never present a search-sourced line as DK's line. Say "DK line as of <source time>, verify in app".
4. Durable fix: allow sportsbook.draftkings.com (or site.api.espn.com) in the environment's network policy at
   claude.ai/code environment settings. Then the routines can pull live lines.
