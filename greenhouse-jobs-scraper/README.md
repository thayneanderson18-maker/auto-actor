# Greenhouse Jobs Scraper

Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link. Title, location, department and date filters, plus an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper
- Price: $0.0012 per job ($1.20 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/greenhouse-jobs-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `boards` | array of strings | Companies to scrape: the board name from the careers URL (`airbnb` in job-boards.greenhouse.io/airbnb) or the full URL. | `["discord"]` |
| `titleSearch` | array of strings | Keep only jobs whose title contains any of these words. | `["engineer", "data"]` |
| `titleExclusionSearch` | array of strings | Drop jobs whose title contains any of these words. | `["intern"]` |
| `locationSearch` | array of strings | Keep only jobs whose location or office contains any of these words. | `["remote", "london"]` |
| `departmentSearch` | array of strings | Keep only jobs in a department whose name contains any of these words. | `["engineering"]` |
| `postedWithinDays` | integer | Keep only jobs first published in the last N days. | `7` |
| `includeSalary` | boolean | Fetch the pay range the company publishes for each job (empty when it doesn't publish one). | `true` |
| `maxItems` | integer | Stop after this many jobs in total across all boards. | `200` |
| `onlyNew` | boolean | Skip jobs already returned by earlier runs (remembered for 180 days in the `greenhouse-jobs-seen` store of your account). Ideal for schedules. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"8162169"` | Greenhouse job id |
| `title` | `"Customer Experience Manager, Robinhood Concierge"` | Job title |
| `organization` | `"Robinhood"` | Company |
| `board` | `"robinhood"` | Greenhouse board name |
| `url` | `"https://boards.greenhouse.io/robinhood/jobs/8162169…"` | Link to the job ad |
| `apply_url` | `"https://boards.greenhouse.io/robinhood/jobs/8162169…#app"` | Link to the application form |
| `date_posted` | `"2026-09-11T16:19:03.000Z"` | When the job was first published |
| `date_updated` | `"2026-11-08T08:04:45.000Z"` | When the ad was last updated |
| `locations` | `["Denver, CO", "Westlake, TX"]` | Every location listed |
| `location` | `"Denver, CO; Westlake, TX"` | Location text as shown on the board |
| `departments` | `["Customer Care"]` | Departments |
| `offices` | `["Denver, CO", "Westlake, TX"]` | Offices |
| `salary_min` | `110500` | Lowest published pay, when the company publishes a range |
| `salary_max` | `130000` | Highest published pay |
| `salary_currency` | `"USD"` | Pay currency |
| `salary_title` | `"Zone 1 (Menlo Park, CA; …)"` | Label of the pay range |
| `requisition_id` | `"JR109347"` | Company's requisition id, when set |
| `description_text` | `"Join us in building the future of finance…"` | Full job description as plain text |
| `description_html` | `"<div class=\"content-intro\">…"` | Full job description as HTML |
| `metadata` | `{"Careers Page Bucket": "CUSTOMER EXPERIENCE"}` | Custom fields the company adds |
| `scrapedAt` | `"2026-11-08T23:08:02.630Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~greenhouse-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"boards": ["discord"], "maxItems": 50}'
```

## Typical uses

- A daily feed of new openings at a list of target companies with `onlyNew: true`.
- Salary benchmarking from the pay ranges companies publish.
- Tracking which teams a company is hiring for (`departments`) as a sales or investment signal.

## Notes

- Works for any company whose careers page is hosted on Greenhouse; find the board name in the careers URL.
- `includeSalary` costs one extra request per job; turn it off if you don't need pay ranges.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
