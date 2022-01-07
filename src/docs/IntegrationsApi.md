# igtcloud.client.services.entities.IntegrationsApi

All URIs are relative to */data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_suite_collections_resource**](IntegrationsApi.md#get_ai_suite_collections_resource) | **GET** /integrations/aisuite/{connection_name}/projects/{aisuite_project_id} | 
[**get_ai_suite_connections_resource**](IntegrationsApi.md#get_ai_suite_connections_resource) | **GET** /integrations/aisuite | 
[**get_ai_suite_projects_resource**](IntegrationsApi.md#get_ai_suite_projects_resource) | **GET** /integrations/aisuite/{connection_name}/projects | 
[**post_ai_suite_collections_resource**](IntegrationsApi.md#post_ai_suite_collections_resource) | **POST** /integrations/aisuite/{connection_name}/projects/{aisuite_project_id} | 


# **get_ai_suite_collections_resource**
> [AISuiteCollection] get_ai_suite_collections_resource(connection_name, aisuite_project_id)



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
# Defining the host is optional and defaults to /data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "/data"
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
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_suite_collections_resource(connection_name, aisuite_project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_collections_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_collections_resource(connection_name, aisuite_project_id, project_id=project_id, institute_id=institute_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_collections_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **aisuite_project_id** | **str**| AI Suite project id or reference |
 **project_id** | **str**| IGTCloud project | [optional]
 **institute_id** | **str**| IGTCloud institute | [optional]
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

# **get_ai_suite_connections_resource**
> [AISuiteConnection] get_ai_suite_connections_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import integrations_api
from igtcloud.client.services.entities.model.ai_suite_connection import AISuiteConnection
from pprint import pprint
# Defining the host is optional and defaults to /data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "/data"
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
        api_response = api_instance.get_ai_suite_connections_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_connections_resource: %s\n" % e)
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

# **get_ai_suite_projects_resource**
> [AISuiteProject] get_ai_suite_projects_resource(connection_name)



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
# Defining the host is optional and defaults to /data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "/data"
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
        api_response = api_instance.get_ai_suite_projects_resource(connection_name)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_projects_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_suite_projects_resource(connection_name, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->get_ai_suite_projects_resource: %s\n" % e)
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

# **post_ai_suite_collections_resource**
> AISuiteCollection post_ai_suite_collections_resource(connection_name, aisuite_project_id)



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
# Defining the host is optional and defaults to /data
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.entities.Configuration(
    host = "/data"
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
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_ai_suite_collections_resource(connection_name, aisuite_project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_collections_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_ai_suite_collections_resource(connection_name, aisuite_project_id, project_id=project_id, institute_id=institute_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling IntegrationsApi->post_ai_suite_collections_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of AI Suite connection |
 **aisuite_project_id** | **str**| AI Suite project id or reference |
 **project_id** | **str**| IGTCloud project | [optional]
 **institute_id** | **str**| IGTCloud institute | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**AISuiteCollection**](AISuiteCollection.md)

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

