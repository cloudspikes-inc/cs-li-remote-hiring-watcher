# GitHub Actions Workflows Setup Guide

This document outlines the setup required for the two new GitHub Actions workflows created for the cs-li-remote-hiring-watcher repository.

## 🔒 Workflow 1: IAM Policy Validation (`iam-policy-validation.yml`)

### Purpose
Validates IAM policy JSON files in the `iam-policies/` directory whenever changes are made via Pull Requests.

### Triggers
- Pull requests targeting `main`, `develop`, or `feature/**` branches
- Only when files under `iam-policies/` are modified

### Validation Steps
1. **JSON Syntax Validation** - Ensures valid JSON format
2. **IAM Structure Validation** - Checks for required fields (Version, Statement, Effect, Action)
3. **AWS Policy Validation** - Uses AWS CLI to validate policy format
4. **PR Comments** - Posts validation results and review checklist

### Required GitHub Secrets
```
AWS_ACCESS_KEY_ID_TEST      # AWS access key for policy validation
AWS_SECRET_ACCESS_KEY_TEST  # AWS secret key for policy validation
```

### Team Members Tagged for Review
- @cloudspikes-inc (owner approval required)
- @dipesh, @dinesh, @amar, @sumit (team review)

---

## 🏗️ Workflow 2: Terraform Infrastructure Pipeline (`terraform-pipeline.yml`)

### Purpose
Runs Terraform validation, planning, and apply stages for infrastructure changes in the `infra/` directory.

### Triggers
- Pull requests targeting `main`, `develop`, or `feature/**` branches
- Only when files under `infra/` are modified

### Pipeline Stages

#### 1. Terraform Validate (Matrix: dev, test, prod)
- Format check (`terraform fmt -check`)
- Initialization (`terraform init`)
- Validation (`terraform validate`)
- Planning (`terraform plan`)
- Uploads plan artifacts

#### 2. Terraform Apply (Currently: test environment only)
- Downloads plan artifacts
- Applies changes (`terraform apply`)
- **Requires manual approval** (see setup below)

#### 3. Security Scan
- Runs Checkov for security compliance
- Runs TFSec for Terraform security analysis
- Uploads results to GitHub Security tab

#### 4. Cost Estimation
- Uses Infracost to estimate AWS costs
- Comments on PR with cost breakdown

### Required GitHub Secrets
```
# AWS Credentials
AWS_ACCESS_KEY_ID_TEST              # AWS access key for Terraform operations
AWS_SECRET_ACCESS_KEY_TEST          # AWS secret key for Terraform operations

# Slack Webhook URLs (for each environment)
SLACK_WEBHOOK_URL_TEST         # Test environment Slack webhook
SLACK_WEBHOOK_URL_DEV          # Dev environment Slack webhook  
SLACK_WEBHOOK_URL_PROD         # Prod environment Slack webhook

# Optional: Cost Estimation
INFRACOST_API_KEY             # Infracost API key for cost estimation
```

---

## 📋 Required Setup Actions

### 1. GitHub Secrets Configuration
Go to **Settings → Secrets and variables → Actions** and add:

```bash
# AWS Credentials (IAM user with appropriate permissions)
AWS_ACCESS_KEY_ID_TEST=AKIA...
AWS_SECRET_ACCESS_KEY_TEST=...

# Slack Webhook URLs
SLACK_WEBHOOK_URL_TEST=https://hooks.slack.com/services/...
SLACK_WEBHOOK_URL_DEV=https://hooks.slack.com/services/...
SLACK_WEBHOOK_URL_PROD=https://hooks.slack.com/services/...

# Optional: Infracost API Key
INFRACOST_API_KEY=ico-...
```

### 2. GitHub Environment Protection (Manual Approval)
To require approval from @cloudspikes-inc before Terraform apply:

1. Go to **Settings → Environments**
2. Create environment named: `terraform-apply-approval`
3. Configure protection rules:
   - ✅ **Required reviewers**: Add `cloudspikes-inc`
   - ✅ **Wait timer**: 0 minutes (optional)
   - ✅ **Deployment branches**: Selected branches (feature/issue#6, main, develop)

Then update the workflow file:
```yaml
terraform-apply:
  environment: terraform-apply-approval  # Add this line back
```

### 3. AWS IAM Permissions
The AWS credentials need the following permissions:

#### For IAM Policy Validation:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreatePolicy",
        "iam:DeletePolicy",
        "iam:GetPolicy",
        "sts:GetCallerIdentity"
      ],
      "Resource": "*"
    }
  ]
}
```

#### For Terraform Operations:
- All permissions required by your Terraform configurations
- Secrets Manager access for webhook URLs
- Any AWS services being provisioned

### 4. Branch Protection Rules
Consider adding branch protection rules:

1. Go to **Settings → Branches**
2. Add rule for `main` branch:
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date
   - Select: `terraform-validate`, `validate-iam-policies`
   - ✅ Require review from code owners

### 5. CODEOWNERS File
Update the `.github/CODEOWNERS` file:
```
# Infrastructure changes require approval
/infra/ @cloudspikes-inc
/iam-policies/ @cloudspikes-inc

# Team members for reviews
*.tf @dipesh @dinesh @amar @sumit
*.json @dipesh @dinesh @amar @sumit
```

---

## 🚀 Testing the Workflows

### Test IAM Policy Validation:
1. Create a branch: `feature/test-iam-validation`
2. Modify any file in `iam-policies/`
3. Create a Pull Request
4. Watch the `IAM Policy Validation` workflow run

### Test Terraform Pipeline:
1. Create a branch: `feature/test-terraform-pipeline`
2. Modify any file in `infra/`
3. Create a Pull Request
4. Watch the `Terraform Infrastructure Pipeline` workflow run

---

## 🔧 Current Limitations & Next Steps

### Current State:
- ✅ Both workflows created and ready to test
- ✅ Terraform apply limited to `test` environment only
- ⚠️ Manual approval mechanism needs GitHub Environment setup
- ⚠️ Cost estimation requires Infracost API key

### Recommended Next Steps:
1. **Set up all required GitHub secrets**
2. **Configure GitHub Environment protection**
3. **Test workflows on feature/issue#6 branch**
4. **Add prod/dev environments to apply stage after testing**
5. **Set up Infracost for cost estimation (optional)**

### Future Enhancements:
- Terraform state locking mechanisms
- Rollback procedures
- Integration with monitoring/alerting
- Multi-region support
- Custom validation rules for IAM policies

---

## 📞 Support

For questions or issues with these workflows:
- **Owner**: @cloudspikes-inc
- **Team**: @dipesh @dinesh @amar @sumit
- **Branch**: feature/issue#6 (for testing)

## 📝 Files Created:
- `.github/workflows/iam-policy-validation.yml`
- `.github/workflows/terraform-pipeline.yml`
- `WORKFLOWS_SETUP.md` (this file)