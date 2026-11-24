"""Run AutoScout24 Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/autoscout24-scraper").call(
    run_input={
        "startUrls": [
            {
                "url": "https://www.autoscout24.com/lst/bmw/x5?atype=C&sort=age&desc=1"
            }
        ],
        "maxItems": 20
    }
)

for car in client.dataset(run.default_dataset_id).iterate_items():
    print(car["title"], "|", car.get("rawPrice"), car.get("currency"), "|", car.get("mileageKm"), "km |", car.get("city"))
