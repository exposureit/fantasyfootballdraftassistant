# Odds API Verification Test

Run from a fresh Claude Code remote session (session_01CGXZ1SzBFPK5vavy8jP8of) on branch `claude/draftkings-nfl-picks-4aiuoj`.
Time of test: 2026-09-12 13:17 UTC.

## Result: FAILED (network policy blocks api.the-odds-api.com)

| Check | Result |
|---|---|
| `ODDS_API_KEY` set in environment | Yes (32 characters) |
| `python3 draftkings/fetch_dk_lines.py` exit code | 1 |
| Script output | `UNVERIFIED: fetch failed (<urlopen error Tunnel connection failed: 403 Forbidden>). Fall back to screenshot protocol.` |
| `curl https://api.the-odds-api.com/v4/sports/?apiKey=...` | `curl: (56) CONNECT tunnel failed, response 403` (HTTP 000, no response from the API itself) |
| Agent proxy status log | Two entries: `connect_rejected` for `api.the-odds-api.com:443`, "gateway answered 403 to CONNECT (policy denial or upstream failure)" at 13:17:14 and 13:17:18 UTC |

No DraftKings NFL board was retrieved, so there is no lines table in this report.

## Diagnosis

1. The key is present in the environment, so the environment variable is wired correctly.
2. The request never reached The Odds API. The session's egress proxy refused the HTTPS CONNECT to `api.the-odds-api.com` with 403 before any TLS handshake or API call. This is the Claude Code environment's outbound network policy, not an API key or quota problem.
3. Because the tunnel was never established, the key's validity and remaining request quota are still unknown.
4. This is a different failure from `network-test.md`. There, DraftKings' own Akamai edge answered 403 after the proxy passed the request through. Here, the proxy itself is the block.

## Fix

Add `api.the-odds-api.com` to the allowed domains in the Claude Code environment's network policy (Settings, Environments, the environment used by this repo, Network access). Then re-run this test. If the key is valid, the script prints `VERIFIED DRAFTKINGS NFL lines via The Odds API` followed by the board and writes `draftkings/lines/latest.json`.

## Security note

The step 1 shell check in the test instructions used `${ODDS_API_KEY:-NOT SET}`, which expands to the key's value when it is set. That printed the full key into this session's tool output. The key is not in this file or in the git history, but it is in the session transcript. Rotate the key at the-odds-api.com and update the environment variable. Use `${ODDS_API_KEY:+set}${ODDS_API_KEY:-NOT SET}` pattern only after removing the value branch, or simply `[ -n "$ODDS_API_KEY" ] && echo set || echo NOT SET`.
