"""Run Google Trends Scraper on Apify and print the results.

    pip install apify-client
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/google-trends-scraper-all-widgets").call(
    run_input={
        "keywords": [
            "bitcoin"
        ],
        "geo": "",
        "timeRange": "past_12_months"
    }
)

rows = client.dataset(run["defaultDatasetId"]).iterate_items()
for row in rows:
    print(row["kind"], "|", row["label"], "|", row["value"])
