import os, json, requests

WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

def send_job(job):
    text = (
        f"🚀 *New Remote Job*\n"
        f"*Title:* {job['title']}\n"
        f"*Company:* {job['company']}\n"
        f"*Location:* {job.get('location','Remote')}\n"
        f"*Link:* {job['link']}\n"
        f"*Matched:* {', '.join(job.get('matched_keywords', []))}"
    )
    resp = requests.post(WEBHOOK, data=json.dumps({"text": text}), headers={"Content-Type": "application/json"})
    resp.raise_for_status()

