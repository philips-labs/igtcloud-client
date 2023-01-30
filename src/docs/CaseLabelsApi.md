# igtcloud.client.services.entities.CaseLabelsApi

All URIs are relative to *http://localhost/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case_labels**](CaseLabelsApi.md#get_case_labels) | **GET** /case-labels | 


# **get_case_labels**
> get_case_labels()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import case_labels_api
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
    api_instance = case_labels_api.CaseLabelsApi(api_client)
    project_id = "projectId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_case_labels(project_id=project_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling CaseLabelsApi->get_case_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [optional]

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

