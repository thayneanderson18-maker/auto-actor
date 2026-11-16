# Flashscore Scraper

Results and fixtures from any Flashscore league, cup, tennis tournament or team page: scores, half-time, sets, quarters, rounds, dates, team IDs and logos. Football, tennis, basketball, hockey and more, with an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/flashscore-scraper
- Price: $0.0008 per match ($0.80 per 1,000); the first 25 matches of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/flashscore-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `startUrls` | array of {url} | Flashscore competition or team pages, any tab (results, fixtures, standings) or a past season, any sport. | `[{"url": "https://www.flashscore.com/football/england/premier-league/results/"}]` |
| `matchType` | string | `results` (finished, newest first), `fixtures` (upcoming) or `both`. | `"results"` |
| `maxItems` | integer | Stop after this many matches across all URLs. Flashscore shows up to about 100 results and 120 fixtures per page. | `200` |
| `onlyNew` | boolean | Skip matches already returned to you in an earlier run (a fixture comes back once it has a final result). Ideal for schedules. | `false` |
| `includeLogos` | boolean | Add `home_team_logo_url` and `away_team_logo_url` to each match. | `true` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `match_id` | `"Me9aWSp3"` | Flashscore match id |
| `match_url` | `"https://www.flashscore.com/match/Me9aWSp3/"` | Link to the match |
| `match_date` | `"2026-11-08T16:30:00.000Z"` | Kick-off time (ISO 8601, UTC) |
| `match_status` | `"finished"` | `finished`, `scheduled` and so on |
| `home_team_name` | `"Manchester Utd"` | Home team |
| `home_team_id` | `"ppjDR086"` | Flashscore team id |
| `home_team_short_name` | `"MNU"` | Three-letter code |
| `away_team_name` | `"Aston Villa"` | Away team |
| `away_team_id` | `"W00wmLO0"` | Flashscore team id |
| `score_home` | `4` | Home score (null for fixtures) |
| `score_away` | `4` | Away score |
| `winner` | `"draw"` | `home`, `away` or `draw` |
| `halftime_score_home` | `2` | Home score at half-time, where the sport has halves |
| `halftime_score_away` | `2` | Away score at half-time |
| `periods` | `[{"period": 1, "home": 2, "away": 2}, …]` | Score per half, set, quarter or period |
| `round_name` | `"Round 10"` | Round or stage |
| `tournament_name` | `"Premier League"` | Competition |
| `country_name` | `"England"` | Country of the competition |
| `sport_name` | `"football"` | Sport |
| `home_team_logo_url` | `"https://static.flashscore.com/res/image/data/…png"` | Team logo (with `includeLogos`) |
| `scraped_at` | `"2026-11-15T23:07:09.631Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~flashscore-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": [{"url": "https://www.flashscore.com/football/england/premier-league/results/"}], "matchType": "results", "maxItems": 20}'
```

## Typical uses

- A results table for a league or team, refreshed after every round with `onlyNew: true`.
- Historical seasons for models and betting research (pass a past-season URL).
- Fixture lists for a club website, newsletter or bot, using `matchType: "fixtures"`.

## Notes

- Flashscore shows about 100 results and 120 fixtures per page, so one URL returns at most that many; add more URLs for more.
- Every run's first 25 matches are free, so small checks cost only Apify compute.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
