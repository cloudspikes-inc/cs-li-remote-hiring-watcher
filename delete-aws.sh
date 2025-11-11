
#!/usr/bin/env bash
#
# AWS Cleanup Script — deletes resources covered by IAM policy
# ⚠️ WARNING: This action is irreversible. Use in non-production only.
#
# Requirements:
#   - AWS CLI v2 installed and configured (`aws configure`)
#   - IAM user/role with sufficient permissions
#

set -euo pipefail

LOG_FILE="aws_cleanup_$(date +%F_%H-%M-%S).log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "========================================"
echo " AWS RESOURCE CLEANUP STARTED"
echo " $(date)"
echo "========================================"

read -rp "⚠️  Are you sure you want to delete all supported resources? (yes/no): " confirm
[[ "$confirm" != "yes" ]] && { echo "Aborted."; exit 1; }

# ---------- S3 ----------
echo "🪣 Deleting S3 buckets..."
for bucket in $(aws s3api list-buckets --query 'Buckets[].Name' --output text); do
  echo "Deleting bucket: $bucket"
  aws s3 rb "s3://$bucket" --force || echo "Failed to delete $bucket"
done

# ---------- Secrets Manager ----------
echo "🔑 Deleting Secrets..."
for secret in $(aws secretsmanager list-secrets --query 'SecretList[].Name' --output text); do
  echo "Deleting secret: $secret"
  aws secretsmanager delete-secret --secret-id "$secret" --force-delete-without-recovery || echo "Failed: $secret"
done

# ---------- DynamoDB ----------
echo "🧮 Deleting DynamoDB tables..."
for table in $(aws dynamodb list-tables --query 'TableNames[]' --output text); do
  echo "Deleting table: $table"
  aws dynamodb delete-table --table-name "$table" || echo "Failed: $table"
done

# ---------- ECR ----------
echo "🐳 Deleting ECR repositories..."
for repo in $(aws ecr describe-repositories --query 'repositories[].repositoryName' --output text); do
  echo "Deleting ECR repo: $repo"
  aws ecr delete-repository --repository-name "$repo" --force || echo "Failed: $repo"
done

# ---------- RDS ----------
echo "🗄️  Deleting RDS instances..."
for db in $(aws rds describe-db-instances --query 'DBInstances[].DBInstanceIdentifier' --output text); do
  echo "Deleting RDS instance: $db"
  aws rds delete-db-instance --db-instance-identifier "$db" --skip-final-snapshot || echo "Failed: $db"
done

# ---------- CloudWatch Logs ----------
echo "📜 Deleting CloudWatch Log Groups..."
for log_group in $(aws logs describe-log-groups --query 'logGroups[].logGroupName' --output text); do
  echo "Deleting log group: $log_group"
  aws logs delete-log-group --log-group-name "$log_group" || echo "Failed: $log_group"
done

# ---------- KMS ----------
echo "🗝️  (Skipping AWS-managed KMS keys; cannot delete)"
for key in $(aws kms list-keys --query 'Keys[].KeyId' --output text); do
  aws kms describe-key --key-id "$key" --query 'KeyMetadata.KeyManager' --output text | grep -q "CUSTOMER" && {
    echo "Scheduling deletion for KMS key: $key"
    aws kms schedule-key-deletion --key-id "$key" --pending-window-in-days 7 || echo "Failed: $key"
  }
done

echo "========================================"
echo "✅ Cleanup completed — check $LOG_FILE for details"
echo "========================================"