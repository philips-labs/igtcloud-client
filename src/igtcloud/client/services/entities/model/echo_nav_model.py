"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from igtcloud.client.services.entities.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from igtcloud.client.services.entities.exceptions import ApiAttributeError


def lazy_import():
    from igtcloud.client.services.entities.model.base_study_model import BaseStudyModel
    from igtcloud.client.services.entities.model.echo_nav_model_all_of import EchoNavModelAllOf
    from igtcloud.client.services.entities.model.patient_model import PatientModel
    globals()['BaseStudyModel'] = BaseStudyModel
    globals()['EchoNavModelAllOf'] = EchoNavModelAllOf
    globals()['PatientModel'] = PatientModel


class EchoNavModel(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'study_type': (str,),  # noqa: E501
            'subject_id': (str,),  # noqa: E501
            'x_ray_system': (str,),  # noqa: E501
            'x_ray_software_release': (str,),  # noqa: E501
            'x_ray_configuration': (str,),  # noqa: E501
            'x_ray_detector': (str,),  # noqa: E501
            'x_ray_table': (str,),  # noqa: E501
            'ultrasound_system': (str,),  # noqa: E501
            'ultrasound_software_release': (str,),  # noqa: E501
            'ultrasound_hardware': (str,),  # noqa: E501
            'echo_navigator_investigational_device': (str,),  # noqa: E501
            'echo_navigator_software_release': (str,),  # noqa: E501
            'hemo': (str,),  # noqa: E501
            'recorded_data': ([str],),  # noqa: E501
            'diseases': ([str],),  # noqa: E501
            'therapy': ([str],),  # noqa: E501
            'redo': (str,),  # noqa: E501
            'implant1_manufacturer': (str,),  # noqa: E501
            'implant1_type': (str,),  # noqa: E501
            'implant1_size': (str,),  # noqa: E501
            'implant2_manufacturer': (str,),  # noqa: E501
            'implant2_type': (str,),  # noqa: E501
            'implant2_size': (str,),  # noqa: E501
            'implant3_manufacturer': (str,),  # noqa: E501
            'implant3_type': (str,),  # noqa: E501
            'implant3_size': (str,),  # noqa: E501
            'implant4_manufacturer': (str,),  # noqa: E501
            'implant4_type': (str,),  # noqa: E501
            'implant4_size': (str,),  # noqa: E501
            'image_transducers': ([str],),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'study_database_id': (str,),  # noqa: E501
            'created_on': (datetime,),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'last_updated_on': (datetime,),  # noqa: E501
            'last_updated_by': (str,),  # noqa: E501
            'max_retention_date': (datetime,),  # noqa: E501
            'legal_basis': ([str],),  # noqa: E501
            'legal_basis_other': (str,),  # noqa: E501
            'purpose': ([str],),  # noqa: E501
            'purpose_other': (str,),  # noqa: E501
            'electronic_record_state': (str,),  # noqa: E501
            'study_id': (str,),  # noqa: E501
            'instance_uid': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'study_date': (datetime,),  # noqa: E501
            'accession_number': (str,),  # noqa: E501
            's3_prefix': (str,),  # noqa: E501
            'hospital_id': (str,),  # noqa: E501
            'project_id': (str,),  # noqa: E501
            'patient_database_id': (str,),  # noqa: E501
            'patient': (PatientModel,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'study_type': val}

    attribute_map = {
        'study_type': 'studyType',  # noqa: E501
        'subject_id': 'subjectId',  # noqa: E501
        'x_ray_system': 'xRaySystem',  # noqa: E501
        'x_ray_software_release': 'xRaySoftwareRelease',  # noqa: E501
        'x_ray_configuration': 'xRayConfiguration',  # noqa: E501
        'x_ray_detector': 'xRayDetector',  # noqa: E501
        'x_ray_table': 'xRayTable',  # noqa: E501
        'ultrasound_system': 'ultrasoundSystem',  # noqa: E501
        'ultrasound_software_release': 'ultrasoundSoftwareRelease',  # noqa: E501
        'ultrasound_hardware': 'ultrasoundHardware',  # noqa: E501
        'echo_navigator_investigational_device': 'echoNavigatorInvestigationalDevice',  # noqa: E501
        'echo_navigator_software_release': 'echoNavigatorSoftwareRelease',  # noqa: E501
        'hemo': 'hemo',  # noqa: E501
        'recorded_data': 'recordedData',  # noqa: E501
        'diseases': 'diseases',  # noqa: E501
        'therapy': 'therapy',  # noqa: E501
        'redo': 'redo',  # noqa: E501
        'implant1_manufacturer': 'implant1Manufacturer',  # noqa: E501
        'implant1_type': 'implant1Type',  # noqa: E501
        'implant1_size': 'implant1Size',  # noqa: E501
        'implant2_manufacturer': 'implant2Manufacturer',  # noqa: E501
        'implant2_type': 'implant2Type',  # noqa: E501
        'implant2_size': 'implant2Size',  # noqa: E501
        'implant3_manufacturer': 'implant3Manufacturer',  # noqa: E501
        'implant3_type': 'implant3Type',  # noqa: E501
        'implant3_size': 'implant3Size',  # noqa: E501
        'implant4_manufacturer': 'implant4Manufacturer',  # noqa: E501
        'implant4_type': 'implant4Type',  # noqa: E501
        'implant4_size': 'implant4Size',  # noqa: E501
        'image_transducers': 'imageTransducers',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'study_database_id': 'studyDatabaseId',  # noqa: E501
        'created_on': 'createdOn',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'last_updated_on': 'lastUpdatedOn',  # noqa: E501
        'last_updated_by': 'lastUpdatedBy',  # noqa: E501
        'max_retention_date': 'maxRetentionDate',  # noqa: E501
        'legal_basis': 'legalBasis',  # noqa: E501
        'legal_basis_other': 'legalBasisOther',  # noqa: E501
        'purpose': 'purpose',  # noqa: E501
        'purpose_other': 'purposeOther',  # noqa: E501
        'electronic_record_state': 'electronicRecordState',  # noqa: E501
        'study_id': 'studyId',  # noqa: E501
        'instance_uid': 'instanceUid',  # noqa: E501
        'state': 'state',  # noqa: E501
        'description': 'description',  # noqa: E501
        'study_date': 'studyDate',  # noqa: E501
        'accession_number': 'accessionNumber',  # noqa: E501
        's3_prefix': 's3Prefix',  # noqa: E501
        'hospital_id': 'hospitalId',  # noqa: E501
        'project_id': 'projectId',  # noqa: E501
        'patient_database_id': 'patientDatabaseId',  # noqa: E501
        'patient': 'patient',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EchoNavModel - a model defined in OpenAPI

        Keyword Args:
            study_type (str):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            subject_id (str): [optional]  # noqa: E501
            x_ray_system (str): [optional]  # noqa: E501
            x_ray_software_release (str): [optional]  # noqa: E501
            x_ray_configuration (str): [optional]  # noqa: E501
            x_ray_detector (str): [optional]  # noqa: E501
            x_ray_table (str): [optional]  # noqa: E501
            ultrasound_system (str): [optional]  # noqa: E501
            ultrasound_software_release (str): [optional]  # noqa: E501
            ultrasound_hardware (str): [optional]  # noqa: E501
            echo_navigator_investigational_device (str): [optional]  # noqa: E501
            echo_navigator_software_release (str): [optional]  # noqa: E501
            hemo (str): [optional]  # noqa: E501
            recorded_data ([str]): [optional]  # noqa: E501
            diseases ([str]): [optional]  # noqa: E501
            therapy ([str]): [optional]  # noqa: E501
            redo (str): [optional]  # noqa: E501
            implant1_manufacturer (str): [optional]  # noqa: E501
            implant1_type (str): [optional]  # noqa: E501
            implant1_size (str): [optional]  # noqa: E501
            implant2_manufacturer (str): [optional]  # noqa: E501
            implant2_type (str): [optional]  # noqa: E501
            implant2_size (str): [optional]  # noqa: E501
            implant3_manufacturer (str): [optional]  # noqa: E501
            implant3_type (str): [optional]  # noqa: E501
            implant3_size (str): [optional]  # noqa: E501
            implant4_manufacturer (str): [optional]  # noqa: E501
            implant4_type (str): [optional]  # noqa: E501
            implant4_size (str): [optional]  # noqa: E501
            image_transducers ([str]): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            study_database_id (str): [optional]  # noqa: E501
            created_on (datetime): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            last_updated_on (datetime): [optional]  # noqa: E501
            last_updated_by (str): [optional]  # noqa: E501
            max_retention_date (datetime): [optional]  # noqa: E501
            legal_basis ([str]): [optional]  # noqa: E501
            legal_basis_other (str): [optional]  # noqa: E501
            purpose ([str]): [optional]  # noqa: E501
            purpose_other (str): [optional]  # noqa: E501
            electronic_record_state (str): [optional]  # noqa: E501
            study_id (str): [optional]  # noqa: E501
            instance_uid (str): [optional]  # noqa: E501
            state (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            study_date (datetime): [optional]  # noqa: E501
            accession_number (str): [optional]  # noqa: E501
            s3_prefix (str): [optional]  # noqa: E501
            hospital_id (str): [optional]  # noqa: E501
            project_id (str): [optional]  # noqa: E501
            patient_database_id (str): [optional]  # noqa: E501
            patient (PatientModel): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EchoNavModel - a model defined in OpenAPI

        Keyword Args:
            study_type (str):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            subject_id (str): [optional]  # noqa: E501
            x_ray_system (str): [optional]  # noqa: E501
            x_ray_software_release (str): [optional]  # noqa: E501
            x_ray_configuration (str): [optional]  # noqa: E501
            x_ray_detector (str): [optional]  # noqa: E501
            x_ray_table (str): [optional]  # noqa: E501
            ultrasound_system (str): [optional]  # noqa: E501
            ultrasound_software_release (str): [optional]  # noqa: E501
            ultrasound_hardware (str): [optional]  # noqa: E501
            echo_navigator_investigational_device (str): [optional]  # noqa: E501
            echo_navigator_software_release (str): [optional]  # noqa: E501
            hemo (str): [optional]  # noqa: E501
            recorded_data ([str]): [optional]  # noqa: E501
            diseases ([str]): [optional]  # noqa: E501
            therapy ([str]): [optional]  # noqa: E501
            redo (str): [optional]  # noqa: E501
            implant1_manufacturer (str): [optional]  # noqa: E501
            implant1_type (str): [optional]  # noqa: E501
            implant1_size (str): [optional]  # noqa: E501
            implant2_manufacturer (str): [optional]  # noqa: E501
            implant2_type (str): [optional]  # noqa: E501
            implant2_size (str): [optional]  # noqa: E501
            implant3_manufacturer (str): [optional]  # noqa: E501
            implant3_type (str): [optional]  # noqa: E501
            implant3_size (str): [optional]  # noqa: E501
            implant4_manufacturer (str): [optional]  # noqa: E501
            implant4_type (str): [optional]  # noqa: E501
            implant4_size (str): [optional]  # noqa: E501
            image_transducers ([str]): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            study_database_id (str): [optional]  # noqa: E501
            created_on (datetime): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            last_updated_on (datetime): [optional]  # noqa: E501
            last_updated_by (str): [optional]  # noqa: E501
            max_retention_date (datetime): [optional]  # noqa: E501
            legal_basis ([str]): [optional]  # noqa: E501
            legal_basis_other (str): [optional]  # noqa: E501
            purpose ([str]): [optional]  # noqa: E501
            purpose_other (str): [optional]  # noqa: E501
            electronic_record_state (str): [optional]  # noqa: E501
            study_id (str): [optional]  # noqa: E501
            instance_uid (str): [optional]  # noqa: E501
            state (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            study_date (datetime): [optional]  # noqa: E501
            accession_number (str): [optional]  # noqa: E501
            s3_prefix (str): [optional]  # noqa: E501
            hospital_id (str): [optional]  # noqa: E501
            project_id (str): [optional]  # noqa: E501
            patient_database_id (str): [optional]  # noqa: E501
            patient (PatientModel): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              BaseStudyModel,
              EchoNavModelAllOf,
          ],
          'oneOf': [
          ],
        }
