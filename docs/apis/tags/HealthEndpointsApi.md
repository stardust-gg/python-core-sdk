<a name="__pageTop"></a>
# stardust_core_sdk.apis.tags.health_endpoints_api.HealthEndpointsApi

All URIs are relative to *https://core-api.stardust.gg/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](#health_get) | **get** /health | Get Health

# **health_get**
<a name="health_get"></a>
> SDHealthResponse health_get()

Get Health

Get system health info

### Example

```python
import stardust_core_sdk
from stardust_core_sdk.apis.tags import health_endpoints_api
from stardust_core_sdk.model.sd_health_response import SDHealthResponse
from stardust_core_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://core-api.stardust.gg/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stardust_core_sdk.Configuration(
    host = "https://core-api.stardust.gg/v1"
)

# Enter a context with an instance of the API client
with stardust_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = health_endpoints_api.HealthEndpointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Health
        api_response = api_instance.health_get()
        pprint(api_response)
    except stardust_core_sdk.ApiException as e:
        print("Exception when calling HealthEndpointsApi->health_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#health_get.ApiResponseFor200) | 200 response
500 | [ApiResponseFor500](#health_get.ApiResponseFor500) | 500 response

#### health_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SDHealthResponse**](../../models/SDHealthResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### health_get.ApiResponseFor500
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

