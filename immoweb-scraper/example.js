// Run Immoweb Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/immoweb-scraper').call({
        "startUrls": [
            "https://www.immoweb.be/en/search/apartment/for-rent?countries=BE&postalCodes=1050&orderBy=newest"
        ],
        "maxResults": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const listing of items) {
        console.log((listing.title || listing.propertyType || '').slice(0, 60), '|', listing.priceDisplay, '|', listing.bedrooms, 'bed |', listing.locality);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
