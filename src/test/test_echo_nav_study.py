"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import igtcloud.client.services.entities
from igtcloud.client.services.entities.model.base_study import BaseStudy
from igtcloud.client.services.entities.model.echo_nav_study_all_of import EchoNavStudyAllOf
from igtcloud.client.services.entities.model.patient import Patient
globals()['BaseStudy'] = BaseStudy
globals()['EchoNavStudyAllOf'] = EchoNavStudyAllOf
globals()['Patient'] = Patient
from igtcloud.client.services.entities.model.echo_nav_study import EchoNavStudy


class TestEchoNavStudy(unittest.TestCase):
    """EchoNavStudy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEchoNavStudy(self):
        """Test EchoNavStudy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EchoNavStudy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()