# Seek NZ Job Scraper

Job listings from SEEK New Zealand (seek.co.nz), straight from SEEK's own JSON search API. No browser, no proxy, so a run takes seconds.

- Store page: https://apify.com/daedal_quintuplet/seek-nz-job-scraper
- Price: $0.001 per job ($1 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/seek-nz-job-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `keywords` | string | Search keywords, e.g. `roof plumber` or `data engineer`. Leave empty for all jobs. | `"carpenter"` |
| `where` | string | Suburb, city or region as you would type it on Seek, e.g. `Auckland` or `All Auckland`. | `"Auckland"` |
| `maxItems` | integer | Stop after this many jobs. | `200` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"95472220"` | SEEK job id |
| `title` | `"Wooden Joinery Installer, repairs and service"` | Job title |
| `company` | `"The Sash Window Company"` | Advertiser |
| `locations` | `["East Tamaki, Auckland"]` | One or more locations |
| `salary` | `"$40 – $60 per hour"` | Salary text as shown on SEEK, when the ad states one |
| `workTypes` | `["Full time"]` | Full time, Part time, Contract/Temp, Casual/Vacation |
| `classifications` | `["Trades & Services"]` | SEEK classification |
| `listingDate` | `"2026-10-23T21:33:38Z"` | When the ad was listed (ISO 8601) |
| `teaser` | `"Ready for a change? Want to be paid what you're worth…"` | First lines of the ad |
| `bulletPoints` | `["Great pay", "Interesting job", "Great team environment"]` | Up to three selling points, often empty |
| `isFeatured` | `true` | Paid placement flag |
| `url` | `"https://www.seek.co.nz/job/95472220"` | Link to the ad |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~seek-nz-job-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": "carpenter", "where": "Auckland", "maxItems": 50}'
```

## Typical uses

- A fresh list of jobs in one region every morning, pushed to a Google Sheet or Slack.
- Salary benchmarking by classification or region.
- Lists of companies that are hiring right now (the `company` field), for sales or recruiting.

## Notes

- Only the fields SEEK returns in search results are included; the full ad text is not.
- Set `maxItems` to what you need: you pay per job returned.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
