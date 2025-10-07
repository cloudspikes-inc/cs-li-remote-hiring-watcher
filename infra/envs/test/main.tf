module "aws_sm_test" {
  source = "../../modules/aws-sm"

  region            = var.region
  aws_profile       = var.aws_profile_test
  secret_name       = var.secret_name_test
  description       = var.description_test
  project_tag       = var.project_tag_test
  purpose_tag       = var.purpose_tag_test
  slack_webhook_url = var.slack_webhook_url_test
  environment       = var.environment_test
}
