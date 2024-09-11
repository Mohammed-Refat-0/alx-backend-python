#!/usr/bin/env python3

'''unittest module for client'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient as GTO
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    ''' TestGithubOrgClient testing class'''

    @parameterized.expand([('google', 'google'),
                           ('abc', 'abc')])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: str, mock_get_json) -> None:
        '''method to test that GithubOrgClient.org
           function returns the correct value.'''

        mock_get_json.return_value = expected
        client = GTO(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self) -> None:
        """method to tes _public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=unittest.mock.PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GTO("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
