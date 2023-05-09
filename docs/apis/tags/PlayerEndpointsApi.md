<a name="__pageTop"></a>
# stardust_core_sdk.apis.tags.player_endpoints_api.PlayerEndpointsApi

All URIs are relative to *https://core-api.stardust.gg/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**player_count_get**](#player_count_get) | **get** /player/count | Get Player Count
[**player_create_post**](#player_create_post) | **post** /player/create | Create Player
[**player_get_all_get**](#player_get_all_get) | **get** /player/get-all | Get All Players
[**player_get_get**](#player_get_get) | **get** /player/get | Get Player
[**player_get_id_get**](#player_get_id_get) | **get** /player/get-id | Get Player ID
[**player_get_ids_get**](#player_get_ids_get) | **get** /player/get-ids | Get All Player IDs
[**player_get_inventory_get**](#player_get_inventory_get) | **get** /player/get-inventory | Get Player Inventory
[**player_mutate_put**](#player_mutate_put) | **put** /player/mutate | Mutate Player
[**player_remove_delete**](#player_remove_delete) | **delete** /player/remove | Remove Player
[**player_wallet_get_get**](#player_wallet_get_get) | **get** /player/wallet-get | Get Player Wallet
[**player_withdraw_post**](#player_withdraw_post) | **post** /player/withdraw | Withdraw From Player

# **player_count_get**
<a name="player_count_get"></a>
> SDPlayerCountResponse player_count_get()

Get Player Count

Get Player count within a game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_count_response import SDPlayerCountResponse
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Player Count
        api_response = api_instance.player_count_get()
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_count_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_count_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_count_get.ApiResponseFor500) | 500 response

#### player_count_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerCountResponse**](../../models/SDPlayerCountResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_count_get.ApiResponseFor500
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

# **player_create_post**
<a name="player_create_post"></a>
> SDPlayerCreateResponse player_create_post(sd_player_create_request)

Create Player

Create a Player for a game. Returns their player id which can be used to reference them later in Stardust's system

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_create_response import SDPlayerCreateResponse
from stardust_core_sdk.model.sd_player_create_request import SDPlayerCreateRequest
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDPlayerCreateRequest(
        unique_id="unique_id_example",
        image="image_example",
        user_data=dict(),
    )
    try:
        # Create Player
        api_response = api_instance.player_create_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_create_post: %s\n" % e)
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
[**SDPlayerCreateRequest**](../../models/SDPlayerCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_create_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_create_post.ApiResponseFor500) | 500 response

#### player_create_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerCreateResponse**](../../models/SDPlayerCreateResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_create_post.ApiResponseFor500
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

# **player_get_all_get**
<a name="player_get_all_get"></a>
> SDPlayerGetAllResponses player_get_all_get()

Get All Players

Get the List of All Players in Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_get_all_responses import SDPlayerGetAllResponses
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only optional values
    query_params = {
        'start': "start_example",
        'filter': "filter_example",
        'limit': "limit_example",
    }
    try:
        # Get All Players
        api_response = api_instance.player_get_all_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_all_get: %s\n" % e)
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
filter | FilterSchema | | optional
limit | LimitSchema | | optional


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
200 | [ApiResponseFor200](#player_get_all_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_get_all_get.ApiResponseFor500) | 500 response

#### player_get_all_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerGetAllResponses**](../../models/SDPlayerGetAllResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_get_all_get.ApiResponseFor500
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

# **player_get_get**
<a name="player_get_get"></a>
> SDPlayerGetResponse player_get_get(player_id)

Get Player

Get Details of a Player Within a Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_get_response import SDPlayerGetResponse
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'playerId': "playerId_example",
    }
    try:
        # Get Player
        api_response = api_instance.player_get_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_get: %s\n" % e)
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
playerId | PlayerIdSchema | | 


# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_get_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_get_get.ApiResponseFor500) | 500 response

#### player_get_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerGetResponse**](../../models/SDPlayerGetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_get_get.ApiResponseFor500
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

# **player_get_id_get**
<a name="player_get_id_get"></a>
> SDPlayerGetIdResponse player_get_id_get(unique_id)

Get Player ID

Get a Player's ID via their Unique ID

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.error import Error
from stardust_core_sdk.model.sd_player_get_id_response import SDPlayerGetIdResponse
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'uniqueId': "uniqueId_example",
    }
    try:
        # Get Player ID
        api_response = api_instance.player_get_id_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_id_get: %s\n" % e)
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
uniqueId | UniqueIdSchema | | 


# UniqueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_get_id_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_get_id_get.ApiResponseFor500) | 500 response

#### player_get_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerGetIdResponse**](../../models/SDPlayerGetIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_get_id_get.ApiResponseFor500
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

# **player_get_ids_get**
<a name="player_get_ids_get"></a>
> SDPlayerGetIdsResponses player_get_ids_get()

Get All Player IDs

Get All Player IDs for a Given Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_get_ids_responses import SDPlayerGetIdsResponses
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get All Player IDs
        api_response = api_instance.player_get_ids_get()
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_ids_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_get_ids_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_get_ids_get.ApiResponseFor500) | 500 response

#### player_get_ids_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerGetIdsResponses**](../../models/SDPlayerGetIdsResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_get_ids_get.ApiResponseFor500
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

# **player_get_inventory_get**
<a name="player_get_inventory_get"></a>
> SDPlayerGetInventoryResponses player_get_inventory_get(player_id)

Get Player Inventory

Get a players inventory and all the items it holds

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.error import Error
from stardust_core_sdk.model.sd_player_get_inventory_responses import SDPlayerGetInventoryResponses
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'playerId': "playerId_example",
    }
    try:
        # Get Player Inventory
        api_response = api_instance.player_get_inventory_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_inventory_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'start': "start_example",
        'tokenIds': "tokenIds_example",
        'playerId': "playerId_example",
        'limit': "limit_example",
    }
    try:
        # Get Player Inventory
        api_response = api_instance.player_get_inventory_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_get_inventory_get: %s\n" % e)
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
tokenIds | TokenIdsSchema | | optional
playerId | PlayerIdSchema | | 
limit | LimitSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TokenIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlayerIdSchema

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
200 | [ApiResponseFor200](#player_get_inventory_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_get_inventory_get.ApiResponseFor500) | 500 response

#### player_get_inventory_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerGetInventoryResponses**](../../models/SDPlayerGetInventoryResponses.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_get_inventory_get.ApiResponseFor500
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

# **player_mutate_put**
<a name="player_mutate_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} player_mutate_put(sd_player_mutate_request)

Mutate Player

Change player data

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_mutate_request import SDPlayerMutateRequest
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDPlayerMutateRequest(
        player_id="player_id_example",
        props=dict(),
    )
    try:
        # Mutate Player
        api_response = api_instance.player_mutate_put(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_mutate_put: %s\n" % e)
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
[**SDPlayerMutateRequest**](../../models/SDPlayerMutateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_mutate_put.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_mutate_put.ApiResponseFor500) | 500 response

#### player_mutate_put.ApiResponseFor200
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


#### player_mutate_put.ApiResponseFor500
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

# **player_remove_delete**
<a name="player_remove_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} player_remove_delete(player_id)

Remove Player

Removes (hides) a player from your game. This is not permanent.

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'playerId': "playerId_example",
    }
    try:
        # Remove Player
        api_response = api_instance.player_remove_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_remove_delete: %s\n" % e)
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
playerId | PlayerIdSchema | | 


# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_remove_delete.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_remove_delete.ApiResponseFor500) | 500 response

#### player_remove_delete.ApiResponseFor200
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


#### player_remove_delete.ApiResponseFor500
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

# **player_wallet_get_get**
<a name="player_wallet_get_get"></a>
> SDPlayerWalletGetResponse player_wallet_get_get(player_id)

Get Player Wallet

Get player's wallet within a game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_wallet_get_response import SDPlayerWalletGetResponse
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'playerId': "playerId_example",
    }
    try:
        # Get Player Wallet
        api_response = api_instance.player_wallet_get_get(
            query_params=query_params,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_wallet_get_get: %s\n" % e)
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
playerId | PlayerIdSchema | | 


# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_wallet_get_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_wallet_get_get.ApiResponseFor500) | 500 response

#### player_wallet_get_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDPlayerWalletGetResponse**](../../models/SDPlayerWalletGetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### player_wallet_get_get.ApiResponseFor500
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

# **player_withdraw_post**
<a name="player_withdraw_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} player_withdraw_post(sd_player_withdraw_request)

Withdraw From Player

Withdraw a Player's Tokens from their Stardust Wallet

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import player_endpoints_api
from stardust_core_sdk.model.sd_player_withdraw_request import SDPlayerWithdrawRequest
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
    api_instance = player_endpoints_api.PlayerEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDPlayerWithdrawRequest(
        address="address_example",
        player_id="player_id_example",
        token_objects=[
            SDPlayerWithdrawObject(
                token_id=0,
                amount="amount_example",
            )
        ],
    )
    try:
        # Withdraw From Player
        api_response = api_instance.player_withdraw_post(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling PlayerEndpointsApi->player_withdraw_post: %s\n" % e)
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
[**SDPlayerWithdrawRequest**](../../models/SDPlayerWithdrawRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_withdraw_post.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#player_withdraw_post.ApiResponseFor500) | 500 response

#### player_withdraw_post.ApiResponseFor200
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


#### player_withdraw_post.ApiResponseFor500
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

