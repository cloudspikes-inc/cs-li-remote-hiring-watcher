#!/usr/bin/env python3
import os
import json
import sys
import requests

try:
    from dotenv import load_dotenv

    load_dotenv()  # loads .env if present
except Exception:
    pass

LI_TOKEN = os.getenv("LI_TOKEN")
if not LI_TOKEN:
    print(
        "LI_TOKEN not set. Export it or create a .env with LI_TOKEN=...",
        file=sys.stderr,
    )
    sys.exit(1)

USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
r = requests.get(
    USERINFO_URL, headers={"Authorization": f"Bearer {LI_TOKEN}"}, timeout=30
)

if r.status_code == 401:
    print(
        "Token expired/invalid (401). Re-run the cURL "
        "token steps to get a new LI_TOKEN.",
        file=sys.stderr,
    )
    sys.exit(2)

try:
    body = r.json()
except Exception:
    print("Non-JSON response:", r.text[:400], file=sys.stderr)
    sys.exit(3)

print(json.dumps(body, indent=2))
