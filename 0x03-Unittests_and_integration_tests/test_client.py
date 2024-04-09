#!/usr/bin/env python3
"""This module defines test cases for the client.py module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


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

    def test_public_repos_url(self):
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


# if __name__ == '__main__':
#    unittest.main()
