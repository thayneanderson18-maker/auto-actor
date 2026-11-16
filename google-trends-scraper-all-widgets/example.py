"""Run Google Trends Scraper on Apify and print the results.

    pip install "apify-client>=3"
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

for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["kind"], "|", row["label"], "|", row["value"])
