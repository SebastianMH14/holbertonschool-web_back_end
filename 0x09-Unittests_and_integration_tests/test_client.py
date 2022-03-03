#!/usr/bin/env python3
"""Testing the client module
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class to rest the github class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, values, mock_json):
        """test the correct org
        """
        test = GithubOrgClient(values)
        test.org
        mock_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=values))

    def test_public_repos_url(self):
        """testing for public_repos_url
        """
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock)as mock_get:
            mock_get.return_value = {"repos_url": "url_for_mock"}
            test = GithubOrgClient("path")
            self.assertEqual(test._public_repos_url, "url_for_mock")
