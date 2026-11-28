# Built In Jobs Scraper

Tech jobs from builtin.com: title, company, location, remote or hybrid, level, salary range, skills, posted date, full description and benefits. Keyword, location, category and date filters, company job pages, and an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/builtin-jobs-scraper
- Price: $0.0009 per job ($0.90 per 1,000); the first 25 jobs of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/builtin-jobs-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `searchQueries` | array of strings | Job titles or keywords, one search each. Leave empty to browse the newest jobs with the filters below. | `["data engineer", "product manager"]` |
| `location` | string | City and state, a US state, or a city and country; `Remote` for remote jobs. | `"Austin, TX"` |
| `startUrls` | array of strings | builtin.com search, category, company job pages or single job links. | `["https://builtin.com/company/stripe/jobs"]` |
| `remoteMode` | string | Keep only remote, hybrid or on-site jobs; `any` for all. | `"remote"` |
| `category` | string | One Built In job category, e.g. `data-analytics`. | `"data-analytics"` |
| `experienceLevel` | string | One experience level, e.g. `senior`. | `"senior"` |
| `postedWithinDays` | string | `1`, `3`, `7` or `30` days; `any` for any time. | `"7"` |
| `maxResultsPerQuery` | integer | Most jobs per keyword or URL; 0 for no limit. | `100` |
| `maxTotalResults` | integer | Stop the run after this many jobs; 0 for no limit. | `500` |
| `fetchDescription` | boolean | Open each job page for the full description, exact salary, addresses and benefits. | `true` |
| `onlyNew` | boolean | Return only jobs earlier runs with the same `stateKey` haven't returned. Ideal for schedules. | `false` |
| `stateKey` | string | Name of the memory `onlyNew` uses; one per saved search. | `"austin-data-jobs"` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `jobId` | `"12480644"` | Built In job id |
| `title` | `"Data Engineer 5 (Senior Manager, IC)-Enterprise Data Tech"` | Job title |
| `jobUrl` | `"https://builtin.com/job/…/12480644"` | Link to the job |
| `company` | `"Capital One"` | Employer |
| `industries` | `["Fintech", "Machine Learning", …]` | Company industries |
| `location` | `"McLean, VA, USA; Richmond, VA, USA; …"` | Locations as text |
| `locations` | `["McLean, VA, USA", …]` | Every location |
| `isRemote` | `false` | Remote job |
| `workplaceType` | `"Hybrid"` | Remote, Hybrid or In-Office |
| `experienceLevel` | `"Senior level"` | Experience level |
| `employmentType` | `"Full-Time"` | Employment type |
| `skills` | `["AWS", "Databricks", …]` | Skills listed |
| `salaryText` | `"209K-286K Annually"` | Salary as shown |
| `salaryMin` | `209000` | Lowest salary |
| `salaryMax` | `286200` | Highest salary |
| `salaryCurrency` | `"USD"` | Currency |
| `salaryPeriod` | `"year"` | Pay period |
| `description` | `"Data Engineer 5 …"` | Full description (with `fetchDescription`) |
| `benefits` | `["Offers 401(K)", …]` | Benefits (with `fetchDescription`) |
| `postedAt` | `"2026-11-25T20:09:02Z"` | When it was posted |
| `scrapedAt` | `"2026-11-25T23:27:27.135Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~builtin-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["data engineer"], "maxTotalResults": 20}'
```

## Typical uses

- A daily feed of new tech jobs for a role and city with `onlyNew: true`.
- Salary benchmarking from the ranges employers publish.
- Tracking hiring at specific companies through their Built In job pages.

## Notes

- Built In mostly lists US jobs, plus some in other countries; leave `location` empty for the whole US.
- Turn off `fetchDescription` for faster runs with only the search-card fields.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
- [Flashscore Scraper](https://apify.com/daedal_quintuplet/flashscore-scraper): Results and fixtures from any Flashscore league, cup, tennis tournament or team page: scores, half-time, sets, quarters, rounds, dates, team IDs and logos.
- [Craigslist Scraper](https://apify.com/daedal_quintuplet/craigslist-scraper): Craigslist listings from any site and category: for sale, cars, housing, jobs, gigs and services.
- [Wappalyzer Alternative: Tech Stack Detector](https://apify.com/daedal_quintuplet/wappalyzer-tech-stack-detector): The technologies any website uses: CMS, ecommerce, analytics, JavaScript frameworks, CDN, hosting and email provider, from 7,700+ open-source fingerprints with evidence, versions and confidence.
- [Amazon Bestsellers Scraper](https://apify.com/daedal_quintuplet/amazon-bestsellers-scraper): Amazon Best Sellers and Hot New Releases: the full top 100 per list with rank, ASIN, name, price, currency, stars, ratings count, URL and image, for the US, UK, DE, FR, ES, IT, CA, AU, IN and JP stores.
- [AutoScout24 Scraper](https://apify.com/daedal_quintuplet/autoscout24-scraper): AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details.
- [Flipkart Scraper](https://apify.com/daedal_quintuplet/flipkart-scraper): Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL.
- [Gumroad Scraper](https://apify.com/daedal_quintuplet/gumroad-scraper): Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants.
- [TradingView Screener Scraper](https://apify.com/daedal_quintuplet/tradingview-screener-scraper): TradingView screener data for stocks in 45 markets, crypto, forex and futures: price, change, volume, market cap, P/E, RSI, MACD, moving averages, technical rating and performance.
- [Immoweb Scraper](https://apify.com/daedal_quintuplet/immoweb-scraper): Belgian real estate from Immoweb: houses, apartments, land and offices for sale or rent, with price, address, coordinates, bedrooms, living area, EPC, photos and agency, plus optional full details.
