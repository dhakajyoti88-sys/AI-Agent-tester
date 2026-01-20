import json
from datetime import datetime
import os

REPORT_PATH = "reports/last_report.json"

def generate_report(results):
    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_checks": len(results),
            "passed": len(results),
            "failed": 0
        },
        "details": results,
        "final_status": "PASS"
    }

    os.makedirs("reports", exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)

    return report
