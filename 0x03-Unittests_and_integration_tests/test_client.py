#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from unittest.mock import patch
from typing import Any, Sequence, Mapping
from utils import access_nested_map, get_json, memoize, requests
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name: str, mock_get_json: Any) -> None:
        """test_org"""
        test_class = GithubOrgClient(test_org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{test_org_name}'
        )

    @patch('GithubOrgClient.org')
    def test_public_repos_url(self) -> None:
        """test_public_repos_url"""
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.return_value = {'repos_url': 'http://some_url'}
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class._public_repos_url,
                             mock_org.return_value.get('repos_url'))
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any) -> None:
        """test_public_repos"""
        json_payload = [{"name": "google"}, {"name": "abc"}]
        mock_get_json.return_value = json_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://some_url"
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos(),
                             ["google", "abc"])
            mock_get_json.assert_called_once_with("http://some_url")
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo: Mapping[str, Any],
                         license_key: str, expected: bool) -> None:
        """test_has_license"""
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.has_license(repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient Class"""

    @classmethod
    def setUpClass(cls) -> None:
        """setUpClass"""
        cls.get_patcher = patch('requests.get', side_effect=requests.get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """tearDownClass"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """test_public_repos"""
        test_class = GithubOrgClient('google')
        self.assertEqual(test_class.org, {'login': 'google', 'id': 1342004})
        self.assertEqual(test_class._public_repos_url,
                         'https://api.github.com/orgs/google/repos')
        self.assertEqual(test_class.public_repos(),
                         ['repo1', 'repo2', 'repo3'])
