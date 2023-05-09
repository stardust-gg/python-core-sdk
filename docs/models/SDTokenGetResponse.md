# stardust_core_sdk.model.sd_token_get_response.SDTokenGetResponse

token data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | token data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gameId** | decimal.Decimal, int,  | decimal.Decimal,  | Game ID Number (unsigned 32 bit integer) | 
**flags** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the token created | 
**templateId** | decimal.Decimal, int,  | decimal.Decimal,  | Template ID Number (unsigned 32 bit integer) | 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**name** | str,  | str,  | The name of the template | [optional] 
**owner** | str,  | str,  | Game Owner&#x27;s Public Key | [optional] 
**[publicMetadata](#publicMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[immutable](#immutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[inherited](#inherited)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[mutable](#mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# immutable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# mutable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# inherited

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# publicMetadata

Returned to marketplaces as token metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as token metadata | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

