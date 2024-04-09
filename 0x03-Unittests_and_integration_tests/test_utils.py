#!/usr/bin/env python3
"""This module defines test cases for the utils.py module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize
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


class TestMemoize(unittest.TestCase):
    """Defines test case for utils.memoize
       function
    """

    def test_memoize(self):
        """Test the memoize function
        """

        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        # Mock the a_method function
        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            # call a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # a_method was only called once?
            mock_a_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


# if __name__ == "__main__":
#     unittest.main()
