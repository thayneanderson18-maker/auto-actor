"""Run Career Site Jobs Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/career-site-jobs-scraper").call(
    run_input={
        "companies": [
            "https://jobs.lever.co/spotify",
            "https://jobs.ashbyhq.com/notion"
        ],
        "maxItems": 50
    }
)

for job in client.dataset(run.default_dataset_id).iterate_items():
    print(job["title"], "|", job["organization"], "|", job["location"], "|", job["source"])
