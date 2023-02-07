# igtcloud.client.services.entities.IntegrationsApi

All URIs are relative to *http://localhost/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_suite_attribute_mappings**](IntegrationsApi.md#get_ai_suite_attribute_mappings) | **GET** /integrations/aisuite/mappings/attributes | 
[**get_ai_suite_collections**](IntegrationsApi.md#get_ai_suite_collections) | **GET** /integrations/aisuite/{connection_name}/collections | 
[**get_ai_suite_connections**](IntegrationsApi.md#get_ai_suite_connections) | **GET** /integrations/aisuite | 
[**get_ai_suite_file_mappings**](IntegrationsApi.md#get_ai_suite_file_mappings) | **GET** /integrations/aisuite/mappings/files | 
[**get_ai_suite_projects**](IntegrationsApi.md#get_ai_suite_projects) | **GET** /integrations/aisuite/{connection_name}/projects | 
[**get_ai_suite_sync**](IntegrationsApi.md#get_ai_suite_sync) | **GET** /integrations/aisuite/{connection_name}/projects/{aisuite_project_id} | 
[**post_ai_suite_collections**](IntegrationsApi.md#post_ai_suite_collections) | **POST** /integrations/aisuite/{connection_name}/collections | 
[**post_ai_suite_mappings**](IntegrationsApi.md#post_ai_suite_mappings) | **POST** /integrations/aisuite/mappings/$generate | 
[**post_ai_suite_sync**](IntegrationsApi.md#post_ai_suite_sync) | **POST** /integrations/aisuite/{connection_name}/projects/{aisuite_project_id} | 
[**post_ai_suite_task**](IntegrationsApi.md#post_ai_suite_task) | **POST** /integrations/aisuite/tasks/completed/{callback_token} | 


# **get_ai_suite_attribute_mappings**
> get_ai_suite_attribute_mappings()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    project_id = "projectId_example" # str | IGTCloud project (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_ai_suite_attribute_mappings(project_id=project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_attribute_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| IGTCloud project | [optional]

### Return type

void (empty response body)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_suite_collections**
> [AISuiteDatabaseCollection] get_ai_suite_collections(connection_name)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.ai_suite_database_collection import AISuiteDatabaseCollection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    connection_name = "connection_name_example" # str | Name of AI Suite connection
    igtcloud_identifier = "igtcloudIdentifier_example" # str | IGTCloud identifier (optional)
    igtcloud_identifier_type = "igtcloudIdentifierType_example" # str | IGTCloud identifier type (project / institute) (optional)
    aisuite_project_id = "aisuiteProjectId_example" # str | AI Suite project id (optional)
    aisuite_collection_id = "aisuiteCollectionId_example" # str | AI Suite collection id (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_suite_collections(connection_name)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_collections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_collections(connection_name, igtcloud_identifier=igtcloud_identifier, igtcloud_identifier_type=igtcloud_identifier_type, aisuite_project_id=aisuite_project_id, aisuite_collection_id=aisuite_collection_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **igtcloud_identifier** | **str**| IGTCloud identifier | [optional]
 **igtcloud_identifier_type** | **str**| IGTCloud identifier type (project / institute) | [optional]
 **aisuite_project_id** | **str**| AI Suite project id | [optional]
 **aisuite_collection_id** | **str**| AI Suite collection id | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[AISuiteDatabaseCollection]**](AISuiteDatabaseCollection.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_suite_connections**
> [AISuiteConnection] get_ai_suite_connections()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.ai_suite_connection import AISuiteConnection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_connections(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[AISuiteConnection]**](AISuiteConnection.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_suite_file_mappings**
> get_ai_suite_file_mappings()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    project_id = "projectId_example" # str | IGTCloud project (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_ai_suite_file_mappings(project_id=project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_file_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| IGTCloud project | [optional]

### Return type

void (empty response body)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_suite_projects**
> [AISuiteProject] get_ai_suite_projects(connection_name)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.ai_suite_project import AISuiteProject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    connection_name = "connection_name_example" # str | Name of AI Suite connection
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_suite_projects(connection_name)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_projects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_projects(connection_name, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[AISuiteProject]**](AISuiteProject.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_suite_sync**
> [AISuiteCollection] get_ai_suite_sync(connection_name, aisuite_project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.ai_suite_collection import AISuiteCollection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    connection_name = "connection_name_example" # str | Name of AI Suite connection
    aisuite_project_id = "aisuite_project_id_example" # str | AI Suite project id or reference
    project_id = "projectId_example" # str | IGTCloud project (optional)
    institute_id = "instituteId_example" # str | IGTCloud institute (optional)
    x_authorization_code = "X-AUTHORIZATION-CODE_example" # str | Authorization code (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_suite_sync(connection_name, aisuite_project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_sync: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_sync(connection_name, aisuite_project_id, project_id=project_id, institute_id=institute_id, x_authorization_code=x_authorization_code, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **aisuite_project_id** | **str**| AI Suite project id or reference |
 **project_id** | **str**| IGTCloud project | [optional]
 **institute_id** | **str**| IGTCloud institute | [optional]
 **x_authorization_code** | **str**| Authorization code | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[AISuiteCollection]**](AISuiteCollection.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_suite_collections**
> AISuiteDatabaseCollection post_ai_suite_collections(connection_name, aisuite_url, identifier, identifier_type, aisuite_collection_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.ai_suite_database_collection import AISuiteDatabaseCollection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    connection_name = "connection_name_example" # str | Name of AI Suite connection
    aisuite_url = "aisuiteUrl_example" # str | 
    identifier = "identifier_example" # str | 
    identifier_type = "identifierType_example" # str | 
    aisuite_collection_id = "aisuiteCollectionId_example" # str | 
    aisuite_project_id = "aisuiteProjectId_example" # str |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_ai_suite_collections(connection_name, aisuite_url, identifier, identifier_type, aisuite_collection_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_collections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_ai_suite_collections(connection_name, aisuite_url, identifier, identifier_type, aisuite_collection_id, aisuite_project_id=aisuite_project_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **aisuite_url** | **str**|  |
 **identifier** | **str**|  |
 **identifier_type** | **str**|  |
 **aisuite_collection_id** | **str**|  |
 **aisuite_project_id** | **str**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**AISuiteDatabaseCollection**](AISuiteDatabaseCollection.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_suite_mappings**
> post_ai_suite_mappings()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    project_id = "projectId_example" # str | IGTCloud project (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_ai_suite_mappings(project_id=project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| IGTCloud project | [optional]

### Return type

void (empty response body)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_suite_sync**
> post_ai_suite_sync(connection_name, aisuite_project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    connection_name = "connection_name_example" # str | Name of AI Suite connection
    aisuite_project_id = "aisuite_project_id_example" # str | AI Suite project id or reference
    project_id = "projectId_example" # str | IGTCloud project (optional)
    institute_id = "instituteId_example" # str | IGTCloud institute (optional)
    x_authorization_code = "X-AUTHORIZATION-CODE_example" # str | Authorization code (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_ai_suite_sync(connection_name, aisuite_project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_sync: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_ai_suite_sync(connection_name, aisuite_project_id, project_id=project_id, institute_id=institute_id, x_authorization_code=x_authorization_code)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **aisuite_project_id** | **str**| AI Suite project id or reference |
 **project_id** | **str**| IGTCloud project | [optional]
 **institute_id** | **str**| IGTCloud institute | [optional]
 **x_authorization_code** | **str**| Authorization code | [optional]

### Return type

void (empty response body)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_suite_task**
> post_ai_suite_task(callback_token, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.task_completed import TaskCompleted
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "http://localhost/data"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: csrf_token
configuration.api_key['csrf_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrf_token'] = 'Bearer'

# Configure API key authorization: jwt
configuration.api_key['jwt'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with igtcloud.client.services.entities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    callback_token = "callback_token_example" # str | 
    payload = TaskCompleted(
        status="status_example",
        message="message_example",
    ) # TaskCompleted | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_ai_suite_task(callback_token, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_token** | **str**|  |
 **payload** | [**TaskCompleted**](TaskCompleted.md)|  |

### Return type

void (empty response body)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

