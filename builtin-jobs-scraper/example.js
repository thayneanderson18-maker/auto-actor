// Run Built In Jobs Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/builtin-jobs-scraper').call({
        "searchQueries": [
            "data engineer"
        ],
        "maxTotalResults": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const job of items) {
        console.log(job.title.slice(0, 60), '|', job.company, '|', job.workplaceType, '|', job.salaryText || 'no salary listed');
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
