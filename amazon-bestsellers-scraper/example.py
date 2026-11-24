"""Run Amazon Bestsellers Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/amazon-bestsellers-scraper").call(
    run_input={
        "startUrls": [
            {
                "url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"
            }
        ],
        "maxItemsPerList": 20
    }
)

for product in client.dataset(run.default_dataset_id).iterate_items():
    print(product["position"], product["name"][:60], "|", product.get("priceText") or "no price", "|", product.get("stars"))
