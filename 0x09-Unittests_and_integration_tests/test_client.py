#!/usr/bin/env python3
"""test for client"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class test_public_repos_url(unittest.TestCase):
    """test to GithubOrgClient._public_repos_url"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, get_patch):
        """Method that tests that GithubOrgClient.org returns the
        correct value
        """
        test_client = GithubOrgClient(org)
        test_return = test_client.org
        self.assertEqual(test_return, get_patch.return_value)
        get_patch.assert_called_once
