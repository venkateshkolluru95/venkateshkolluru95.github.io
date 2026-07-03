"""Fetch Google Scholar author metrics and write them to results/ as JSON.

Run by .github/workflows/google_scholar_crawler.yml on a daily schedule.
The JSON is force-pushed to the `google-scholar-stats` branch, and the site
reads it live. If Google blocks the scrape on a given day, the workflow just
fails and the last good numbers on the branch are kept.
"""
from scholarly import scholarly
import json
import os
from datetime import datetime, timezone

SID = os.environ.get("GOOGLE_SCHOLAR_ID", "7Tji1bMAAAAJ")

author = scholarly.search_author_id(SID)
scholarly.fill(author, sections=["basics", "indices", "counts"])

out = {
    "name": author.get("name"),
    "citations": author.get("citedby"),
    "hindex": author.get("hindex"),
    "i10": author.get("i10index"),
    "cites_per_year": author.get("cites_per_year", {}),
    "user": SID,
    "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
}
print(out)

os.makedirs("results", exist_ok=True)
with open("results/gs_data.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# shields.io endpoint (optional badge use)
with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump(
        {"schemaVersion": 1, "label": "citations", "message": str(out["citations"]), "color": "brightgreen"},
        f,
    )
