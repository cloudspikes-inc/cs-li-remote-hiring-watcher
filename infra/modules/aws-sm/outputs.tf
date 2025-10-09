output "aws_sm_secret_name" {
  description = "Name of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.aws_sm_slack_webhook_url.name
}

output "aws_sm_secret_arn" {
  description = "ARN of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.aws_sm_slack_webhook_url.arn
}

output "aws_sm_secret_id" {
  description = "ID of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.aws_sm_slack_webhook_url.id
}
