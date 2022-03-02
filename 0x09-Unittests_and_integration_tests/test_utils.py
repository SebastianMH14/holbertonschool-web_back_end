#!/usr/bin/env python3
"""test access_nested_map function"""
from utils import access_nested_map, get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """class for test"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """test the result"""
        result = access_nested_map(map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map, path):
        """ test nested map exception"""
        self.assertRaises(KeyError, access_nested_map, map, path)


class TestGetJson(unittest.TestCase):
    """test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, response):
        """test result"""
        with patch("utils.requests.get") as req:
            req.return_value = req
            req.json.return_value = response
            json = get_json(url)
            req.assert_called_once_with(url)
            self.assertEqual(response, json)
