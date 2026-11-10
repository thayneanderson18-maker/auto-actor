// Run Career Site Jobs Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/career-site-jobs-scraper').call({
        "companies": [
            "https://jobs.lever.co/spotify",
            "https://jobs.ashbyhq.com/notion"
        ],
        "maxItems": 50
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const job of items) {
        console.log(job.title, '|', job.organization, '|', job.location, '|', job.source);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
