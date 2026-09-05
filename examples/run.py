"""Fetch today's tennis matches with the Apify client."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfetch/flashscore-tennis-scraper").call(run_input={"mode": "matches", "days": ["0"], "categories": ["ATP", "WTA"]})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["startTime"], item["status"], item["home"]["name"], "vs", item["away"]["name"])
