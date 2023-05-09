# stardust_core_sdk.model.sd_token_mutate_request.SDTokenMutateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tokenId** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies which tokenId you want to manipulate (ex. 11) | 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7}) | 
**[publicMetadata](#publicMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7})

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7}) | 

# publicMetadata

Returned to marketplaces as token metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

