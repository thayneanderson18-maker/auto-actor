# Apify actors by daedal_quintuplet

Working examples for every public actor we run on the [Apify Store](https://apify.com/daedal_quintuplet). Each folder has a README with the exact input and output fields, a Python example, a Node.js example, and notes for n8n, Make and plain HTTP.

| Actor | What it returns | Price | Page |
|---|---|---|---|
| [Seek AU Job Scraper](seek-au-job-scraper/) | Job listings from SEEK Australia (seek. | $0.001 per job | [Store](https://apify.com/daedal_quintuplet/seek-au-job-scraper) |
| [Seek NZ Job Scraper](seek-nz-job-scraper/) | Job listings from SEEK New Zealand (seek. | $0.001 per job | [Store](https://apify.com/daedal_quintuplet/seek-nz-job-scraper) |
| [Google Trends Scraper](google-trends-scraper-all-widgets/) | Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent. | $0.0025 per row | [Store](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets) |
| [Google Jobs Scraper (US & UK)](google-jobs-scraper/) | Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing. | $0.0025 per job | [Store](https://apify.com/daedal_quintuplet/google-jobs-scraper) |
| [Greenhouse Jobs Scraper](greenhouse-jobs-scraper/) | Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link. | $0.0012 per job | [Store](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper) |
| [Google Images Scraper](google-images-scraper/) | Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website. | $0.0021 per image | [Store](https://apify.com/daedal_quintuplet/google-images-scraper) |
| [Career Site Jobs Scraper](career-site-jobs-scraper/) | Open jobs straight from company career sites on Lever, Ashby, SmartRecruiters, Workday and Workable: title, company, location, remote flag, salary, department, posted date, full description and apply link. | $0.0015 per job | [Store](https://apify.com/daedal_quintuplet/career-site-jobs-scraper) |
| [Flashscore Scraper](flashscore-scraper/) | Results and fixtures from any Flashscore league, cup, tennis tournament or team page: scores, half-time, sets, quarters, rounds, dates, team IDs and logos. | $0.0008 per match | [Store](https://apify.com/daedal_quintuplet/flashscore-scraper) |
| [Craigslist Scraper](craigslist-scraper/) | Craigslist listings from any site and category: for sale, cars, housing, jobs, gigs and services. | $0.001 per listing | [Store](https://apify.com/daedal_quintuplet/craigslist-scraper) |
| [Wappalyzer Alternative: Tech Stack Detector](wappalyzer-tech-stack-detector/) | The technologies any website uses: CMS, ecommerce, analytics, JavaScript frameworks, CDN, hosting and email provider, from 7,700+ open-source fingerprints with evidence, versions and confidence. | $0.002 per website | [Store](https://apify.com/daedal_quintuplet/wappalyzer-tech-stack-detector) |
| [Amazon Bestsellers Scraper](amazon-bestsellers-scraper/) | Amazon Best Sellers and Hot New Releases: the full top 100 per list with rank, ASIN, name, price, currency, stars, ratings count, URL and image, for the US, UK, DE, FR, ES, IT, CA, AU, IN and JP stores. | $0.001 per product | [Store](https://apify.com/daedal_quintuplet/amazon-bestsellers-scraper) |
| [AutoScout24 Scraper](autoscout24-scraper/) | AutoScout24 car listings from 8 European countries: price, mileage, registration, fuel, power, equipment, description, photos and dealer details. | $0.0008 per listing | [Store](https://apify.com/daedal_quintuplet/autoscout24-scraper) |
| [Flipkart Scraper](flipkart-scraper/) | Flipkart search, category and product pages: title, brand, price, MRP, discount, rating, star breakdown, key specs, stock, images and URL. | $0.0008 per product | [Store](https://apify.com/daedal_quintuplet/flipkart-scraper) |
| [Gumroad Scraper](gumroad-scraper/) | Gumroad products from Discover searches, categories, tags, creator storefronts and product pages: name, price, USD price, rating, seller, type and link, with optional description, sales count and variants. | $0.001 per product | [Store](https://apify.com/daedal_quintuplet/gumroad-scraper) |
| [Built In Jobs Scraper](builtin-jobs-scraper/) | Tech jobs from builtin. | $0.0009 per job | [Store](https://apify.com/daedal_quintuplet/builtin-jobs-scraper) |

All actors are pay-per-event: you pay per result, nothing per month, and Apify's free plan includes $5 of usage a month.

## Running any of them

1. Create an Apify account and copy your API token (Console → Settings → Integrations).
2. Open the actor's folder here and run `example.py` or `example.js`, or follow `n8n-make.md` for no-code tools.
3. Or make one HTTP call:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~seek-au-job-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": "carpenter", "where": "Brisbane", "maxItems": 50}'
```

## About this repository

The examples are regenerated from live test runs of each actor, so the fields shown are the fields you get. Found a problem? Open an issue here or on the actor's Store page.

## Maintaining this repository

`actors.json` holds the facts for each actor (fields, examples, pitch, uses, notes). `tools/generate.py` renders everything else from it. To add or update an actor, edit `actors.json` and run:

```bash
python3 tools/generate.py
```
