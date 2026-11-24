// Run Amazon Bestsellers Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/amazon-bestsellers-scraper').call({
        "startUrls": [
            {
                "url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"
            }
        ],
        "maxItemsPerList": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const product of items) {
        console.log(product.position, product.name.slice(0, 60), '|', product.priceText || 'no price', '|', product.stars);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
