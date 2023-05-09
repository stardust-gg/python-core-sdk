# stardust_core_sdk.model.sd_template_mutate_request.SDTemplateMutateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**templateId** | decimal.Decimal, int,  | decimal.Decimal,  | This is the templateId returned from template/create (ex. 5) | 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7}) | [optional] 
**[publicContractMetadata](#publicContractMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | [optional] 
**[publicTokenMetadata](#publicTokenMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Inherited by tokens, and returned to marketplaces as token metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7})

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies which properties you want to change (ex. {prop1: 5, prop2: 6, prop3: 7}) | 

# publicContractMetadata

Returned to marketplaces as contract metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | 

# publicTokenMetadata

Inherited by tokens, and returned to marketplaces as token metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Inherited by tokens, and returned to marketplaces as token metadata | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

