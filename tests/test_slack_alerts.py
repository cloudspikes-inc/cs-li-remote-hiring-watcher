import json
import os
import sys
import unittest
from typing import Dict, Any
from unittest.mock import patch, MagicMock

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from alerts.slack_alerts import send_job  # noqa: E402


class TestSlackAlerts(unittest.TestCase):

    @patch("alerts.slack_alerts.WEBHOOK", "https://hooks.slack.com/test")
    @patch("alerts.slack_alerts.requests.post")
    def test_send_job_success(self, mock_post: MagicMock) -> None:
        """Test successful job alert sending."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # Test job data
        job = {
            "title": "DevOps Engineer",
            "company": "Test Company",
            "location": "Remote",
            "link": "https://example.com/job/123",
            "devops": ["docker", "kubernetes"],
            "aws": ["ec2", "s3"],
            "kubernetes": ["helm"],
        }

        # Call the function
        send_job(job)

        # Verify the request was made correctly
        mock_post.assert_called_once()
        call_args = mock_post.call_args

        # Check URL
        self.assertEqual(call_args[0][0], "https://hooks.slack.com/test")

        # Check headers
        content_type = call_args[1]["headers"]["Content-Type"]
        self.assertEqual(content_type, "application/json")

        # Check timeout
        self.assertEqual(call_args[1]["timeout"], 10)

        # Check data contains expected content
        data = json.loads(call_args[1]["data"])
        self.assertIn("DevOps Engineer", data["text"])
        self.assertIn("Test Company", data["text"])

    @patch("alerts.slack_alerts.WEBHOOK", "https://hooks.slack.com/test")
    @patch("alerts.slack_alerts.requests.post")
    def test_send_job_with_missing_fields(self, mock_post: MagicMock) -> None:
        """Test job alert with missing optional fields."""
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # Job with minimal data
        job: Dict[str, Any] = {}

        send_job(job)

        # Verify it handles missing fields gracefully
        call_args = mock_post.call_args
        data = json.loads(call_args[1]["data"])
        self.assertIn("N/A", data["text"])

    @patch("alerts.slack_alerts.WEBHOOK", None)
    def test_send_job_no_webhook(self) -> None:
        """Test that ValueError is raised when WEBHOOK is not set."""
        job = {"title": "Test Job"}

        with self.assertRaises(ValueError) as context:
            send_job(job)

        self.assertIn(
            "SLACK_WEBHOOK_URL environment variable is not set",
            str(context.exception),
        )


if __name__ == "__main__":
    unittest.main()
