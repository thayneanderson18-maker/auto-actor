# Google Images Scraper

Google Images search results: full-size image URL, width and height, thumbnail, title, source page and website. About 100 images per page, with size, type and date filters, any country, and an only-new mode for scheduled runs.

- Store page: https://apify.com/daedal_quintuplet/google-images-scraper
- Price: $0.0021 per image ($2.10 per 1,000). Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/google-images-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `queries` | array of strings | Searches, written the way you would type them into Google. | `["red sneakers"]` |
| `maxResultsPerQuery` | integer | The most images to return for each search (Google serves about 100 per page). | `100` |
| `country` | string | Two-letter country code Google searches from, e.g. `us`, `gb`, `de`. | `"us"` |
| `language` | string | Interface language code, e.g. `en`, `de`. | `"en"` |
| `imageSize` | string | `any`, `large`, `medium` or `icon`. | `"large"` |
| `imageType` | string | `any`, `photo`, `clipart`, `lineart` or `animated`. | `"photo"` |
| `timeRange` | string | `any`, `day`, `week`, `month` or `year`. | `"month"` |
| `safeSearch` | boolean | Keep Google SafeSearch on. | `true` |
| `onlyNew` | boolean | Skip images already returned by earlier runs (remembered for 90 days in the `google-images-seen` store of your account). Ideal for schedules. | `false` |
| `debug` | boolean | Save raw HTML for debugging. | `false` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `query` | `"lighthouse watercolor"` | The query that found it |
| `position` | `3` | Rank in the results |
| `imageId` | `"eUsS9nT4JvA4tM"` | Google's image id |
| `title` | `"Step-by-Step Watercolor Painting: Highland Light…"` | Title Google shows |
| `imageUrl` | `"https://i0.wp.com/farm8.staticflickr.com/…jpg"` | Full-size image URL |
| `imageWidth` | `408` | Full-size width in pixels |
| `imageHeight` | `640` | Full-size height in pixels |
| `thumbnailUrl` | `"https://encrypted-tbn0.gstatic.com/images?q=…"` | Google's thumbnail |
| `thumbnailWidth` | `408` | Thumbnail width |
| `thumbnailHeight` | `640` | Thumbnail height |
| `contentUrl` | `"https://www.lesliefehling.com/step-by-step-…"` | The page the image appears on |
| `origin` | `"www.lesliefehling.com"` | Website domain |
| `source` | `"Leslie Fehling"` | Website name |
| `fileSize` | `"59KB"` | File size when Google shows it |
| `country` | `"us"` | Country searched from |
| `scrapedAt` | `"2026-11-08T23:07:59.702Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~google-images-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["red sneakers"], "maxResultsPerQuery": 100, "country": "us"}'
```

## Typical uses

- Collecting reference or mood-board images for a topic, with source pages for attribution.
- Monitoring where a product or brand image appears across the web, daily with `onlyNew: true`.
- Building image datasets with dimensions to filter by size.

## Notes

- Images belong to their owners; check the source page's licence before reusing one.
- Google serves about 100 images per page; use several specific queries for more.

## Our other actors

- [Seek AU Job Scraper](https://apify.com/daedal_quintuplet/seek-au-job-scraper): Job listings from SEEK Australia (seek.
- [Seek NZ Job Scraper](https://apify.com/daedal_quintuplet/seek-nz-job-scraper): Job listings from SEEK New Zealand (seek.
- [Google Trends Scraper](https://apify.com/daedal_quintuplet/google-trends-scraper-all-widgets): Google Trends data for up to 20 keywords per run: interest over time, interest by region and related queries, as flat rows that drop straight into Sheets, a BI tool or an AI agent.
- [Google Jobs Scraper (US & UK)](https://apify.com/daedal_quintuplet/google-jobs-scraper): Google Jobs results for US and UK searches: title, company, location, salary, job type, the full description and the real apply links behind each listing.
- [Greenhouse Jobs Scraper](https://apify.com/daedal_quintuplet/greenhouse-jobs-scraper): Every open job from any company's Greenhouse job board: title, company, locations, departments, posted date, published salary range, full description and apply link.
