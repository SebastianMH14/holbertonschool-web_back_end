#!/usr/bin/env python3
"""test for client"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class test_public_repos_url(unittest.TestCase):
    """
    method to unit-test GithubOrgClient._public_repos_url
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, result, patch_data):
        """ Test the org of the client """
        patch_data.return_value = result
        x = GithubOrgClient(org)
        self.assertEqual(x.org, result)
        patch_data.assert_called_once_with("https://api.github.com/orgs/"+org)
