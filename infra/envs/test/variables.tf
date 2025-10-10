variable "region" {
  description = "AWS region for test environment"
  type        = string
  default     = "ap-south-1"
}

# variable "aws_profile" {
#   description = "AWS profile for test environment"
#   type        = string
#   default     = "default"
# }

# variable "aws_profile_test" {
#   description = "AWS profile for test environment"
#   type        = string
#   default     = "default"
# }

variable "secret_name_test" {
  description = "Name of the secret in AWS Secrets Manager"
  type        = string
  default     = "linkedin-scanner-slack-webhook-test"
}

variable "description_test" {
  description = "Description of the secret"
  type        = string
  default     = "Slack webhook URL for LinkedIn Scanner test environment"
}

variable "project_tag_test" {
  description = "Project tag for resources"
  type        = string
  default     = "linkedin-scanner"
}

variable "purpose_tag_test" {
  description = "Purpose tag for resources"
  type        = string
  default     = "slack-integration"
}

variable "slack_webhook_url_test" {
  description = "Slack webhook URL for test environment"
  type        = string
  sensitive   = true
}

variable "environment_test" {
  description = "Environment name"
  type        = string
  default     = "test"
}
