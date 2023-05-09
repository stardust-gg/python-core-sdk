<a name="__pageTop"></a>
# stardust_core_sdk.apis.tags.token_endpoints_api.TokenEndpointsApi

All URIs are relative to *https://core-api.stardust.gg/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_burn_post**](#token_burn_post) | **post** /token/burn | Burn Token
[**token_get_get**](#token_get_get) | **get** /token/get | Get Token
[**token_mint_bulk_post**](#token_mint_bulk_post) | **post** /token/mint-bulk | Mint Tokens
[**token_mutate_put**](#token_mutate_put) | **put** /token/mutate | Mutate Token
[**token_props_remove_delete**](#token_props_remove_delete) | **delete** /token/props-remove | Remove Token Property
[**token_transfer_post**](#token_transfer_post) | **post** /token/transfer | Transfer Tokens
[**token_withdraw_post**](#token_withdraw_post) | **post** /token/withdraw | Withdraw Token

# **token_burn_post**
<a name="token_burn_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} token_burn_post(sd_token_burn_request)

Burn Token

Burns token on-chain. Cannot be reversed.

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_burn_request import SDTokenBurnRequest
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTokenBurnRequest(
        player_id="player_id_example",
        token_objects=[
            dict(
                token_id=0,
                amount="amount_example",
            )
        ],
    )
    try:
        # Burn Token
        api_response = api_instance.token_burn_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_burn_post: %s\n" % e)
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
[**SDTokenBurnRequest**](../../models/SDTokenBurnRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_burn_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_burn_post.ApiResponseFor500) | 500 response

#### token_burn_post.ApiResponseFor200
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


#### token_burn_post.ApiResponseFor500
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

# **token_get_get**
<a name="token_get_get"></a>
> SDTokenGetResponses token_get_get(token_ids)

Get Token

Some of the details of this token are based upon the Template that it was created from (using token/mint)

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_get_responses import SDTokenGetResponses
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'tokenIds': "tokenIds_example",
    }
    try:
        # Get Token
        api_response = api_instance.token_get_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_get_get: %s\n" % e)
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
tokenIds | TokenIdsSchema | | 


# TokenIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_get_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_get_get.ApiResponseFor500) | 500 response

#### token_get_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTokenGetResponses**](../../models/SDTokenGetResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### token_get_get.ApiResponseFor500
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

# **token_mint_bulk_post**
<a name="token_mint_bulk_post"></a>
> SDTokenMintBulkResponses token_mint_bulk_post(sd_token_mint_bulk_request)

Mint Tokens

Mint tokens to a player

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_mint_bulk_request import SDTokenMintBulkRequest
from stardust_core_sdk.model.sd_token_mint_bulk_responses import SDTokenMintBulkResponses
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTokenMintBulkRequest(
        player_id="player_id_example",
        token_objects=[
            SDTokenMintBulkTokenObject(
                template_id=0,
                amount="amount_example",
                props=dict(
                    mutable=dict(),
                    immutable=dict(),
                ),
                public_metadata=dict(),
            )
        ],
    )
    try:
        # Mint Tokens
        api_response = api_instance.token_mint_bulk_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_mint_bulk_post: %s\n" % e)
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
[**SDTokenMintBulkRequest**](../../models/SDTokenMintBulkRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_mint_bulk_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_mint_bulk_post.ApiResponseFor500) | 500 response

#### token_mint_bulk_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDTokenMintBulkResponses**](../../models/SDTokenMintBulkResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### token_mint_bulk_post.ApiResponseFor500
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

# **token_mutate_put**
<a name="token_mutate_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} token_mutate_put(sd_token_mutate_request)

Mutate Token

Mutates a Property of a Token

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_mutate_request import SDTokenMutateRequest
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTokenMutateRequest(
        token_id=0,
        props=dict(),
        public_metadata=dict(),
    )
    try:
        # Mutate Token
        api_response = api_instance.token_mutate_put(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_mutate_put: %s\n" % e)
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
[**SDTokenMutateRequest**](../../models/SDTokenMutateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_mutate_put.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_mutate_put.ApiResponseFor500) | 500 response

#### token_mutate_put.ApiResponseFor200
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


#### token_mutate_put.ApiResponseFor500
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

# **token_props_remove_delete**
<a name="token_props_remove_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} token_props_remove_delete(token_idprops)

Remove Token Property

Removes a Tokens Property from Your Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'tokenId': "tokenId_example",
        'props': "props_example",
    }
    try:
        # Remove Token Property
        api_response = api_instance.token_props_remove_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_props_remove_delete: %s\n" % e)
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
tokenId | TokenIdSchema | | 
props | PropsSchema | | 


# TokenIdSchema

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
200 | [ApiResponseFor200](#token_props_remove_delete.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_props_remove_delete.ApiResponseFor500) | 500 response

#### token_props_remove_delete.ApiResponseFor200
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


#### token_props_remove_delete.ApiResponseFor500
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

# **token_transfer_post**
<a name="token_transfer_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} token_transfer_post(sd_token_transfer_request)

Transfer Tokens

Use this Endpoint to Facilitate Moving Tokens from one Player to Another

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_transfer_request import SDTokenTransferRequest
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTokenTransferRequest(
        from_player_id="from_player_id_example",
        to_player_id="to_player_id_example",
        token_objects=[
            dict(
                token_id=0,
                amount="amount_example",
            )
        ],
    )
    try:
        # Transfer Tokens
        api_response = api_instance.token_transfer_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_transfer_post: %s\n" % e)
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
[**SDTokenTransferRequest**](../../models/SDTokenTransferRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_transfer_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_transfer_post.ApiResponseFor500) | 500 response

#### token_transfer_post.ApiResponseFor200
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


#### token_transfer_post.ApiResponseFor500
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

# **token_withdraw_post**
<a name="token_withdraw_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} token_withdraw_post(sd_token_withdraw_request)

Withdraw Token

Withdraw tokens from a Stardust Wallet

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import token_endpoints_api
from stardust_core_sdk.model.sd_token_withdraw_request import SDTokenWithdrawRequest
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
    api_instance = token_endpoints_api.TokenEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDTokenWithdrawRequest(
        address="address_example",
        player_id="player_id_example",
        token_objects=[
            SDTokenWithdrawObject(
                token_id=1,
                amount="amount_example",
            )
        ],
    )
    try:
        # Withdraw Token
        api_response = api_instance.token_withdraw_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling TokenEndpointsApi->token_withdraw_post: %s\n" % e)
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
[**SDTokenWithdrawRequest**](../../models/SDTokenWithdrawRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#token_withdraw_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#token_withdraw_post.ApiResponseFor500) | 500 response

#### token_withdraw_post.ApiResponseFor200
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


#### token_withdraw_post.ApiResponseFor500
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

