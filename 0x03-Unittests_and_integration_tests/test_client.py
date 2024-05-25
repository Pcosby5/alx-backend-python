#!/usr/bin/env python3
"""
Unit tests for client module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class.
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_has_license):
        """
        Test that GithubOrgClient.has_license returns the correct value.
        """
        with patch('client.access_nested_map') as mock_access_nested_map:
            mock_access_nested_map.return_value = repo

            result = GithubOrgClient.has_license(repo, license_key)

            self.assertEqual(result, expected_has_license)

            mock_access_nested_map.assert_called_once_with(repo,
                                                           ("license", "key"))


if __name__ == "__main__":
    unittest.main()
