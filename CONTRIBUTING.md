# Contributing to CloudSpikes – LinkedIn Remote Job Scanner

We ❤️ contributions from our team and community!
This document explains how to contribute code, tests, or documentation.

---

## 📌 How to Contribute

1. **Fork & Clone**
   - Fork the repo under your GitHub account.
   - Clone your fork locally.

2. **Branching Model**
   - Use `main` branch for stable code only.
   - Create feature branches with naming convention:
     - `feature/<short-description>`
     - `fix/<short-description>`
     - `chore/<short-description>`

   Example: `feature/linkedin-api-connector`

3. **Commit Messages**
   - Follow [Conventional Commits](https://www.conventionalcommits.org/).
   - Examples:
     - `feat: add LinkedIn API connector`
     - `fix: handle Slack webhook error gracefully`
     - `chore: update pre-commit config`

4. **Coding Standards**
   - Python 3.11+
   - Use **Black** for formatting and **Flake8** for linting.
   - Pre-commit hooks are required (`pre-commit install`).

5. **Tests**
   - Write unit tests for new code in `tests/`.
   - Run `pytest` before submitting.

6. **Pull Requests**
   - Ensure CI checks pass.
   - Provide a clear description of what and why.
   - Link related issue numbers (`Closes #123`).

---

## 📋 Review & Merge

- At least **1 reviewer approval** is required before merging.
- CI must pass (lint + tests).
- PRs must be rebased on latest `main`.

---

## 🐛 Reporting Bugs

- Use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md).
- Include steps to reproduce, expected vs actual behavior, logs/screenshots if possible.

---

## 🌟 Feature Requests

- Use the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).
- Describe the problem, your proposal, and any alternatives.

---

## 📜 Code of Conduct

- Be respectful in all discussions.
- Support collaborative feedback.
- Ask questions freely!

---

Thank you for contributing to CloudSpikes 🚀
