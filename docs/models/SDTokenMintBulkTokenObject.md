# stardust_core_sdk.model.sd_token_mint_bulk_token_object.SDTokenMintBulkTokenObject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | u64 Number as String, min: 0, max: 9223372036854775807 (ex. \&quot;6\&quot;) | 
**templateId** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies which Template you are creating an instance of (ex. 3) | 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Internal metadata | [optional] 
**[publicMetadata](#publicMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

Internal metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Internal metadata | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mutable](#mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7}) | 
**[immutable](#immutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7}) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mutable

Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7})

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7}) | 

# immutable

Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7})

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to add (ex. {prop1: 5, prop2: 6, prop3: 7}) | 

# publicMetadata

Returned to marketplaces as token metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

