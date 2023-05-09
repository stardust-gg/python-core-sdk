# stardust_core_sdk.model.sd_game_get_response.SDGameGetResponse

This is the data output json model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This is the data output json model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bucketName** | str,  | str,  | Game bucket name | 
**image** | str,  | str,  | Game image | 
**name** | str,  | str,  | Game name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Game ID Number (unsigned 32 bit integer) | 
**ownerId** | str,  | str,  | Game Owner ID | 
**desc** | str,  | str,  | Game description | 
**news** | str,  | str,  | Game news | [optional] 
**[fees](#fees)** | list, tuple,  | tuple,  |  | [optional] 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Game properties | [optional] 
**testMode** | bool,  | BoolClass,  | If on test mode features are enabled. Currently in development. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fees

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**feePercentage** | decimal.Decimal, int,  | decimal.Decimal,  | The integer value of feePercentage.  | [optional] 
**feeType** | str,  | str,  | The type of fee | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

Game properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Game properties | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

