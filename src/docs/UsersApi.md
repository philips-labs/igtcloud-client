# igtcloud.client.services.entities.UsersApi

All URIs are relative to */data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_resource**](UsersApi.md#delete_user_resource) | **DELETE** /users/{user_uuid} | 
[**get_me_resource**](UsersApi.md#get_me_resource) | **GET** /users/me | 
[**get_user_resource**](UsersApi.md#get_user_resource) | **GET** /users/{user_uuid} | 
[**get_user_storage_resource**](UsersApi.md#get_user_storage_resource) | **GET** /users/$storage | 
[**get_users_resource**](UsersApi.md#get_users_resource) | **GET** /users | 
[**post_resend_activation_resource**](UsersApi.md#post_resend_activation_resource) | **POST** /users/$resend-activation | 
[**post_reset_mfa_resource**](UsersApi.md#post_reset_mfa_resource) | **POST** /users/$mfa-reset | 
[**post_user_profile_resource**](UsersApi.md#post_user_profile_resource) | **POST** /users/$profile | 
[**post_users_resource**](UsersApi.md#post_users_resource) | **POST** /users | 
[**put_user_resource**](UsersApi.md#put_user_resource) | **PUT** /users/{user_uuid} | 


# **delete_user_resource**
> delete_user_resource(user_uuid)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_uuid = "user_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user_resource(user_uuid)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->delete_user_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  |

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

# **get_me_resource**
> UserInfoModel get_me_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_info_model import UserInfoModel
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
    api_instance = users_api.UsersApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_me_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->get_me_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**UserInfoModel**](UserInfoModel.md)

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

# **get_user_resource**
> UserInfoModel get_user_resource(user_uuid)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_info_model import UserInfoModel
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
    api_instance = users_api.UsersApi(api_client)
    user_uuid = "user_uuid_example" # str | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_resource(user_uuid)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->get_user_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_resource(user_uuid, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->get_user_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**UserInfoModel**](UserInfoModel.md)

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

# **get_user_storage_resource**
> StorageModel get_user_storage_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    region = "region_example" # str |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_storage_resource(region=region, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->get_user_storage_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_users_resource**
> [UserInfoModel] get_users_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_info_model import UserInfoModel
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
    api_instance = users_api.UsersApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_users_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->get_users_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**[UserInfoModel]**](UserInfoModel.md)

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

# **post_resend_activation_resource**
> UserActivationModel post_resend_activation_resource(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.user_activation_model import UserActivationModel
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_activation_create_model import UserActivationCreateModel
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
    api_instance = users_api.UsersApi(api_client)
    payload = UserActivationCreateModel(
        login_id="login_id_example",
    ) # UserActivationCreateModel | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_resend_activation_resource(payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_resend_activation_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_resend_activation_resource(payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_resend_activation_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserActivationCreateModel**](UserActivationCreateModel.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**UserActivationModel**](UserActivationModel.md)

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

# **post_reset_mfa_resource**
> Model4xxMessage post_reset_mfa_resource(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_activation_create_model import UserActivationCreateModel
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
    api_instance = users_api.UsersApi(api_client)
    payload = UserActivationCreateModel(
        login_id="login_id_example",
    ) # UserActivationCreateModel | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_reset_mfa_resource(payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_reset_mfa_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserActivationCreateModel**](UserActivationCreateModel.md)|  |

### Return type

[**Model4xxMessage**](Model4xxMessage.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No data |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_profile_resource**
> post_user_profile_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.post_user_profile_resource()
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_user_profile_resource: %s\n" % e)
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

# **post_users_resource**
> UserInfoModel post_users_resource(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.user_create_model import UserCreateModel
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.user_info_model import UserInfoModel
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
    api_instance = users_api.UsersApi(api_client)
    payload = UserCreateModel(
        name="name_example",
        family_name="family_name_example",
        email="email_example",
        mobile="mobile_example",
        login_id="login_id_example",
    ) # UserCreateModel | 
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_users_resource(payload)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_users_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_users_resource(payload, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->post_users_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserCreateModel**](UserCreateModel.md)|  |
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**UserInfoModel**](UserInfoModel.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Existing user found, onboarded |  -  |
**201** | User created and onboarded |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_resource**
> put_user_resource(user_uuid, payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):

```python
import time
import igtcloud.client.services.entities
from igtcloud.client.services.entities.api import users_api
from igtcloud.client.services.entities.model.user_create_model import UserCreateModel
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
    api_instance = users_api.UsersApi(api_client)
    user_uuid = "user_uuid_example" # str | 
    payload = UserCreateModel(
        name="name_example",
        family_name="family_name_example",
        email="email_example",
        mobile="mobile_example",
        login_id="login_id_example",
    ) # UserCreateModel | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.put_user_resource(user_uuid, payload)
    except igtcloud.client.services.entities.ApiException as e:
        print("Exception when calling UsersApi->put_user_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**|  |
 **payload** | [**UserCreateModel**](UserCreateModel.md)|  |

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

