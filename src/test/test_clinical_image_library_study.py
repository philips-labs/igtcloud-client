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
from igtcloud.client.services.entities.model.clinical_image_library_study_all_of import ClinicalImageLibraryStudyAllOf
from igtcloud.client.services.entities.model.patient import Patient
globals()['BaseStudy'] = BaseStudy
globals()['ClinicalImageLibraryStudyAllOf'] = ClinicalImageLibraryStudyAllOf
globals()['Patient'] = Patient
from igtcloud.client.services.entities.model.clinical_image_library_study import ClinicalImageLibraryStudy


class TestClinicalImageLibraryStudy(unittest.TestCase):
    """ClinicalImageLibraryStudy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClinicalImageLibraryStudy(self):
        """Test ClinicalImageLibraryStudy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClinicalImageLibraryStudy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
