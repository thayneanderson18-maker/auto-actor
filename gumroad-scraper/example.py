"""Run Gumroad Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/gumroad-scraper").call(
    run_input={
        "searchQueries": [
            "notion template"
        ],
        "maxItems": 20
    }
)

for product in client.dataset(run.default_dataset_id).iterate_items():
    print(product["name"][:60], "|", product.get("price_usd"), "USD |", product.get("rating_average"), f'({product.get("rating_count")})', "|", product.get("seller_name"))
