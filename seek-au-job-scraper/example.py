"""Run Seek AU Job Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/seek-au-job-scraper").call(
    run_input={
        "keywords": "carpenter",
        "where": "Brisbane",
        "maxItems": 50
    }
)

for job in client.dataset(run.default_dataset_id).iterate_items():
    print(job["title"], "|", job["company"], "|", job.get("salary") or "no salary listed", "|", job["url"])
