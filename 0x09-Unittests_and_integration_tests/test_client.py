#!/usr/bin/env python3
"""unitest for module client
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class to test GithubOrgClient
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_values, get_patch):
        """test correct org
        """
        test = GithubOrgClient(org_values)
        test.org
        get_patch.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_values))

    def test_public_repos_url(self):
        """testing for public_repos_url
        """
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock)as mock_get:
            mock_get.return_value = {"repos_url": "url_for_mock"}
            test = GithubOrgClient("path")
            self.assertEqual(test._public_repos_url, "url_for_mock")
