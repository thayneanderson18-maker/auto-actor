# Career Site Jobs Scraper

Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link. Title, location, department, remote and date filters, plus an only-new mode for daily feeds.

- Store page: https://apify.com/daedal_quintuplet/career-site-jobs-scraper
- Price: $0.0015 per job ($1.50 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/career-site-jobs-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `companies` | array of strings | Career sites to scrape: the careers URL (e.g. `https://jobs.lever.co/spotify`) or `ats:name` (e.g. `ashby:notion`). A bare name is looked up on Lever, Ashby, SmartRecruiters and Workable. | `["https://jobs.lever.co/spotify", "ashby:notion"]` |
| `titleSearch` | array of strings | Keep only jobs whose title contains any of these words. | `["engineer", "data"]` |
| `titleExclusionSearch` | array of strings | Drop jobs whose title contains any of these words. | `["intern"]` |
| `locationSearch` | array of strings | Keep only jobs whose location contains any of these words. | `["London", "remote"]` |
| `departmentSearch` | array of strings | Keep only jobs whose department or team contains any of these words. Workday boards don't publish departments, so this drops Workday jobs. | `["engineering"]` |
| `remoteOnly` | boolean | Keep only jobs marked remote. | `false` |
| `postedWithinDays` | integer | Keep only jobs posted in the last N days. | `7` |
| `includeDescription` | boolean | Return the full description as text and HTML (one extra request per job on SmartRecruiters, Workday and Workable). | `true` |
| `maxItemsPerCompany` | integer | Stop after this many jobs from any one career site. | `100` |
| `maxItems` | integer | Stop after this many jobs in total. | `500` |
| `onlyNew` | boolean | Skip jobs already returned by earlier runs (remembered for 180 days in the `career-site-jobs-seen` store of your account). Ideal for schedules. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"2a55d6c9-c564-443a-be3e-a3851db5a93b"` | The career site's job id |
| `title` | `"Account Executive - Commercial, Spotify Technology"` | Job title |
| `organization` | `"Spotify"` | Company |
| `organization_url` | `"https://jobs.lever.co/spotify"` | The company's career site |
| `url` | `"https://jobs.lever.co/spotify/2a55d6c9-…"` | Link to the job ad |
| `apply_url` | `"https://jobs.lever.co/spotify/2a55d6c9-…/apply"` | Link to the application form |
| `date_posted` | `"2026-10-23T15:00:40.768Z"` | When the job was posted |
| `location` | `"New York, NY"` | Location text |
| `locations` | `["New York, NY"]` | Every location listed |
| `countries` | `["United States"]` | Countries |
| `remote_derived` | `false` | True when the job is marked remote or says remote in its location |
| `workplace_type` | `"Hybrid"` | On-site, Hybrid or Remote, when the site says |
| `employment_type` | `["Permanent"]` | Employment type |
| `departments` | `["Operations and Business Support", "Platform"]` | Departments or teams |
| `salary` | `null` | Salary when the career site publishes one |
| `description_text` | `"Spotify Technology is our business-to-business software team…"` | Full description as plain text |
| `description_html` | `"<div><p>Spotify Technology is…"` | Full description as HTML |
| `source` | `"lever"` | Which platform it came from: lever, ashby, smartrecruiters, workday or workable |
| `company_slug` | `"spotify"` | The company's id on that platform |
| `scrapedAt` | `"2026-11-09T23:24:13.443Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~career-site-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["https://jobs.lever.co/spotify", "https://jobs.ashbyhq.com/notion"], "maxItems": 50}'
```

## Typical uses

- One daily feed of new openings across a list of target companies, whatever platform each one hires on, with `onlyNew: true`.
- Remote-job boards and newsletters, using `remoteOnly` and `postedWithinDays`.
- Tracking which teams a company is growing (`departments`) as a sales or investment signal.

## Notes

- Covers Lever, Ashby, SmartRecruiters, Workday and Workable. For Greenhouse boards, use our Greenhouse Jobs Scraper.
- Turn off `includeDescription` for faster, smaller runs when you only need titles and links.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
