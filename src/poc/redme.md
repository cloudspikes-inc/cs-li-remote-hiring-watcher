# LinkedIn `/v2/userinfo` — End-to-End POC (Python)

This guide shows the exact process used to test **LinkedIn’s official OpenID Connect `/v2/userinfo` endpoint** using Python.
You can follow the same pattern to call other LinkedIn APIs later.

---

## 1️⃣ What You’ll Build

* A **token-setter script** (`linkedin_token_setter.py`) that:

  * Launches the LinkedIn consent screen
  * Captures the redirect
  * Exchanges the authorization code
  * Sets `LI_TOKEN` in your shell

* A **caller script** (`use_li_token.py`) that:

  * Reads the token
  * Calls [`https://api.linkedin.com/v2/userinfo`](https://api.linkedin.com/v2/userinfo)

> ✅ Works on macOS/Linux shells (Zsh/Bash).
> 🪟 PowerShell users: adapt the `eval` and `export` parts.

---

## 2️⃣ Prerequisites

* A [LinkedIn Developer App](https://www.linkedin.com/developers/apps) with **Sign in with LinkedIn using OpenID Connect** added.
* In the app → **Auth → Redirect URLs**, add:

  ```
  http://localhost:8000/callback
  ```
* Your app’s **Client ID** and **Client Secret**
* Python 3.9+ and `pip`

---

## 3️⃣ Project Files

Create a folder (e.g. `linkedin-app/`) and add:

* `linkedin_token_setter.py` → Fetches a token, prints an `export LI_TOKEN='...'` line
* `use_li_token.py` → Uses that token to call `/v2/userinfo`

---

## 4️⃣ Install Dependencies

```bash
python3 -m pip install requests
```

---

## 5️⃣ Get and Set the Access Token (One-Time per ~60 Days)

Run the token setter — it opens the consent page, captures the redirect, exchanges the code, sets `LI_TOKEN` in your shell, and prints the exact expiry time.

```bash
eval "$(python3 linkedin_token_setter.py \
  --client-id '<YOUR_CLIENT_ID>' \
  --client-secret '<YOUR_CLIENT_SECRET>' \
  --redirect-uri 'http://localhost:8000/callback' \
  --scopes 'openid profile')"
```

**Example Output:**

```
[INFO] Browser opened for LinkedIn consent. Waiting for redirect...
[INFO] Access token fetched successfully!
[INFO] Valid for: 5,183,999 seconds (~60.0 days)
[INFO] Expires on: 2025-12-03 13:57:20 EDT (-0400)
```

> 🕓 The **“Expires on”** line is the exact local date/time the token expires.
> Copy this into your notes or calendar to know when to refresh.

**Verify the token is set:**

```bash
echo "$LI_TOKEN"
```

(You should see a long string — **don’t share it**.)

### Notes

* `openid profile` → sufficient for `/v2/userinfo`
* Add `email` if you also need email data
* Authorization code = short-lived, one-time use
* Access token = valid until printed **expiry timestamp (~60 days)**
* When expired → rerun this command to refresh

---

## 6️⃣ Call the Official API

```bash
LI_TOKEN="$LI_TOKEN" python3 use_li_token.py
```

**Expected Output:**

```json
{
  "name": "Your Name",
  "sub": "BtXn4sJ7GQ",
  "locale": {"country": "US", "language": "en"},
  "given_name": "Your",
  "family_name": "Name",
  "picture": "https://media.licdn.com/..."
}
```

---

## 7️⃣ Extend for Other LinkedIn APIs

1. Pick your endpoint + scopes
   Example: Email → add `email`
   Org posts → need **Community Management** and `r_organization_social`

2. Re-run token setter with those scopes:

   ```bash
   eval "$(python3 linkedin_token_setter.py \
     --client-id '<YOUR_CLIENT_ID>' \
     --client-secret '<YOUR_CLIENT_SECRET>' \
     --redirect-uri 'http://localhost:8000/callback' \
     --scopes 'openid profile email')"
   ```

3. Call the new endpoint using the same token.
   For classic REST APIs, include:

   ```python
   headers = {
     "Authorization": f"Bearer {LI_TOKEN}",
     "X-Restli-Protocol-Version": "2.0.0",
     "LinkedIn-Version": "202509"  # YYYYMM format
   }
   ```

---

## 8️⃣ Token Renewal

* `LI_TOKEN` lasts ≈ 60 days
* When expired (`401 Unauthorized`), rerun the setter command to mint a new one
* No code changes needed

---

## 9️⃣ Troubleshooting Quick Refs

| Problem                             | Fix                                                       |
| ----------------------------------- | --------------------------------------------------------- |
| ❌ Redirect URI not allowed          | Add `http://localhost:8000/callback` in your app settings |
| ❌ `invalid_client`                  | Client ID/secret or redirect mismatch                     |
| ❌ `openid_insufficient_scope_error` | Include both `openid profile` (and `email` if needed)     |
| ⚠️ Token empty in Python            | Use `eval "$( ... )"` to set the env var                  |

---

## 🔒 10) Security & Hygiene

* Never commit your **client secret** or token
* Use secret vaults or environment variables
* Treat `LI_TOKEN` like a password — it grants API access until expiry

---

## ⚡ Quick Reference — Example Command

```bash
eval "$(python3 linkedin_token_setter.py \
  --client-id '78seural244bqk' \
  --client-secret '<YOUR_CLIENT_SECRET>' \
  --redirect-uri 'http://localhost:8000/callback' \
  --scopes 'openid profile')"

echo "$LI_TOKEN"              # sanity check
LI_TOKEN="$LI_TOKEN" python3 use_li_token.py
```

---
