# igtcloud.client.services.entities.ApplicationsApi

All URIs are relative to */data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_applications_resource**](ApplicationsApi.md#get_applications_resource) | **GET** /applications | 
[**get_training_application_guide_resource**](ApplicationsApi.md#get_training_application_guide_resource) | **GET** /training-applications/{training_application}/guide | 
[**get_training_application_storage_resource**](ApplicationsApi.md#get_training_application_storage_resource) | **GET** /training-applications/{training_application}/$storage | 
[**get_training_applications_resource**](ApplicationsApi.md#get_training_applications_resource) | **GET** /training-applications | 


# **get_applications_resource**
> ApplicationsResponse get_applications_resource(project_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.applications_response import ApplicationsResponse
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
    api_instance = applications_api.ApplicationsApi(api_client)
    project_id = "projectId_example" # str | 
    application = "application_example" # str |  (optional)
    format = "format_example" # str |  (optional)
    vm_environment = "vmEnvironment_example" # str |  (optional)
    does_open_on_study = True # bool |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_applications_resource(project_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_applications_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_applications_resource(project_id, application=application, format=format, vm_environment=vm_environment, does_open_on_study=does_open_on_study, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_applications_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **application** | **str**|  | [optional]
 **format** | **str**|  | [optional]
 **vm_environment** | **str**|  | [optional]
 **does_open_on_study** | **bool**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**ApplicationsResponse**](ApplicationsResponse.md)

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

# **get_training_application_guide_resource**
> get_training_application_guide_resource(training_application)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    training_application = "training_application_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_training_application_guide_resource(training_application)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_guide_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_application** | **str**|  |

### Return type

void (empty response body)

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

# **get_training_application_storage_resource**
> StorageModel get_training_application_storage_resource(training_application)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.storage_model import StorageModel
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
    api_instance = applications_api.ApplicationsApi(api_client)
    training_application = "training_application_example" # str | 
    region = "region_example" # str |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_training_application_storage_resource(training_application)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_storage_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_training_application_storage_resource(training_application, region=region, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_application_storage_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_application** | **str**|  |
 **region** | **str**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**StorageModel**](StorageModel.md)

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

# **get_training_applications_resource**
> TrainingApplicationsResponse get_training_applications_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import applications_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.training_applications_response import TrainingApplicationsResponse
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_training_applications_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling ApplicationsApi->get_training_applications_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**TrainingApplicationsResponse**](TrainingApplicationsResponse.md)

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

