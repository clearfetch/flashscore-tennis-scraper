# Flashscore Tennis Scraper - Live Scores, Stats & Point by Point

Get tennis data from Flashscore as clean JSON: fixtures for the days you choose, live scores, final results with
set and tiebreak scores, players with country and Flashscore IDs, tournament and surface context, plus
optional per-match statistics, set-by-set summaries and complete point-by-point sequences. ATP, WTA, ITF and
Challenger, singles and doubles. No login, no API key and no proxy needed.

## What data you get

**Matches mode** returns one row per match:

- **Status** that reflects reality: scheduled, live, finished, retired, walkover, postponed, cancelled and
  interrupted, resolved from Flashscore's own stage codes rather than guessed, plus `stageDetail` with the exact
  stage it is in (`FIRST_SET`, `SECOND_SET`, `FIRST_SET_TIEBREAK`, `AWARDED`, and so on).
- **Scores**: sets won by each player, per-set games, tiebreak points, and the winner.
- **Players**: display and full name, Flashscore player ID and slug, three-letter code, country, photo URL.
- **Tournament**: name, tour (ATP, WTA, ITF, Challenger, Team, Exhibition), gender, singles or doubles, surface,
  IDs and the Flashscore URL.
- **Live state** while a match is in play: whether it is in play, who is serving, and the current game score
  (which is the tiebreak count during a tiebreak).
- **Times** as ISO timestamps: scheduled start and last update.
- **`raw`**: all 53 original feed keys for this match, so nothing is lost if you need a field we did not map.

**Match details mode** takes match IDs and returns, per match:

- **Set summary** with the duration of each set, total match duration, venue and city.
- **Match statistics**: aces, double faults, first and second serve percentages, break points, return points,
  average serve speeds and more, each split by period (Match, Set 1, Set 2...) and group (Service, Return,
  Points, Games). 83 rows for the example below.
- **Point by point**: every game with its point sequence and a break flag. 38 games in the example.
- **Head to head**: recent form for both players and their previous meetings, grouped by surface.

## How to use

1. Choose **Matches** mode and set **Days** (0 is today, -1 yesterday, 1 tomorrow; add several entries for a range).
2. Optionally narrow it down by status, tour, tournament name or doubles.
3. Run it, then export the dataset as JSON, CSV or Excel, or read it from the API. To go deeper on a match, run
   the Actor again in **Match details** mode with the `matchId` values you got back.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | string | `matches` | `matches` for fixtures, live scores and results; `matchDetails` for statistics, point by point and head to head. |
| `days` | array | `["0"]` | Day offsets from today, from -7 to 7. Several entries are fetched in one run and deduplicated. |
| `status` | array | all | Keep only `scheduled`, `live`, `finished`, `postponed` or `cancelled`. Retired and walkover count as finished. |
| `categories` | array | all | Keep only these tours: `ATP`, `WTA`, `ITF`, `Challenger`, `Exhibition`, `Team`, `Other`. |
| `includeDoubles` | boolean | `false` | Doubles are excluded by default, which roughly halves a typical day. |
| `tournamentFilter` | string | — | Case-insensitive regular expression on the full tournament name, e.g. `wimbledon|roland`. |
| `matchIds` | array | — | Details mode: match IDs such as `l8CtAPRG`, or full `flashscore.com/match/...` URLs. |
| `details` | array | all four | Details mode: `summary`, `statistics`, `pointByPoint`, `h2h`. |
| `maxItems` | integer | `0` | Stop after this many rows; 0 means no limit. |
| `maxConcurrency` | integer | `5` | Parallel requests in details mode. |
| `timeoutSecs` | integer | `30` | Per-request timeout. |
| `token` | string | — | Advanced. Overrides the feed signature, which the Actor otherwise discovers by itself. |
| `proxyConfiguration` | object | off | Optional. Not needed in normal use. |

## Output example

One match from a **matches** run (the `raw` object with all 53 feed keys is omitted here for readability):

```json
{
  "matchId": "l8CtAPRG",
  "url": "https://www.flashscore.com/match/l8CtAPRG/",
  "sport": "tennis",
  "status": "finished",
  "stage": "finished",
  "stageCode": 3,
  "stageDetailCode": 3,
  "startTime": "2026-09-04T21:20:00.000Z",
  "lastUpdate": "2026-09-04T23:51:56.000Z",
  "tournament": {
    "name": "US Open (USA)",
    "fullName": "ATP - SINGLES: US Open (USA), hard",
    "category": "ATP - SINGLES",
    "categoryLabel": "ATP - Singles",
    "tour": "ATP",
    "gender": "men",
    "discipline": "singles",
    "surface": "hard",
    "id": "tQZGKy9k",
    "stageId": "65k5lHxU",
    "path": "/tennis/atp-singles/us-open/",
    "url": "https://www.flashscore.com/tennis/atp-singles/us-open/"
  },
  "isDoubles": false,
  "home": {
    "name": "Lehecka J.",
    "fullName": "Lehecka J.",
    "id": "8Y0hD4UP",
    "slug": "lehecka-jiri",
    "url": "https://www.flashscore.com/player/lehecka-jiri/8Y0hD4UP/",
    "code": "LEH",
    "country": "Czech Republic",
    "countryId": 62,
    "image": "https://static.flashscore.com/res/image/data/44C5ipAN-ne6Kkdx9.png",
    "altId": "6PlgfXKR"
  },
  "away": {
    "name": "Tsitsipas S.",
    "fullName": "Tsitsipas S.",
    "id": "44nO7rhm",
    "slug": "tsitsipas-stefanos",
    "url": "https://www.flashscore.com/player/tsitsipas-stefanos/44nO7rhm/",
    "code": "TSI",
    "country": "Greece",
    "countryId": 83,
    "image": "https://static.flashscore.com/res/image/data/rVaClcVH-hbIQr8HQ.png",
    "altId": "hb6oWfc6"
  },
  "score": {
    "setsHome": 1,
    "setsAway": 3,
    "currentSetsHome": 1,
    "currentSetsAway": 3,
    "sets": [
      {
        "home": 6,
        "away": 2,
        "tiebreakHome": null,
        "tiebreakAway": null
      },
      {
        "home": 1,
        "away": 6,
        "tiebreakHome": null,
        "tiebreakAway": null
      },
      {
        "home": 6,
        "away": 7,
        "tiebreakHome": 3,
        "tiebreakAway": 7
      },
      {
        "home": 1,
        "away": 6,
        "tiebreakHome": null,
        "tiebreakAway": null
      }
    ]
  },
  "winner": "away",
  "inPlay": false,
  "serving": null,
  "currentGame": null,
  "ok": true,
  "dayOffset": 0,
  "scrapedAt": "2026-09-05T13:11:16.596Z"
}
```

The three live fields above are null on a finished match. While a match is in play they look like this, taken
from a run that caught a first-set tiebreak at 6-6:

```json
{
  "status": "live",
  "inPlay": true,
  "serving": "home",
  "currentGame": { "home": "5", "away": "6" },
  "score": { "sets": [{ "home": 6, "away": 6, "tiebreakHome": 5, "tiebreakAway": 6 }] }
}
```

A **match details** item, trimmed to the first statistic rows, one game and one head-to-head match:

```json
{
  "matchId": "QHRir1KG",
  "url": "https://www.flashscore.com/match/QHRir1KG/",
  "sport": "tennis",
  "ok": true,
  "summary": {
    "sets": [
      {
        "label": "Set 1",
        "home": 6,
        "away": 2,
        "tiebreakHome": null,
        "tiebreakAway": null,
        "duration": "0:37"
      },
      {
        "label": "Set 2",
        "home": 7,
        "away": 6,
        "tiebreakHome": 7,
        "tiebreakAway": 4,
        "duration": "0:57"
      },
      {
        "label": "Set 3",
        "home": 6,
        "away": 0,
        "tiebreakHome": null,
        "tiebreakAway": null,
        "duration": "0:25"
      }
    ],
    "totalDuration": "1:59",
    "venue": "USTA Billie Jean King NTC",
    "city": "New York, NY",
    "referee": null,
    "attendance": null,
    "venueOther": null
  },
  "statistics": [
    {
      "period": "Match",
      "group": "Service",
      "name": "Aces",
      "home": "8",
      "away": "6"
    },
    {
      "period": "Match",
      "group": "Service",
      "name": "Double Faults",
      "home": "1",
      "away": "7"
    },
    {
      "period": "Match",
      "group": "Service",
      "name": "1st serve percentage",
      "home": "52%",
      "away": "55%"
    }
  ],
  "pointByPoint": [
    {
      "set": "Set 1",
      "game": 1,
      "homeGames": 0,
      "awayGames": 2,
      "server": 1,
      "points": [
        "15:0",
        "15:15",
        "15:30",
        "15:40",
        "30:40",
        "40:40",
        "A:40"
      ],
      "isBreak": true
    }
  ],
  "h2h": [
    {
      "heading": "Last matches: Bonzi B.",
      "surfaceSection": "All surfaces",
      "matches": [
        {
          "matchId": "QHRir1KG",
          "url": "https://www.flashscore.com/match/QHRir1KG/",
          "date": "2026-09-03T21:05:00.000Z",
          "tournament": "US Open",
          "tournamentCode": "USO",
          "country": "USA",
          "surface": "hard",
          "home": {
            "name": "Bonzi B.",
            "slug": "bonzi-benjamin",
            "id": "M5OpGHqH"
          },
          "away": {
            "name": "Buse I.",
            "slug": "buse-ignacio",
            "id": "A1LQjAPb"
          },
          "score": "3:0",
          "setsHome": 3,
          "setsAway": 0,
          "winner": "home"
        }
      ]
    }
  ],
  "scrapedAt": "2026-09-05T13:08:28.790Z"
}
```

A match that cannot be found, or has no data yet, produces `{ "matchId": "...", "ok": false, "error": "..." }`
and is not charged.

## Pricing

- **$0.001 per match** in matches mode. A full day of professional tennis is roughly 150-250 matches, so about
  $0.15-0.25 for everything, or a few cents with the doubles and tour filters on.
- **$0.01 per match** in details mode, whatever number of sections you request. Statistics, every point of every
  game and both players' recent form count as one charge.
- Matches that fail or have no data are free. Runs on the Apify free plan.

Paid Apify plans pay less: 10% off on Bronze, 20% on Silver and 30% on Gold and higher tiers.

Apify also charges a run-start fee of $0.00005 per started GB of allocated memory (minimum one event), including runs that produce no chargeable results.

## Use cases

- **Betting and trading models**: build a serve, return and fatigue history from set durations, point-by-point
  sequences and surface, then keep it current with a scheduled daily run.
- **Live scoreboards and bots**: poll matches mode for in-play state and push updates to a site, app or Discord.
- **Fantasy and prediction games**: populate fixtures and settle results automatically.
- **Sports media**: generate daily results digests and previews with head-to-head context.
- **Research and machine learning**: label datasets across tours and surfaces, including retirements and walkovers,
  which most feeds hide.
- **AI agents**: give an assistant a tool that answers "who plays today at the US Open and who won yesterday".

## Integrations

```bash
curl -X POST "https://api.apify.com/v2/acts/clearfetch~flashscore-tennis-scraper/run-sync-get-dataset-items?token=YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"days": ["0"], "categories": ["ATP", "WTA"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient("YOUR_TOKEN")
run = client.actor("clearfetch/flashscore-tennis-scraper").call(run_input={"days": ["0"], "status": ["finished"]})
for match in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(match["startTime"], match["home"]["name"], match["score"]["setsHome"], "-", match["score"]["setsAway"], match["away"]["name"])
```

Works with the Apify integrations for n8n, Make, Zapier, Google Sheets, Slack and webhooks, with scheduled runs,
and with AI agents through the Apify MCP server.

## FAQ

**Do I need a proxy?** No. The feed answers ordinary datacenter requests. A proxy input exists if you want one.

**Do I need a Flashscore account?** No. Nothing here requires a login or a cookie.

**How fresh is the data?** Each run reads the feed live, so a match in progress carries its current set scores,
the current game score and who is serving. Schedule a run every few minutes if you need a running scoreboard.

**Are rate limits a problem?** One day of tennis is a single request, so a normal run is very light. Details mode
makes up to four requests per match and runs five matches at a time by default.

**What if Flashscore changes its feed signature?** The Actor discovers the current signature from the site on
every run and falls back to a known value, so a rotation does not break it. The `token` input is there as a last
resort.

**Which sports does this cover?** Tennis. The same feed carries other sports; ask if you want one added.

**Is this legal?** It reads the same public endpoints a browser reads, with no login and no personal data.
Scores and results are facts. You are responsible for how you use the data, including any redistribution.

## More tools from clearfetch

- [Flashscore Football Scraper](https://apify.com/clearfetch/flashscore-football-scraper): fixtures, live scores and results from every league
- [Flashscore Basketball Scraper](https://apify.com/clearfetch/flashscore-basketball-scraper): NBA, EuroLeague and every league, by quarter
- [Flashscore Baseball Scraper](https://apify.com/clearfetch/flashscore-baseball-scraper): MLB, NPB and KBO with inning-by-inning line scores
- [Flashscore Hockey Scraper](https://apify.com/clearfetch/flashscore-hockey-scraper): NHL, KHL and every league, by period

## Changelog

- **1.0.1** (2026-09) — match links copied from the browser work in details mode. Flashscore's current links
  carry the match ID in `?mid=`, after team names that were being read as the ID; a link with no ID in it is now
  skipped with a message saying where to find one.
- **1.0.0** (2026-09) — first release: matches mode with day ranges and status, tour, doubles and tournament
  filters; details mode with set summary, statistics split by period and group, point by point and head to head;
  automatic feed-signature discovery.
