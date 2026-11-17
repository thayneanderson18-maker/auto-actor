"""Run Craigslist Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/craigslist-scraper").call(
    run_input={
        "startUrls": [
            {
                "url": "https://newyork.craigslist.org/search/sss?query=bike"
            }
        ],
        "maxItems": 20
    }
)

for listing in client.dataset(run.default_dataset_id).iterate_items():
    print(listing["title"], "|", listing.get("price") or "no price", "|", listing.get("location"), "|", listing["url"])
