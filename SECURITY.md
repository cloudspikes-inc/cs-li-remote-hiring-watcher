# Security Policy

## Supported Versions

This project is currently in **Phase 0 (MVP)**.  
We only support the latest `main` branch.

## Reporting a Vulnerability

If you discover a security issue, **DO NOT** open a GitHub issue.  
Instead, please:

- Email: <security@cloudspikes.com> (internal team list).  
- Or message the repo maintainers directly on Slack.  

We will:

1. Acknowledge receipt of your report within 48 hours.  
2. Provide updates as we investigate.  
3. Release a patch as soon as practical.  

---

## Guidelines

- Never commit secrets (`.env`, API keys, Slack webhooks).  
- Always use `.env.example` for placeholders.  
- Use pre-commit hooks to avoid accidental leaks.
