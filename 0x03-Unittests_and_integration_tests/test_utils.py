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

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, map: Dict,
                                         path: Tuple[str]) -> None:
        '''test case to test exception handling in access_nested_map'''
        with self.assertRaises(KeyError):
            utils.access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    '''TestGetJson class'''

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @ unittest.mock.patch('requests.get')
    def test_get_json(self, test_url: str, test_response: Dict,
                      mock_get) -> None:
        '''method to test get_json function'''
        mock_get.return_value.json.return_value = test_response
        self.assertEqual(utils.get_json(test_url), test_response)
        mock_get.assert_called_once_with(test_url)
