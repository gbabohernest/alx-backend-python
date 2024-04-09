#!/usr/bin/env python3
"""This module defines test cases for the client.py module
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Defines test case for client.GithubOrgClient
       class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 mock_get_json: unittest.mock.Mock
                 ) -> None:
        """Test the client.GithubOrgClient
           correct return value
        """
        github_client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"name": org_name,
                                      "description": "Mock org"}

        org_info = github_client.org

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        #  Assert that the returned org_info matches the expected value
        expected_org_info = {"name": org_name, "description": "Mock org"}
        self.assertEqual(org_info, expected_org_info)

    def test_public_repos_url(self) -> None:
        """Test GithubOrgClient._public_repos_url function
            """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos function"""

        # Define the mocked payload for get_json
        mock_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None},
        ]

        mock_get_json.return_value = mock_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:

            # Set the return value of mock_public_repos_url to a known URL
            mock_public_repos_url.return_value = \
                "https://api.github.com/orgs/google/repos"

            github_client = GithubOrgClient("google")

            public_repos = github_client.public_repos(license="mit")

            # Assert that the public_repos list matches the expected
            # repos based on the mocked payload
            expected_repos = ["repo1"]
            self.assertEqual(public_repos, expected_repos)

            mock_get_json.assert_called_once()

        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict,
                         license_key: str, expected_result: bool) -> None:
        """Test GithubOrgClient.has_license method
        """
        github_client = GithubOrgClient("google")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


# if __name__ == '__main__':
#    unittest.main()
