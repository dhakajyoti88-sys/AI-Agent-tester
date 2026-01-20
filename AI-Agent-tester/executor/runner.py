import asyncio
import json
from playwright.async_api import async_playwright
from datetime import datetime

async def run_test(steps):
    report = {
        "time": str(datetime.now()),
        "steps": steps,
        "status": "PASS",
        "error": None
    }

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            for step in steps:
                await eval(step)

            await browser.close()

    except Exception as e:
        report["status"] = "FAIL"
        report["error"] = str(e)

    with open("reports/report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report


def execute_playwright(steps):
    return asyncio.run(run_test(steps))


