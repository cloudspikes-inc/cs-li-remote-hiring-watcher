# Create the secret
resource "aws_secretsmanager_secret" "aws_sm_slack_webhook_url" {
  name        = var.secret_name
  description = var.description

  tags = {
    Project     = var.project_tag
    Purpose     = var.purpose_tag
    Environment = var.environment
  }
}

# Store the secret value
resource "aws_secretsmanager_secret_version" "aws_sm_sv_slack_webhook_url" {
  secret_id = aws_secretsmanager_secret.aws_sm_slack_webhook_url.id
  secret_string = jsonencode({
    slack_webhook_url = var.slack_webhook_url
  })
}
