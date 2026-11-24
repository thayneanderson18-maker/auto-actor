// Run Wappalyzer Alternative: Tech Stack Detector on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/wappalyzer-tech-stack-detector').call({
        "urls": [
            "https://stripe.com",
            "https://shopify.com",
            "https://wordpress.org"
        ]
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const site of items) {
        console.log(site.domain, '|', site.tech_count, '|', site.tech_names);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
