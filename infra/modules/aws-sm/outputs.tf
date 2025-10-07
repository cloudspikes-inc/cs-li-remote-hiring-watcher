output "aws_sm_secret_name" {
  description = "Name of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.example.name
}

output "aws_sm_secret_arn" {
  description = "ARN of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.example.arn
}

output "aws_sm_secret_id" {
  description = "ID of the AWS Secrets Manager secret"
  value       = aws_secretsmanager_secret.example.id
}
