terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Create the secret
resource "aws_secretsmanager_secret" "example" {
  name        = var.secret_name
  description = var.description

  tags = {
    Project     = var.project_tag
    Purpose     = var.purpose_tag
    Environment = var.environment
  }
}

# Store the secret value
resource "aws_secretsmanager_secret_version" "example" {
  secret_id = aws_secretsmanager_secret.example.id
  secret_string = jsonencode({
    slack_webhook_url = var.slack_webhook_url
  })
}
