# igtcloud.client.services.auth.AuthApi

All URIs are relative to *http://localhost/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_introspect_resource**](AuthApi.md#get_introspect_resource) | **GET** /introspect | 
[**get_login_aud_resource**](AuthApi.md#get_login_aud_resource) | **GET** /login/$aud | Retrieve &#39;aud&#39; property used for assertion login
[**get_permissions_resource**](AuthApi.md#get_permissions_resource) | **GET** /permissions | Gets a list of permissions
[**get_s3_credentials_resource**](AuthApi.md#get_s3_credentials_resource) | **GET** /s3credentials | 
[**post_audit_resource**](AuthApi.md#post_audit_resource) | **POST** /audit-trail | 
[**post_login_resource_login**](AuthApi.md#post_login_resource_login) | **POST** /login | Authorize by using your IAM credentials
[**post_logout_resource**](AuthApi.md#post_logout_resource) | **POST** /logout | 
[**post_refresh_resource**](AuthApi.md#post_refresh_resource) | **POST** /refresh | 


# **get_introspect_resource**
> IntrospectResponse get_introspect_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.auth.model.introspect_response import IntrospectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_introspect_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->get_introspect_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**IntrospectResponse**](IntrospectResponse.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_aud_resource**
> str get_login_aud_resource()

Retrieve 'aud' property used for assertion login

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve 'aud' property used for assertion login
        api_response = api_instance.get_login_aud_resource()
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->get_login_aud_resource: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **get_permissions_resource**
> PermissionsResponse get_permissions_resource()

Gets a list of permissions

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.auth.model.permissions_response import PermissionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of permissions
        api_response = api_instance.get_permissions_resource(x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->get_permissions_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

# **get_s3_credentials_resource**
> S3CredentialResponse get_s3_credentials_resource(action)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.s3_credential_response import S3CredentialResponse
from igtcloud.client.services.auth.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    action = "action_example" # str | 
    prefix = "prefix_example" # str |  (optional)
    x_fields = "X-Fields_example" # str | An optional fields mask (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_s3_credentials_resource(action)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->get_s3_credentials_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_s3_credentials_resource(action, prefix=prefix, x_fields=x_fields)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->get_s3_credentials_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  |
 **prefix** | **str**|  | [optional]
 **x_fields** | **str**| An optional fields mask | [optional]

### Return type

[**S3CredentialResponse**](S3CredentialResponse.md)

### Authorization

[csrf_token](../README.md#csrf_token), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_audit_resource**
> post_audit_resource(payload)



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.audit_trail import AuditTrail
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    payload = AuditTrail(
        event_action="event_action_example",
        event_outcome="event_outcome_example",
        event_subtype="event_subtype_example",
        event_type="event_type_example",
        application_name="application_name_example",
        application_version="application_version_example",
        component_name="component_name_example",
        arguments="arguments_example",
        object_type="object_type_example",
        object_lifecycle="object_lifecycle_example",
        environment="environment_example",
    ) # AuditTrail | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_audit_resource(payload)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->post_audit_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**AuditTrail**](AuditTrail.md)|  |

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_login_resource_login**
> LoginResponse post_login_resource_login(payload)

Authorize by using your IAM credentials

Set the grant type to 'password' for user authentication.             Set the grant type 'jwt-key' for service authentication.             Service authentication is only available for inside the hospitals in order to up/download data.

### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.login_response import LoginResponse
from igtcloud.client.services.auth.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.auth.model.login_model import LoginModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    payload = LoginModel(
        grant_type="grant_type_example",
        username="username_example",
        password="password_example",
        assertion="assertion_example",
    ) # LoginModel | 
    includes3creds = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Authorize by using your IAM credentials
        api_response = api_instance.post_login_resource_login(payload)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->post_login_resource_login: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authorize by using your IAM credentials
        api_response = api_instance.post_login_resource_login(payload, includes3creds=includes3creds)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->post_login_resource_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoginModel**](LoginModel.md)|  |
 **includes3creds** | **bool**|  | [optional]

### Return type

[**LoginResponse**](LoginResponse.md)

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

# **post_logout_resource**
> LogoutResponse post_logout_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.logout_response import LogoutResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    has_expired = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_logout_resource(has_expired=has_expired)
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->post_logout_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_expired** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**LogoutResponse**](LogoutResponse.md)

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

# **post_refresh_resource**
> LoginResponse post_refresh_resource()



### Example

* Api Key Authentication (csrf_token):
* Api Key Authentication (jwt):
```python
import time
import igtcloud.client.services.auth
from igtcloud.client.services.auth.api import auth_api
from igtcloud.client.services.auth.model.login_response import LoginResponse
from igtcloud.client.services.auth.model.model4xx_message import Model4xxMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = igtcloud.client.services.auth.Configuration(
    host = "http://localhost/auth"
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
with igtcloud.client.services.auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_refresh_resource()
        pprint(api_response)
    except igtcloud.client.services.auth.ApiException as e:
        print("Exception when calling AuthApi->post_refresh_resource: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginResponse**](LoginResponse.md)

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

