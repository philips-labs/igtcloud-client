# igtcloud.client.services.entities.ApplicationsApi

All URIs are relative to *http://localhost/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_application_specific**](ApplicationsApi.md#delete_application_specific) | **DELETE** /applications/{application_id} | 
[**get_application_file_formats**](ApplicationsApi.md#get_application_file_formats) | **GET** /applications/file-formats | 
[**get_application_specific**](ApplicationsApi.md#get_application_specific) | **GET** /applications/{application_id} | 
[**get_applications**](ApplicationsApi.md#get_applications) | **GET** /applications | 
[**get_training_application_guide**](ApplicationsApi.md#get_training_application_guide) | **GET** /training-applications/{training_application}/guide | 
[**get_training_application_storage**](ApplicationsApi.md#get_training_application_storage) | **GET** /training-applications/{training_application}/$storage | 
[**get_training_applications**](ApplicationsApi.md#get_training_applications) | **GET** /training-applications | 
[**post_applications**](ApplicationsApi.md#post_applications) | **POST** /applications | 
[**put_application_specific**](ApplicationsApi.md#put_application_specific) | **PUT** /applications/{application_id} | 


# **delete_application_specific**
> delete_application_specific(application_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_application_specific(application_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->delete_application_specific: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  |

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
**204** | No Content |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_file_formats**
> get_application_file_formats()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_application_file_formats()
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_file_formats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_application_specific**
> Application get_application_specific(application_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = 1 # int | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_specific(application_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_specific: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_application_specific(application_id, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_specific: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Application**](Application.md)

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

# **get_applications**
> [Application] get_applications()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    enabled = True # bool |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_applications(enabled=enabled, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[Application]**](Application.md)

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

# **get_training_application_guide**
> file_type get_training_application_guide(training_application)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    training_application = "training_application_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_training_application_guide(training_application)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_guide: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_application** | **str**|  |

### Return type

**file_type**

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_application_storage**
> Storage get_training_application_storage(training_application)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.storage import Storage
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
    api_instance = applications_api.ApplicationsApi(api_client)
    training_application = "training_application_example" # str | 
    region = "region_example" # str |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_training_application_storage(training_application)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_storage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_training_application_storage(training_application, region=region, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_application** | **str**|  |
 **region** | **str**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Storage**](Storage.md)

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

# **get_training_applications**
> [TrainingApplication] get_training_applications()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.training_application import TrainingApplication
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_training_applications(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[TrainingApplication]**](TrainingApplication.md)

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

# **post_applications**
> Application post_applications(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.application import Application
from igtcloud.client.services.entities.model.inline_object import InlineObject
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
    api_instance = applications_api.ApplicationsApi(api_client)
    payload = InlineObject(
        app_id="app_id_example",
        name="name_example",
        supported_formats="supported_formats_example",
        vm_environment="vm_environment_example",
        default_in_project_types="default_in_project_types_example",
        enabled=True,
    ) # InlineObject | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_applications(payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->post_applications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_applications(payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->post_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**InlineObject**](InlineObject.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Application**](Application.md)

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

# **put_application_specific**
> Application put_application_specific(application_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.inline_object1 import InlineObject1
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = 1 # int | 
    payload = InlineObject1(
        app_id="app_id_example",
        name="name_example",
        supported_formats="supported_formats_example",
        vm_environment="vm_environment_example",
        default_in_project_types="default_in_project_types_example",
        enabled=True,
    ) # InlineObject1 | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_application_specific(application_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->put_application_specific: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.put_application_specific(application_id, payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->put_application_specific: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  |
 **payload** | [**InlineObject1**](InlineObject1.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**Application**](Application.md)

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

