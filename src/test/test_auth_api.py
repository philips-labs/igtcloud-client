"""
    Apis

    Api containing all apis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import igtcloud.client.services.auth
from igtcloud.client.services.auth.api.auth_api import AuthApi  # noqa: E501


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_introspect_resource(self):
        """Test case for get_introspect_resource

        """
        pass

    def test_get_permissions_resource(self):
        """Test case for get_permissions_resource

        Gets a list of permissions  # noqa: E501
        """
        pass

    def test_get_s3_credentials_resource(self):
        """Test case for get_s3_credentials_resource

        """
        pass

    def test_post_audit_resource(self):
        """Test case for post_audit_resource

        """
        pass

    def test_post_login_resource_login(self):
        """Test case for post_login_resource_login

        Authorize by using your IAM credentials  # noqa: E501
        """
        pass

    def test_post_logout_resource(self):
        """Test case for post_logout_resource

        """
        pass

    def test_post_refresh_resource(self):
        """Test case for post_refresh_resource

        """
        pass


if __name__ == '__main__':
    unittest.main()
