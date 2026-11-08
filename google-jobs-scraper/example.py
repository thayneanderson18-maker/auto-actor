"""Run Google Jobs Scraper (US & UK) on Apify and print the results.

    pip install apify-client
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/google-jobs-scraper").call(
    run_input={
        "queries": [
            "data analyst new york"
        ],
        "country": "us",
        "maxItems": 10
    }
)

jobs = client.dataset(run["defaultDatasetId"]).iterate_items()
for job in jobs:
    print(job["title"], "|", job["company"], "|", job["location"], "|", job.get("salary") or "no salary listed")
