# Google Jobs Scraper (US & UK)

Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing. Up to 10 jobs per query, with an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/google-jobs-scraper
- Price: $0.0025 per job ($2.50 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/google-jobs-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `queries` | array of strings | Job searches, e.g. `software engineer london`. | `["data analyst new york"]` |
| `country` | string | `us` or `uk`. | `"us"` |
| `maxItems` | integer | Stop after this many jobs in total. | `10` |
| `onlyNew` | boolean | Skip jobs already returned by earlier runs (remembered in the `google-jobs-seen` store of your account). Ideal for schedules. | `false` |
| `debug` | boolean | Save raw HTML for debugging. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"93Ca3Nw89N0VnIw-AAAAAA=="` | Google's job id |
| `title` | `"Customer Data Analyst"` | Job title |
| `company` | `"L'Occitane En Provence"` | Employer |
| `location` | `"New York, NY"` | Location text |
| `via` | `"Built In NYC"` | The job board Google sourced it from |
| `postedAt` | `"2 days ago"` | Posting age as Google shows it |
| `salary` | `"75K–85K a year"` | Salary text when shown |
| `jobType` | `"Full-time"` | Full-time, Part-time, Contractor, Internship |
| `description` | `"Born of a simple gesture in 1976…"` | Full job description |
| `applyLinks` | `[{"name": "Built In NYC", "url": "https://…"}, …]` | Every apply option Google lists, with its URL |
| `googleJobsUrl` | `"https://www.google.com/search?ibp=htl;jobs&htidocid=…"` | Link to the listing on Google Jobs |
| `query` | `"data analyst new york"` | The query that found it |
| `country` | `"us"` | `us` or `uk` |
| `scrapedAt` | `"2026-11-07T23:59:45.648Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~google-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["data analyst new york"], "country": "us", "maxItems": 10}'
```

## Typical uses

- A daily feed of new postings for a role and city with `onlyNew: true`, so you only see jobs you haven't seen.
- Salary and job-type snapshots across cities.
- Lists of employers hiring for a skill, with direct apply links.

## Notes

- Google returns 10 jobs per query; use several specific queries rather than one broad one.
- US and UK only. Google does not show a jobs panel for some countries, Australia included.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
