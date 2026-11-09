"""Run Google Images Scraper on Apify and print the results.

    pip install apify-client
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

images = client.dataset(run["defaultDatasetId"]).iterate_items()
for image in images:
    print(image["position"], image["title"], image["imageUrl"], f'{image["imageWidth"]}x{image["imageHeight"]}')
