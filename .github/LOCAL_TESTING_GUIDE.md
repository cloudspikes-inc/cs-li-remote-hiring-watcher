# 🧪 Local Testing Guide for GitHub Actions Workflows

This guide provides multiple methods to test the GitHub Actions workflows locally before pushing to GitHub.

## 📋 Prerequisites

### Install Required Tools

```bash
# Install act (GitHub Actions runner)
brew install act

# Install jq (JSON processor)
brew install jq

# Install Terraform (if not already installed)
brew install terraform

# Install AWS CLI (if not already installed)
brew install awscli

# Optional: Security scanning tools
brew install tfsec
pip install checkov

# Optional: Cost estimation
brew install infracost
```

## 🔧 Setup Local Environment

### 1. Configure Local Secrets

Edit the `.secrets` file (already created):

```bash
# Add your real AWS credentials and webhook URLs
nano .secrets
```

### 2. Configure AWS Credentials (if testing AWS components)

```bash
aws configure
# Or set environment variables:
export AWS_ACCESS_KEY_ID_TEST="your-key"
export AWS_SECRET_ACCESS_KEY_TEST="your-secret"
export AWS_DEFAULT_REGION="ap-south-1"
```

## 🧪 Testing Methods

### Method 1: Component Testing (Recommended for Initial Testing)

#### Test IAM Policy Validation

```bash
cd /Users/dhruvrana/Downloads/CSI/cs-li-remote-hiring-watcher
./test-iam-validation.sh
```

#### Test Terraform Pipeline

```bash
cd /Users/dhruvrana/Downloads/CSI/cs-li-remote-hiring-watcher
./test-terraform-pipeline.sh
```

### Method 2: Using `act` (GitHub Actions Local Runner)

#### Test IAM Policy Validation Workflow

```bash
cd /Users/dhruvrana/Downloads/CSI/cs-li-remote-hiring-watcher

# Test on pull_request event with changed IAM files
act pull_request \
  --workflows .github/workflows/iam-policy-validation.yml \
  --secret-file .secrets \
  --verbose
```

#### Test Terraform Pipeline Workflow

```bash
# Test terraform validation job only (safer)
act pull_request \
  --workflows .github/workflows/terraform-pipeline.yml \
  --job terraform-validate \
  --secret-file .secrets \
  --verbose
```

#### Test with specific event data

```bash
# Create event payload
cat > event.json << 'EOF'
{
  "pull_request": {
    "number": 1,
    "head": {
      "ref": "feature/test-branch"
    },
    "base": {
      "ref": "main"
    }
  }
}
EOF

# Run with event data
act pull_request \
  --eventpath event.json \
  --workflows .github/workflows/iam-policy-validation.yml \
  --secret-file .secrets
```

### Method 3: Docker Testing (Most Accurate)

#### Run in GitHub Actions Ubuntu environment

```bash
# Pull the GitHub Actions runner image
docker pull catthehacker/ubuntu:act-latest

# Run act with specific runner image
act pull_request \
  --workflows .github/workflows/iam-policy-validation.yml \
  --secret-file .secrets \
  --platform ubuntu-latest=catthehacker/ubuntu:act-latest
```

## 🎯 Focused Testing Scenarios

### Test Scenario 1: IAM Policy Change

```bash
# Create a test IAM policy change
echo '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "*"
    }
  ]
}' > iam-policies/test-policy-new.json

# Test the workflow
act pull_request --workflows .github/workflows/iam-policy-validation.yml --secret-file .secrets
```

### Test Scenario 2: Terraform Change

```bash
# Make a small change to terraform files
echo "# Test change $(date)" >> infra/envs/test/terraform.tfvars

# Test the workflow (validation job only)
act pull_request --workflows .github/workflows/terraform-pipeline.yml --job terraform-validate --secret-file .secrets
```

### Test Scenario 3: Security Scan

```bash
# Test security scanning locally
cd infra/

# Run Checkov
checkov -d . --framework terraform

# Run TFSec
tfsec .
```

## 🔍 Debugging Workflows

### Enable Debug Mode

```bash
# Add to .secrets file:
echo "ACTIONS_STEP_DEBUG=true" >> .secrets
echo "ACTIONS_RUNNER_DEBUG=true" >> .secrets
```

### Test Individual Steps

```bash
# Test just the validation steps
act pull_request \
  --workflows .github/workflows/iam-policy-validation.yml \
  --secret-file .secrets \
  --job validate-iam-policies \
  --verbose \
  --dryrun
```

## 📝 Manual Validation Commands

### IAM Policy Validation

```bash
# Check JSON syntax
for file in iam-policies/*.json; do
  echo "Checking $file"
  jq empty "$file" && echo "✅ Valid JSON" || echo "❌ Invalid JSON"
done

# Validate with AWS CLI (requires AWS credentials)
aws iam create-policy --policy-name temp-test --policy-document file://iam-policies/test-policy.json --dry-run
```

### Terraform Validation

```bash
cd infra/envs/test/

# Format check
terraform fmt -check -recursive

# Initialize (be careful with this)
terraform init

# Validate
terraform validate

# Plan (be careful - this might create resources)
terraform plan
```

## 🚨 Safety Notes

### ⚠️ **IMPORTANT WARNINGS:**

1. **Never run `terraform apply` locally** - it will create real AWS resources
2. **Use dummy/test AWS credentials** when possible
3. **The `.secrets` file contains sensitive data** - never commit it
4. **act runs in Docker** - some commands might behave differently than in real GitHub Actions

### Safe Testing Practices

- Use separate AWS account for testing
- Use read-only IAM permissions when possible
- Test validation and planning only, avoid apply operations
- Review all commands before running

## 📊 Expected Output Examples

### Successful IAM Validation

```
🔍 Testing IAM Policy Validation Components...
✅ test-policy.json has valid JSON syntax
✅ test-policy.json has valid IAM policy structure
🎉 IAM Policy validation test completed!
```

### Successful Terraform Validation

```
🏗️ Testing Terraform Pipeline Components...
✅ Terraform is installed: Terraform v1.6.0
✅ All terraform files formatted correctly
✅ Terraform validation passed
🎉 Terraform pipeline test completed!
```

## 🚀 Ready for GitHub Testing

After local testing passes:

1. **Commit your changes** (excluding `.secrets`)
2. **Push to feature/issue#6 branch**
3. **Create a Pull Request**
4. **Watch the workflows run on GitHub**

## 🔧 Troubleshooting

### Common Issues

#### act fails to run

```bash
# Check Docker is running
docker ps

# Use different runner image
act --platform ubuntu-latest=catthehacker/ubuntu:act-20.04
```

#### Terraform init fails

```bash
# Make sure AWS credentials are configured
aws sts get-caller-identity

# Check backend configuration
cat infra/envs/test/backend.tf
```

#### Permission issues

```bash
# Make scripts executable
chmod +x *.sh

# Check file permissions
ls -la iam-policies/
```

This testing approach ensures your workflows will work correctly when deployed to GitHub Actions!
