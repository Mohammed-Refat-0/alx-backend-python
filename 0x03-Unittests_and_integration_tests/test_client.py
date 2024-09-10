#!/usr/bin/env python3

'''unittest module for client'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient as GTO
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    ''' TestGithubOrgClient testing class'''

    @parameterized.expand([('google', {'login': 'google'}),
                           ('abc', {'login': 'abc'})])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: Dict[str, str],
                 mock_get_json) -> None:
        '''method to test that GithubOrgClient.org
           function returns the correct value.'''

        mock_get_json.return_value = expected
        client = GTO(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
