# Secure Setup Instructions

## Setting up Terraform Variables

1. Copy the example file:
   ```bash
   cp infra/envs/test/terraform.tfvars.example infra/envs/test/terraform.tfvars
   ```

2. Edit the terraform.tfvars file and replace the placeholder values:
   ```terraform
   slack_webhook_url_test = "your-actual-webhook-url-here"
   ```

3. Never commit the actual terraform.tfvars file - it's already in .gitignore

## Environment Variables Alternative

Instead of using terraform.tfvars, you can also set environment variables:

```bash
export TF_VAR_slack_webhook_url_test="your-webhook-url"
export TF_VAR_region="ap-south-1"
# ... other variables
```

## Security Best Practices

- Always use AWS Secrets Manager in production
- Never commit webhook URLs to git
- Use environment variables for CI/CD
- Rotate webhook URLs regularly
