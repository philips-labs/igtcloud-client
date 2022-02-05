# igtcloud.client.services.entities.ProjectsApi

All URIs are relative to */data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_files**](ProjectsApi.md#delete_project_files) | **DELETE** /projects/{project_id}/files | 
[**get_institute**](ProjectsApi.md#get_institute) | **GET** /projects/hospitals/{hospital_id} | 
[**get_institutes**](ProjectsApi.md#get_institutes) | **GET** /projects/{project_id}/hospitals | 
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{project_id} | 
[**get_project_download_file**](ProjectsApi.md#get_project_download_file) | **GET** /projects/{project_id}/download-files | 
[**get_project_files**](ProjectsApi.md#get_project_files) | **GET** /projects/{project_id}/files | 
[**get_project_types**](ProjectsApi.md#get_project_types) | **GET** /project-types | 
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | 
[**post_institutes**](ProjectsApi.md#post_institutes) | **POST** /projects/{project_id}/hospitals | 
[**post_project_files**](ProjectsApi.md#post_project_files) | **POST** /projects/{project_id}/files | This create project files endpoint actually only stores the file size of a project_id + key combination
[**post_projects**](ProjectsApi.md#post_projects) | **POST** /projects | 


# **delete_project_files**
> delete_project_files(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    keys = [
        "[]",
    ] # [str] |  (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_project_files(project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_project_files(project_id, keys=keys)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **keys** | **[str]**|  | [optional] if omitted the server will use the default value of []

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
**204** | No Data |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institute**
> Institute get_institute(hospital_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.institute import Institute
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_institute(hospital_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_institute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_institute(hospital_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_institute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Institute**](Institute.md)

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

# **get_institutes**
> [Institute] get_institutes(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.institute import Institute
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_institutes(project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_institutes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_institutes(project_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_institutes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[Institute]**](Institute.md)

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

# **get_project**
> Project get_project(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.project import Project
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    include_child_relations = False # bool |  (optional) if omitted the server will use the default value of False
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_project(project_id, include_child_relations=include_child_relations, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **include_child_relations** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Project**](Project.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_download_file**
> file_type get_project_download_file(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_project_download_file(project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

**file_type**

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_files**
> Files get_project_files(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.files import Files
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_project_files(project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_project_files(project_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Files**](Files.md)

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

# **get_project_types**
> [str] get_project_types()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_project_types()
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project types |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> [Project] get_projects()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.project import Project
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_projects(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[Project]**](Project.md)

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

# **post_institutes**
> Institute post_institutes(project_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.institute import Institute
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    payload = Institute(
        name="name_example",
        description="description_example",
    ) # Institute | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_institutes(project_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_institutes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_institutes(project_id, payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_institutes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **payload** | [**Institute**](Institute.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Institute**](Institute.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_files**
> Files post_project_files(project_id, payload)

This create project files endpoint actually only stores the file size of a project_id + key combination

Used only for retrieving progress percentage of uploads.

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.files import Files
from igtcloud.client.services.entities.model.file import File
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_id = "project_id_example" # str | 
    payload = [
        File(
            key="key_example",
            file_size=1,
        ),
    ] # [File] | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        # This create project files endpoint actually only stores the file size of a project_id + key combination
        api_response = api_instance.post_project_files(project_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_project_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # This create project files endpoint actually only stores the file size of a project_id + key combination
        api_response = api_instance.post_project_files(project_id, payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_project_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **payload** | [**[File]**](File.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Files**](Files.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_projects**
> [Project] post_projects(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import projects_api
from igtcloud.client.services.entities.model.project import Project
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
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
    api_instance = projects_api.ProjectsApi(api_client)
    payload = Project(
        name="name_example",
        description="description_example",
        project_type_name="project_type_name_example",
        continents=[
            "continents_example",
        ],
    ) # Project | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_projects(payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_projects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_projects(payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ProjectsApi->post_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Project**](Project.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[Project]**](Project.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

