# Wappalyzer Alternative: Tech Stack Detector

The technologies any website uses: CMS, ecommerce, analytics, JavaScript frameworks, CDN, hosting and email provider, from 7,700+ open-source fingerprints with evidence, versions and confidence. An only-changes mode suits scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/wappalyzer-tech-stack-detector
- Price: $0.002 per website ($2 per 1,000); the first 25 websites of every run are free, and error rows are never charged. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/wappalyzer-tech-stack-detector`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `urls` | array of strings | Websites to analyze: bare domains or full URLs. One result row per website. | `["stripe.com", "https://shopify.com"]` |
| `categories_filter` | array of strings | Return only technologies in these categories, e.g. `CMS`, `Ecommerce`, `Analytics`. | `["CMS", "Ecommerce"]` |
| `include_versions` | boolean | Add the version number a site exposes (e.g. WordPress 6.6). | `true` |
| `include_confidence` | boolean | Add a 0 to 100 confidence score per technology. | `true` |
| `includeDns` | boolean | Also read MX, TXT, NS and SOA records to find email and DNS providers. | `true` |
| `onlyChanges` | boolean | For schedules: return a site only when it is new or its technology list changed since the last run. | `false` |
| `timeout_seconds` | integer | How long to wait for each site, 3 to 60 seconds. | `20` |
| `maxConcurrency` | integer | How many sites to fetch at once, 1 to 50. | `10` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `url` | `"https://mailchimp.com/"` | The URL analyzed |
| `domain` | `"mailchimp.com"` | Domain |
| `status_code` | `200` | HTTP status of the page |
| `final_url` | `"https://mailchimp.com/"` | URL after redirects |
| `title` | `"Email & SMS Marketing Platform | Mailchimp"` | Page title |
| `tech_count` | `2` | Number of technologies found |
| `tech_names` | `"Apple iCloud Mail, Microsoft 365"` | Technology names, comma-separated |
| `category_list` | `"Webmail, Email"` | Categories found, comma-separated |
| `categories` | `{"Webmail": ["Apple iCloud Mail", …], …}` | Technologies grouped by category |
| `technologies` | `[{"name": …, "category": …, "evidence": …}, …]` | One entry per technology, with evidence and, when enabled, version and confidence |
| `dns_mx` | `["mx1.intuit.iphmx.com", …]` | Mail servers (with `includeDns`) |
| `blocked_page` | `false` | True when the site served a block or challenge page |
| `scan_time_ms` | `1113` | How long the scan took |
| `scanned_at` | `"2026-11-18T23:18:40.128Z"` | When it was scanned |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~wappalyzer-tech-stack-detector/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://stripe.com", "https://shopify.com", "https://wordpress.org"]}'
```

## Typical uses

- Lead lists: find which sites in a list run Shopify, WordPress or a competitor's tool.
- Watching competitors' stacks on a schedule with `onlyChanges: true`.
- Enriching a CRM with each account's CMS, analytics and email provider.

## Notes

- Some technologies come from DNS records, including TXT domain-verification entries (e.g. `openai-domain-verification`). Those show services the company has an account with, not what the website itself runs on; each technology's `evidence` says where it was found.
- Sites that block data-center traffic can be scanned through an Apify proxy (`proxyConfiguration`).

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
- [Amazon Bestsellers Scraper](https://apify.com/daedal_quintuplet/amazon-bestsellers-scraper): Amazon Best Sellers and Hot New Releases: the full top 100 per list with rank, ASIN, name, price, currency, stars, ratings count, URL and image, for the US, UK, DE, FR, ES, IT, CA, AU, IN and JP stores.
- [AutoScout24 Scraper](https://apify.com/daedal_quintuplet/autoscout24-scraper): AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details.
- [Flipkart Scraper](https://apify.com/daedal_quintuplet/flipkart-scraper): Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL.
- [Gumroad Scraper](https://apify.com/daedal_quintuplet/gumroad-scraper): Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants.
- [Built In Jobs Scraper](https://apify.com/daedal_quintuplet/builtin-jobs-scraper): Tech jobs from builtin.
