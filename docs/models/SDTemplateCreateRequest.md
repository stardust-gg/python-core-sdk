# stardust_core_sdk.model.sd_template_create_request.SDTemplateCreateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cap** | str,  | str,  | u96 Number as String (ex. 200000000)  | 
**name** | str,  | str,  | The name of the template (ex. Bronze Axe) | 
**type** | str,  | str,  | FT is a currency where every instance is the same, NFT is where every token instance differes (ex. FT) | must be one of ["FT", "NFT", ] 
**[props](#props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**contractType** | str,  | str,  | The type of custom contract to use for this template. Default will use a shared contract. | [optional] must be one of ["internal-mint", "ERC721", "ERC20", ] 
**ownerAddress** | str,  | str,  | Blockchain address to set as owner of the custom contract. Required if contractType is set. | [optional] 
**[publicContractMetadata](#publicContractMetadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | [optional] 
**symbol** | str,  | str,  | For ERC20 contracts, this is the ticker symbol | [optional] 
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

# publicContractMetadata

Returned to marketplaces as contract metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returned to marketplaces as contract metadata | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

