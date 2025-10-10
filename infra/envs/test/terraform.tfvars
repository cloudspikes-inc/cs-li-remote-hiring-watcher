# Common values for Providers(Some values can be reused in multiple environments)
region = "ap-south-1"
# aws_profile = "default"

#AWS_SM
# aws_profile_test = "default"
secret_name_test = "cs-linkedin-scanner-slack-webhook-url-test"
description_test = "Slack webhook URL for LinkedIn Scanner job alerts"
project_tag_test = "linkedin-scanner"
purpose_tag_test = "slack-integration-test"
# slack_webhook_url_test will be provided via TF_VAR_slack_webhook_url_test environment variable
environment_test = "test"

