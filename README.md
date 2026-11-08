# Apify actors by daedal_quintuplet

Working examples for every public actor we run on the [Apify Store](https://apify.com/daedal_quintuplet). Each folder has a README with the exact input and output fields, a Python example, a Node.js example, and notes for n8n, Make and plain HTTP.

| Actor | What it returns | Price | Page |
|---|---|---|---|
| [Seek AU Job Scraper](seek-au-job-scraper/) | Job listings from SEEK Australia (seek. | $0.001 per job | [Store](https://apify.com/daedal_quintuplet/seek-au-job-scraper) |
| [Seek NZ Job Scraper](seek-nz-job-scraper/) | Job listings from SEEK New Zealand (seek. | $0.001 per job | [Store](https://apify.com/daedal_quintuplet/seek-nz-job-scraper) |
| [Google Trends Scraper](google-trends-scraper-all-widgets/) | Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent. | $0.0025 per row | [Store](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets) |
| [Google Jobs Scraper (US & UK)](google-jobs-scraper/) | Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing. | $0.0025 per job | [Store](https://apify.com/daedal_quintuplet/google-jobs-scraper) |

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
