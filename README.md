# 📌 CloudSpikes – LinkedIn Remote Job Scanner

Automated pipeline that ingests LinkedIn recruiter/job posts, filters for **remote Cloud/DevOps/SRE-related roles**, deduplicates results, and sends **real-time + daily digest alerts** into Slack.

This repo: `cs-li-remote-hiring-watcher` -– LinkedIn Remote Job Scanner – CloudSpikes Automated pipeline that ingests LinkedIn recruiter/job posts, filters for remote Cloud/DevOps/SRE roles, deduplicates results, and delivers real-time + daily digest alerts into Slack.

---

## 🎯 Project Scope (Phase 0 – MVP)

* Fetch jobs/recruiter posts from LinkedIn.
* Store raw + filtered jobs in Postgres.
* Apply keyword-based filters (roles, remote indicators, exclusions).
* Deduplicate results to avoid spam.
* Send Slack alerts:

  * ⚡ Real-time job notifications
  * 📩 Daily digest (last 24h)
  * 📊 Health check summary (jobs fetched/filtered/alerted)

👉 Current release is **Slack-only, LinkedIn-only**. Future phases will expand to other platforms and dashboards.

---

## 🚀 LinkedIn Scanner Task Board

All the task-related details about everyone are documented in the Google sheet's link given below:

<https://docs.google.com/spreadsheets/d/1xkrC7jQNHkrERcOLLz6NBv8dCcfZvddP8IJqKJ3CuS4/edit?usp=sharing>

## 🗂️ Repository Structure

cloudspikes-linkedin-remote-scanner/
├─ src/                # Source code
│  ├─ connectors/      # LinkedIn API connector
│  ├─ filters/         # Keyword filter logic
│  ├─ alerts/          # Slack alerts + daily digest
│  ├─ scheduler/       # APScheduler jobs
│  ├─ db/              # DB schema + helper scripts
│  ├─ health/          # Health check scripts
│  └─ **init**.py
├─ config/             # Config files (keywords, app settings)
├─ tests/              # Unit tests
├─ .github/            # CI/CD workflows + issue/PR templates
├─ docker/             # Dockerfile + docker-compose
├─ scripts/            # Helper scripts for DB + local runs
├─ .env.example        # Sample env vars
├─ .gitignore
├─ .pre-commit-config.yaml
├─ Makefile
├─ pyproject.toml / requirements.txt
├─ CONTRIBUTING.md
├─ CODEOWNERS
├─ SECURITY.md
├─ LICENSE
└─ README.md

```
cloudspikes-linkedin-remote-scanner/
├─ src/                # Source code
│  ├─ connectors/      # LinkedIn API connector
│  ├─ filters/         # Keyword filter logic
│  ├─ alerts/          # Slack alerts + daily digest
│  ├─ scheduler/       # APScheduler jobs
│  ├─ db/              # DB schema + helper scripts
│  ├─ health/          # Health check scripts
│  └─ __init__.py
├─ config/             # Config files (keywords, app settings)
├─ tests/              # Unit tests
├─ .github/            # CI/CD workflows + issue/PR templates
├─ docker/             # Dockerfile + docker-compose
├─ scripts/            # Helper scripts for DB + local runs
├─ .env.example        # Sample env vars
├─ .gitignore
├─ .pre-commit-config.yaml
├─ Makefile
├─ pyproject.toml / requirements.txt
├─ CONTRIBUTING.md
├─ CODEOWNERS
├─ SECURITY.md
├─ LICENSE
└─ README.md
```

---

## ⚡ Quickstart

```bash
# 1. Clone repo
git clone https://github.com/cloudspikes/cloudspikes-linkedin-remote-scanner.git
cd cloudspikes-linkedin-remote-scanner

# 2. Setup environment
cp .env.example .env
# Fill in LinkedIn + Slack secrets

# 3. Start Postgres
docker-compose -f docker/docker-compose.yml up -d db

# 4. Bootstrap database schema
bash scripts/bootstrap_db.sh

# 5. Run fetcher manually (test)
python src/connectors/linkedin_fetcher.py

# 6. Run scheduler for auto fetch
python src/scheduler/aps_scheduler.py
```

---

## 🔑 Environment Variables

Defined in `.env.example`:

* `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `LINKEDIN_ACCESS_TOKEN`
* `SLACK_WEBHOOK_URL`
* `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
* `FETCH_INTERVAL_MINUTES`

---

## 🧪 Running Tests

```bash
# Run unit tests
pytest

# Run pre-commit checks
pre-commit run --all-files
```

CI is enforced with GitHub Actions (`.github/workflows/ci.yml`).

---

## 🤝 Contributing

* See [CONTRIBUTING.md](CONTRIBUTING.md) for workflow & branch rules.
* Code ownership defined in [CODEOWNERS](CODEOWNERS).
* Security issues: report via [SECURITY.md](SECURITY.md).

---

## 📌 License

This project is licensed under the **Apache License 2.0** – see [LICENSE](LICENSE) file.

---
