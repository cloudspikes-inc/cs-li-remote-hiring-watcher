#!/usr/bin/env python3
import argparse, json, os, sys, threading, webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, urlencode
from datetime import datetime, timedelta
import requests

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"


class CodeCatcher(BaseHTTPRequestHandler):
    expected_state = ""
    result = {"code": None, "state_ok": False, "error": None}
    done_event: threading.Event = None

    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/callback":
            self._send(404, "Not Found")
            return

        qs = parse_qs(url.query)
        if "error" in qs:
            CodeCatcher.result["error"] = qs.get("error_description", qs["error"])[0]
            self._send(400, "Error")
            CodeCatcher.done_event.set()
            return

        code = qs.get("code", [None])[0]
        state = qs.get("state", [None])[0]
        CodeCatcher.result["code"] = code
        CodeCatcher.result["state_ok"] = state == CodeCatcher.expected_state
        self._send(200, "OK")
        CodeCatcher.done_event.set()

    def log_message(self, *args, **kwargs):
        return

    def _send(self, status, body: str):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def build_auth_url(client_id, redirect_uri, state, scopes):
    return f"{AUTH_URL}?{urlencode({'response_type': 'code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'state': state, 'scope': scopes})}"


def exchange_code_for_token(client_id, client_secret, redirect_uri, code):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    r = requests.post(TOKEN_URL, data=data, timeout=30)
    body = r.json()
    if r.status_code != 200 or "access_token" not in body:
        sys.exit(f"Token exchange failed: {body}")
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-id", default=os.getenv("LI_CLIENT_ID"))
    ap.add_argument("--client-secret", default=os.getenv("LI_CLIENT_SECRET"))
    ap.add_argument("--redirect-uri", default="http://localhost:8000/callback")
    ap.add_argument("--scopes", default="openid profile")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--timeout", type=int, default=180)
    args = ap.parse_args()

    state = "state-" + os.urandom(8).hex()

    CodeCatcher.expected_state = state
    CodeCatcher.done_event = threading.Event()
    server = HTTPServer(("localhost", args.port), CodeCatcher)
    threading.Thread(target=server.handle_request, daemon=True).start()

    auth_url = build_auth_url(args.client_id, args.redirect_uri, state, args.scopes)
    webbrowser.open(auth_url)
    print(
        f"[INFO] Browser opened for LinkedIn consent. Waiting for redirect...",
        file=sys.stderr,
    )
    if not CodeCatcher.done_event.wait(timeout=args.timeout):
        sys.exit("Timeout waiting for LinkedIn redirect")

    server.server_close()
    code = CodeCatcher.result["code"]
    if not code:
        sys.exit("No authorization code captured from LinkedIn redirect.")

    token = exchange_code_for_token(
        args.client_id, args.client_secret, args.redirect_uri, code
    )
    access_token = token["access_token"]
    expires_in = token.get("expires_in", 0)

    now_local = datetime.now().astimezone()
    expiry_dt = now_local + timedelta(seconds=expires_in)
    expiry_str = expiry_dt.strftime("%Y-%m-%d %H:%M:%S %Z (%z)")

    # Pretty info goes to stderr so eval ignores it
    print(f"\n[INFO] Access token fetched successfully!", file=sys.stderr)
    print(
        f"[INFO] Valid for: {expires_in:,} seconds (~{expires_in/86400:.1f} days)",
        file=sys.stderr,
    )
    print(f"[INFO] Expires on: {expiry_str}\n", file=sys.stderr)

    # Plain export only (stdout)
    print(f"export LI_TOKEN='{access_token}'")


if __name__ == "__main__":
    main()
