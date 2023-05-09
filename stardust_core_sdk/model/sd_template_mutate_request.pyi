# coding: utf-8

"""
    Stardust API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2023-05-08T04:33:59Z
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stardust_core_sdk import schemas  # noqa: F401


class SDTemplateMutateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "templateId",
        }
        
        class properties:
            
            
            class templateId(
                schemas.IntSchema
            ):
                pass
            props = schemas.DictSchema
            publicContractMetadata = schemas.DictSchema
            publicTokenMetadata = schemas.DictSchema
            __annotations__ = {
                "templateId": templateId,
                "props": props,
                "publicContractMetadata": publicContractMetadata,
                "publicTokenMetadata": publicTokenMetadata,
            }
    
    templateId: MetaOapg.properties.templateId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["props"]) -> MetaOapg.properties.props: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicContractMetadata"]) -> MetaOapg.properties.publicContractMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicTokenMetadata"]) -> MetaOapg.properties.publicTokenMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templateId", "props", "publicContractMetadata", "publicTokenMetadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["props"]) -> typing.Union[MetaOapg.properties.props, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicContractMetadata"]) -> typing.Union[MetaOapg.properties.publicContractMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicTokenMetadata"]) -> typing.Union[MetaOapg.properties.publicTokenMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templateId", "props", "publicContractMetadata", "publicTokenMetadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        templateId: typing.Union[MetaOapg.properties.templateId, decimal.Decimal, int, ],
        props: typing.Union[MetaOapg.properties.props, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        publicContractMetadata: typing.Union[MetaOapg.properties.publicContractMetadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        publicTokenMetadata: typing.Union[MetaOapg.properties.publicTokenMetadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDTemplateMutateRequest':
        return super().__new__(
            cls,
            *_args,
            templateId=templateId,
            props=props,
            publicContractMetadata=publicContractMetadata,
            publicTokenMetadata=publicTokenMetadata,
            _configuration=_configuration,
            **kwargs,
        )
