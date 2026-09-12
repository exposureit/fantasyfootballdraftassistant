# DraftKings Network Access Test

Test run from the Claude Code remote execution environment (outbound HTTPS via the session agent proxy).
Fetch window: 2026-09-12 13:07:17 UTC to 2026-09-12 13:09:11 UTC.

## Bottom line

DraftKings is only partially reachable. The public NFL league page loads over curl, but it is a JavaScript shell with no odds in the HTML. Every odds API endpoint (the ones the picks system needs) is blocked by DraftKings' Akamai edge with HTTP 403 "Access Denied". WebFetch is blocked on all four URLs. No NFL odds data was obtained, so there is no odds table in this report.

## Results by URL

| # | URL | WebFetch | curl (`-A "Mozilla/5.0"`) | Notes |
|---|-----|----------|---------------------------|-------|
| a | `https://sportsbook.draftkings.com/leagues/football/nfl` | HTTP 403 Forbidden (body not retrieved) | HTTP 200, `text/html`, 2,455,057 bytes | Page loads, title "NFL Odds, Spreads & Lines". Embedded `window.__INITIAL_STATE__` has empty `eventGroups`, `offers`, `outcomes`, `stadiumLeagueData.events`, `stadiumLeagueData.markets`. Team names present only in a logo map. No odds in the HTML. |
| b | `https://sportsbook-nash.draftkings.com/api/sportscontent/dkusnj/v1/leagues/88808` | HTTP 403 Forbidden | HTTP 403, `text/html`, 449 bytes, Akamai "Access Denied" (errors.edgesuite.net reference) | Blocked at the edge. |
| c | `https://sportsbook.draftkings.com/sites/US-SB/api/v5/eventgroups/88808?format=json` | HTTP 403 Forbidden | HTTP 403, `text/html`, 442 bytes, Akamai "Access Denied" | Blocked at the edge. |
| d | `https://sportsbook-nash.draftkings.com/api/sportscontent/dkuspa/v1/leagues/88808` | HTTP 403 Forbidden | HTTP 403, `text/html`, 449 bytes, Akamai "Access Denied" | Blocked at the edge. |

Fetch timestamps (UTC): WebFetch calls ran at approximately 13:07:20. curl for a ran at 13:07:29, b at 13:07:30, c at 13:07:31, d at 13:07:31.

## Additional attempts (beyond the four requested URLs)

| Attempt | Result |
|---------|--------|
| b, c, d re-run with full Chrome UA plus `Accept: application/json`, `Accept-Language`, `Referer: https://sportsbook.draftkings.com/leagues/football/nfl`, `Origin: https://sportsbook.draftkings.com` | All still HTTP 403 Akamai "Access Denied". Browser-like headers do not help. |
| `https://sportsbook-nash.draftkings.com/api/sportscontent/dkuswv/v1/leagues/88808` (site key `dkuswv` is the one the NFL page itself references) | HTTP 403 Akamai "Access Denied". |
| `https://sportsbook-nash.draftkings.com/api/sportscontent/views/dkuswv/v1/leagues/88808` | HTTP 403 Akamai "Access Denied". |
| `https://sportsbook-nash.draftkings.com/api/sdinfo/dkuswv/` | HTTP 403 Akamai "Access Denied". |
| `https://sportsbook.draftkings.com/api/sportscontent/dkuswv/v1/leagues/88808` | HTTP 301 to `https://sportsbook.draftkings.com/` (home page, HTTP 200). Not an API route on that host. |

## Interpretation

1. This is not an egress block on our side. The agent proxy passed every request through and DraftKings answered. The HTML host answers 200; the API hosts answer 403 from Akamai.
2. The 403s come from DraftKings' bot protection on `sportsbook-nash.draftkings.com` and on the `/sites/US-SB/api/` path. It is rejecting datacenter-origin requests before they reach the API. Adding browser headers does not change the outcome, which points to IP reputation or TLS fingerprinting rather than header checks.
3. The NFL league page is a client-rendered app. Odds are fetched by the browser from the same blocked `sportscontent` API, so scraping the HTML yields nothing useful.

## Working endpoint

None. No endpoint returned NFL odds data from this environment.

## Odds table

Not available. No odds were retrieved in this test.

## Recommended next step

1. Do not build the picks pipeline on direct DraftKings API calls from this environment. They will fail on every run.
2. Use a licensed odds aggregator that carries DraftKings lines (for example The Odds API, with `bookmakers=draftkings`), or run the fetch from a residential or local machine and push the JSON into the repo.
3. Keep this file as the baseline. Re-run the same four URLs if the environment's network policy or egress path changes.
