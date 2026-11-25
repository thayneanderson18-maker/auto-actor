# Craigslist Scraper

Craigslist listings from any site and category: for sale, cars, housing, jobs, gigs and services. Title, price, dates, full description, photos, coordinates and attributes such as condition, make and year, with an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/craigslist-scraper
- Price: $0.001 per listing ($1 per 1,000); the first 25 listings of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/craigslist-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `startUrls` | array of {url} | Craigslist search results pages (any site, category and filters) or single listing pages. Old-style (`newyork.craigslist.org/search/sss`) and new-style addresses both work. | `[{"url": "https://newyork.craigslist.org/search/sss?query=bike"}]` |
| `locations` | array of strings | Instead of URLs: Craigslist site names, the part before `.craigslist.org`. | `["newyork", "chicago"]` |
| `category` | string | Category code used with `locations`, e.g. `sss` all for sale, `cta` cars & trucks, `apa` apartments, `jjj` jobs. | `"cta"` |
| `searchQueries` | array of strings | Search terms to run on every site in `locations`, one search each. | `["honda civic"]` |
| `maxItems` | integer | Stop after this many listings in total. One search page lists up to about 350. | `100` |
| `includeDetails` | boolean | Open every listing for the full description, all photos, dates and attributes. Off returns only what the search page shows, faster. | `true` |
| `maxAgeDays` | integer | Skip listings posted more than this many days ago (needs `includeDetails`). | `7` |
| `onlyNew` | boolean | Skip listings already returned to you in an earlier run (remembered for 120 days). Ideal for schedules. | `false` |
| `maxConcurrency` | integer | How many listing pages to open at once when `includeDetails` is on. | `5` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"8001776502"` | Craigslist post id |
| `url` | `"https://www.craigslist.org/view/d/santa-rosa-2008-honda-cbr-…"` | Link to the listing |
| `title` | `"2008 Honda CBR 1000RR"` | Listing title |
| `datetime` | `"2026-11-16T14:51:50-0800"` | When it was posted |
| `updatedAt` | `null` | When it was last updated, if it was |
| `price` | `"$7,000"` | Price as shown |
| `priceNumber` | `7000` | Price as a number |
| `currency` | `"USD"` | Currency |
| `location` | `"santa rosa"` | Location text from the ad |
| `city` | `"Santa Rosa"` | City |
| `region` | `"CA"` | State or region |
| `postalCode` | `"95406"` | Postal code, when given |
| `latitude` | `38.421157` | Map latitude |
| `longitude` | `-122.705011` | Map longitude |
| `area` | `"sfbay"` | Craigslist site |
| `subarea` | `"north bay"` | Sub-area |
| `category` | `"for sale"` | Category |
| `subcategory` | `"motorcycles"` | Subcategory |
| `post` | `"This Bike is in excellent condition…"` | Full description (with `includeDetails`) |
| `pics` | `["https://images.craigslist.org/…_600x450.jpg", …]` | Photo URLs |
| `attributesMap` | `{"year": "2008", "condition": "excellent", …}` | Listing attributes as key/value pairs |
| `condition` | `"excellent"` | Condition, when given |
| `makeModel` | `"honda cbr1000rr"` | Make and model, for vehicles |
| `year` | `2008` | Year, for vehicles |
| `scrapedAt` | `"2026-11-16T23:12:24.214Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~craigslist-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": [{"url": "https://newyork.craigslist.org/search/sss?query=bike"}], "maxItems": 20}'
```

## Typical uses

- A morning alert of new listings for a search (a car model, a flat in a price range) with `onlyNew: true`.
- Price research: compare asking prices for the same item across cities.
- Feeding listings with coordinates into a map or spreadsheet.

## Notes

- One Craigslist search page lists up to about 350 listings; for more, split the search by sub-area, price range or search terms.
- Resumes, personals and missed connections are not supported.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
- [Google Images Scraper](https://apify.com/daedal_quintuplet/google-images-scraper): Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website.
- [Career Site Jobs Scraper](https://apify.com/daedal_quintuplet/career-site-jobs-scraper): Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link.
- [Flashscore Scraper](https://apify.com/daedal_quintuplet/flashscore-scraper): Results and fixtures from any Flashscore league, cup, tennis tournament or team page: scores, half-time, sets, quarters, rounds, dates, team IDs and logos.
- [Wappalyzer Alternative: Tech Stack Detector](https://apify.com/daedal_quintuplet/wappalyzer-tech-stack-detector): The technologies any website uses: CMS, ecommerce, analytics, JavaScript frameworks, CDN, hosting and email provider, from 7,700+ open-source fingerprints with evidence, versions and confidence.
- [Amazon Bestsellers Scraper](https://apify.com/daedal_quintuplet/amazon-bestsellers-scraper): Amazon Best Sellers and Hot New Releases: the full top 100 per list with rank, ASIN, name, price, currency, stars, ratings count, URL and image, for the US, UK, DE, FR, ES, IT, CA, AU, IN and JP stores.
- [AutoScout24 Scraper](https://apify.com/daedal_quintuplet/autoscout24-scraper): AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details.
- [Flipkart Scraper](https://apify.com/daedal_quintuplet/flipkart-scraper): Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL.
- [Gumroad Scraper](https://apify.com/daedal_quintuplet/gumroad-scraper): Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants.
