// Run Google Images Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/google-images-scraper').call({
        "queries": [
            "red sneakers"
        ],
        "maxResultsPerQuery": 100,
        "country": "us"
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const image of items) {
        console.log(image.position, image.title, image.imageUrl, `${image.imageWidth}x${image.imageHeight}`);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
