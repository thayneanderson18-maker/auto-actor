"""Run Google Images Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/google-images-scraper").call(
    run_input={
        "queries": [
            "red sneakers"
        ],
        "maxResultsPerQuery": 100,
        "country": "us"
    }
)

for image in client.dataset(run.default_dataset_id).iterate_items():
    print(image["position"], image["title"], image["imageUrl"], f'{image["imageWidth"]}x{image["imageHeight"]}')
