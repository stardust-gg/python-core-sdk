# stardust_core_sdk.model.sd_token_withdraw_request.SDTokenWithdrawRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  | External (non-custodial) blockchain wallet address | 
**[tokenObjects](#tokenObjects)** | list, tuple,  | tuple,  | Array of Token objects | 
**playerId** | str,  | str,  | The Player&#x27;s id, can be found with Player/getId(s) in uuid format. Also returned from player/create (ex. XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX) | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tokenObjects

Array of Token objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of Token objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SDTokenWithdrawObject**](SDTokenWithdrawObject.md) | [**SDTokenWithdrawObject**](SDTokenWithdrawObject.md) | [**SDTokenWithdrawObject**](SDTokenWithdrawObject.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

