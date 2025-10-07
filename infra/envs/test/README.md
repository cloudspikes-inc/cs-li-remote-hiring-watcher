## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 4.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_aws_sm_test"></a> [aws\_sm\_test](#module\_aws\_sm\_test) | ../../modules/aws-sm | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_profile"></a> [aws\_profile](#input\_aws\_profile) | AWS profile for test environment | `string` | `"default"` | no |
| <a name="input_aws_profile_test"></a> [aws\_profile\_test](#input\_aws\_profile\_test) | AWS profile for test environment | `string` | `"default"` | no |
| <a name="input_description_test"></a> [description\_test](#input\_description\_test) | Description of the secret | `string` | `"Slack webhook URL for LinkedIn Scanner test environment"` | no |
| <a name="input_environment_test"></a> [environment\_test](#input\_environment\_test) | Environment name | `string` | `"test"` | no |
| <a name="input_project_tag_test"></a> [project\_tag\_test](#input\_project\_tag\_test) | Project tag for resources | `string` | `"linkedin-scanner"` | no |
| <a name="input_purpose_tag_test"></a> [purpose\_tag\_test](#input\_purpose\_tag\_test) | Purpose tag for resources | `string` | `"slack-integration"` | no |
| <a name="input_region"></a> [region](#input\_region) | AWS region for test environment | `string` | `"ap-south-1"` | no |
| <a name="input_secret_name_test"></a> [secret\_name\_test](#input\_secret\_name\_test) | Name of the secret in AWS Secrets Manager | `string` | `"linkedin-scanner-slack-webhook-test"` | no |
| <a name="input_slack_webhook_url_test"></a> [slack\_webhook\_url\_test](#input\_slack\_webhook\_url\_test) | Slack webhook URL for test environment | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_aws_sm_secret_arn"></a> [aws\_sm\_secret\_arn](#output\_aws\_sm\_secret\_arn) | ARN of the AWS Secrets Manager secret |
| <a name="output_aws_sm_secret_name"></a> [aws\_sm\_secret\_name](#output\_aws\_sm\_secret\_name) | Name of the AWS Secrets Manager secret |
