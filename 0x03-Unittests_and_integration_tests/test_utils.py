#!/usr/bin/env python3
"""This module defines test cases for the utils.py module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map, get_json
)

from typing import (
    Dict, Mapping, Sequence, Any
)


class TestAccessNestedMap(unittest.TestCase):
    """Defines test case for utils.access_nested_map
       function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            expected_result: Any) -> None:
        """Test access_nested_map function for correct output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence,
            expected_result: Any) -> None:
        """Test access_nested_map function for exception"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path),
                             expected_result)


class TestGetJson(unittest.TestCase):
    """Defines test case for utils.get_json
       function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self, test_url: str,
            test_payload: Dict,
            mock_requests_get: Mock
    ) -> None:
        """Test get_json functon for expected result
        """
        # Mock the json method of the response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # call get_json with test URL
        result = get_json(test_url)

        # check that requests.get was called exactly once with the test URL
        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


# if __name__ == "__main__":
#     unittest.main()
