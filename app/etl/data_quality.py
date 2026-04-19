import json
import os

REPORT_PATH = "reports/data_quality_report.json"


def generate_report(stats: dict):
    os.makedirs("reports", exist_ok=True)

    with open(REPORT_PATH, "w") as f:
        json.dump(stats, f, indent=4)

    print(f"Data quality report saved to {REPORT_PATH}")