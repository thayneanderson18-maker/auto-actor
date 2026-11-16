// Run Flashscore Scraper on Apify and print the results.
//
//   npm install apify-client
//   APIFY_TOKEN=... node example.js     (token: Apify Console -> Settings -> Integrations)

const { ApifyClient } = require('apify-client');

async function main() {
    const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

    const run = await client.actor('daedal_quintuplet/flashscore-scraper').call({
        "startUrls": [
            {
                "url": "https://www.flashscore.com/football/england/premier-league/results/"
            }
        ],
        "matchType": "results",
        "maxItems": 20
    });

    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    for (const match of items) {
        console.log(match.match_date.slice(0, 10), match.home_team_name, match.score_home, '-', match.score_away, match.away_team_name);
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
