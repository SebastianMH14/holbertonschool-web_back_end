#!/usr/bin/env python3
"""unitest for module client
"""

import unittest
from unittest.mock import patch, PropertyMock, call
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

    @patch.object(GithubOrgClient, 'org')
    def test_public_repos(self, mock_org):
        """ now  check or test public repos
        Args:
            mock_org ([type]): [description]
        """
        payload = {
            'obj': {
                'name': 'Victor',
                'last_name': 'Zuluaga',
                'profile': 'developer',
                'edad': 100
            },
            'url_pattern': 'repos_url',
        }
        mock_org.return_value = payload
        create_instance = GithubOrgClient('org')
        value = create_instance.org

        with patch(f'{__name__}.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = value()['url_pattern']
            self.assertEqual(mock_repos_url(), 'repos_url')
            mock_repos_url.assert_called_once()
            mock_org.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test the initial parameters
        Args:
            repo ([type]): [description]
            license_key ([type]): [description]
            expected ([type]): [description]
        """
        ret = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(ret, expected)

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
