"""Run Wappalyzer Alternative: Tech Stack Detector on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/wappalyzer-tech-stack-detector").call(
    run_input={
        "urls": [
            "https://stripe.com",
            "https://shopify.com",
            "https://wordpress.org"
        ]
    }
)

for site in client.dataset(run.default_dataset_id).iterate_items():
    print(site["domain"], "|", site.get("tech_count"), "|", site.get("tech_names"))
