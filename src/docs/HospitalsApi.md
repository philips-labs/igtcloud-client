# igtcloud.client.services.entities.HospitalsApi

All URIs are relative to */data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_study_files_resource**](HospitalsApi.md#delete_study_files_resource) | **DELETE** /hospitals/{hospital_id}/studies/{study_id}/files | 
[**delete_study_resource**](HospitalsApi.md#delete_study_resource) | **DELETE** /hospitals/{hospital_id}/studies/{study_id} | 
[**delete_study_series_resource**](HospitalsApi.md#delete_study_series_resource) | **DELETE** /hospitals/{hospital_id}/studies/{study_id}/series/{series_id} | 
[**get_all_hospitals_resource**](HospitalsApi.md#get_all_hospitals_resource) | **GET** /hospitals | 
[**get_series_list_resource**](HospitalsApi.md#get_series_list_resource) | **GET** /hospitals/{hospital_id}/series | 
[**get_series_preview_resource**](HospitalsApi.md#get_series_preview_resource) | **GET** /hospitals/{hospital_id}/series/{series_id}/{file_name} | 
[**get_series_resource**](HospitalsApi.md#get_series_resource) | **GET** /hospitals/{hospital_id}/series/{series_id} | 
[**get_studies_resource**](HospitalsApi.md#get_studies_resource) | **GET** /hospitals/{hospital_id}/studies | 
[**get_study_download_file_resource**](HospitalsApi.md#get_study_download_file_resource) | **GET** /hospitals/{hospital_id}/studies/{study_id}/download-files | 
[**get_study_files_resource**](HospitalsApi.md#get_study_files_resource) | **GET** /hospitals/{hospital_id}/studies/{study_id}/files | 
[**get_study_resource**](HospitalsApi.md#get_study_resource) | **GET** /hospitals/{hospital_id}/studies/{study_id} | 
[**get_study_series_list_resource**](HospitalsApi.md#get_study_series_list_resource) | **GET** /hospitals/{hospital_id}/studies/{study_id}/series | 
[**patch_study_resource**](HospitalsApi.md#patch_study_resource) | **PATCH** /hospitals/{hospital_id}/studies/{study_id} | 
[**post_studies_resource**](HospitalsApi.md#post_studies_resource) | **POST** /hospitals/{hospital_id}/studies | 
[**post_study_annotation_state_resource**](HospitalsApi.md#post_study_annotation_state_resource) | **POST** /hospitals/{hospital_id}/studies/{study_id}/annotation-state | 
[**post_study_download_link_resource**](HospitalsApi.md#post_study_download_link_resource) | **POST** /hospitals/{hospital_id}/studies/{study_id}/download-link | 
[**post_study_electronic_record_state_resource**](HospitalsApi.md#post_study_electronic_record_state_resource) | **POST** /hospitals/{hospital_id}/studies/{study_id}/electronic-record-state | 
[**post_study_files_resource**](HospitalsApi.md#post_study_files_resource) | **POST** /hospitals/{hospital_id}/studies/{study_id}/files | This create study files endpoint actually only stores the file size of a study_id + key combination
[**put_study_resource**](HospitalsApi.md#put_study_resource) | **PUT** /hospitals/{hospital_id}/studies/{study_id} | 
[**put_study_series_resource**](HospitalsApi.md#put_study_series_resource) | **PUT** /hospitals/{hospital_id}/studies/{study_id}/series/{series_id} | 


# **delete_study_files_resource**
> delete_study_files_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_files_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->delete_study_files_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **delete_study_resource**
> delete_study_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->delete_study_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **delete_study_series_resource**
> delete_study_series_resource(hospital_id, study_id, series_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    series_id = "series_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_series_resource(hospital_id, study_id, series_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->delete_study_series_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **series_id** | **str**|  |

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

# **get_all_hospitals_resource**
> HospitalsResponse get_all_hospitals_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.hospitals_response import HospitalsResponse
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_hospitals_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_all_hospitals_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**HospitalsResponse**](HospitalsResponse.md)

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

# **get_series_list_resource**
> get_series_list_resource(hospital_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_series_list_resource(hospital_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_series_list_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_series_list_resource(hospital_id, filter=filter)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_series_list_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **filter** | **str**|  | [optional]

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

# **get_series_preview_resource**
> get_series_preview_resource(hospital_id, series_id, file_name)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    series_id = "series_id_example" # str | 
    file_name = "file_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_series_preview_resource(hospital_id, series_id, file_name)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_series_preview_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **series_id** | **str**|  |
 **file_name** | **str**|  |

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

# **get_series_resource**
> get_series_resource(hospital_id, series_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    series_id = "series_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_series_resource(hospital_id, series_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_series_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **series_id** | **str**|  |

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

# **get_studies_resource**
> get_studies_resource(hospital_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_studies_resource(hospital_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_studies_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_studies_resource(hospital_id, filter=filter)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_studies_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **filter** | **str**|  | [optional]

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

# **get_study_download_file_resource**
> get_study_download_file_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_study_download_file_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_download_file_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **get_study_files_resource**
> FilesResponse get_study_files_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.files_response import FilesResponse
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    auxiliary = False # bool |  (optional) if omitted the server will use the default value of False
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_study_files_resource(hospital_id, study_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_files_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_study_files_resource(hospital_id, study_id, auxiliary=auxiliary, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_files_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **auxiliary** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**FilesResponse**](FilesResponse.md)

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

# **get_study_resource**
> get_study_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_study_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **get_study_series_list_resource**
> get_study_series_list_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_study_series_list_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_series_list_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_study_series_list_resource(hospital_id, study_id, filter=filter)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->get_study_series_list_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **filter** | **str**|  | [optional]

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

# **patch_study_resource**
> patch_study_resource(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.patch_study_resource(hospital_id, study_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->patch_study_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_studies_resource**
> post_studies_resource(hospital_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    payload = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_studies_resource(hospital_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->post_studies_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **payload** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_annotation_state_resource**
> post_study_annotation_state_resource(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.annotation_state_model import AnnotationStateModel
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = AnnotationStateModel(
        annotation_state="annotation_state_example",
    ) # AnnotationStateModel | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_study_annotation_state_resource(hospital_id, study_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->post_study_annotation_state_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**AnnotationStateModel**](AnnotationStateModel.md)|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_download_link_resource**
> post_study_download_link_resource(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_study_download_link_resource(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->post_study_download_link_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **post_study_electronic_record_state_resource**
> post_study_electronic_record_state_resource(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.electronic_record_state_model import ElectronicRecordStateModel
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = ElectronicRecordStateModel(
        username="username_example",
        password="password_example",
        electronic_record_state="electronic_record_state_example",
    ) # ElectronicRecordStateModel | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_study_electronic_record_state_resource(hospital_id, study_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->post_study_electronic_record_state_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**ElectronicRecordStateModel**](ElectronicRecordStateModel.md)|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_files_resource**
> FilesResponse post_study_files_resource(hospital_id, study_id, payload)

This create study files endpoint actually only stores the file size of a study_id + key combination

Used only for retrieving progress percentage of uploads.

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.file_sizes_model import FileSizesModel
from igtcloud.client.services.entities.model.files_response import FilesResponse
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = FileSizesModel(
        file_sizes=[
            FileSizeModel(
                key="key_example",
                file_size=1,
            ),
        ],
    ) # FileSizesModel | 

    # example passing only required values which don't have defaults set
    try:
        # This create study files endpoint actually only stores the file size of a study_id + key combination
        api_response = api_instance.post_study_files_resource(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->post_study_files_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**FileSizesModel**](FileSizesModel.md)|  |

### Return type

[**FilesResponse**](FilesResponse.md)

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

# **put_study_resource**
> put_study_resource(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.put_study_resource(hospital_id, study_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->put_study_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_study_series_resource**
> put_study_series_resource(hospital_id, study_id, series_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import hospitals_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.series_create_model import SeriesCreateModel
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
    api_instance = hospitals_api.HospitalsApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    series_id = "series_id_example" # str | 
    payload = SeriesCreateModel(
        series_database_id="series_database_id_example",
        instance_uid="instance_uid_example",
        modality="modality_example",
        preview_url="preview_url_example",
        procedure_database_id="procedure_database_id_example",
        s3_prefix="s3_prefix_example",
        series_format="series_format_example",
        related_study_instance_uid="related_study_instance_uid_example",
        related_series_instance_uid="related_series_instance_uid_example",
        document_title="document_title_example",
        display_name="display_name_example",
    ) # SeriesCreateModel | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.put_study_series_resource(hospital_id, study_id, series_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling HospitalsApi->put_study_series_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **series_id** | **str**|  |
 **payload** | [**SeriesCreateModel**](SeriesCreateModel.md)|  |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

