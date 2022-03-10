"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from igtcloud.client.services.entities.api_client import ApiClient, Endpoint as _Endpoint
from igtcloud.client.services.entities.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from igtcloud.client.services.entities.model.application import Application
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.storage import Storage
from igtcloud.client.services.entities.model.training_application import TrainingApplication


class ApplicationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_applications(
            self,
            project_id,
            **kwargs
        ):
            """get_applications  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_applications(project_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):

            Keyword Args:
                application (str): [optional]
                format (str): [optional]
                vm_environment (str): [optional]
                does_open_on_study (bool): [optional]
                x_fields (str): An optional fields mask. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Application]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            return self.call_with_http_info(**kwargs)

        self.get_applications = _Endpoint(
            settings={
                'response_type': ([Application],),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/applications',
                'operation_id': 'get_applications',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'application',
                    'format',
                    'vm_environment',
                    'does_open_on_study',
                    'x_fields',
                ],
                'required': [
                    'project_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'application':
                        (str,),
                    'format':
                        (str,),
                    'vm_environment':
                        (str,),
                    'does_open_on_study':
                        (bool,),
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'application': 'application',
                    'format': 'format',
                    'vm_environment': 'vmEnvironment',
                    'does_open_on_study': 'doesOpenOnStudy',
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'project_id': 'query',
                    'application': 'query',
                    'format': 'query',
                    'vm_environment': 'query',
                    'does_open_on_study': 'query',
                    'x_fields': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_applications
        )

        def __get_training_application_guide(
            self,
            training_application,
            **kwargs
        ):
            """get_training_application_guide  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_training_application_guide(training_application, async_req=True)
            >>> result = thread.get()

            Args:
                training_application (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['training_application'] = \
                training_application
            return self.call_with_http_info(**kwargs)

        self.get_training_application_guide = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/training-applications/{training_application}/guide',
                'operation_id': 'get_training_application_guide',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'training_application',
                ],
                'required': [
                    'training_application',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'training_application':
                        (str,),
                },
                'attribute_map': {
                    'training_application': 'training_application',
                },
                'location_map': {
                    'training_application': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_training_application_guide
        )

        def __get_training_application_storage(
            self,
            training_application,
            **kwargs
        ):
            """get_training_application_storage  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_training_application_storage(training_application, async_req=True)
            >>> result = thread.get()

            Args:
                training_application (str):

            Keyword Args:
                region (str): [optional]
                x_fields (str): An optional fields mask. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Storage
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['training_application'] = \
                training_application
            return self.call_with_http_info(**kwargs)

        self.get_training_application_storage = _Endpoint(
            settings={
                'response_type': (Storage,),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/training-applications/{training_application}/$storage',
                'operation_id': 'get_training_application_storage',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'training_application',
                    'region',
                    'x_fields',
                ],
                'required': [
                    'training_application',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'training_application':
                        (str,),
                    'region':
                        (str,),
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'training_application': 'training_application',
                    'region': 'region',
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'training_application': 'path',
                    'region': 'query',
                    'x_fields': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_training_application_storage
        )

        def __get_training_applications(
            self,
            **kwargs
        ):
            """get_training_applications  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_training_applications(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_fields (str): An optional fields mask. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [TrainingApplication]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_training_applications = _Endpoint(
            settings={
                'response_type': ([TrainingApplication],),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/training-applications',
                'operation_id': 'get_training_applications',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_fields',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'x_fields': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_training_applications
        )
