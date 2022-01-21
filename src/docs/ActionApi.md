# igtcloud.client.services.action.ActionApi

All URIs are relative to */action*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_preprocess_file**](ActionApi.md#post_preprocess_file) | **POST** /preprocess-file | 
[**post_update_database**](ActionApi.md#post_update_database) | **POST** /update-database | 


# **post_preprocess_file**
> post_preprocess_file(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.action
from igtcloud.client.services.action.api import action_api
from igtcloud.client.services.action.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.action.model.preprocessing_request import PreprocessingRequest
from pprint import pprint
# Defining the host is optional and defaults to /action
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.action.Configuration(
    host = "/action"
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
with igtcloud.client.services.action.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = action_api.ActionApi(api_client)
    payload = PreprocessingRequest(
        uploaded_path="uploaded_path_example",
        hospital_id="hospital_id_example",
        patient_id="patient_id_example",
        study_id="study_id_example",
    ) # PreprocessingRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_preprocess_file(payload)
    except igtcloud.client.services.action.ApiException as e:
        print("Exception when calling ActionApi->post_preprocess_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PreprocessingRequest**](PreprocessingRequest.md)|  |

### Return type

void (empty response body)

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update_database**
> post_update_database(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.action
from igtcloud.client.services.action.api import action_api
from igtcloud.client.services.action.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.action.model.update_database_request import UpdateDatabaseRequest
from pprint import pprint
# Defining the host is optional and defaults to /action
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.action.Configuration(
    host = "/action"
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
with igtcloud.client.services.action.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = action_api.ActionApi(api_client)
    payload = UpdateDatabaseRequest(
        uploaded_path="uploaded_path_example",
        hospital_id="hospital_id_example",
    ) # UpdateDatabaseRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_update_database(payload)
    except igtcloud.client.services.action.ApiException as e:
        print("Exception when calling ActionApi->post_update_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateDatabaseRequest**](UpdateDatabaseRequest.md)|  |

### Return type

void (empty response body)

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

