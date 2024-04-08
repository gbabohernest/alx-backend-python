#!/usr/bin/env python3
"""This module defines test cases for the utils.py module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

from typing import (
    Mapping, Sequence, Any
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


# if __name__ == "__main__":
#     unittest.main()
