# client.py
from typing import List, Dict, Callable, Any

import requests
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """A Github org client"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Init method of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict[str, Any]:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Public repos URL"""
        return self.org()["repos_url"]

    @memoize
    def repos_payload(self) -> List[Dict[str, Any]]:
        """Memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = "") -> List[str]:
        """Public repos"""
        json_payload = self.repos_payload()
        public_repos = [
            repo["name"] for repo in json_payload
            if license == "" or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict[str, Any]], license_key: str) -> bool:
        """Static: has_license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
