# Flipkart Scraper

Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL. No residential proxy needed, with an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/flipkart-scraper
- Price: $0.0008 per product ($0.80 per 1,000); the first 25 products of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/flipkart-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `searchQueries` | array of strings | Words to search on Flipkart, one search each. | `["iphone 15", "running shoes"]` |
| `startUrls` | array of {url} | Flipkart search, category (`/pr?sid=`) or product (`/p/itm`) pages. | `[{"url": "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&marketplace=FLIPKART"}]` |
| `maxItems` | integer | Stop each search or URL after this many unique products. | `100` |
| `sort` | string | `relevance`, `popularity`, `price_asc`, `price_desc` or `newest`. | `"price_asc"` |
| `includeDetails` | boolean | Also open each product page for the description, colour, return window and full-size photos. | `false` |
| `onlyNew` | boolean | Skip products already returned to you (remembered 120 days). Leave off for price tracking. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"MOBHQV9YCUG4ZQZK"` | Flipkart product id |
| `title` | `"Apple iPhone 17 (Black, 256 GB)"` | Product title |
| `brand` | `"Apple"` | Brand |
| `category` | `"Mobile"` | Category |
| `price` | `89100` | Selling price |
| `original_price` | `99900` | MRP |
| `discount_percent` | `10` | Discount in percent |
| `rating` | `4.6` | Average rating |
| `rating_count` | `50678` | Number of ratings |
| `review_count` | `3115` | Number of reviews |
| `rating_breakdown` | `{"1": 2085, …, "5": 40103}` | Ratings per star |
| `key_specs` | `["256 GB ROM", "16.0 cm (6.3 inch) Super Retina XDR Display", …]` | Key specifications |
| `availability_status` | `"IN_STOCK"` | Stock status |
| `is_flipkart_assured` | `true` | Flipkart Assured badge |
| `currency` | `"INR"` | Currency |
| `image_url` | `"https://rukmini1.flixcart.com/image/…"` | Main image |
| `url` | `"https://www.flipkart.com/apple-iphone-17-black-256-gb/p/…"` | Product page |
| `position` | `1` | Position in the results |
| `search_query` | `"iphone"` | The search that found it |
| `fetched_at` | `"2026-11-19T23:15:21.086Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~flipkart-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["iphone"], "maxItems": 20}'
```

## Typical uses

- Daily price tracking for a list of products or a search.
- Discount and rating comparisons across a category.
- New-listing alerts with `onlyNew: true`.

## Notes

- Flipkart shows 24 to 40 products per page; the actor follows pages up to `maxItems` per search.
- Turn on `includeDetails` only when you need the description or full-size photos: it opens every product page.

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
- [Gumroad Scraper](https://apify.com/daedal_quintuplet/gumroad-scraper): Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants.
