"""Run Flipkart Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/flipkart-scraper").call(
    run_input={
        "searchQueries": [
            "iphone"
        ],
        "maxItems": 20
    }
)

for product in client.dataset(run.default_dataset_id).iterate_items():
    print(product["title"], "|", product.get("price"), product.get("currency"), "|", product.get("rating"))
