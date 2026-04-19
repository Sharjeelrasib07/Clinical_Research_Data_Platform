import json
import os
from datetime import datetime

REPORT_PATH = "reports/data_quality_report.json"


def generate_report(stats: dict):
    os.makedirs("reports", exist_ok=True)

    stats["metadata"] = {
        "last_etl_run": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

    print(f"Data quality report saved to {REPORT_PATH}")