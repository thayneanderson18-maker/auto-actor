"""Run Greenhouse Jobs Scraper on Apify and print the results.

    pip install apify-client
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/greenhouse-jobs-scraper").call(
    run_input={
        "boards": [
            "discord"
        ],
        "maxItems": 50
    }
)

jobs = client.dataset(run["defaultDatasetId"]).iterate_items()
for job in jobs:
    print(job["title"], "|", job["organization"], "|", job["location"], "|", job.get("salary_min") or "no salary listed")
