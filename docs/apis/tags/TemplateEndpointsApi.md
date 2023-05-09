<a name="__pageTop"></a>
# stardust_core_sdk.apis.tags.template_endpoints_api.TemplateEndpointsApi

All URIs are relative to *https://core-api.stardust.gg/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_count_get**](#template_count_get) | **get** /template/count | Get Template Count
[**template_create_post**](#template_create_post) | **post** /template/create | Create Template
[**template_get_all_get**](#template_get_all_get) | **get** /template/get-all | Get All Templates
[**template_get_get**](#template_get_get) | **get** /template/get | Get Template
[**template_get_tokens_get**](#template_get_tokens_get) | **get** /template/get-tokens | Get Template Tokens
[**template_mutate_put**](#template_mutate_put) | **put** /template/mutate | Mutate Template
[**template_props_remove_delete**](#template_props_remove_delete) | **delete** /template/props-remove | Remove Template Property
[**template_remove_delete**](#template_remove_delete) | **delete** /template/remove | Remove Template

# **template_count_get**
<a name="template_count_get"></a>
> SDTemplateCountResponse template_count_get()

Get Template Count

Get a Template's Count Within a Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_count_response import SDTemplateCountResponse
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
    }
    try:
        # Get Template Count
        api_response = api_instance.template_count_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_count_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_count_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_count_get.ApiResponseFor500) | 500 response

#### template_count_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateCountResponse**](../../models/SDTemplateCountResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_count_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_create_post**
<a name="template_create_post"></a>
> SDTemplateCreateResponse template_create_post(sd_template_create_request)

Create Template

Adds a New Token Template that lets Players Acquire that Token using the Token/Mint Endpoint

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_create_response import SDTemplateCreateResponse
from stardust_core_sdk.model.error import Error
from stardust_core_sdk.model.sd_template_create_request import SDTemplateCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTemplateCreateRequest(
        name="name_example",
        cap="cap_example",
        contract_type="internal-mint",
        type="FT",
        owner_address="owner_address_example",
        props=dict(
            immutable=dict(),
            mutable=dict(),
        ),
        public_contract_metadata=dict(),
        symbol="symbol_example",
    )
    try:
        # Create Template
        api_response = api_instance.template_create_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_create_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateCreateRequest**](../../models/SDTemplateCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_create_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_create_post.ApiResponseFor500) | 500 response

#### template_create_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateCreateResponse**](../../models/SDTemplateCreateResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_create_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_get_all_get**
<a name="template_get_all_get"></a>
> SDTemplateGetAllResponses template_get_all_get(startlimit)

Get All Templates

Get All of the Templates Within a Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_get_all_responses import SDTemplateGetAllResponses
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'start': "start_example",
        'limit': "limit_example",
    }
    try:
        # Get All Templates
        api_response = api_instance.template_get_all_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_get_all_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'start': "start_example",
        'filter': "filter_example",
        'limit': "limit_example",
    }
    try:
        # Get All Templates
        api_response = api_instance.template_get_all_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_get_all_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | 
filter | FilterSchema | | optional
limit | LimitSchema | | 


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_get_all_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_get_all_get.ApiResponseFor500) | 500 response

#### template_get_all_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateGetAllResponses**](../../models/SDTemplateGetAllResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_get_all_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_get_get**
<a name="template_get_get"></a>
> SDTemplateGetResponse template_get_get(template_id)

Get Template

Get the Details of a Template

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_get_response import SDTemplateGetResponse
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'templateId': "templateId_example",
    }
    try:
        # Get Template
        api_response = api_instance.template_get_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_get_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateId | TemplateIdSchema | | 


# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_get_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_get_get.ApiResponseFor500) | 500 response

#### template_get_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateGetResponse**](../../models/SDTemplateGetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_get_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_get_tokens_get**
<a name="template_get_tokens_get"></a>
> SDTemplateGetTokensResponses template_get_tokens_get(template_id)

Get Template Tokens

Get a List of All Minted Tokens from a Given Template

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_get_tokens_responses import SDTemplateGetTokensResponses
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'templateId': "templateId_example",
    }
    try:
        # Get Template Tokens
        api_response = api_instance.template_get_tokens_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_get_tokens_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'start': "start_example",
        'templateId': "templateId_example",
        'limit': "limit_example",
        'includeDeleted': "includeDeleted_example",
    }
    try:
        # Get Template Tokens
        api_response = api_instance.template_get_tokens_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_get_tokens_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
templateId | TemplateIdSchema | | 
limit | LimitSchema | | optional
includeDeleted | IncludeDeletedSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_get_tokens_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_get_tokens_get.ApiResponseFor500) | 500 response

#### template_get_tokens_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateGetTokensResponses**](../../models/SDTemplateGetTokensResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_get_tokens_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_mutate_put**
<a name="template_mutate_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} template_mutate_put(sd_template_mutate_request)

Mutate Template

Mutates a Property of a Template, Which in Turn will Affect the Inherited Property on All of the Tokens Created from this Template (via token/mint)

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.sd_template_mutate_request import SDTemplateMutateRequest
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTemplateMutateRequest(
        template_id=0,
        props=dict(),
        public_contract_metadata=dict(),
        public_token_metadata=dict(),
    )
    try:
        # Mutate Template
        api_response = api_instance.template_mutate_put(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_mutate_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTemplateMutateRequest**](../../models/SDTemplateMutateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_mutate_put.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_mutate_put.ApiResponseFor500) | 500 response

#### template_mutate_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

Empty Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Empty Schema | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_mutate_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_props_remove_delete**
<a name="template_props_remove_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} template_props_remove_delete(template_idprops)

Remove Template Property

Removes a Templates Property from Your Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'templateId': "templateId_example",
        'props': "props_example",
    }
    try:
        # Remove Template Property
        api_response = api_instance.template_props_remove_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_props_remove_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateId | TemplateIdSchema | | 
props | PropsSchema | | 


# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PropsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_props_remove_delete.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_props_remove_delete.ApiResponseFor500) | 500 response

#### template_props_remove_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

Empty Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Empty Schema | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_props_remove_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **template_remove_delete**
<a name="template_remove_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} template_remove_delete(template_id)

Remove Template

Removes a Template from Your Game. If Players have Instances of this Template from the token/mint Command, Their Tokens will NOT be Removed

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import template_endpoints_api
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = template_endpoints_api.TemplateEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'templateId': "templateId_example",
    }
    try:
        # Remove Template
        api_response = api_instance.template_remove_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TemplateEndpointsApi->template_remove_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateId | TemplateIdSchema | | 


# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#template_remove_delete.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#template_remove_delete.ApiResponseFor500) | 500 response

#### template_remove_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

Empty Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Empty Schema | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### template_remove_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

