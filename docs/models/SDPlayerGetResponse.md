# stardust_core_sdk.model.sd_player_get_response.SDPlayerGetResponse

This is the data output json model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This is the data output json model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uniqueId** | str,  | str,  | Player ID in the form of a the game owner&#x27;s internal playerId, i.e. email address | 
**playerId** | str,  | str,  | Player ID in the form of a UUID | 
**lastSeen** | str,  | str,  | Date and time the player was &#x27;last seen&#x27; actively participating in the game | [optional] 
**image** | str,  | str,  | URL of image cached by Stardust | [optional] 
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

