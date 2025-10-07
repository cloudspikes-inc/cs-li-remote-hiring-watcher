## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 4.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | ~> 4.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_secretsmanager_secret.aws_sm_slack_webhook](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/secretsmanager_secret) | resource |
| [aws_secretsmanager_secret_version.aws_sm_sv_slack_webhook](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/secretsmanager_secret_version) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_profile"></a> [aws\_profile](#input\_aws\_profile) | The AWS CLI profile to use | `string` | n/a | yes |
| <a name="input_description"></a> [description](#input\_description) | The description of the secret | `string` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | The deployment environment (e.g., dev, prod) | `string` | n/a | yes |
| <a name="input_project_tag"></a> [project\_tag](#input\_project\_tag) | The project tag for the secret | `string` | n/a | yes |
| <a name="input_purpose_tag"></a> [purpose\_tag](#input\_purpose\_tag) | The purpose tag for the secret | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | The AWS region where the secret will be created | `string` | n/a | yes |
| <a name="input_secret_name"></a> [secret\_name](#input\_secret\_name) | The name of the secret | `string` | n/a | yes |
| <a name="input_slack_webhook_url"></a> [slack\_webhook\_url](#input\_slack\_webhook\_url) | The Slack webhook URL to be stored in Secrets Manager | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_aws_sm_secret_arn"></a> [aws\_sm\_secret\_arn](#output\_aws\_sm\_secret\_arn) | n/a |
| <a name="output_aws_sm_secret_name"></a> [aws\_sm\_secret\_name](#output\_aws\_sm\_secret\_name) | n/a |
