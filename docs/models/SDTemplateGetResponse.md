# stardust_core_sdk.model.sd_template_get_response.SDTemplateGetResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gameId** | decimal.Decimal, int,  | decimal.Decimal,  | Game ID Number (unsigned 32 bit integer) | 
**cap** | str,  | str,  | u96 Number as String, min: 0, max: 39614081257132168796771975167 | 
**totalSupply** | str,  | str,  | u96 Number as String, min: 0, max: 39614081257132168796771975167 | 
**name** | str,  | str,  | The name of the template | 
**_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**type** | str,  | str,  |  | must be one of ["FT", "NFT", ] 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**contractType** | str,  | str,  | The type of custom contract bieng used for this template. | [optional] must be one of ["ERC721", "internal-mint", "external-no-mint", ] 
**[publicContractMetadata](#publicContractMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | [optional] 
**[publicTokenMetadata](#publicTokenMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Inherited by tokens, and returned to marketplaces as token metadata | [optional] 
**[fees](#fees)** | list, tuple,  | tuple,  |  | [optional] 
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
**[mutable](#mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[$mutable](#$mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
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

# $mutable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

