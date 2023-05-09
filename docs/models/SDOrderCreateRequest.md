# stardust_core_sdk.model.sd_order_create_request.SDOrderCreateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tokensRequested](#tokensRequested)** | list, tuple,  | tuple,  |  | 
**offeredBy** | str,  | str,  | PlayerId creating the order | 
**[tokensOffered](#tokensOffered)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tokensOffered

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SDOrderCreateTokens**](SDOrderCreateTokens.md) | [**SDOrderCreateTokens**](SDOrderCreateTokens.md) | [**SDOrderCreateTokens**](SDOrderCreateTokens.md) |  | 

# tokensRequested

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SDOrderCreateTokens**](SDOrderCreateTokens.md) | [**SDOrderCreateTokens**](SDOrderCreateTokens.md) | [**SDOrderCreateTokens**](SDOrderCreateTokens.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

