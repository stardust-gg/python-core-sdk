# stardust_core_sdk.model.sd_player_get_all_response.SDPlayerGetAllResponse

This is the data output json model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This is the data output json model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uniqueId** | str,  | str,  | Game player&#x27;s unique ID from the game itself | 
**playerId** | str,  | str,  | Player ID in the form of a UUID | 
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Game player&#x27;s ID in the database | [optional] 
**lastSeen** | str,  | str,  | Date and time the player was &#x27;last seen&#x27; actively participating in the game | [optional] 
**image** | str,  | str,  | URL of image cached by Stardust | [optional] 
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

