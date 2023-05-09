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


class SDTokenMintBulkTokenObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "amount",
            "templateId",
        }
        
        class properties:
            
            
            class templateId(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 2147483647
                    inclusive_minimum = 0
            amount = schemas.StrSchema
            
            
            class props(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "mutable",
                    }
                    
                    class properties:
                        mutable = schemas.DictSchema
                        immutable = schemas.DictSchema
                        __annotations__ = {
                            "mutable": mutable,
                            "immutable": immutable,
                        }
                
                mutable: MetaOapg.properties.mutable
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["immutable"]) -> MetaOapg.properties.immutable: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["mutable", "immutable", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["immutable"]) -> typing.Union[MetaOapg.properties.immutable, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mutable", "immutable", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    mutable: typing.Union[MetaOapg.properties.mutable, dict, frozendict.frozendict, ],
                    immutable: typing.Union[MetaOapg.properties.immutable, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'props':
                    return super().__new__(
                        cls,
                        *_args,
                        mutable=mutable,
                        immutable=immutable,
                        _configuration=_configuration,
                        **kwargs,
                    )
            publicMetadata = schemas.DictSchema
            __annotations__ = {
                "templateId": templateId,
                "amount": amount,
                "props": props,
                "publicMetadata": publicMetadata,
            }
    
    amount: MetaOapg.properties.amount
    templateId: MetaOapg.properties.templateId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["props"]) -> MetaOapg.properties.props: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicMetadata"]) -> MetaOapg.properties.publicMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templateId", "amount", "props", "publicMetadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["props"]) -> typing.Union[MetaOapg.properties.props, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicMetadata"]) -> typing.Union[MetaOapg.properties.publicMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templateId", "amount", "props", "publicMetadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        templateId: typing.Union[MetaOapg.properties.templateId, decimal.Decimal, int, ],
        props: typing.Union[MetaOapg.properties.props, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        publicMetadata: typing.Union[MetaOapg.properties.publicMetadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDTokenMintBulkTokenObject':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            templateId=templateId,
            props=props,
            publicMetadata=publicMetadata,
            _configuration=_configuration,
            **kwargs,
        )
