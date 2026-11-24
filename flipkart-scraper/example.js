// Run Flipkart Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/flipkart-scraper').call({
        "searchQueries": [
            "iphone"
        ],
        "maxItems": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const product of items) {
        console.log(product.title, '|', product.price, product.currency, '|', product.rating);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
