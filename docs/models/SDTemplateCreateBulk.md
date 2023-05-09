# stardust_core_sdk.model.sd_template_create_bulk.SDTemplateCreateBulk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image** | str,  | str,  | image url | 
**name** | str,  | str,  | The name of the template (ex. Bronze Axe) | 
**cap** | str,  | str,  | u96 Number as String (ex. 200000000), default 39614081257132168796771975168  | [optional] 
**contractType** | str,  | str,  | The type of custom contract to use for this template. Default will use a shared contract. | [optional] must be one of ["ERC721", ] 
**type** | str,  | str,  | FT is a currency where every instance is the same, NFT is where every token instance differes (ex. FT) | [optional] must be one of ["FT", "NFT", ] 
**description** | str,  | str,  | Description of template | [optional] 
**activeListing** | bool,  | BoolClass,  | Set if the Template is active or not | [optional] 
**ownerAddress** | str,  | str,  | Blockchain address to set as owner of the custom contract, if contractType is passed in. | [optional] 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[publicContractMetadata](#publicContractMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | [optional] 
**[publicTokenMetadata](#publicTokenMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Inherited by tokens, and returned to marketplaces as token metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# props

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[immutable](#immutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for immutable on the Template | [optional] 
**[mutable](#mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for mutable on the Template | [optional] 
**[$mutable](#$mutable)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for mutable on the Item | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# immutable

Properties for immutable on the Template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for immutable on the Template | 

# mutable

Properties for mutable on the Template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for mutable on the Template | 

# $mutable

Properties for mutable on the Item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Properties for mutable on the Item | 

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

