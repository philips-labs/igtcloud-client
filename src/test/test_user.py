"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import igtcloud.client.services.entities
from igtcloud.client.services.entities.model.account_status import AccountStatus
from igtcloud.client.services.entities.model.profile import Profile
from igtcloud.client.services.entities.model.user_settings import UserSettings
globals()['AccountStatus'] = AccountStatus
globals()['Profile'] = Profile
globals()['UserSettings'] = UserSettings
from igtcloud.client.services.entities.model.user import User


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = User()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()