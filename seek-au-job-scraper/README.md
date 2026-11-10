# Seek AU Job Scraper

Job listings from SEEK Australia (seek.com.au), straight from SEEK's own JSON search API. No browser, no proxy, so a run takes seconds.

- Store page: https://apify.com/daedal_quintuplet/seek-au-job-scraper
- Price: $0.001 per job ($1 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/seek-au-job-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `keywords` | string | Search keywords, e.g. `roof plumber` or `data engineer`. Leave empty for all jobs. | `"carpenter"` |
| `where` | string | Suburb, city or region as you would type it on Seek, e.g. `Brisbane` or `All Sydney NSW`. | `"Brisbane"` |
| `maxItems` | integer | Stop after this many jobs. | `200` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"95672979"` | SEEK job id |
| `title` | `"Carpenter"` | Job title |
| `company` | `"SE Building Solutions"` | Advertiser |
| `locations` | `["Brisbane QLD"]` | One or more locations |
| `salary` | `"$50 – $60 per hour"` | Salary text as shown on SEEK, when the ad states one |
| `workTypes` | `["Full time"]` | Full time, Part time, Contract/Temp, Casual/Vacation |
| `classifications` | `["Trades & Services"]` | SEEK classification |
| `listingDate` | `"2026-11-03T20:43:53Z"` | When the ad was listed (ISO 8601) |
| `teaser` | `"Join the Award Winning SE Building Solutions for…"` | First lines of the ad |
| `bulletPoints` | `["Great pay", "Interesting job"]` | Up to three selling points, often empty |
| `isFeatured` | `false` | Paid placement flag |
| `url` | `"https://www.seek.com.au/job/95672979"` | Link to the ad |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~seek-au-job-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": "carpenter", "where": "Brisbane", "maxItems": 50}'
```

## Typical uses

- A fresh list of trade or office jobs in one city every morning, pushed to a Google Sheet.
- Salary benchmarking by classification or region.
- Lists of companies that are hiring right now (the `company` field), for sales or recruiting.

## Notes

- Only the fields SEEK returns in search results are included; the full ad text is not.
- Set `maxItems` to what you need: you pay per job returned.

## Our other actors

- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
