# Amazon Bestsellers Scraper

Amazon Best Sellers and Hot New Releases: the full top 100 per list with rank, ASIN, name, price, currency, stars, ratings count, URL and image, for the US, UK, DE, FR, ES, IT, CA, AU, IN and JP stores. Sub-departments and an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/amazon-bestsellers-scraper
- Price: $0.001 per product ($1 per 1,000); the first 25 products of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/amazon-bestsellers-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `startUrls` | array of {url} | Amazon ranking pages: Best Sellers, Hot New Releases, Movers and Shakers, Most Wished For or Gift Ideas, from any supported store. | `[{"url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"}]` |
| `maxItemsPerList` | integer | How many ranked products to take from each list, from rank 1 down (lists hold at most 100). | `100` |
| `includeSubcategories` | boolean | Also scrape every sub-department one level down (e.g. Electronics → Headphones). | `false` |
| `maxSubcategories` | integer | Upper limit on sub-departments followed per start URL. | `40` |
| `maxItems` | integer | Stop the run after this many products in total; 0 means no limit. | `1000` |
| `onlyNew` | boolean | Return only products that newly entered a list since the last run (remembered 120 days per list). Ideal for schedules. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `position` | `1` | Rank in the list |
| `asin` | `"B0CSP8H16R"` | Amazon ASIN |
| `name` | `"Hex Bots - Radio-controlled Gecko…"` | Product name |
| `price` | `13.99` | Price as a number (null when not shown) |
| `currency` | `"€"` | Currency symbol |
| `currencyCode` | `"EUR"` | Currency code |
| `priceText` | `"€13.99"` | Price as shown |
| `stars` | `4.2` | Average rating |
| `reviewsCount` | `3432` | Number of ratings |
| `url` | `"https://www.amazon.fr/-/en/Hex-Bots…/dp/B0CSP8H16R"` | Product page |
| `imageUrl` | `"https://images-eu.ssl-images-amazon.com/images/I/…jpg"` | Product image |
| `categoryName` | `"Best Sellers in Toys & Games"` | The list it came from |
| `categoryUrl` | `"https://www.amazon.fr/gp/bestsellers/toys"` | List URL |
| `listType` | `"bestsellers"` | Best Sellers, Hot New Releases and so on |
| `domain` | `"amazon.fr"` | Amazon store |
| `scrapedAt` | `"2026-11-23T23:10:01.591Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~amazon-bestsellers-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": [{"url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"}], "maxItemsPerList": 20}'
```

## Typical uses

- Daily snapshots of a category's top 100 to see what's rising, with `onlyNew: true` for new entries.
- Product research across Amazon stores in several countries.
- Price and rating tracking for the bestsellers in your niche.

## Notes

- Amazon's ranking lists hold at most 100 products each.
- The actor picks the right Apify proxy per store by default; keep the default `proxyConfiguration`.

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
- [AutoScout24 Scraper](https://apify.com/daedal_quintuplet/autoscout24-scraper): AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details.
- [Flipkart Scraper](https://apify.com/daedal_quintuplet/flipkart-scraper): Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL.
