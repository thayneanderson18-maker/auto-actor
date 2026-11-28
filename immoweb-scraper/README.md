# Immoweb Scraper

Belgian real estate from Immoweb: houses, apartments, land and offices for sale or rent, with price, address, coordinates, bedrooms, living area, EPC, photos and agency, plus optional full details. Search URLs or filters, and an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/immoweb-scraper
- Price: $0.0009 per listing ($0.90 per 1,000); the first 25 listings of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/immoweb-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `startUrls` | array of strings | Immoweb search result URLs in any language (set filters on immoweb.be and copy the address bar), or single listing URLs. | `["https://www.immoweb.be/en/search/apartment/for-rent?countries=BE&postalCodes=1050&orderBy=newest"]` |
| `propertyType` | string | Instead of URLs: the kind of property, e.g. `apartment`. | `"apartment"` |
| `transactionType` | string | `for-sale` or `for-rent`. | `"for-rent"` |
| `postalCodes` | string | Belgian postal codes, comma-separated; empty for all of Belgium. | `"1000, 1050, 9000"` |
| `minPrice / maxPrice` | integer | Price range in euros (monthly rent for rentals). | `200000 / 450000` |
| `minBedrooms / maxBedrooms` | integer | Bedroom range. | `2 / 4` |
| `minSurface / maxSurface` | integer | Living-area range in m². | `80 / 200` |
| `epcScores` | string | Energy labels to keep, comma-separated. | `"A, B, C"` |
| `sortBy` | string | Result order; `newest` suits only-new mode. | `"newest"` |
| `maxResults` | integer | Stop after this many listings; 0 for no limit. | `500` |
| `includeDetails` | boolean | Open each listing for the description, construction year, heating, parking, energy use, all photos and more. | `false` |
| `onlyNew` | boolean | Return only listings that no earlier run with the same `stateKey` returned. Ideal for schedules. | `true` |
| `stateKey` | string | Name of the memory `onlyNew` uses; one per scheduled search. | `"brussels-rentals"` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `22017399` | Immoweb listing id |
| `url` | `"https://www.immoweb.be/en/classified/…/22017399"` | Link to the listing |
| `title` | `"Recente enkele garagebox te huur in Houthulst"` | Listing title (can be empty) |
| `propertyType` | `"GARAGE"` | Property type |
| `propertySubtype` | `"LOCK_UP_PARKING"` | Subtype |
| `transactionType` | `"FOR_RENT"` | For sale or for rent |
| `price` | `85` | Price in euros (monthly for rentals) |
| `priceDisplay` | `"€85/month"` | Price as shown |
| `bedrooms` | `0` | Bedrooms |
| `livingArea` | `null` | Living area in m² |
| `landArea` | `null` | Land area in m² |
| `epcScore` | `null` | Energy label |
| `street` | `"Kerkstraat"` | Street, when shown |
| `postalCode` | `"8650"` | Postal code |
| `locality` | `"Houthulst"` | Town |
| `province` | `"West Flanders"` | Province |
| `latitude` | `50.9782275` | Latitude |
| `longitude` | `2.9495377` | Longitude |
| `advertiserName` | `"Bordes Roeselare-Hooglede"` | Agency or advertiser |
| `advertiserType` | `"PROFESSIONAL"` | Professional or private |
| `imageUrl` | `"https://media-resize.immowebstatic.be/…"` | Main photo |
| `isNewlyListed` | `true` | Immoweb's 'new' flag |
| `lastModificationDate` | `"2026-11-27T19:56:23.283Z"` | When the listing last changed |
| `scrapedAt` | `"2026-11-27T23:09:59.416Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~immoweb-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": ["https://www.immoweb.be/en/search/apartment/for-rent?countries=BE&postalCodes=1050&orderBy=newest"], "maxResults": 20}'
```

## Typical uses

- A morning alert of new rentals or homes for sale in your postal codes, with `sortBy: "newest"` and `onlyNew: true`.
- Price-per-m² research by town or province.
- Mapping listings with their coordinates.

## Notes

- Immoweb shows at most about 10,000 listings per search; split big searches by postal code or price.
- `includeDetails` opens every listing page, so runs take longer; leave it off when the search fields are enough.

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
- [Built In Jobs Scraper](https://apify.com/daedal_quintuplet/builtin-jobs-scraper): Tech jobs from builtin.
- [TradingView Screener Scraper](https://apify.com/daedal_quintuplet/tradingview-screener-scraper): TradingView screener data for stocks in 45 markets, crypto, forex and futures: price, change, volume, market cap, P/E, RSI, MACD, moving averages, technical rating and performance.
