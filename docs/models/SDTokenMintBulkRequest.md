# stardust_core_sdk.model.sd_token_mint_bulk_request.SDTokenMintBulkRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tokenObjects](#tokenObjects)** | list, tuple,  | tuple,  | array of Token objects | 
**playerId** | str,  | str,  | The player ID that was returned from player/create | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tokenObjects

array of Token objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | array of Token objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SDTokenMintBulkTokenObject**](SDTokenMintBulkTokenObject.md) | [**SDTokenMintBulkTokenObject**](SDTokenMintBulkTokenObject.md) | [**SDTokenMintBulkTokenObject**](SDTokenMintBulkTokenObject.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

