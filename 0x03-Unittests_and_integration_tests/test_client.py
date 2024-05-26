#!/usr/bin/env python3
"""Integration testing on GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class #type: ignore
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up class method to start patching."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = lambda url: cls.MockResponse(
            url, cls.org_payload, cls.repos_payload)

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patching."""
        cls.get_patcher.stop()

    class MockResponse:
        def __init__(self, url, org_payload, repos_payload):
            self.url = url
            self.org_payload = org_payload
            self.repos_payload = repos_payload

        def json(self):
            if self.url == 'https://api.github.com/orgs/google':
                return self.org_payload
            if self.url == 'https://api.github.com/orgs/google/repos':
                return self.repos_payload

    def test_public_repos(self):
        """Test public_repos method."""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter."""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos('apache-2.0'), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
