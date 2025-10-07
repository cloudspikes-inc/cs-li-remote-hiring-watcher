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
| <a name="input_aws_profile"></a> [aws\_profile](#input\_aws\_profile) | The AWS CLI profile to use | `string` | n/a | yes |
| <a name="input_aws_profile_test"></a> [aws\_profile\_test](#input\_aws\_profile\_test) | The AWS CLI profile to use for test environment | `string` | n/a | yes |
| <a name="input_description_test"></a> [description\_test](#input\_description\_test) | The description of the secret for test environment | `string` | n/a | yes |
| <a name="input_environment_test"></a> [environment\_test](#input\_environment\_test) | The deployment environment (e.g., dev, prod) for test environment | `string` | n/a | yes |
| <a name="input_project_tag_test"></a> [project\_tag\_test](#input\_project\_tag\_test) | The project tag for the secret for test environment | `string` | n/a | yes |
| <a name="input_purpose_tag_test"></a> [purpose\_tag\_test](#input\_purpose\_tag\_test) | The purpose tag for the secret for test environment | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | The AWS region where the secret will be created | `string` | n/a | yes |
| <a name="input_secret_name_test"></a> [secret\_name\_test](#input\_secret\_name\_test) | The name of the secret for test environment | `string` | n/a | yes |
| <a name="input_slack_webhook_url_test"></a> [slack\_webhook\_url\_test](#input\_slack\_webhook\_url\_test) | The Slack webhook URL to be stored in Secrets Manager for test environment | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_aws_sm_secret_arn"></a> [aws\_sm\_secret\_arn](#output\_aws\_sm\_secret\_arn) | n/a |
| <a name="output_aws_sm_secret_name"></a> [aws\_sm\_secret\_name](#output\_aws\_sm\_secret\_name) | n/a |
