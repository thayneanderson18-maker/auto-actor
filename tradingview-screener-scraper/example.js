// Run TradingView Screener Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/tradingview-screener-scraper').call({
        "market": "america",
        "preset": "top_gainers",
        "maxResults": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const row of items) {
        console.log(row.fullSymbol, '|', row.close, row.currency, '|', (row.changePercent ?? 0).toFixed(2), '% |', row.recommendationLabel);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
