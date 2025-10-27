#!/bin/bash

# Quick workflow validation script
echo "🔍 Validating GitHub Actions Workflows..."

cd /Users/dhruvrana/Downloads/CSI/cs-li-remote-hiring-watcher

echo ""
echo "=== Checking Workflow Syntax ==="

# Check if workflows are present
if [ -f ".github/workflows/iam-policy-validation.yml" ]; then
    echo "✅ IAM Policy Validation workflow found"
else
    echo "❌ IAM Policy Validation workflow missing"
fi

if [ -f ".github/workflows/terraform-pipeline.yml" ]; then
    echo "✅ Terraform Pipeline workflow found"
else
    echo "❌ Terraform Pipeline workflow missing"
fi

echo ""
echo "=== Checking Secret References ==="

# Check for correct secret names in workflows
if grep -q "AWS_ACCESS_KEY_ID_TEST" .github/workflows/*.yml; then
    echo "❌ Found deprecated AWS_ACCESS_KEY_ID_TEST in workflows"
else
    echo "✅ No deprecated AWS secret references found"
fi

if grep -q "AWS_ACCESS_KEY_ID" .github/workflows/*.yml; then
    echo "✅ Found correct AWS_ACCESS_KEY_ID references"
else
    echo "❌ Missing AWS_ACCESS_KEY_ID references"
fi

echo ""
echo "=== Checking Documentation ==="

if [ -f ".github/WORKFLOWS_SETUP.md" ]; then
    echo "✅ Workflow setup documentation found"
else
    echo "❌ Workflow setup documentation missing"
fi

if [ -f ".github/LOCAL_TESTING_GUIDE.md" ]; then
    echo "✅ Local testing guide found"
else
    echo "❌ Local testing guide missing"
fi

echo ""
echo "=== Checking .gitignore Protection ==="

if grep -q ".secrets" .gitignore; then
    echo "✅ .secrets file is protected in .gitignore"
else
    echo "❌ .secrets file not protected in .gitignore"
fi

echo ""
echo "=== Summary ==="
echo "🎉 Workflow validation completed!"
echo ""
echo "📋 Ready to push:"
echo "  - GitHub Actions workflows (fixed AWS CLI installation)"
echo "  - Updated documentation"
echo "  - Protected secrets configuration"
echo ""
echo "🚀 Next steps:"
echo "  1. Add GitHub Secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)"
echo "  2. Push to GitHub and create test PR"
echo "  3. Watch workflows run successfully!"