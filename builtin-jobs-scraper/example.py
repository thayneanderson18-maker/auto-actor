"""Run Built In Jobs Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/builtin-jobs-scraper").call(
    run_input={
        "searchQueries": [
            "data engineer"
        ],
        "maxTotalResults": 20
    }
)

for job in client.dataset(run.default_dataset_id).iterate_items():
    print(job["title"][:60], "|", job["company"], "|", job.get("workplaceType"), "|", job.get("salaryText") or "no salary listed")
