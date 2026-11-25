# Gumroad Scraper

Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants. Price, rating and file-type filters, plus an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/gumroad-scraper
- Price: $0.001 per product ($1 per 1,000); the first 25 products of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/gumroad-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `searchQueries` | array of strings | Searches in Gumroad Discover, one per entry. | `["notion template", "lightroom presets"]` |
| `tags` | array of strings | Gumroad tags to browse, one listing per tag. | `["procreate"]` |
| `categories` | array of strings | Category paths as in Gumroad URLs, e.g. `design`, `3d/vrchat`. | `["3d/vrchat"]` |
| `startUrls` | array of {url} | Discover searches, category pages, creator storefronts or single products. | `[{"url": "https://gumroad.com/discover?query=notion"}]` |
| `sort` | string | Order of results, as on Gumroad Discover, e.g. `best_sellers`. | `"best_sellers"` |
| `minPrice / maxPrice` | integer | Price range in US dollars; 0 means no limit. | `5 / 50` |
| `minRating` | integer | Minimum average star rating, 1 to 4. | `4` |
| `fileTypes` | array of strings | Only products containing these file types, e.g. `pdf`, `zip`. | `["pdf"]` |
| `maxItems` | integer | Stop after this many products in total; 0 means no limit. | `100` |
| `maxItemsPerSource` | integer | At most this many products from each input. | `200` |
| `productDetails` | boolean | Also open each product page for the description, sales count (when shown), rating breakdown, covers and variants. | `false` |
| `onlyNew` | boolean | Return only products not returned before under the same `stateKey` (remembered 180 days). Ideal for schedules. | `false` |
| `stateKey` | string | Name of the memory `onlyNew` uses; one per schedule. | `"notion-templates"` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"rS7gSD0HH4dRnYrlzIQHkg=="` | Gumroad product id |
| `name` | `"Headquarters Notion Productivity Template"` | Product name |
| `url` | `"https://productivesetups.gumroad.com/l/headquarters"` | Product page |
| `price` | `79` | Price in the seller's currency |
| `currency_code` | `"AUD"` | Seller's currency |
| `price_usd` | `52.45` | Price converted to US dollars |
| `is_pay_what_you_want` | `false` | Pay-what-you-want pricing |
| `native_type` | `"digital"` | Product type, e.g. digital, bundle, course, membership |
| `recurrence` | `null` | Billing period for subscriptions |
| `rating_count` | `202` | Number of ratings |
| `rating_average` | `5` | Average rating |
| `seller_name` | `"Productive Setups"` | Creator |
| `thumbnail_url` | `"https://public-files.gumroad.com/…"` | Thumbnail |
| `search_query` | `"notion template"` | The search that found it |
| `position` | `1` | Position in the results |
| `scraped_at` | `"2026-11-24T23:36:31.754Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~gumroad-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["notion template"], "maxItems": 20}'
```

## Typical uses

- Market research for a digital product: prices, ratings and top sellers in a niche.
- Watching a search or tag for new products with `onlyNew: true`.
- Tracking competitors' storefronts and price changes.

## Notes

- Gumroad Discover returns 36 products per page; the actor follows pages until your limits or the results run out.
- Sales counts only appear with `productDetails` on, and only when the seller shows them.

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
