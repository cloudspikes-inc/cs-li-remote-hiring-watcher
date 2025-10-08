"""Slack alerting for new jobs."""

import json
import os
from typing import Dict, Any

import requests

WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")


def send_job(job: Dict[str, Any]) -> None:
    """Sends a job alert to Slack via webhook."""
    if not WEBHOOK:
        raise ValueError("SLACK_WEBHOOK_URL environment variable is not set")

    matched_keywords = (
        job.get("devops", []) + job.get("aws", []) + job.get("kubernetes", [])
    )

    matched_text = ", ".join(matched_keywords) if matched_keywords else "None"
    text = (
        f"🚀 *New Remote Job*\n"
        f"*Title:* {job.get('title', 'N/A')}\n"
        f"*Company:* {job.get('company', 'N/A')}\n"
        f"*Location:* {job.get('location', 'Remote')}\n"
        f"*Link:* {job.get('link', 'N/A')}\n"
        f"*Matched:* {matched_text}"
    )

    resp = requests.post(
        WEBHOOK,
        data=json.dumps({"text": text}),
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    resp.raise_for_status()
