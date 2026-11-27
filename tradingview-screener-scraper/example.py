"""Run TradingView Screener Scraper on Apify and print the results.

    pip install "apify-client>=3"
    export APIFY_TOKEN=...   # Apify Console -> Settings -> Integrations
    python example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("daedal_quintuplet/tradingview-screener-scraper").call(
    run_input={
        "market": "america",
        "preset": "top_gainers",
        "maxResults": 20
    }
)

for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["fullSymbol"], "|", row.get("close"), row.get("currency"), "|", round(row.get("changePercent") or 0, 2), "% |", row.get("recommendationLabel"))
