# AutoScout24 Scraper

AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details. Paste any search URL or set make and model, with an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/autoscout24-scraper
- Price: $0.0008 per listing ($0.80 per 1,000); the first 25 listings of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/autoscout24-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `startUrls` | array of {url} | AutoScout24 search results pages (address contains `/lst/`) or single listings, on .com, .de, .it, .fr, .nl, .be, .at, .es or .lu. | `[{"url": "https://www.autoscout24.com/lst/bmw/x5?atype=C&sort=age&desc=1"}]` |
| `make` | string | Instead of URLs: car make as in AutoScout24 addresses, e.g. `volkswagen`, `bmw`. | `"volkswagen"` |
| `model` | string | Model within the make, e.g. `golf`. | `"golf"` |
| `countries` | array of strings | Countries to search with `make`: DE, AT, BE, ES, FR, IT, LU, NL. | `["DE", "AT"]` |
| `priceFrom / priceTo` | integer | Price range in euros. | `5000 / 20000` |
| `yearFrom / yearTo` | integer | First-registration year range. | `2018 / 2022` |
| `mileageTo` | integer | Highest mileage in km. | `100000` |
| `fuelTypes` | array of strings | e.g. `petrol`, `diesel`, `electric`, `hybrid-petrol`. | `["diesel", "electric"]` |
| `condition` | string | `used`, `new` or `any`. | `"used"` |
| `sortBy` | string | `standard`, `newest`, `price` or `mileage`. | `"newest"` |
| `maxItems` | integer | Stop after this many listings in total. | `100` |
| `includeDetails` | boolean | Open every listing for the description, equipment, body type, colour, owners and more. | `true` |
| `onlyNew` | boolean | Skip listings already returned to you (remembered 180 days). Ideal for schedules. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `id` | `"af9e7c3a-8b1c-4c2a-b4f5-3a12582a24e1"` | Listing id |
| `url` | `"https://www.autoscout24.es/anuncios/seat-ibiza-…"` | Link to the listing |
| `title` | `"SEAT Ibiza 1.5 TSI S&S FR XS Edition DSG7 150"` | Listing title |
| `make` | `"SEAT"` | Make |
| `model` | `"Ibiza"` | Model |
| `rawPrice` | `14950` | Price as a number |
| `currency` | `"EUR"` | Currency |
| `mileageKm` | `90000` | Mileage in km |
| `firstRegistration` | `"03/2022"` | First registration |
| `year` | `2022` | Year |
| `fuelType` | `"Gasolina"` | Fuel type as shown on the site |
| `gearbox` | `"Automático"` | Gearbox |
| `powerKw` | `110` | Power in kW |
| `powerHp` | `150` | Power in hp |
| `offerType` | `"Used"` | Used or new |
| `city` | `"Igualada"` | Location |
| `countryCode` | `"ES"` | Country |
| `seller` | `"Dealer"` | Dealer or private |
| `dealerName` | `"ANOIA MOTOR SEAT - HYUNDAI"` | Dealer name |
| `images` | `["https://prod.pictures.autoscout24.net/…", …]` | Photo URLs |
| `scrapedAt` | `"2026-11-17T23:16:40.495Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~autoscout24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": [{"url": "https://www.autoscout24.com/lst/bmw/x5?atype=C&sort=age&desc=1"}], "maxItems": 20}'
```

## Typical uses

- A daily alert of new listings for a make and model with `sortBy: "newest"` and `onlyNew: true`.
- Used-car price research across countries and years.
- Dealer stock monitoring.

## Notes

- AutoScout24 shows 20 listings per page; the actor follows the pages up to `maxItems`.
- Text fields such as `fuelType` come in the language of the site you search.

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
- [Flipkart Scraper](https://apify.com/daedal_quintuplet/flipkart-scraper): Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL.
