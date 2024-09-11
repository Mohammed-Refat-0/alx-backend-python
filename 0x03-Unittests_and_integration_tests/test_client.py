#!/usr/bin/env python3

'''unittest module for client'''

from client import GithubOrgClient as GTO
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import requests
import unittest
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tmethod to test has_license """
        org_client = GTO("google")
        client_has_licence = org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration tests class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return requests.HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests public_repos method"""
        self.assertEqual(
            GTO("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests public_repos method with a license"""
        self.assertEqual(
            GTO("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests"""
        cls.get_patcher.stop()
