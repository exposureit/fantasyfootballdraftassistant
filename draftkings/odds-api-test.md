# Odds API Verification Test

Run from a Claude Code remote worker session on branch `claude/draftkings-nfl-picks-4aiuoj`.
Time of test: 2026-09-12 13:43 UTC.

## Result: VERIFIED

| Check | Result |
|---|---|
| `ODDS_API_KEY` set in environment | Yes |
| `python3 draftkings/fetch_dk_lines.py` exit code | 0 |
| `python3 draftkings/fetch_dk_lines.py --book fanduel` exit code | 0 |
| Games returned per book | 212 |
| `draftkings/lines/latest.json` | Written (DraftKings snapshot, re-run last so it holds DraftKings, not FanDuel) |
| Requests remaining this month after the three calls | 482 |

The network block recorded in the previous version of this file is resolved. The proxy now passes `api.the-odds-api.com` and The Odds API accepted the key.

Note: each run of the script overwrites `draftkings/lines/latest.json` with whichever book was requested, so run the DraftKings fetch last if the JSON must stay DraftKings.

## DraftKings NFL lines

VERIFIED DRAFTKINGS NFL lines via The Odds API, fetched 2026-09-12 13:43 UTC. Requests remaining this month: 482

| Kickoff (ET) | Game | Spread | Total | Moneyline |
|---|---|---|---|---|
| Sun 09/13 01:00 PM | Atlanta Falcons at Pittsburgh Steelers | Atlanta Falcons +6 (-110) / Pittsburgh Steelers -6 (-110) | 41.5 (O -105 / U -115) | Atlanta Falcons +220 / Pittsburgh Steelers -270 |
| Sun 09/13 01:00 PM | Baltimore Ravens at Indianapolis Colts | Baltimore Ravens -3.5 (-105) / Indianapolis Colts +3.5 (-115) | 47.5 (O -115 / U -105) | Baltimore Ravens -175 / Indianapolis Colts +145 |
| Sun 09/13 01:00 PM | Buffalo Bills at Houston Texans | Buffalo Bills -1.5 (-108) / Houston Texans +1.5 (-112) | 44.5 (O -110 / U -110) | Buffalo Bills -118 / Houston Texans -102 |
| Sun 09/13 01:00 PM | Chicago Bears at Carolina Panthers | Chicago Bears -3 (-118) / Carolina Panthers +3 (-102) | 47.5 (O -110 / U -110) | Chicago Bears -166 / Carolina Panthers +140 |
| Sun 09/13 01:00 PM | Tampa Bay Buccaneers at Cincinnati Bengals | Tampa Bay Buccaneers +3.5 (-108) / Cincinnati Bengals -3.5 (-112) | 50.5 (O -108 / U -112) | Tampa Bay Buccaneers +170 / Cincinnati Bengals -205 |
| Sun 09/13 01:00 PM | Cleveland Browns at Jacksonville Jaguars | Cleveland Browns +8.5 (-108) / Jacksonville Jaguars -8.5 (-112) | 39.5 (O -118 / U -102) | Cleveland Browns +350 / Jacksonville Jaguars -455 |
| Sun 09/13 01:00 PM | New Orleans Saints at Detroit Lions | New Orleans Saints +7 (-110) / Detroit Lions -7 (-110) | 49.5 (O -112 / U -108) | New Orleans Saints +270 / Detroit Lions -340 |
| Sun 09/13 01:00 PM | New York Jets at Tennessee Titans | New York Jets +1.5 (-110) / Tennessee Titans -1.5 (-110) | 38.5 (O -112 / U -108) | New York Jets +102 / Tennessee Titans -122 |
| Sun 09/13 04:25 PM | Arizona Cardinals at Los Angeles Chargers | Arizona Cardinals +9.5 (-105) / Los Angeles Chargers -9.5 (-115) | 47.5 (O -102 / U -118) | Arizona Cardinals +380 / Los Angeles Chargers -500 |
| Sun 09/13 04:25 PM | Green Bay Packers at Minnesota Vikings | Green Bay Packers +1.5 (-108) / Minnesota Vikings -1.5 (-112) | 46.5 (O -108 / U -112) | Green Bay Packers +105 / Minnesota Vikings -125 |
| Sun 09/13 04:25 PM | Miami Dolphins at Las Vegas Raiders | Miami Dolphins +3 (-108) / Las Vegas Raiders -3 (-112) | 40.5 (O -105 / U -115) | Miami Dolphins +142 / Las Vegas Raiders -170 |
| Sun 09/13 04:25 PM | Washington Commanders at Philadelphia Eagles | Washington Commanders +6 (-112) / Philadelphia Eagles -6 (-108) | 44.5 (O -105 / U -115) | Washington Commanders +205 / Philadelphia Eagles -250 |
| Sun 09/13 08:20 PM | Dallas Cowboys at New York Giants | Dallas Cowboys -3 (-105) / New York Giants +3 (-115) | 48.5 (O -105 / U -115) | Dallas Cowboys -162 / New York Giants +136 |
| Mon 09/14 08:15 PM | Denver Broncos at Kansas City Chiefs | Denver Broncos +2.5 (-105) / Kansas City Chiefs -2.5 (-115) | 43.5 (O -115 / U -105) | Denver Broncos +120 / Kansas City Chiefs -142 |
| Thu 09/17 08:15 PM | Detroit Lions at Buffalo Bills | Detroit Lions +3 (-105) / Buffalo Bills -3 (-115) | 51.5 (O -115 / U -105) | Detroit Lions +136 / Buffalo Bills -162 |
| Sun 09/20 01:00 PM | Carolina Panthers at Atlanta Falcons | Carolina Panthers +1.5 (-110) / Atlanta Falcons -1.5 (-110) | 42.5 (O -110 / U -110) | Carolina Panthers +105 / Atlanta Falcons -125 |
| Sun 09/20 01:00 PM | New Orleans Saints at Baltimore Ravens | New Orleans Saints +7.5 (-110) / Baltimore Ravens -7.5 (-110) | 46.5 (O -110 / U -110) | New Orleans Saints +280 / Baltimore Ravens -355 |
| Sun 09/20 01:00 PM | Minnesota Vikings at Chicago Bears | Minnesota Vikings +3 (-110) / Chicago Bears -3 (-110) | 45.5 (O -110 / U -110) | Minnesota Vikings +142 / Chicago Bears -170 |
| Sun 09/20 01:00 PM | Cincinnati Bengals at Houston Texans | Cincinnati Bengals +2.5 (-102) / Houston Texans -2.5 (-118) | 45.5 (O -110 / U -110) | Cincinnati Bengals +124 / Houston Texans -148 |
| Sun 09/20 01:00 PM | Cleveland Browns at Tampa Bay Buccaneers | Cleveland Browns +6.5 (-110) / Tampa Bay Buccaneers -6.5 (-110) | 42.5 (O -110 / U -110) | Cleveland Browns +230 / Tampa Bay Buccaneers -285 |
| Sun 09/20 01:00 PM | Green Bay Packers at New York Jets | Green Bay Packers -5.5 (-110) / New York Jets +5.5 (-110) | 42.5 (O -110 / U -110) | Green Bay Packers -245 / New York Jets +200 |
| Sun 09/20 01:00 PM | Pittsburgh Steelers at New England Patriots | Pittsburgh Steelers +4.5 (-115) / New England Patriots -4.5 (-105) | 43.5 (O -110 / U -110) | Pittsburgh Steelers +170 / New England Patriots -205 |
| Sun 09/20 01:00 PM | Philadelphia Eagles at Tennessee Titans | Philadelphia Eagles -5.5 (-110) / Tennessee Titans +5.5 (-110) | 42.5 (O -110 / U -110) | Philadelphia Eagles -230 / Tennessee Titans +190 |
| Sun 09/20 04:05 PM | Jacksonville Jaguars at Denver Broncos | Jacksonville Jaguars +3 (-110) / Denver Broncos -3 (-110) | 43.5 (O -110 / U -110) | Jacksonville Jaguars +130 / Denver Broncos -155 |
| Sun 09/20 04:05 PM | Las Vegas Raiders at Los Angeles Chargers | Las Vegas Raiders +9.5 (-110) / Los Angeles Chargers -9.5 (-110) | 42.5 (O -110 / U -110) | Las Vegas Raiders +310 / Los Angeles Chargers -395 |
| Sun 09/20 04:25 PM | Washington Commanders at Dallas Cowboys | Washington Commanders +4.5 (-115) / Dallas Cowboys -4.5 (-105) | 51.5 (O -110 / U -110) | Washington Commanders +164 / Dallas Cowboys -198 |
| Sun 09/20 08:20 PM | Indianapolis Colts at Kansas City Chiefs | Indianapolis Colts +6.5 (-110) / Kansas City Chiefs -6.5 (-110) | 47.5 (O -110 / U -110) | Indianapolis Colts +250 / Kansas City Chiefs -310 |
| Thu 09/24 08:15 PM | Atlanta Falcons at Green Bay Packers | Atlanta Falcons +7.5 (-110) / Green Bay Packers -7.5 (-110) | 46.5 (O -110 / U -110) | Atlanta Falcons +295 / Green Bay Packers -375 |
| Sun 09/27 01:00 PM | Los Angeles Chargers at Buffalo Bills | Los Angeles Chargers +3 (-110) / Buffalo Bills -3 (-110) | 48.5 (O -110 / U -110) | Los Angeles Chargers +136 / Buffalo Bills -162 |
| Sun 09/27 01:00 PM | Carolina Panthers at Cleveland Browns | Carolina Panthers -1.5 (-110) / Cleveland Browns +1.5 (-110) | 39.5 (O -110 / U -110) | Carolina Panthers -125 / Cleveland Browns +105 |
| Sun 09/27 01:00 PM | Cincinnati Bengals at Pittsburgh Steelers | Cincinnati Bengals -1.5 (-110) / Pittsburgh Steelers +1.5 (-110) | 46.5 (O -118 / U -102) | Cincinnati Bengals -125 / Pittsburgh Steelers +105 |
| Sun 09/27 01:00 PM | New York Jets at Detroit Lions | New York Jets +9.5 (-110) / Detroit Lions -9.5 (-110) | 45.5 (O -110 / U -110) | New York Jets +330 / Detroit Lions -425 |
| Sun 09/27 01:00 PM | Houston Texans at Indianapolis Colts | Houston Texans -1.5 (-110) / Indianapolis Colts +1.5 (-110) | 45.5 (O -110 / U -110) | Houston Texans -122 / Indianapolis Colts +102 |
| Sun 09/27 01:00 PM | Kansas City Chiefs at Miami Dolphins | Kansas City Chiefs -7.5 (-110) / Miami Dolphins +7.5 (-110) | 44.5 (O -110 / U -110) | Kansas City Chiefs -440 / Miami Dolphins +340 |
| Sun 09/27 01:00 PM | Tennessee Titans at New York Giants | Tennessee Titans +3 (-105) / New York Giants -3 (-115) | 44.5 (O -110 / U -110) | Tennessee Titans +140 / New York Giants -166 |
| Sun 09/27 04:05 PM | Minnesota Vikings at Tampa Bay Buccaneers | Minnesota Vikings +1.5 (-110) / Tampa Bay Buccaneers -1.5 (-110) | 44.5 (O -110 / U -110) | Minnesota Vikings +105 / Tampa Bay Buccaneers -125 |
| Sun 09/27 04:25 PM | Baltimore Ravens at Dallas Cowboys | Baltimore Ravens -2.5 (-110) / Dallas Cowboys +2.5 (-110) | 51.5 (O -110 / U -110) | Baltimore Ravens -135 / Dallas Cowboys +114 |
| Sun 09/27 04:25 PM | Las Vegas Raiders at New Orleans Saints | Las Vegas Raiders +3.5 (-110) / New Orleans Saints -3.5 (-110) | 42.5 (O -110 / U -110) | Las Vegas Raiders +154 / New Orleans Saints -185 |
| Mon 09/28 08:15 PM | Philadelphia Eagles at Chicago Bears | Philadelphia Eagles +1.5 (-115) / Chicago Bears -1.5 (-105) | 46.5 (O -110 / U -110) | Philadelphia Eagles -102 / Chicago Bears -118 |
| Thu 10/01 08:15 PM | Pittsburgh Steelers at Cleveland Browns | Pittsburgh Steelers -2.5 (-110) / Cleveland Browns +2.5 (-110) | 40.5 (O -110 / U -110) | Pittsburgh Steelers -135 / Cleveland Browns +114 |
| Sun 10/04 09:30 AM | Indianapolis Colts at Washington Commanders | Indianapolis Colts +1.5 (-115) / Washington Commanders -1.5 (-105) | 50.5 (O -110 / U -110) | Indianapolis Colts -102 / Washington Commanders -118 |
| Sun 10/04 01:00 PM | Arizona Cardinals at New York Giants | Arizona Cardinals +7 (-110) / New York Giants -7 (-110) | 45.5 (O -110 / U -110) | Arizona Cardinals +260 / New York Giants -325 |
| Sun 10/04 01:00 PM | Tennessee Titans at Baltimore Ravens | Tennessee Titans +8.5 (-110) / Baltimore Ravens -8.5 (-110) | 47.5 (O -110 / U -110) | Tennessee Titans +310 / Baltimore Ravens -395 |
| Sun 10/04 01:00 PM | New York Jets at Chicago Bears | New York Jets +8.5 (-110) / Chicago Bears -8.5 (-110) | 45.5 (O -110 / U -110) | New York Jets +340 / Chicago Bears -440 |
| Sun 10/04 01:00 PM | Jacksonville Jaguars at Cincinnati Bengals | Jacksonville Jaguars +2.5 (-110) / Cincinnati Bengals -2.5 (-110) | 51.5 (O -110 / U -110) | Jacksonville Jaguars +114 / Cincinnati Bengals -135 |
| Sun 10/04 01:00 PM | Dallas Cowboys at Houston Texans | Dallas Cowboys +2.5 (-110) / Houston Texans -2.5 (-110) | 47.5 (O -110 / U -110) | Dallas Cowboys +114 / Houston Texans -135 |
| Sun 10/04 01:00 PM | Green Bay Packers at Tampa Bay Buccaneers | Green Bay Packers -1.5 (-110) / Tampa Bay Buccaneers +1.5 (-110) | 47.5 (O -110 / U -110) | Green Bay Packers -125 / Tampa Bay Buccaneers +105 |
| Sun 10/04 04:05 PM | Miami Dolphins at Minnesota Vikings | Miami Dolphins +7.5 (-110) / Minnesota Vikings -7.5 (-110) | 43.5 (O -110 / U -110) | Miami Dolphins +310 / Minnesota Vikings -395 |
| Sun 10/04 04:25 PM | Kansas City Chiefs at Las Vegas Raiders | Kansas City Chiefs -5.5 (-110) / Las Vegas Raiders +5.5 (-110) | 43.5 (O -110 / U -110) | Kansas City Chiefs -250 / Las Vegas Raiders +205 |
| Sun 10/04 08:20 PM | Detroit Lions at Carolina Panthers | Detroit Lions -3 (-110) / Carolina Panthers +3 (-110) | 47.5 (O -110 / U -110) | Detroit Lions -162 / Carolina Panthers +136 |
| Mon 10/05 08:15 PM | Atlanta Falcons at New Orleans Saints | Atlanta Falcons +2.5 (-110) / New Orleans Saints -2.5 (-110) | 45.5 (O -115 / U -105) | Atlanta Falcons +114 / New Orleans Saints -135 |
| Thu 10/08 08:15 PM | Tampa Bay Buccaneers at Dallas Cowboys | Tampa Bay Buccaneers +3.5 (-110) / Dallas Cowboys -3.5 (-110) | 52.5 (O -110 / U -110) | Tampa Bay Buccaneers +170 / Dallas Cowboys -205 |
| Sun 10/11 09:30 AM | Philadelphia Eagles at Jacksonville Jaguars | Philadelphia Eagles -1.5 (-110) / Jacksonville Jaguars +1.5 (-110) | 45.5 (O -110 / U -110) | Philadelphia Eagles -125 / Jacksonville Jaguars +105 |
| Sun 10/11 01:00 PM | Cincinnati Bengals at Miami Dolphins | Cincinnati Bengals -6 (-110) / Miami Dolphins +6 (-110) | 49.5 (O -110 / U -110) | Cincinnati Bengals -278 / Miami Dolphins +225 |
| Sun 10/11 01:00 PM | Cleveland Browns at New York Jets | Cleveland Browns +2.5 (-115) / New York Jets -2.5 (-105) | 39.5 (O -110 / U -110) | Cleveland Browns +110 / New York Jets -130 |
| Sun 10/11 01:00 PM | Houston Texans at Tennessee Titans | Houston Texans -3.5 (-110) / Tennessee Titans +3.5 (-110) | 43.5 (O -110 / U -110) | Houston Texans -185 / Tennessee Titans +154 |
| Sun 10/11 01:00 PM | Indianapolis Colts at Pittsburgh Steelers | Indianapolis Colts +2.5 (-110) / Pittsburgh Steelers -2.5 (-110) | 47.5 (O -110 / U -110) | Indianapolis Colts +120 / Pittsburgh Steelers -142 |
| Sun 10/11 01:00 PM | Minnesota Vikings at New Orleans Saints | Minnesota Vikings -1.5 (-110) / New Orleans Saints +1.5 (-110) | 44.5 (O -110 / U -110) | Minnesota Vikings -125 / New Orleans Saints +105 |
| Sun 10/11 01:00 PM | New York Giants at Washington Commanders | New York Giants +2.5 (-115) / Washington Commanders -2.5 (-105) | 48.5 (O -110 / U -110) | New York Giants +110 / Washington Commanders -130 |
| Sun 10/11 04:05 PM | Denver Broncos at Los Angeles Chargers | Denver Broncos +2.5 (-110) / Los Angeles Chargers -2.5 (-110) | 44.5 (O -110 / U -110) | Denver Broncos +120 / Los Angeles Chargers -142 |
| Sun 10/11 04:25 PM | Detroit Lions at Arizona Cardinals | Detroit Lions -8.5 (-110) / Arizona Cardinals +8.5 (-110) | 48.5 (O -110 / U -110) | Detroit Lions -395 / Arizona Cardinals +310 |
| Sun 10/11 04:25 PM | Chicago Bears at Green Bay Packers | Chicago Bears +3 (-110) / Green Bay Packers -3 (-110) | 49.5 (O -110 / U -110) | Chicago Bears +140 / Green Bay Packers -166 |
| Sun 10/11 08:20 PM | Baltimore Ravens at Atlanta Falcons | Baltimore Ravens -4.5 (-110) / Atlanta Falcons +4.5 (-110) | 48.5 (O -110 / U -110) | Baltimore Ravens -205 / Atlanta Falcons +170 |
| Sun 10/18 09:30 AM | Houston Texans at Jacksonville Jaguars | Houston Texans +1.5 (-122) / Jacksonville Jaguars -1.5 (+102) | 42.5 (O -110 / U -110) | Houston Texans -108 / Jacksonville Jaguars -112 |
| Sun 10/18 01:00 PM | Chicago Bears at Atlanta Falcons | Chicago Bears -3 (-110) / Atlanta Falcons +3 (-110) | 47.5 (O -110 / U -110) | Chicago Bears -155 / Atlanta Falcons +130 |
| Sun 10/18 01:00 PM | Baltimore Ravens at Cleveland Browns | Baltimore Ravens -6.5 (-110) / Cleveland Browns +6.5 (-110) | 44.5 (O -110 / U -110) | Baltimore Ravens -250 / Cleveland Browns +205 |
| Sun 10/18 01:00 PM | Carolina Panthers at Philadelphia Eagles | Carolina Panthers +6.5 (-110) / Philadelphia Eagles -6.5 (-110) | 43.5 (O -110 / U -110) | Carolina Panthers +225 / Philadelphia Eagles -278 |
| Sun 10/18 01:00 PM | Tennessee Titans at Indianapolis Colts | Tennessee Titans +3.5 (-110) / Indianapolis Colts -3.5 (-110) | 47.5 (O -110 / U -110) | Tennessee Titans +164 / Indianapolis Colts -198 |
| Sun 10/18 01:00 PM | New Orleans Saints at New York Giants | New Orleans Saints +2.5 (-110) / New York Giants -2.5 (-110) | 44.5 (O -110 / U -110) | New Orleans Saints +120 / New York Giants -142 |
| Sun 10/18 01:00 PM | Pittsburgh Steelers at Tampa Bay Buccaneers | Pittsburgh Steelers +1.5 (-110) / Tampa Bay Buccaneers -1.5 (-110) | 45.5 (O -110 / U -110) | Pittsburgh Steelers +105 / Tampa Bay Buccaneers -125 |
| Sun 10/18 04:25 PM | Buffalo Bills at Las Vegas Raiders | Buffalo Bills -6.5 (-110) / Las Vegas Raiders +6.5 (-110) | 47.5 (O -110 / U -110) | Buffalo Bills -270 / Las Vegas Raiders +220 |
| Sun 10/18 04:25 PM | Los Angeles Chargers at Kansas City Chiefs | Los Angeles Chargers +2.5 (-110) / Kansas City Chiefs -2.5 (-110) | 46.5 (O -110 / U -110) | Los Angeles Chargers +120 / Kansas City Chiefs -142 |
| Sun 10/18 08:20 PM | Dallas Cowboys at Green Bay Packers | Dallas Cowboys +3 (-110) / Green Bay Packers -3 (-110) | 51.5 (O -110 / U -110) | Dallas Cowboys +142 / Green Bay Packers -170 |
| Sun 10/25 09:30 AM | Pittsburgh Steelers at New Orleans Saints | Pittsburgh Steelers -2.5 (-110) / New Orleans Saints +2.5 (-110) | 42.5 (O -110 / U -110) | Pittsburgh Steelers -142 / New Orleans Saints +120 |
| Sun 10/25 01:00 PM | Cincinnati Bengals at Baltimore Ravens | Cincinnati Bengals +3.5 (-110) / Baltimore Ravens -3.5 (-110) | 51.5 (O -110 / U -110) | Cincinnati Bengals +150 / Baltimore Ravens -180 |
| Sun 10/25 01:00 PM | Tampa Bay Buccaneers at Carolina Panthers | Tampa Bay Buccaneers -1.5 (-110) / Carolina Panthers +1.5 (-110) | 45.5 (O -110 / U -110) | Tampa Bay Buccaneers -125 / Carolina Panthers +105 |
| Sun 10/25 01:00 PM | Cleveland Browns at Tennessee Titans | Cleveland Browns +2.5 (-110) / Tennessee Titans -2.5 (-110) | 40.5 (O -110 / U -110) | Cleveland Browns +114 / Tennessee Titans -135 |
| Sun 10/25 01:00 PM | New York Giants at Houston Texans | New York Giants +5.5 (-110) / Houston Texans -5.5 (-110) | 43.5 (O -110 / U -110) | New York Giants +195 / Houston Texans -238 |
| Sun 10/25 01:00 PM | Indianapolis Colts at Minnesota Vikings | Indianapolis Colts +2.5 (-110) / Minnesota Vikings -2.5 (-110) | 46.5 (O -110 / U -110) | Indianapolis Colts +120 / Minnesota Vikings -142 |
| Sun 10/25 01:00 PM | Miami Dolphins at New York Jets | Miami Dolphins +2.5 (-110) / New York Jets -2.5 (-110) | 41.5 (O -110 / U -110) | Miami Dolphins +120 / New York Jets -142 |
| Sun 10/25 04:05 PM | Denver Broncos at Arizona Cardinals | Denver Broncos -7.5 (-110) / Arizona Cardinals +7.5 (-110) | 43.5 (O -110 / U -110) | Denver Broncos -375 / Arizona Cardinals +295 |
| Sun 10/25 04:25 PM | Green Bay Packers at Detroit Lions | Green Bay Packers +2.5 (-110) / Detroit Lions -2.5 (-110) | 50.5 (O -110 / U -110) | Green Bay Packers +114 / Detroit Lions -135 |
| Mon 10/26 08:15 PM | Dallas Cowboys at Philadelphia Eagles | Dallas Cowboys +3 (-110) / Philadelphia Eagles -3 (-110) | 48.5 (O -110 / U -110) | Dallas Cowboys +136 / Philadelphia Eagles -162 |
| Thu 10/29 08:15 PM | Carolina Panthers at Green Bay Packers | Carolina Panthers +7 (-110) / Green Bay Packers -7 (-110) | 45.5 (O -110 / U -110) | Carolina Panthers +275 / Green Bay Packers -345 |
| Sun 11/01 01:00 PM | Arizona Cardinals at Dallas Cowboys | Arizona Cardinals +10.5 (-110) / Dallas Cowboys -10.5 (-110) | 47.5 (O -110 / U -110) | Arizona Cardinals +400 / Dallas Cowboys -535 |
| Sun 11/01 01:00 PM | Atlanta Falcons at Tampa Bay Buccaneers | Atlanta Falcons +4.5 (-110) / Tampa Bay Buccaneers -4.5 (-110) | 46.5 (O -110 / U -110) | Atlanta Falcons +180 / Tampa Bay Buccaneers -218 |
| Sun 11/01 01:00 PM | Baltimore Ravens at Buffalo Bills | Baltimore Ravens +2.5 (-110) / Buffalo Bills -2.5 (-110) | 51.5 (O -110 / U -110) | Baltimore Ravens +114 / Buffalo Bills -135 |
| Sun 11/01 01:00 PM | Tennessee Titans at Cincinnati Bengals | Tennessee Titans +6.5 (-110) / Cincinnati Bengals -6.5 (-110) | 49.5 (O -110 / U -110) | Tennessee Titans +235 / Cincinnati Bengals -290 |
| Sun 11/01 01:00 PM | Cleveland Browns at Pittsburgh Steelers | Cleveland Browns +6 (-110) / Pittsburgh Steelers -6 (-110) | 39.5 (O -110 / U -110) | Cleveland Browns +210 / Pittsburgh Steelers -258 |
| Sun 11/01 01:00 PM | Minnesota Vikings at Detroit Lions | Minnesota Vikings +4.5 (-110) / Detroit Lions -4.5 (-110) | 47.5 (O -110 / U -110) | Minnesota Vikings +185 / Detroit Lions -225 |
| Sun 11/01 01:00 PM | Indianapolis Colts at Jacksonville Jaguars | Indianapolis Colts +4.5 (-110) / Jacksonville Jaguars -4.5 (-110) | 49.5 (O -110 / U -110) | Indianapolis Colts +185 / Jacksonville Jaguars -225 |
| Sun 11/01 01:00 PM | Las Vegas Raiders at New York Jets | Las Vegas Raiders +1.5 (-110) / New York Jets -1.5 (-110) | 40.5 (O -110 / U -110) | Las Vegas Raiders +102 / New York Jets -122 |
| Sun 11/01 04:25 PM | Kansas City Chiefs at Denver Broncos | Kansas City Chiefs +1.5 (-110) / Denver Broncos -1.5 (-110) | 43.5 (O -110 / U -110) | Kansas City Chiefs +105 / Denver Broncos -125 |
| Sun 11/01 08:20 PM | Philadelphia Eagles at Washington Commanders | Philadelphia Eagles -1.5 (-110) / Washington Commanders +1.5 (-110) | 46.5 (O -110 / U -110) | Philadelphia Eagles -125 / Washington Commanders +105 |
| Thu 11/05 08:15 PM | Jacksonville Jaguars at Baltimore Ravens | Jacksonville Jaguars +4.5 (-110) / Baltimore Ravens -4.5 (-110) | 49.5 (O -110 / U -110) | Jacksonville Jaguars +170 / Baltimore Ravens -205 |
| Sun 11/08 09:30 AM | Cincinnati Bengals at Atlanta Falcons | Cincinnati Bengals -5.5 (-110) / Atlanta Falcons +5.5 (-110) | 49.5 (O -110 / U -110) | Cincinnati Bengals -230 / Atlanta Falcons +190 |
| Sun 11/08 01:00 PM | Denver Broncos at Carolina Panthers | Denver Broncos -3 (-110) / Carolina Panthers +3 (-110) | 42.5 (O -110 / U -110) | Denver Broncos -162 / Carolina Panthers +136 |
| Sun 11/08 01:00 PM | Cleveland Browns at New Orleans Saints | Cleveland Browns +3.5 (-105) / New Orleans Saints -3.5 (-115) | 41.5 (O -110 / U -110) | Cleveland Browns +164 / New Orleans Saints -198 |
| Sun 11/08 01:00 PM | Dallas Cowboys at Indianapolis Colts | Dallas Cowboys -1.5 (-110) / Indianapolis Colts +1.5 (-110) | 52.5 (O -110 / U -110) | Dallas Cowboys -125 / Indianapolis Colts +105 |
| Sun 11/08 01:00 PM | Detroit Lions at Miami Dolphins | Detroit Lions -6.5 (-110) / Miami Dolphins +6.5 (-110) | 47.5 (O -110 / U -110) | Detroit Lions -278 / Miami Dolphins +225 |
| Sun 11/08 01:00 PM | New York Jets at Kansas City Chiefs | New York Jets +9.5 (-110) / Kansas City Chiefs -9.5 (-110) | 41.5 (O -110 / U -110) | New York Jets +350 / Kansas City Chiefs -455 |
| Sun 11/08 01:00 PM | New York Giants at Philadelphia Eagles | New York Giants +5.5 (-110) / Philadelphia Eagles -5.5 (-110) | 44.5 (O -110 / U -110) | New York Giants +195 / Philadelphia Eagles -238 |
| Sun 11/08 04:05 PM | Houston Texans at Los Angeles Chargers | Houston Texans +2.5 (-110) / Los Angeles Chargers -2.5 (-110) | 43.5 (O -110 / U -110) | Houston Texans +114 / Los Angeles Chargers -135 |
| Sun 11/08 08:20 PM | Tampa Bay Buccaneers at Chicago Bears | Tampa Bay Buccaneers +3.5 (-110) / Chicago Bears -3.5 (-110) | 48.5 (O -110 / U -110) | Tampa Bay Buccaneers +160 / Chicago Bears -192 |
| Mon 11/09 08:15 PM | Buffalo Bills at Minnesota Vikings | Buffalo Bills -3 (-110) / Minnesota Vikings +3 (-110) | 48.5 (O -110 / U -110) | Buffalo Bills -170 / Minnesota Vikings +142 |
| Thu 11/12 08:15 PM | Washington Commanders at New York Giants | Washington Commanders +1.5 (-110) / New York Giants -1.5 (-110) | 47.5 (O -110 / U -110) | Washington Commanders +102 / New York Giants -122 |
| Sun 11/15 01:00 PM | Kansas City Chiefs at Atlanta Falcons | Kansas City Chiefs -4.5 (-110) / Atlanta Falcons +4.5 (-110) | 45.5 (O -110 / U -110) | Kansas City Chiefs -230 / Atlanta Falcons +190 |
| Sun 11/15 01:00 PM | Buffalo Bills at New York Jets | Buffalo Bills -7 (-115) / New York Jets +7 (-105) | 46.5 (O -110 / U -110) | Buffalo Bills -345 / New York Jets +275 |
| Sun 11/15 01:00 PM | Carolina Panthers at New Orleans Saints | Carolina Panthers +1.5 (-115) / New Orleans Saints -1.5 (-105) | 43.5 (O -110 / U -110) | Carolina Panthers -102 / New Orleans Saints -118 |
| Sun 11/15 01:00 PM | Houston Texans at Cleveland Browns | Houston Texans -4.5 (-110) / Cleveland Browns +4.5 (-110) | 38.5 (O -110 / U -110) | Houston Texans -205 / Cleveland Browns +170 |
| Sun 11/15 01:00 PM | Minnesota Vikings at Green Bay Packers | Minnesota Vikings +4.5 (-110) / Green Bay Packers -4.5 (-110) | 45.5 (O -110 / U -110) | Minnesota Vikings +195 / Green Bay Packers -238 |
| Sun 11/15 01:00 PM | Miami Dolphins at Indianapolis Colts | Miami Dolphins +6.5 (-110) / Indianapolis Colts -6.5 (-110) | 47.5 (O -110 / U -110) | Miami Dolphins +245 / Indianapolis Colts -305 |
| Sun 11/15 01:00 PM | Jacksonville Jaguars at Tennessee Titans | Jacksonville Jaguars -2.5 (-110) / Tennessee Titans +2.5 (-110) | 45.5 (O -110 / U -110) | Jacksonville Jaguars -135 / Tennessee Titans +114 |
| Sun 11/15 08:20 PM | Pittsburgh Steelers at Cincinnati Bengals | Pittsburgh Steelers +3.5 (-110) / Cincinnati Bengals -3.5 (-110) | 47.5 (O -110 / U -110) | Pittsburgh Steelers +164 / Cincinnati Bengals -198 |
| Mon 11/16 08:15 PM | Los Angeles Chargers at Baltimore Ravens | Los Angeles Chargers +3.5 (-110) / Baltimore Ravens -3.5 (-110) | 47.5 (O -110 / U -110) | Los Angeles Chargers +150 / Baltimore Ravens -180 |
| Thu 11/19 08:15 PM | Indianapolis Colts at Houston Texans | Indianapolis Colts +5.5 (-110) / Houston Texans -5.5 (-110) | 45.5 (O -110 / U -110) | Indianapolis Colts +195 / Houston Texans -238 |
| Sun 11/22 01:00 PM | Arizona Cardinals at Kansas City Chiefs | Arizona Cardinals +11.5 (-110) / Kansas City Chiefs -11.5 (-110) | 44.5 (O -110 / U -110) | Arizona Cardinals +440 / Kansas City Chiefs -600 |
| Sun 11/22 01:00 PM | Baltimore Ravens at Carolina Panthers | Baltimore Ravens -4.5 (-110) / Carolina Panthers +4.5 (-110) | 46.5 (O -110 / U -110) | Baltimore Ravens -218 / Carolina Panthers +180 |
| Sun 11/22 01:00 PM | Miami Dolphins at Buffalo Bills | Miami Dolphins +11.5 (-110) / Buffalo Bills -11.5 (-110) | 47.5 (O -110 / U -110) | Miami Dolphins +470 / Buffalo Bills -650 |
| Sun 11/22 01:00 PM | New Orleans Saints at Chicago Bears | New Orleans Saints +6.5 (-110) / Chicago Bears -6.5 (-110) | 46.5 (O -110 / U -110) | New Orleans Saints +235 / Chicago Bears -290 |
| Sun 11/22 01:00 PM | Tennessee Titans at Dallas Cowboys | Tennessee Titans +6.5 (-110) / Dallas Cowboys -6.5 (-110) | 48.5 (O -110 / U -110) | Tennessee Titans +230 / Dallas Cowboys -285 |
| Sun 11/22 01:00 PM | Tampa Bay Buccaneers at Detroit Lions | Tampa Bay Buccaneers +4.5 (-110) / Detroit Lions -4.5 (-110) | 49.5 (O -110 / U -110) | Tampa Bay Buccaneers +180 / Detroit Lions -218 |
| Sun 11/22 01:00 PM | Jacksonville Jaguars at New York Giants | Jacksonville Jaguars -1.5 (-110) / New York Giants +1.5 (-110) | 46.5 (O -110 / U -110) | Jacksonville Jaguars -122 / New York Giants +102 |
| Sun 11/22 04:05 PM | New York Jets at Los Angeles Chargers | New York Jets +9.5 (-110) / Los Angeles Chargers -9.5 (-110) | 41.5 (O -110 / U -110) | New York Jets +330 / Los Angeles Chargers -425 |
| Sun 11/22 04:25 PM | Las Vegas Raiders at Denver Broncos | Las Vegas Raiders +7.5 (-110) / Denver Broncos -7.5 (-110) | 41.5 (O -110 / U -110) | Las Vegas Raiders +270 / Denver Broncos -340 |
| Sun 11/22 04:25 PM | Pittsburgh Steelers at Philadelphia Eagles | Pittsburgh Steelers +5.5 (-110) / Philadelphia Eagles -5.5 (-110) | 42.5 (O -110 / U -110) | Pittsburgh Steelers +195 / Philadelphia Eagles -238 |
| Mon 11/23 08:15 PM | Cincinnati Bengals at Washington Commanders | Cincinnati Bengals -1.5 (-110) / Washington Commanders +1.5 (-110) | 52.5 (O -110 / U -110) | Cincinnati Bengals -122 / Washington Commanders +102 |
| Thu 11/26 01:00 PM | Chicago Bears at Detroit Lions | Chicago Bears +2.5 (-105) / Detroit Lions -2.5 (-115) | 52.5 (O -110 / U -110) | Chicago Bears +120 / Detroit Lions -142 |
| Thu 11/26 03:30 PM | Philadelphia Eagles at Dallas Cowboys | Philadelphia Eagles +1.5 (-110) / Dallas Cowboys -1.5 (-110) | 49.5 (O -110 / U -110) | Philadelphia Eagles +105 / Dallas Cowboys -125 |
| Thu 11/26 08:20 PM | Kansas City Chiefs at Buffalo Bills | Kansas City Chiefs +2.5 (-105) / Buffalo Bills -2.5 (-115) | 50.5 (O -110 / U -110) | Kansas City Chiefs +124 / Buffalo Bills -148 |
| Fri 11/27 03:00 PM | Denver Broncos at Pittsburgh Steelers | Denver Broncos -1.5 (-110) / Pittsburgh Steelers +1.5 (-110) | 39.5 (O -110 / U -110) | Denver Broncos -122 / Pittsburgh Steelers +102 |
| Sun 11/29 01:00 PM | Atlanta Falcons at Minnesota Vikings | Atlanta Falcons +4.5 (-110) / Minnesota Vikings -4.5 (-110) | 43.5 (O -110 / U -110) | Atlanta Falcons +180 / Minnesota Vikings -218 |
| Sun 11/29 01:00 PM | Baltimore Ravens at Houston Texans | Baltimore Ravens +1.5 (-110) / Houston Texans -1.5 (-110) | 45.5 (O -110 / U -110) | Baltimore Ravens +102 / Houston Texans -122 |
| Sun 11/29 01:00 PM | New Orleans Saints at Cincinnati Bengals | New Orleans Saints +6.5 (-110) / Cincinnati Bengals -6.5 (-110) | 48.5 (O -110 / U -110) | New Orleans Saints +235 / Cincinnati Bengals -290 |
| Sun 11/29 01:00 PM | Las Vegas Raiders at Cleveland Browns | Las Vegas Raiders +1.5 (-110) / Cleveland Browns -1.5 (-110) | 39.5 (O -110 / U -110) | Las Vegas Raiders +102 / Cleveland Browns -122 |
| Sun 11/29 01:00 PM | New York Giants at Indianapolis Colts | New York Giants +2.5 (-110) / Indianapolis Colts -2.5 (-110) | 47.5 (O -110 / U -110) | New York Giants +114 / Indianapolis Colts -135 |
| Sun 11/29 01:00 PM | Tennessee Titans at Jacksonville Jaguars | Tennessee Titans +5.5 (-110) / Jacksonville Jaguars -5.5 (-110) | 45.5 (O -110 / U -110) | Tennessee Titans +195 / Jacksonville Jaguars -238 |
| Sun 11/29 01:00 PM | New York Jets at Miami Dolphins | New York Jets +1.5 (-110) / Miami Dolphins -1.5 (-110) | 40.5 (O -110 / U -110) | New York Jets +105 / Miami Dolphins -125 |
| Sun 11/29 04:25 PM | Washington Commanders at Arizona Cardinals | Washington Commanders -4.5 (-110) / Arizona Cardinals +4.5 (-110) | 47.5 (O -110 / U -110) | Washington Commanders -218 / Arizona Cardinals +180 |
| Mon 11/30 08:15 PM | Carolina Panthers at Tampa Bay Buccaneers | Carolina Panthers +3.5 (-110) / Tampa Bay Buccaneers -3.5 (-110) | 44.5 (O -110 / U -110) | Carolina Panthers +164 / Tampa Bay Buccaneers -198 |
| Sun 12/06 01:00 PM | Detroit Lions at Atlanta Falcons | Detroit Lions -3.5 (-110) / Atlanta Falcons +3.5 (-110) | 48.5 (O -110 / U -110) | Detroit Lions -185 / Atlanta Falcons +154 |
| Sun 12/06 01:00 PM | Jacksonville Jaguars at Chicago Bears | Jacksonville Jaguars +3 (-115) / Chicago Bears -3 (-105) | 47.5 (O -110 / U -110) | Jacksonville Jaguars +130 / Chicago Bears -155 |
| Sun 12/06 01:00 PM | Cincinnati Bengals at Cleveland Browns | Cincinnati Bengals -4.5 (-110) / Cleveland Browns +4.5 (-110) | 45.5 (O -110 / U -110) | Cincinnati Bengals -218 / Cleveland Browns +180 |
| Sun 12/06 01:00 PM | Miami Dolphins at Denver Broncos | Miami Dolphins +9.5 (-110) / Denver Broncos -9.5 (-110) | 42.5 (O -110 / U -110) | Miami Dolphins +360 / Denver Broncos -470 |
| Sun 12/06 01:00 PM | Green Bay Packers at New Orleans Saints | Green Bay Packers -4.5 (-110) / New Orleans Saints +4.5 (-110) | 45.5 (O -110 / U -110) | Green Bay Packers -225 / New Orleans Saints +185 |
| Sun 12/06 01:00 PM | Los Angeles Chargers at Tampa Bay Buccaneers | Los Angeles Chargers -2.5 (-110) / Tampa Bay Buccaneers +2.5 (-110) | 46.5 (O -110 / U -110) | Los Angeles Chargers -135 / Tampa Bay Buccaneers +114 |
| Sun 12/06 01:00 PM | Washington Commanders at Tennessee Titans | Washington Commanders -1.5 (-110) / Tennessee Titans +1.5 (-110) | 46.5 (O -110 / U -110) | Washington Commanders -125 / Tennessee Titans +105 |
| Sun 12/06 04:05 PM | Philadelphia Eagles at Arizona Cardinals | Philadelphia Eagles -8.5 (-110) / Arizona Cardinals +8.5 (-110) | 43.5 (O -110 / U -110) | Philadelphia Eagles -395 / Arizona Cardinals +310 |
| Sun 12/06 04:25 PM | Carolina Panthers at Minnesota Vikings | Carolina Panthers +3.5 (-110) / Minnesota Vikings -3.5 (-110) | 42.5 (O -110 / U -110) | Carolina Panthers +160 / Minnesota Vikings -192 |
| Sun 12/06 08:20 PM | Houston Texans at Pittsburgh Steelers | Houston Texans -1.5 (-110) / Pittsburgh Steelers +1.5 (-110) | 41.5 (O -110 / U -110) | Houston Texans -122 / Pittsburgh Steelers +102 |
| Sun 12/13 01:00 PM | Atlanta Falcons at Cleveland Browns | Atlanta Falcons +1.5 (-110) / Cleveland Browns -1.5 (-110) | 40.5 (O -110 / U -110) | Atlanta Falcons +102 / Cleveland Browns -122 |
| Sun 12/13 01:00 PM | Tampa Bay Buccaneers at Baltimore Ravens | Tampa Bay Buccaneers +6 (-110) / Baltimore Ravens -6 (-110) | 48.5 (O -110 / U -110) | Tampa Bay Buccaneers +210 / Baltimore Ravens -258 |
| Sun 12/13 01:00 PM | New Orleans Saints at Carolina Panthers | New Orleans Saints +2.5 (-110) / Carolina Panthers -2.5 (-110) | 43.5 (O -110 / U -110) | New Orleans Saints +120 / Carolina Panthers -142 |
| Sun 12/13 01:00 PM | Chicago Bears at Miami Dolphins | Chicago Bears -5.5 (-110) / Miami Dolphins +5.5 (-110) | 46.5 (O -110 / U -110) | Chicago Bears -250 / Miami Dolphins +205 |
| Sun 12/13 01:00 PM | Denver Broncos at New York Jets | Denver Broncos -5.5 (-110) / New York Jets +5.5 (-110) | 39.5 (O -110 / U -110) | Denver Broncos -230 / New York Jets +190 |
| Sun 12/13 01:00 PM | Tennessee Titans at Detroit Lions | Tennessee Titans +7.5 (-110) / Detroit Lions -7.5 (-110) | 47.5 (O -110 / U -110) | Tennessee Titans +285 / Detroit Lions -360 |
| Sun 12/13 01:00 PM | Houston Texans at Washington Commanders | Houston Texans -1.5 (-110) / Washington Commanders +1.5 (-110) | 44.5 (O -110 / U -110) | Houston Texans -122 / Washington Commanders +102 |
| Sun 12/13 01:00 PM | Indianapolis Colts at Philadelphia Eagles | Indianapolis Colts +5.5 (-110) / Philadelphia Eagles -5.5 (-110) | 46.5 (O -110 / U -110) | Indianapolis Colts +205 / Philadelphia Eagles -250 |
| Sun 12/13 04:05 PM | Los Angeles Chargers at Las Vegas Raiders | Los Angeles Chargers -5.5 (-110) / Las Vegas Raiders +5.5 (-110) | 43.5 (O -110 / U -110) | Los Angeles Chargers -230 / Las Vegas Raiders +190 |
| Sun 12/13 04:25 PM | Kansas City Chiefs at Cincinnati Bengals | Kansas City Chiefs +1.5 (-110) / Cincinnati Bengals -1.5 (-110) | 48.5 (O -110 / U -110) | Kansas City Chiefs +105 / Cincinnati Bengals -125 |
| Sun 12/13 08:20 PM | Buffalo Bills at Green Bay Packers | Buffalo Bills +1.5 (-110) / Green Bay Packers -1.5 (-110) | 49.5 (O -110 / U -110) | Buffalo Bills +105 / Green Bay Packers -125 |
| Mon 12/14 08:15 PM | Pittsburgh Steelers at Jacksonville Jaguars | Pittsburgh Steelers +3 (-110) / Jacksonville Jaguars -3 (-110) | 44.5 (O -110 / U -110) | Pittsburgh Steelers +136 / Jacksonville Jaguars -162 |
| Sat 12/19 08:20 PM | Chicago Bears at Buffalo Bills | Chicago Bears +3.5 (-110) / Buffalo Bills -3.5 (-110) | 51.5 (O -110 / U -110) | Chicago Bears +154 / Buffalo Bills -185 |
| Sun 12/20 01:00 PM | Atlanta Falcons at Washington Commanders | Atlanta Falcons +3.5 (-110) / Washington Commanders -3.5 (-110) | 46.5 (O -110 / U -110) | Atlanta Falcons +154 / Washington Commanders -185 |
| Sun 12/20 01:00 PM | Baltimore Ravens at Pittsburgh Steelers | Baltimore Ravens -2.5 (-120) / Pittsburgh Steelers +2.5 (+100) | 46.5 (O -110 / U -110) | Baltimore Ravens -148 / Pittsburgh Steelers +124 |
| Sun 12/20 01:00 PM | Cincinnati Bengals at Carolina Panthers | Cincinnati Bengals -2.5 (-120) / Carolina Panthers +2.5 (+100) | 47.5 (O -110 / U -110) | Cincinnati Bengals -148 / Carolina Panthers +124 |
| Sun 12/20 01:00 PM | Cleveland Browns at New York Giants | Cleveland Browns +4.5 (-110) / New York Giants -4.5 (-110) | 40.5 (O -110 / U -110) | Cleveland Browns +180 / New York Giants -218 |
| Sun 12/20 01:00 PM | Miami Dolphins at Green Bay Packers | Miami Dolphins +10.5 (-110) / Green Bay Packers -10.5 (-110) | 45.5 (O -110 / U -110) | Miami Dolphins +470 / Green Bay Packers -650 |
| Sun 12/20 01:00 PM | Jacksonville Jaguars at Houston Texans | Jacksonville Jaguars +3 (-110) / Houston Texans -3 (-110) | 43.5 (O -110 / U -110) | Jacksonville Jaguars +130 / Houston Texans -155 |
| Sun 12/20 01:00 PM | Indianapolis Colts at Tennessee Titans | Indianapolis Colts -1.5 (-110) / Tennessee Titans +1.5 (-110) | 47.5 (O -110 / U -110) | Indianapolis Colts -125 / Tennessee Titans +105 |
| Sun 12/20 01:00 PM | New Orleans Saints at Tampa Bay Buccaneers | New Orleans Saints +3.5 (-110) / Tampa Bay Buccaneers -3.5 (-110) | 45.5 (O -110 / U -110) | New Orleans Saints +160 / Tampa Bay Buccaneers -192 |
| Sun 12/20 04:05 PM | New York Jets at Arizona Cardinals | New York Jets +1.5 (-125) / Arizona Cardinals -1.5 (+105) | 41.5 (O -110 / U -110) | New York Jets -110 / Arizona Cardinals -110 |
| Sun 12/20 04:25 PM | Denver Broncos at Las Vegas Raiders | Denver Broncos -4.5 (-110) / Las Vegas Raiders +4.5 (-110) | 41.5 (O -110 / U -110) | Denver Broncos -205 / Las Vegas Raiders +170 |
| Sun 12/20 08:20 PM | Detroit Lions at Minnesota Vikings | Detroit Lions -1.5 (-110) / Minnesota Vikings +1.5 (-110) | 46.5 (O -110 / U -110) | Detroit Lions -122 / Minnesota Vikings +102 |
| Thu 12/24 08:15 PM | Houston Texans at Philadelphia Eagles | Houston Texans +2.5 (-112) / Philadelphia Eagles -2.5 (-108) | 37.5 (O -110 / U -110) | Houston Texans +114 / Philadelphia Eagles -135 |
| Fri 12/25 01:00 PM | Green Bay Packers at Chicago Bears | Green Bay Packers +1.5 (-115) / Chicago Bears -1.5 (-105) | 47.5 (O -110 / U -110) | Green Bay Packers -102 / Chicago Bears -118 |
| Fri 12/25 04:30 PM | Buffalo Bills at Denver Broncos | Buffalo Bills -1.5 (-115) / Denver Broncos +1.5 (-105) | 46.5 (O -110 / U -110) | Buffalo Bills -130 / Denver Broncos +110 |
| Sun 12/27 01:00 PM | Arizona Cardinals at New Orleans Saints | Arizona Cardinals +5.5 (-110) / New Orleans Saints -5.5 (-110) | 44.5 (O -110 / U -110) | Arizona Cardinals +200 / New Orleans Saints -245 |
| Sun 12/27 01:00 PM | Tampa Bay Buccaneers at Atlanta Falcons | Tampa Bay Buccaneers -1.5 (-110) / Atlanta Falcons +1.5 (-110) | 45.5 (O -110 / U -110) | Tampa Bay Buccaneers -125 / Atlanta Falcons +105 |
| Sun 12/27 01:00 PM | Cleveland Browns at Baltimore Ravens | Cleveland Browns +10 (-110) / Baltimore Ravens -10 (-110) | 43.5 (O -110 / U -110) | Cleveland Browns +330 / Baltimore Ravens -425 |
| Sun 12/27 01:00 PM | Carolina Panthers at Pittsburgh Steelers | Carolina Panthers +3.5 (-110) / Pittsburgh Steelers -3.5 (-110) | 41.5 (O -110 / U -110) | Carolina Panthers +160 / Pittsburgh Steelers -192 |
| Sun 12/27 01:00 PM | Cincinnati Bengals at Indianapolis Colts | Cincinnati Bengals -1.5 (-110) / Indianapolis Colts +1.5 (-110) | 52.5 (O -110 / U -110) | Cincinnati Bengals -125 / Indianapolis Colts +105 |
| Sun 12/27 01:00 PM | Tennessee Titans at Las Vegas Raiders | Tennessee Titans +1.5 (-110) / Las Vegas Raiders -1.5 (-110) | 42.5 (O -110 / U -110) | Tennessee Titans +105 / Las Vegas Raiders -125 |
| Sun 12/27 01:00 PM | Los Angeles Chargers at Miami Dolphins | Los Angeles Chargers -7 (-112) / Miami Dolphins +7 (-108) | 45.5 (O -110 / U -110) | Los Angeles Chargers -375 / Miami Dolphins +295 |
| Sun 12/27 01:00 PM | Washington Commanders at Minnesota Vikings | Washington Commanders +2.5 (-110) / Minnesota Vikings -2.5 (-110) | 46.5 (O -110 / U -110) | Washington Commanders +114 / Minnesota Vikings -135 |
| Sun 12/27 08:20 PM | Jacksonville Jaguars at Dallas Cowboys | Jacksonville Jaguars +3 (-118) / Dallas Cowboys -3 (-102) | 51.5 (O -110 / U -110) | Jacksonville Jaguars +136 / Dallas Cowboys -162 |
| Mon 12/28 08:15 PM | New York Giants at Detroit Lions | New York Giants +4.5 (-110) / Detroit Lions -4.5 (-110) | 49.5 (O -110 / U -110) | New York Giants +170 / Detroit Lions -205 |
| Thu 12/31 08:15 PM | Baltimore Ravens at Cincinnati Bengals | Baltimore Ravens +2.5 (-110) / Cincinnati Bengals -2.5 (-110) | 51.5 (O -110 / U -110) | Baltimore Ravens +114 / Cincinnati Bengals -135 |
| Sun 01/03 01:00 PM | New Orleans Saints at Atlanta Falcons | New Orleans Saints +1.5 (-110) / Atlanta Falcons -1.5 (-110) | 44.5 (O -110 / U -110) | New Orleans Saints +102 / Atlanta Falcons -122 |
| Sun 01/03 01:00 PM | Buffalo Bills at Miami Dolphins | Buffalo Bills -7.5 (-110) / Miami Dolphins +7.5 (-110) | 47.5 (O -110 / U -110) | Buffalo Bills -380 / Miami Dolphins +300 |
| Sun 01/03 01:00 PM | Indianapolis Colts at Cleveland Browns | Indianapolis Colts -2.5 (-110) / Cleveland Browns +2.5 (-110) | 43.5 (O -110 / U -110) | Indianapolis Colts -135 / Cleveland Browns +114 |
| Sun 01/03 01:00 PM | New York Giants at Dallas Cowboys | New York Giants +4.5 (-110) / Dallas Cowboys -4.5 (-110) | 49.5 (O -110 / U -110) | New York Giants +180 / Dallas Cowboys -218 |
| Sun 01/03 01:00 PM | Washington Commanders at Jacksonville Jaguars | Washington Commanders +3.5 (-110) / Jacksonville Jaguars -3.5 (-110) | 48.5 (O -110 / U -110) | Washington Commanders +154 / Jacksonville Jaguars -185 |
| Sun 01/03 01:00 PM | Minnesota Vikings at New York Jets | Minnesota Vikings -3.5 (-110) / New York Jets +3.5 (-110) | 39.5 (O -110 / U -110) | Minnesota Vikings -192 / New York Jets +160 |
| Sun 01/03 01:00 PM | Pittsburgh Steelers at Tennessee Titans | Pittsburgh Steelers -1.5 (-110) / Tennessee Titans +1.5 (-110) | 42.5 (O -110 / U -110) | Pittsburgh Steelers -125 / Tennessee Titans +105 |
| Sun 01/03 04:05 PM | Las Vegas Raiders at Arizona Cardinals | Las Vegas Raiders -1.5 (-115) / Arizona Cardinals +1.5 (-105) | 42.5 (O -110 / U -110) | Las Vegas Raiders -130 / Arizona Cardinals +110 |
| Sun 01/03 04:25 PM | Detroit Lions at Chicago Bears | Detroit Lions +1.5 (-110) / Chicago Bears -1.5 (-110) | 49.5 (O -110 / U -110) | Detroit Lions +102 / Chicago Bears -122 |
| Sun 01/03 04:25 PM | Kansas City Chiefs at Los Angeles Chargers | Kansas City Chiefs +1.5 (-110) / Los Angeles Chargers -1.5 (-110) | 45.5 (O -110 / U -110) | Kansas City Chiefs +105 / Los Angeles Chargers -125 |
| Mon 01/04 08:15 PM | Houston Texans at Green Bay Packers | Houston Texans +2.5 (-110) / Green Bay Packers -2.5 (-110) | 42.5 (O -110 / U -110) | Houston Texans +114 / Green Bay Packers -135 |
| Sun 01/10 01:00 PM | Atlanta Falcons at Carolina Panthers | Atlanta Falcons +2.5 (-110) / Carolina Panthers -2.5 (-110) | 41.5 (O -110 / U -110) | Atlanta Falcons +114 / Carolina Panthers -135 |
| Sun 01/10 01:00 PM | Pittsburgh Steelers at Baltimore Ravens | Pittsburgh Steelers +5.5 (-110) / Baltimore Ravens -5.5 (-110) | 43.5 (O -110 / U -110) | Pittsburgh Steelers +190 / Baltimore Ravens -230 |
| Sun 01/10 01:00 PM | New York Jets at Buffalo Bills | New York Jets +10 (-110) / Buffalo Bills -10 (-110) | 43.5 (O -110 / U -110) | New York Jets +360 / Buffalo Bills -470 |
| Sun 01/10 01:00 PM | Chicago Bears at Minnesota Vikings | Chicago Bears +1.5 (-110) / Minnesota Vikings -1.5 (-110) | 43.5 (O -110 / U -110) | Chicago Bears +105 / Minnesota Vikings -125 |
| Sun 01/10 01:00 PM | Cleveland Browns at Cincinnati Bengals | Cleveland Browns +7.5 (-110) / Cincinnati Bengals -7.5 (-110) | 43.5 (O -110 / U -110) | Cleveland Browns +285 / Cincinnati Bengals -360 |
| Sun 01/10 01:00 PM | Dallas Cowboys at Washington Commanders | Dallas Cowboys -1.5 (-110) / Washington Commanders +1.5 (-110) | 49.5 (O -110 / U -110) | Dallas Cowboys -122 / Washington Commanders +102 |
| Sun 01/10 01:00 PM | Los Angeles Chargers at Denver Broncos | Los Angeles Chargers +1.5 (-110) / Denver Broncos -1.5 (-110) | 41.5 (O -110 / U -110) | Los Angeles Chargers +102 / Denver Broncos -122 |
| Sun 01/10 01:00 PM | Detroit Lions at Green Bay Packers | Detroit Lions +2.5 (-110) / Green Bay Packers -2.5 (-110) | 47.5 (O -110 / U -110) | Detroit Lions +114 / Green Bay Packers -135 |
| Sun 01/10 01:00 PM | Tennessee Titans at Houston Texans | Tennessee Titans +7 (-110) / Houston Texans -7 (-110) | 39.5 (O -110 / U -110) | Tennessee Titans +240 / Houston Texans -298 |
| Sun 01/10 01:00 PM | Jacksonville Jaguars at Indianapolis Colts | Jacksonville Jaguars +1.5 (-110) / Indianapolis Colts -1.5 (-110) | 46.5 (O -110 / U -110) | Jacksonville Jaguars +102 / Indianapolis Colts -122 |
| Sun 01/10 01:00 PM | Las Vegas Raiders at Kansas City Chiefs | Las Vegas Raiders +8.5 (-110) / Kansas City Chiefs -8.5 (-110) | 40.5 (O -110 / U -110) | Las Vegas Raiders +320 / Kansas City Chiefs -410 |
| Sun 01/10 01:00 PM | Tampa Bay Buccaneers at New Orleans Saints | Tampa Bay Buccaneers -1.5 (-110) / New Orleans Saints +1.5 (-110) | 43.5 (O -110 / U -110) | Tampa Bay Buccaneers -125 / New Orleans Saints +105 |
| Sun 01/10 01:00 PM | Philadelphia Eagles at New York Giants | Philadelphia Eagles -3 (-110) / New York Giants +3 (-110) | 41.5 (O -110 / U -110) | Philadelphia Eagles -162 / New York Giants +136 |

## FanDuel NFL lines (line shopping)

VERIFIED FANDUEL NFL lines via The Odds API, fetched 2026-09-12 13:43 UTC. Requests remaining this month: 485

| Kickoff (ET) | Game | Spread | Total | Moneyline |
|---|---|---|---|---|
| Sun 09/13 01:00 PM | Atlanta Falcons at Pittsburgh Steelers | Atlanta Falcons +5.5 (-104) / Pittsburgh Steelers -5.5 (-118) | 40.5 (O -118 / U -104) | Atlanta Falcons +235 / Pittsburgh Steelers -290 |
| Sun 09/13 01:00 PM | Baltimore Ravens at Indianapolis Colts | Baltimore Ravens -3.5 (-102) / Indianapolis Colts +3.5 (-120) | 47.5 (O -114 / U -106) | Baltimore Ravens -176 / Indianapolis Colts +148 |
| Sun 09/13 01:00 PM | Buffalo Bills at Houston Texans | Buffalo Bills -1.5 (-105) / Houston Texans +1.5 (-115) | 44.5 (O -115 / U -105) | Buffalo Bills -118 / Houston Texans +100 |
| Sun 09/13 01:00 PM | Chicago Bears at Carolina Panthers | Chicago Bears -3 (-115) / Carolina Panthers +3 (-105) | 47.5 (O -102 / U -120) | Chicago Bears -176 / Carolina Panthers +148 |
| Sun 09/13 01:00 PM | Tampa Bay Buccaneers at Cincinnati Bengals | Tampa Bay Buccaneers +3.5 (-105) / Cincinnati Bengals -3.5 (-115) | 50.5 (O -112 / U -108) | Tampa Bay Buccaneers +172 / Cincinnati Bengals -205 |
| Sun 09/13 01:00 PM | Cleveland Browns at Jacksonville Jaguars | Cleveland Browns +8.5 (-108) / Jacksonville Jaguars -8.5 (-112) | 40.5 (O -102 / U -120) | Cleveland Browns +360 / Jacksonville Jaguars -460 |
| Sun 09/13 01:00 PM | New Orleans Saints at Detroit Lions | New Orleans Saints +6.5 (+100) / Detroit Lions -6.5 (-122) | 49.5 (O -115 / U -105) | New Orleans Saints +270 / Detroit Lions -335 |
| Sun 09/13 01:00 PM | New York Jets at Tennessee Titans | New York Jets +1.5 (-112) / Tennessee Titans -1.5 (-108) | 38.5 (O -110 / U -110) | New York Jets +100 / Tennessee Titans -118 |
| Sun 09/13 04:25 PM | Arizona Cardinals at Los Angeles Chargers | Arizona Cardinals +9.5 (-115) / Los Angeles Chargers -9.5 (-105) | 47.5 (O -104 / U -118) | Arizona Cardinals +380 / Los Angeles Chargers -490 |
| Sun 09/13 04:25 PM | Green Bay Packers at Minnesota Vikings | Green Bay Packers +1.5 (-110) / Minnesota Vikings -1.5 (-110) | 46.5 (O -108 / U -112) | Green Bay Packers +108 / Minnesota Vikings -126 |
| Sun 09/13 04:25 PM | Miami Dolphins at Las Vegas Raiders | Miami Dolphins +3 (-108) / Las Vegas Raiders -3 (-112) | 39.5 (O -118 / U -104) | Miami Dolphins +138 / Las Vegas Raiders -164 |
| Sun 09/13 04:25 PM | Washington Commanders at Philadelphia Eagles | Washington Commanders +5.5 (-110) / Philadelphia Eagles -5.5 (-110) | 44.5 (O -105 / U -115) | Washington Commanders +205 / Philadelphia Eagles -250 |
| Sun 09/13 08:20 PM | Dallas Cowboys at New York Giants | Dallas Cowboys -3 (-108) / New York Giants +3 (-112) | 48.5 (O -105 / U -115) | Dallas Cowboys -158 / New York Giants +134 |
| Mon 09/14 08:15 PM | Denver Broncos at Kansas City Chiefs | Denver Broncos +2.5 (-110) / Kansas City Chiefs -2.5 (-110) | 43.5 (O -112 / U -108) | Denver Broncos +114 / Kansas City Chiefs -134 |
| Thu 09/17 08:15 PM | Detroit Lions at Buffalo Bills | Detroit Lions +3.5 (-110) / Buffalo Bills -3.5 (-110) | 52.5 (O -110 / U -110) | Detroit Lions +164 / Buffalo Bills -196 |
| Sun 09/20 01:00 PM | Carolina Panthers at Atlanta Falcons | Carolina Panthers +1.5 (-122) / Atlanta Falcons -1.5 (+100) | 42.5 (O -110 / U -110) | Carolina Panthers -108 / Atlanta Falcons -108 |
| Sun 09/20 01:00 PM | New Orleans Saints at Baltimore Ravens | New Orleans Saints +8.5 (-118) / Baltimore Ravens -8.5 (-104) | 46.5 (O -118 / U -104) | New Orleans Saints +360 / Baltimore Ravens -460 |
| Sun 09/20 01:00 PM | Minnesota Vikings at Chicago Bears | Minnesota Vikings +3 (-110) / Chicago Bears -3 (-110) | 46.5 (O -110 / U -110) | Minnesota Vikings +138 / Chicago Bears -164 |
| Sun 09/20 01:00 PM | Cincinnati Bengals at Houston Texans | Cincinnati Bengals +2.5 (-110) / Houston Texans -2.5 (-110) | 46.5 (O -110 / U -110) | Cincinnati Bengals +116 / Houston Texans -136 |
| Sun 09/20 01:00 PM | Cleveland Browns at Tampa Bay Buccaneers | Cleveland Browns +6.5 (-102) / Tampa Bay Buccaneers -6.5 (-120) | 40.5 (O -105 / U -115) | Cleveland Browns +265 / Tampa Bay Buccaneers -330 |
| Sun 09/20 01:00 PM | Green Bay Packers at New York Jets | Green Bay Packers -5.5 (-110) / New York Jets +5.5 (-110) | 42.5 (O -118 / U -104) | Green Bay Packers -245 / New York Jets +200 |
| Sun 09/20 01:00 PM | Pittsburgh Steelers at New England Patriots | n/a | n/a | n/a |
| Sun 09/20 01:00 PM | Philadelphia Eagles at Tennessee Titans | Philadelphia Eagles -5.5 (-110) / Tennessee Titans +5.5 (-110) | 41.5 (O -115 / U -105) | Philadelphia Eagles -255 / Tennessee Titans +210 |
| Sun 09/20 04:05 PM | Jacksonville Jaguars at Denver Broncos | Jacksonville Jaguars +2.5 (-106) / Denver Broncos -2.5 (-114) | 44.5 (O -118 / U -104) | Jacksonville Jaguars +120 / Denver Broncos -142 |
| Sun 09/20 04:05 PM | Las Vegas Raiders at Los Angeles Chargers | Las Vegas Raiders +9.5 (-114) / Los Angeles Chargers -9.5 (-106) | 42.5 (O -105 / U -115) | Las Vegas Raiders +400 / Los Angeles Chargers -520 |
| Sun 09/20 04:25 PM | Washington Commanders at Dallas Cowboys | Washington Commanders +4.5 (-105) / Dallas Cowboys -4.5 (-115) | 51.5 (O -115 / U -105) | Washington Commanders +190 / Dallas Cowboys -230 |
| Sun 09/20 08:20 PM | Indianapolis Colts at Kansas City Chiefs | Indianapolis Colts +5.5 (-110) / Kansas City Chiefs -5.5 (-110) | 46.5 (O -110 / U -110) | Indianapolis Colts +205 / Kansas City Chiefs -250 |
| Thu 09/24 08:15 PM | Atlanta Falcons at Green Bay Packers | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Los Angeles Chargers at Buffalo Bills | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Carolina Panthers at Cleveland Browns | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Cincinnati Bengals at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | New York Jets at Detroit Lions | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Houston Texans at Indianapolis Colts | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Kansas City Chiefs at Miami Dolphins | n/a | n/a | n/a |
| Sun 09/27 01:00 PM | Tennessee Titans at New York Giants | n/a | n/a | n/a |
| Sun 09/27 04:05 PM | Minnesota Vikings at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 09/27 04:25 PM | Baltimore Ravens at Dallas Cowboys | n/a | n/a | n/a |
| Sun 09/27 04:25 PM | Las Vegas Raiders at New Orleans Saints | n/a | n/a | n/a |
| Mon 09/28 08:15 PM | Philadelphia Eagles at Chicago Bears | n/a | n/a | n/a |
| Thu 10/01 08:15 PM | Pittsburgh Steelers at Cleveland Browns | n/a | n/a | n/a |
| Sun 10/04 09:30 AM | Indianapolis Colts at Washington Commanders | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | Arizona Cardinals at New York Giants | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | Tennessee Titans at Baltimore Ravens | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | New York Jets at Chicago Bears | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | Jacksonville Jaguars at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | Dallas Cowboys at Houston Texans | n/a | n/a | n/a |
| Sun 10/04 01:00 PM | Green Bay Packers at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 10/04 04:05 PM | Miami Dolphins at Minnesota Vikings | n/a | n/a | n/a |
| Sun 10/04 04:25 PM | Kansas City Chiefs at Las Vegas Raiders | n/a | n/a | n/a |
| Sun 10/04 08:20 PM | Detroit Lions at Carolina Panthers | n/a | n/a | n/a |
| Mon 10/05 08:15 PM | Atlanta Falcons at New Orleans Saints | n/a | n/a | n/a |
| Thu 10/08 08:15 PM | Tampa Bay Buccaneers at Dallas Cowboys | n/a | n/a | n/a |
| Sun 10/11 09:30 AM | Philadelphia Eagles at Jacksonville Jaguars | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | Cincinnati Bengals at Miami Dolphins | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | Cleveland Browns at New York Jets | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | Houston Texans at Tennessee Titans | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | Indianapolis Colts at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | Minnesota Vikings at New Orleans Saints | n/a | n/a | n/a |
| Sun 10/11 01:00 PM | New York Giants at Washington Commanders | n/a | n/a | n/a |
| Sun 10/11 04:05 PM | Denver Broncos at Los Angeles Chargers | n/a | n/a | n/a |
| Sun 10/11 04:25 PM | Detroit Lions at Arizona Cardinals | n/a | n/a | n/a |
| Sun 10/11 04:25 PM | Chicago Bears at Green Bay Packers | n/a | n/a | n/a |
| Sun 10/11 08:20 PM | Baltimore Ravens at Atlanta Falcons | n/a | n/a | n/a |
| Sun 10/18 09:30 AM | Houston Texans at Jacksonville Jaguars | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | Chicago Bears at Atlanta Falcons | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | Baltimore Ravens at Cleveland Browns | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | Carolina Panthers at Philadelphia Eagles | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | Tennessee Titans at Indianapolis Colts | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | New Orleans Saints at New York Giants | n/a | n/a | n/a |
| Sun 10/18 01:00 PM | Pittsburgh Steelers at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 10/18 04:25 PM | Buffalo Bills at Las Vegas Raiders | n/a | n/a | n/a |
| Sun 10/18 04:25 PM | Los Angeles Chargers at Kansas City Chiefs | n/a | n/a | n/a |
| Sun 10/18 08:20 PM | Dallas Cowboys at Green Bay Packers | n/a | n/a | n/a |
| Sun 10/25 09:30 AM | Pittsburgh Steelers at New Orleans Saints | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | Cincinnati Bengals at Baltimore Ravens | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | Tampa Bay Buccaneers at Carolina Panthers | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | Cleveland Browns at Tennessee Titans | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | New York Giants at Houston Texans | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | Indianapolis Colts at Minnesota Vikings | n/a | n/a | n/a |
| Sun 10/25 01:00 PM | Miami Dolphins at New York Jets | n/a | n/a | n/a |
| Sun 10/25 04:05 PM | Denver Broncos at Arizona Cardinals | n/a | n/a | n/a |
| Sun 10/25 04:25 PM | Green Bay Packers at Detroit Lions | n/a | n/a | n/a |
| Mon 10/26 08:15 PM | Dallas Cowboys at Philadelphia Eagles | n/a | n/a | n/a |
| Thu 10/29 08:15 PM | Carolina Panthers at Green Bay Packers | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Arizona Cardinals at Dallas Cowboys | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Atlanta Falcons at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Baltimore Ravens at Buffalo Bills | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Tennessee Titans at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Cleveland Browns at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Minnesota Vikings at Detroit Lions | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Indianapolis Colts at Jacksonville Jaguars | n/a | n/a | n/a |
| Sun 11/01 01:00 PM | Las Vegas Raiders at New York Jets | n/a | n/a | n/a |
| Sun 11/01 04:25 PM | Kansas City Chiefs at Denver Broncos | n/a | n/a | n/a |
| Sun 11/01 08:20 PM | Philadelphia Eagles at Washington Commanders | n/a | n/a | n/a |
| Thu 11/05 08:15 PM | Jacksonville Jaguars at Baltimore Ravens | n/a | n/a | n/a |
| Sun 11/08 09:30 AM | Cincinnati Bengals at Atlanta Falcons | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | Denver Broncos at Carolina Panthers | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | Cleveland Browns at New Orleans Saints | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | Dallas Cowboys at Indianapolis Colts | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | Detroit Lions at Miami Dolphins | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | New York Jets at Kansas City Chiefs | n/a | n/a | n/a |
| Sun 11/08 01:00 PM | New York Giants at Philadelphia Eagles | n/a | n/a | n/a |
| Sun 11/08 04:05 PM | Houston Texans at Los Angeles Chargers | n/a | n/a | n/a |
| Sun 11/08 08:20 PM | Tampa Bay Buccaneers at Chicago Bears | n/a | n/a | n/a |
| Mon 11/09 08:15 PM | Buffalo Bills at Minnesota Vikings | n/a | n/a | n/a |
| Thu 11/12 08:15 PM | Washington Commanders at New York Giants | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Kansas City Chiefs at Atlanta Falcons | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Buffalo Bills at New York Jets | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Carolina Panthers at New Orleans Saints | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Houston Texans at Cleveland Browns | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Minnesota Vikings at Green Bay Packers | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Miami Dolphins at Indianapolis Colts | n/a | n/a | n/a |
| Sun 11/15 01:00 PM | Jacksonville Jaguars at Tennessee Titans | n/a | n/a | n/a |
| Sun 11/15 08:20 PM | Pittsburgh Steelers at Cincinnati Bengals | n/a | n/a | n/a |
| Mon 11/16 08:15 PM | Los Angeles Chargers at Baltimore Ravens | n/a | n/a | n/a |
| Thu 11/19 08:15 PM | Indianapolis Colts at Houston Texans | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Arizona Cardinals at Kansas City Chiefs | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Baltimore Ravens at Carolina Panthers | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Miami Dolphins at Buffalo Bills | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | New Orleans Saints at Chicago Bears | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Tennessee Titans at Dallas Cowboys | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Tampa Bay Buccaneers at Detroit Lions | n/a | n/a | n/a |
| Sun 11/22 01:00 PM | Jacksonville Jaguars at New York Giants | n/a | n/a | n/a |
| Sun 11/22 04:05 PM | New York Jets at Los Angeles Chargers | n/a | n/a | n/a |
| Sun 11/22 04:25 PM | Las Vegas Raiders at Denver Broncos | n/a | n/a | n/a |
| Sun 11/22 04:25 PM | Pittsburgh Steelers at Philadelphia Eagles | n/a | n/a | n/a |
| Mon 11/23 08:15 PM | Cincinnati Bengals at Washington Commanders | n/a | n/a | n/a |
| Thu 11/26 01:00 PM | Chicago Bears at Detroit Lions | n/a | n/a | n/a |
| Thu 11/26 03:30 PM | Philadelphia Eagles at Dallas Cowboys | n/a | n/a | n/a |
| Thu 11/26 08:20 PM | Kansas City Chiefs at Buffalo Bills | n/a | n/a | n/a |
| Fri 11/27 03:00 PM | Denver Broncos at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | Atlanta Falcons at Minnesota Vikings | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | Baltimore Ravens at Houston Texans | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | New Orleans Saints at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | Las Vegas Raiders at Cleveland Browns | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | New York Giants at Indianapolis Colts | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | Tennessee Titans at Jacksonville Jaguars | n/a | n/a | n/a |
| Sun 11/29 01:00 PM | New York Jets at Miami Dolphins | n/a | n/a | n/a |
| Sun 11/29 04:25 PM | Washington Commanders at Arizona Cardinals | n/a | n/a | n/a |
| Mon 11/30 08:15 PM | Carolina Panthers at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Detroit Lions at Atlanta Falcons | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Jacksonville Jaguars at Chicago Bears | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Cincinnati Bengals at Cleveland Browns | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Miami Dolphins at Denver Broncos | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Green Bay Packers at New Orleans Saints | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Los Angeles Chargers at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 12/06 01:00 PM | Washington Commanders at Tennessee Titans | n/a | n/a | n/a |
| Sun 12/06 04:05 PM | Philadelphia Eagles at Arizona Cardinals | n/a | n/a | n/a |
| Sun 12/06 04:25 PM | Carolina Panthers at Minnesota Vikings | n/a | n/a | n/a |
| Sun 12/06 08:20 PM | Houston Texans at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Atlanta Falcons at Cleveland Browns | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Tampa Bay Buccaneers at Baltimore Ravens | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | New Orleans Saints at Carolina Panthers | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Chicago Bears at Miami Dolphins | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Denver Broncos at New York Jets | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Tennessee Titans at Detroit Lions | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Houston Texans at Washington Commanders | n/a | n/a | n/a |
| Sun 12/13 01:00 PM | Indianapolis Colts at Philadelphia Eagles | n/a | n/a | n/a |
| Sun 12/13 04:05 PM | Los Angeles Chargers at Las Vegas Raiders | n/a | n/a | n/a |
| Sun 12/13 04:25 PM | Kansas City Chiefs at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 12/13 08:20 PM | Buffalo Bills at Green Bay Packers | n/a | n/a | n/a |
| Mon 12/14 08:15 PM | Pittsburgh Steelers at Jacksonville Jaguars | n/a | n/a | n/a |
| Sat 12/19 08:20 PM | Chicago Bears at Buffalo Bills | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Atlanta Falcons at Washington Commanders | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Baltimore Ravens at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Cincinnati Bengals at Carolina Panthers | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Cleveland Browns at New York Giants | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Miami Dolphins at Green Bay Packers | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Jacksonville Jaguars at Houston Texans | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | Indianapolis Colts at Tennessee Titans | n/a | n/a | n/a |
| Sun 12/20 01:00 PM | New Orleans Saints at Tampa Bay Buccaneers | n/a | n/a | n/a |
| Sun 12/20 04:05 PM | New York Jets at Arizona Cardinals | n/a | n/a | n/a |
| Sun 12/20 04:25 PM | Denver Broncos at Las Vegas Raiders | n/a | n/a | n/a |
| Sun 12/20 08:20 PM | Detroit Lions at Minnesota Vikings | n/a | n/a | n/a |
| Thu 12/24 08:15 PM | Houston Texans at Philadelphia Eagles | n/a | n/a | n/a |
| Fri 12/25 01:00 PM | Green Bay Packers at Chicago Bears | n/a | n/a | n/a |
| Fri 12/25 04:30 PM | Buffalo Bills at Denver Broncos | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Arizona Cardinals at New Orleans Saints | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Tampa Bay Buccaneers at Atlanta Falcons | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Cleveland Browns at Baltimore Ravens | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Carolina Panthers at Pittsburgh Steelers | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Cincinnati Bengals at Indianapolis Colts | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Tennessee Titans at Las Vegas Raiders | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Los Angeles Chargers at Miami Dolphins | n/a | n/a | n/a |
| Sun 12/27 01:00 PM | Washington Commanders at Minnesota Vikings | n/a | n/a | n/a |
| Sun 12/27 08:20 PM | Jacksonville Jaguars at Dallas Cowboys | n/a | n/a | n/a |
| Mon 12/28 08:15 PM | New York Giants at Detroit Lions | n/a | n/a | n/a |
| Thu 12/31 08:15 PM | Baltimore Ravens at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | New Orleans Saints at Atlanta Falcons | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | Buffalo Bills at Miami Dolphins | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | Indianapolis Colts at Cleveland Browns | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | New York Giants at Dallas Cowboys | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | Washington Commanders at Jacksonville Jaguars | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | Minnesota Vikings at New York Jets | n/a | n/a | n/a |
| Sun 01/03 01:00 PM | Pittsburgh Steelers at Tennessee Titans | n/a | n/a | n/a |
| Sun 01/03 04:05 PM | Las Vegas Raiders at Arizona Cardinals | n/a | n/a | n/a |
| Sun 01/03 04:25 PM | Detroit Lions at Chicago Bears | n/a | n/a | n/a |
| Sun 01/03 04:25 PM | Kansas City Chiefs at Los Angeles Chargers | n/a | n/a | n/a |
| Mon 01/04 08:15 PM | Houston Texans at Green Bay Packers | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Atlanta Falcons at Carolina Panthers | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Pittsburgh Steelers at Baltimore Ravens | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | New York Jets at Buffalo Bills | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Chicago Bears at Minnesota Vikings | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Cleveland Browns at Cincinnati Bengals | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Dallas Cowboys at Washington Commanders | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Los Angeles Chargers at Denver Broncos | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Detroit Lions at Green Bay Packers | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Tennessee Titans at Houston Texans | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Jacksonville Jaguars at Indianapolis Colts | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Las Vegas Raiders at Kansas City Chiefs | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Tampa Bay Buccaneers at New Orleans Saints | n/a | n/a | n/a |
| Sun 01/10 01:00 PM | Philadelphia Eagles at New York Giants | n/a | n/a | n/a |
