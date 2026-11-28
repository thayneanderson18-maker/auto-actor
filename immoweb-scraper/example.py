"""Run Immoweb Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/immoweb-scraper").call(
    run_input={
        "startUrls": [
            "https://www.immoweb.be/en/search/apartment/for-rent?countries=BE&postalCodes=1050&orderBy=newest"
        ],
        "maxResults": 20
    }
)

for listing in client.dataset(run.default_dataset_id).iterate_items():
    print((listing.get("title") or listing.get("propertyType") or "")[:60], "|", listing.get("priceDisplay"), "|", listing.get("bedrooms"), "bed |", listing.get("locality"))
