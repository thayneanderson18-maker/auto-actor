// Run Google Trends Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/google-trends-scraper-all-widgets').call({
        "keywords": [
            "bitcoin"
        ],
        "geo": "",
        "timeRange": "past_12_months"
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const row of items) {
        console.log(row.kind, '|', row.label, '|', row.value);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
