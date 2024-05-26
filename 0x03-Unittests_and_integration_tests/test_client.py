#!/usr/bin/env python3
"""
Unit tests for client module.
"""

import unittest
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
        result = GithubOrgClient.has_license(repo, license_key)

        print(f"Test: repo={repo}, license_key={license_key}, "
              f"expected_has_license={expected_has_license}, result={result}")
        self.assertEqual(result, expected_has_license)


if __name__ == "__main__":
    unittest.main()
