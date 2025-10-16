# URGENT: GitHub Environment Setup Required

## ⚠️ IMPORTANT: Manual Approval Not Working Without This Setup

The Terraform pipeline requires **GitHub Environment Protection Rules** to enforce manual approval by CODEOWNERS. Without this setup, the terraform-apply job will execute automatically without approval.

## Quick Setup Steps

### 1. Create GitHub Environment

1. Go to **Repository Settings** → **Environments**
2. Click **"New environment"**
3. Name: `test`
4. Click **"Configure environment"**

### 2. Configure Environment Protection Rules

**Required Reviewers:**

- ✅ Enable **"Required reviewers"**
- Add reviewers: `cloudspikes-inc` (or individual CODEOWNER usernames)
- Set minimum approvals: `1`

**Deployment Branches (Optional but Recommended):**

- ✅ Enable **"Deployment branches"**
- Add rule: `main`
- Add rule: `develop`
- Add rule: `feature/*`

### 3. How It Works

**Before Setup (Current Issue):**

```text
terraform-plan → terraform-apply (runs automatically) ❌
```

**After Setup (Correct Behavior):**

```text
terraform-plan → terraform-apply (⏸️ waits for approval) → ✅ manual approval → continues
```

### 4. Approval Process

When terraform-apply job runs:

1. **Pipeline Pauses** at environment protection checkpoint
2. **"Waiting for approval"** status appears
3. **Reviewer** gets notification
4. **Actions Tab** shows **"Review deployments"** button
5. **Approve** specific environment to continue
6. **Pipeline Continues** with terraform apply

### 5. Verification

After setup, test the pipeline:

1. Make a change to `infra/**` files
2. Create/update a PR
3. terraform-plan should run automatically
4. terraform-apply should **pause** and show "Waiting for approval"
5. You should see **"Review deployments"** button in Actions UI

### 6. Current Status

⚠️ **Status:** Environment protection NOT configured
🔧 **Action:** Complete steps 1-2 above IMMEDIATELY
✅ **Expected:** terraform-apply will pause for manual approval

### 7. CODEOWNERS Integration

The environment reviewers should match your CODEOWNERS file:

- If CODEOWNERS has `@cloudspikes-inc`, add `cloudspikes-inc` as reviewer
- If CODEOWNERS has individual users, add those specific users

### 8. Troubleshooting

**Q: Pipeline still runs automatically?**
A: Environment not configured correctly. Double-check:

- Environment name exactly matches: `test`
- Required reviewers enabled and configured
- Reviewers have proper permissions

**Q: Can't find "Review deployments" button?**
A: Check the workflow run page, it appears when environment protection is active

**Q: Approval not working?**
A: Ensure the reviewer has write access to the repository

---

## 🚨 Action Required

**This setup must be completed BEFORE the next pipeline run to ensure proper approval enforcement.**
