"""
    Apis

    Api containing all apis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import igtcloud.client.services.auth
from igtcloud.client.services.auth.model.organizations import Organizations
globals()['Organizations'] = Organizations
from igtcloud.client.services.auth.model.introspect_response import IntrospectResponse


class TestIntrospectResponse(unittest.TestCase):
    """IntrospectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIntrospectResponse(self):
        """Test IntrospectResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IntrospectResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()