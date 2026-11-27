# TradingView Screener Scraper

TradingView screener data for stocks in 45 markets, crypto, forex and futures: price, change, volume, market cap, P/E, RSI, MACD, moving averages, technical rating and performance. Ready-made presets, custom filters, symbol lookups and an only-new mode for scheduled screens.

- Store page: https://apify.com/daedal_quintuplet/tradingview-screener-scraper
- Price: $0.001 per row ($1 per 1,000); the first 25 rows of every run are free. Pay per result, nothing per month. Apify's free plan includes $5 of usage a month, enough to try it.
- Actor id for the API and clients: `daedal_quintuplet/tradingview-screener-scraper`

## Input

| Field | Type | What it does | Example |
|---|---|---|---|
| `market` | string | Which screener to scan: a country's stock market (`america` = US), `crypto`, `coin`, `forex`, `futures`, `bond`, `cfd` or `global`. | `"america"` |
| `preset` | string | A ready-made screen, e.g. `top_gainers` or `oversold_rsi`. Leave empty to scan the whole market with your own filters. | `"top_gainers"` |
| `minMarketCap` | integer | Only symbols worth at least this many US dollars; 0 turns it off. | `1000000000` |
| `filters` | array of objects | Extra conditions, each `{"left": field, "operation": op, "right": value}`. | `[{"left": "RSI", "operation": "less", "right": 40}]` |
| `sortBy` | string | Field to sort by, e.g. `volume`, `marketCap`, `changePercent`, `rsi`. | `"marketCap"` |
| `sortOrder` | string | `desc` or `asc`. | `"desc"` |
| `maxResults` | integer | Most rows to return; 0 returns every match (a full US scan is about 20,000 rows). | `100` |
| `symbols` | array of strings | Look up specific symbols instead of screening, as `EXCHANGE:SYMBOL`. | `["NASDAQ:AAPL", "BINANCE:BTCUSDT"]` |
| `searchQueries` | array of strings | Company, coin or ticker names to look up with TradingView symbol search. | `["Tesla"]` |
| `onlyNew` | boolean | For schedules: return only symbols that newly match the screen since the last run with the same `stateKey`. | `false` |
| `stateKey` | string | Name of the memory `onlyNew` uses; one per scheduled screen. | `"us-oversold-daily"` |

## Output

One row per result, saved to the run's dataset. Download as JSON, CSV or Excel from Apify, or read it with the examples below.

| Field | Example | Meaning |
|---|---|---|
| `symbol` | `"MRNA"` | Ticker |
| `fullSymbol` | `"NASDAQ:MRNA"` | Exchange and ticker |
| `name` | `"Moderna, Inc."` | Name |
| `exchange` | `"NASDAQ"` | Exchange |
| `type` | `"stock"` | stock, dr, fund, crypto and so on |
| `currency` | `"USD"` | Price currency |
| `close` | `220.84` | Last price |
| `changePercent` | `-2.88` | Change today, % |
| `volume` | `6812616` | Volume today |
| `relativeVolume` | `0.85` | Volume compared with the 10-day average |
| `marketCap` | `89356493904` | Market capitalisation |
| `peRatio` | `null` | Price/earnings ratio |
| `eps` | `-7.068` | Earnings per share |
| `dividendYield` | `0` | Dividend yield, % |
| `rsi` | `51.1` | RSI (14) |
| `macdValue` | `-0.115` | MACD |
| `sma50` | `212.37` | 50-day simple moving average (also `ema10`…`sma200`) |
| `recommendationAll` | `0.22` | TradingView technical rating, −1 (strong sell) to 1 (strong buy) |
| `recommendationLabel` | `"buy"` | The rating as a word |
| `perfYTD` | `640.33` | Performance year to date, % (also week, month, 3/6 months, year) |
| `sector` | `"Health Technology"` | Sector |
| `industry` | `"Biotechnology"` | Industry |
| `country` | `"United States"` | Country |
| `url` | `"https://www.tradingview.com/symbols/NASDAQ-MRNA/"` | TradingView page |
| `scrapedAt` | `"2026-11-26T23:09:54.087Z"` | When it was scraped |

## Run it

- [`example.py`](example.py): Python, with the official `apify-client` package.
- [`example.js`](example.js): Node.js, with the official `apify-client` package.
- [`n8n-make.md`](n8n-make.md): no-code, in n8n, Make or anything that can send an HTTP request.
- One HTTP call, no library:

```bash
curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~tradingview-screener-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"market": "america", "preset": "top_gainers", "maxResults": 20}'
```

## Typical uses

- A daily list of stocks that newly turned oversold or broke out, with a preset or filters and `onlyNew: true`.
- Snapshots of fundamentals and technicals for a watchlist of symbols, into a spreadsheet.
- Crypto and forex screens with the same fields as stocks.

## Notes

- Data is TradingView's screener data, which can be delayed by the exchange; it is not for trading decisions on its own.
- Stock-market presets keep primary listings of liquid companies (market cap over $300M, 10-day average volume over 100k).

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
