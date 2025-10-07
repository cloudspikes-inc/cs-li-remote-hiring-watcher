output "aws_sm_secret_name" {
  description = "Name of the AWS Secrets Manager secret"
  value       = module.aws_sm_test.aws_sm_secret_name
}

output "aws_sm_secret_arn" {
  description = "ARN of the AWS Secrets Manager secret"
  value       = module.aws_sm_test.aws_sm_secret_arn
}
