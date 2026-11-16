"""Run Flashscore Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/flashscore-scraper").call(
    run_input={
        "startUrls": [
            {
                "url": "https://www.flashscore.com/football/england/premier-league/results/"
            }
        ],
        "matchType": "results",
        "maxItems": 20
    }
)

for match in client.dataset(run.default_dataset_id).iterate_items():
    print(match["match_date"][:10], match["home_team_name"], match["score_home"], "-", match["score_away"], match["away_team_name"])
