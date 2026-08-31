# War Room '26 — Fantasy Football Draft Assistant

A single-file, offline-capable draft war room for a 10-team, full-PPR ESPN league (2026 season). Open `index.html` in any browser — no build, no dependencies.

## Features

- **Big Board** — tiered top-190 rankings blended from consensus ADP (ESPN/FFC/Underdog, Aug 30 2026) with news-adjusted board ranks, 2026 season projections, VORP (value over replacement), bye weeks, and value/risk/rookie/handcuff flags
- **Tier Pulse** — live per-position counters of how many players remain in each tier
- **Draft Board** — 10-team × 16-round snake grid with one-tap pick logging, fix-any-pick, unknown-pick placeholders, and league team names with a fast "set draft order" flow
- **Advice engine** — best-available scoring that weighs board value, tier cliffs, roster needs, round context, QB stacks, bye pile-ups, and injury/news flags
- **Monte Carlo survival odds** — simulates the room to estimate the % chance a player is gone by your next pick
- **Plan Ahead + Draft Script** — predicts who'll be available at your future picks and generates a full personalized round-by-round plan that regenerates after every pick
- **Room Intel** — profiles each opponent's roster needs and drafting tendency (reaches early / by ADP / value hunter), with position-run and falling-value alarms
- **Live draft grades** — projected starting-lineup points for all 10 teams, updated every pick
- **Mock trainer** — practice against ADP-realistic simulated opponents
- **News ticker** — auto-scrolling feed of injuries, suspensions, and cut-day fallout (as of Aug 30, 2026)

Draft state auto-saves to the browser (`localStorage`). Player data is embedded and reflects rosters/news as of August 30, 2026.
