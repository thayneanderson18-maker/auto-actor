// Run AutoScout24 Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/autoscout24-scraper').call({
        "startUrls": [
            {
                "url": "https://www.autoscout24.com/lst/bmw/x5?atype=C&sort=age&desc=1"
            }
        ],
        "maxItems": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const car of items) {
        console.log(car.title, '|', car.rawPrice, car.currency, '|', car.mileageKm, 'km |', car.city);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
