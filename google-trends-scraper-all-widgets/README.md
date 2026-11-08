# Google Trends Scraper

Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent. Any country or worldwide, 7 days to 5 years. No browser, no API key.

- Store page: https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets
- Price: $0.0025 per row ($2.50 per 1,000). One keyword over 12 months produced about 170 rows in our tests.. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/google-trends-scraper-all-widgets`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `keywords` | array of strings | Up to 20 search terms to analyse. | `["bitcoin"]` |
| `geo` | string | Two-letter country code such as `US`, `AU` or `GB`, or empty for worldwide. | `""` |
| `timeRange` | string | One of `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years`. | `"past_12_months"` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `keyword` | `"bitcoin"` | The search term the row belongs to |
| `kind` | `"interest_over_time"` | `interest_over_time`, `interest_by_region` or `related_query` |
| `label` | `"Nov 2 – 8, 2025"` | Week range, region name or related query text, depending on `kind` |
| `time` | `"1762041600"` | Unix seconds for `interest_over_time` rows; null otherwise |
| `value` | `50` | Google's relative score, 0 to 100 |
| `geo` | `"worldwide"` | Country code or `worldwide` |
| `trend` | `"top"` | `related_query` rows only: whether the query is from the top or rising list |
| `link` | `"https://trends.google.com/…"` | `related_query` rows only: link to that query on Google Trends |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~google-trends-scraper-all-widgets/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["bitcoin"], "geo": "", "timeRange": "past_12_months"}'
```

## Typical uses

- Weekly demand tracking for your product category or brand in one spreadsheet.
- Finding rising related queries before they peak, for content and ads.
- Comparing interest across countries for market entry decisions.

## Notes

- Rows are flat on purpose: filter on `kind` to get one table per widget.
- Google Trends values are relative to the highest point in the selected period, not absolute search counts.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
