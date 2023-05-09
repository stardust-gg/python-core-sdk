# stardust_core_sdk.model.sd_player_withdraw_request.SDPlayerWithdrawRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  | Blockchain Address | 
**[tokenObjects](#tokenObjects)** | list, tuple,  | tuple,  | array of Token objects | 
**playerId** | str,  | str,  | The Player&#x27;s id, can be found with Player/getId(s). Also returned from player/create (ex. CzySggxVQz51jciGRFDY7d5BER2fav6TNEnPGjusPJPd) | 
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
[**SDPlayerWithdrawObject**](SDPlayerWithdrawObject.md) | [**SDPlayerWithdrawObject**](SDPlayerWithdrawObject.md) | [**SDPlayerWithdrawObject**](SDPlayerWithdrawObject.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

