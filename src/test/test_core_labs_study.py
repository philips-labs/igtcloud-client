"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import igtcloud.client.services.entities
from igtcloud.client.services.entities.model.annotation_study import AnnotationStudy
from igtcloud.client.services.entities.model.base_study import BaseStudy
from igtcloud.client.services.entities.model.core_labs_study_all_of import CoreLabsStudyAllOf
from igtcloud.client.services.entities.model.patient import Patient
globals()['AnnotationStudy'] = AnnotationStudy
globals()['BaseStudy'] = BaseStudy
globals()['CoreLabsStudyAllOf'] = CoreLabsStudyAllOf
globals()['Patient'] = Patient
from igtcloud.client.services.entities.model.core_labs_study import CoreLabsStudy


class TestCoreLabsStudy(unittest.TestCase):
    """CoreLabsStudy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCoreLabsStudy(self):
        """Test CoreLabsStudy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CoreLabsStudy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
