#!/usr/bin/env python3

'''unittest module for utils'''

from parameterized import parameterized
import unittest
import utils
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    '''TestAccessNestedMap class'''

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        '''method to test test_access_nested_map function'''
        self.assertEqual(utils.access_nested_map(map, path), expected)
