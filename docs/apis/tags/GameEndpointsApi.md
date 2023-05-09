<a name="__pageTop"></a>
# stardust_core_sdk.apis.tags.game_endpoints_api.GameEndpointsApi

All URIs are relative to *https://core-api.stardust.gg/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**game_get_get**](#game_get_get) | **get** /game/get | Get Game
[**game_mutate_put**](#game_mutate_put) | **put** /game/mutate | Mutate Game

# **game_get_get**
<a name="game_get_get"></a>
> SDGameGetResponse game_get_get()

Get Game

Get the Details of Your Game

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import game_endpoints_api
from stardust_core_sdk.model.sd_game_get_response import SDGameGetResponse
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
    api_instance = game_endpoints_api.GameEndpointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Game
        api_response = api_instance.game_get_get()
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling GameEndpointsApi->game_get_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_get_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#game_get_get.ApiResponseFor500) | 500 response

#### game_get_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDGameGetResponse**](../../models/SDGameGetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### game_get_get.ApiResponseFor500
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

# **game_mutate_put**
<a name="game_mutate_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} game_mutate_put(sd_game_mutate_request)

Mutate Game

Change a games data

### Example

* Api Key Authentication (api_key):
```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import game_endpoints_api
from stardust_core_sdk.model.sd_game_mutate_request import SDGameMutateRequest
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
    api_instance = game_endpoints_api.GameEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SDGameMutateRequest(
        description="description_example",
        news="news_example",
        props=dict(),
        test_mode=True,
    )
    try:
        # Mutate Game
        api_response = api_instance.game_mutate_put(
            body=body,
        )
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling GameEndpointsApi->game_mutate_put: %s\n" % e)
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
[**SDGameMutateRequest**](../../models/SDGameMutateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_mutate_put.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#game_mutate_put.ApiResponseFor500) | 500 response

#### game_mutate_put.ApiResponseFor200
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


#### game_mutate_put.ApiResponseFor500
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

