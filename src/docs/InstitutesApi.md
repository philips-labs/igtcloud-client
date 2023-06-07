# igtcloud.client.services.entities.InstitutesApi

All URIs are relative to *http://localhost/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_study**](InstitutesApi.md#delete_study) | **DELETE** /hospitals/{hospital_id}/studies/{study_id} | 
[**delete_study_annotations**](InstitutesApi.md#delete_study_annotations) | **DELETE** /hospitals/{hospital_id}/studies/{study_id}/annotations | 
[**delete_study_files**](InstitutesApi.md#delete_study_files) | **DELETE** /hospitals/{hospital_id}/studies/{study_id}/files | 
[**delete_study_series**](InstitutesApi.md#delete_study_series) | **DELETE** /hospitals/{hospital_id}/studies/{study_id}/series/{series_id} | 
[**get_all_institutes**](InstitutesApi.md#get_all_institutes) | **GET** /hospitals | 
[**get_series**](InstitutesApi.md#get_series) | **GET** /hospitals/{hospital_id}/series/{series_id} | 
[**get_series_list**](InstitutesApi.md#get_series_list) | **GET** /hospitals/{hospital_id}/series | 
[**get_series_preview**](InstitutesApi.md#get_series_preview) | **GET** /hospitals/{hospital_id}/series/{series_id}/{file_name} | 
[**get_studies**](InstitutesApi.md#get_studies) | **GET** /hospitals/{hospital_id}/studies | 
[**get_study**](InstitutesApi.md#get_study) | **GET** /hospitals/{hospital_id}/studies/{study_id} | 
[**get_study_download_file**](InstitutesApi.md#get_study_download_file) | **GET** /hospitals/{hospital_id}/studies/{study_id}/download-files | 
[**get_study_files**](InstitutesApi.md#get_study_files) | **GET** /hospitals/{hospital_id}/studies/{study_id}/files | 
[**get_study_series_list**](InstitutesApi.md#get_study_series_list) | **GET** /hospitals/{hospital_id}/studies/{study_id}/series | 
[**patch_study**](InstitutesApi.md#patch_study) | **PATCH** /hospitals/{hospital_id}/studies/{study_id} | 
[**post_studies**](InstitutesApi.md#post_studies) | **POST** /hospitals/{hospital_id}/studies | 
[**post_study_annotation_state**](InstitutesApi.md#post_study_annotation_state) | **POST** /hospitals/{hospital_id}/studies/{study_id}/annotation-state | 
[**post_study_annotations_updated**](InstitutesApi.md#post_study_annotations_updated) | **POST** /hospitals/{hospital_id}/studies/{study_id}/annotations_updated | 
[**post_study_case_labels**](InstitutesApi.md#post_study_case_labels) | **POST** /hospitals/{hospital_id}/studies/{study_id}/case-labels | 
[**post_study_comments**](InstitutesApi.md#post_study_comments) | **POST** /hospitals/{hospital_id}/studies/{study_id}/study_comments | 
[**post_study_download_link**](InstitutesApi.md#post_study_download_link) | **POST** /hospitals/{hospital_id}/studies/{study_id}/download-link | 
[**post_study_electronic_record_state**](InstitutesApi.md#post_study_electronic_record_state) | **POST** /hospitals/{hospital_id}/studies/{study_id}/electronic-record-state | 
[**post_study_files**](InstitutesApi.md#post_study_files) | **POST** /hospitals/{hospital_id}/studies/{study_id}/files | This create study files endpoint actually only stores the file size of a study_id + key combination
[**post_study_files_upload_completed**](InstitutesApi.md#post_study_files_upload_completed) | **POST** /hospitals/{hospital_id}/studies/{study_id}/files/$file-upload-completed | Initiates a background job and should be invoked with a token that is valid for at least 10 minutes
[**put_study**](InstitutesApi.md#put_study) | **PUT** /hospitals/{hospital_id}/studies/{study_id} | 
[**put_study_series**](InstitutesApi.md#put_study_series) | **PUT** /hospitals/{hospital_id}/studies/{study_id}/series/{series_id} | 
[**put_study_sticky_note**](InstitutesApi.md#put_study_sticky_note) | **PUT** /hospitals/{hospital_id}/studies/{study_id}/sticky-note | 


# **delete_study**
> delete_study(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->delete_study: %s\n" % e)
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
**204** | Study Deleted |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_study_annotations**
> delete_study_annotations(hospital_id, study_id, patient_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    patient_id = "patientId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_annotations(hospital_id, study_id, patient_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->delete_study_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **patient_id** | **str**|  |

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
**204** | Annotations deleted |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_study_files**
> delete_study_files(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    keys = [
        "[]",
    ] # [str] |  (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_files(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->delete_study_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_study_files(hospital_id, study_id, keys=keys)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->delete_study_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
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
**204** | No Content |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_study_series**
> delete_study_series(hospital_id, study_id, series_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    series_id = "series_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_study_series(hospital_id, study_id, series_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->delete_study_series: %s\n" % e)
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
**204** | No content |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_institutes**
> [Institute] get_all_institutes()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.institute import Institute
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
    api_instance = institutes_api.InstitutesApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_institutes(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_all_institutes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_series**
> Series get_series(hospital_id, series_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.series import Series
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    series_id = "series_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_series(hospital_id, series_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_series: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **series_id** | **str**|  |

### Return type

[**Series**](Series.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_list**
> [Series] get_series_list(hospital_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.series import Series
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_series_list(hospital_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_series_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_series_list(hospital_id, filter=filter)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_series_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **filter** | **str**|  | [optional]

### Return type

[**[Series]**](Series.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_preview**
> file_type get_series_preview(hospital_id, series_id, file_name)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    series_id = "series_id_example" # str | 
    file_name = "file_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_series_preview(hospital_id, series_id, file_name)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_series_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **series_id** | **str**|  |
 **file_name** | **str**|  |

### Return type

**file_type**

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpg


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studies**
> [RootStudy] get_studies(hospital_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_studies(hospital_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_studies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_studies(hospital_id, filter=filter)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_studies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **filter** | **str**|  | [optional]

### Return type

[**[RootStudy]**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study**
> RootStudy get_study(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_study(hospital_id, study_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_download_file**
> file_type get_study_download_file(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_study_download_file(hospital_id, study_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study_download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |

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

# **get_study_files**
> Files get_study_files(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.files import Files
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    auxiliary = "false" # str |  (optional) if omitted the server will use the default value of "false"
    completed = False # bool |  (optional) if omitted the server will use the default value of False
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_study_files(hospital_id, study_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_study_files(hospital_id, study_id, auxiliary=auxiliary, completed=completed, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **auxiliary** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **completed** | **bool**|  | [optional] if omitted the server will use the default value of False
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

# **get_study_series_list**
> [Series] get_study_series_list(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.series import Series
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    filter = "$filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_study_series_list(hospital_id, study_id)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study_series_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_study_series_list(hospital_id, study_id, filter=filter)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->get_study_series_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **filter** | **str**|  | [optional]

### Return type

[**[Series]**](Series.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_study**
> RootStudy patch_study(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = RootStudy() # RootStudy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_study(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->patch_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**RootStudy**](RootStudy.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_studies**
> RootStudy post_studies(hospital_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    payload = RootStudy() # RootStudy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_studies(hospital_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_studies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **payload** | [**RootStudy**](RootStudy.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_annotation_state**
> RootStudy post_study_annotation_state(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model.annotation_state import AnnotationState
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = AnnotationState(
        annotation_state="annotation_state_example",
    ) # AnnotationState | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_study_annotation_state(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_annotation_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**AnnotationState**](AnnotationState.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_annotations_updated**
> RootStudy post_study_annotations_updated(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model.latest_annotations import LatestAnnotations
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = LatestAnnotations(
        latest_annotations=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # LatestAnnotations | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_study_annotations_updated(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_annotations_updated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**LatestAnnotations**](LatestAnnotations.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_case_labels**
> RootStudy post_study_case_labels(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model.case_label import CaseLabel
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = CaseLabel(
        case_labels=[
            "case_labels_example",
        ],
    ) # CaseLabel | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_study_case_labels(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_case_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**CaseLabel**](CaseLabel.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_comments**
> RootStudy post_study_comments(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.study_comments import StudyComments
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = StudyComments(
        study_comments="study_comments_example",
    ) # StudyComments | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_study_comments(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**StudyComments**](StudyComments.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_download_link**
> post_study_download_link(hospital_id, study_id)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_study_download_link(hospital_id, study_id)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_download_link: %s\n" % e)
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
**202** | Accepted |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_electronic_record_state**
> RootStudy post_study_electronic_record_state(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.electronic_record_state import ElectronicRecordState
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = ElectronicRecordState(
        username="username_example",
        password="password_example",
        electronic_record_state="electronic_record_state_example",
    ) # ElectronicRecordState | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_study_electronic_record_state(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_electronic_record_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**ElectronicRecordState**](ElectronicRecordState.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_study_files**
> Files post_study_files(hospital_id, study_id, payload)

This create study files endpoint actually only stores the file size of a study_id + key combination

Used only for retrieving progress percentage of uploads.

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.files import Files
from igtcloud.client.services.entities.model.file import File
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = [
        File(
            key="key_example",
            file_size=1,
        ),
    ] # [File] | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        # This create study files endpoint actually only stores the file size of a study_id + key combination
        api_response = api_instance.post_study_files(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # This create study files endpoint actually only stores the file size of a study_id + key combination
        api_response = api_instance.post_study_files(hospital_id, study_id, payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
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

# **post_study_files_upload_completed**
> post_study_files_upload_completed(hospital_id, study_id, payload)

Initiates a background job and should be invoked with a token that is valid for at least 10 minutes

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.file_upload_completed import FileUploadCompleted
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = FileUploadCompleted(
        uploaded_path="uploaded_path_example",
        trigger_action=False,
    ) # FileUploadCompleted | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates a background job and should be invoked with a token that is valid for at least 10 minutes
        api_instance.post_study_files_upload_completed(hospital_id, study_id, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->post_study_files_upload_completed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**FileUploadCompleted**](FileUploadCompleted.md)|  |

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
**204** | No Content |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_study**
> RootStudy put_study(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = RootStudy() # RootStudy | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_study(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->put_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**RootStudy**](RootStudy.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_study_series**
> Series put_study_series(hospital_id, study_id, series_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.series import Series
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    series_id = "series_id_example" # str | 
    payload = Series() # Series | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_study_series(hospital_id, study_id, series_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->put_study_series: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **series_id** | **str**|  |
 **payload** | [**Series**](Series.md)|  |

### Return type

[**Series**](Series.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_study_sticky_note**
> RootStudy put_study_sticky_note(hospital_id, study_id, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import institutes_api
from igtcloud.client.services.entities.model.study_sticky_note import StudyStickyNote
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.root_study import RootStudy
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
    api_instance = institutes_api.InstitutesApi(api_client)
    hospital_id = "hospital_id_example" # str | 
    study_id = "study_id_example" # str | 
    payload = StudyStickyNote(
        has_sticky_note=False,
    ) # StudyStickyNote | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.put_study_sticky_note(hospital_id, study_id, payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling InstitutesApi->put_study_sticky_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hospital_id** | **str**|  |
 **study_id** | **str**|  |
 **payload** | [**StudyStickyNote**](StudyStickyNote.md)|  |

### Return type

[**RootStudy**](RootStudy.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

