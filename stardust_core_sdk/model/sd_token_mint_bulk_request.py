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


class SDTokenMintBulkRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tokenObjects",
            "playerId",
        }
        
        class properties:
            playerId = schemas.StrSchema
            
            
            class tokenObjects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SDTokenMintBulkTokenObject']:
                        return SDTokenMintBulkTokenObject
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SDTokenMintBulkTokenObject'], typing.List['SDTokenMintBulkTokenObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tokenObjects':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SDTokenMintBulkTokenObject':
                    return super().__getitem__(i)
            __annotations__ = {
                "playerId": playerId,
                "tokenObjects": tokenObjects,
            }
    
    tokenObjects: MetaOapg.properties.tokenObjects
    playerId: MetaOapg.properties.playerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenObjects"]) -> MetaOapg.properties.tokenObjects: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["playerId", "tokenObjects", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenObjects"]) -> MetaOapg.properties.tokenObjects: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playerId", "tokenObjects", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tokenObjects: typing.Union[MetaOapg.properties.tokenObjects, list, tuple, ],
        playerId: typing.Union[MetaOapg.properties.playerId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDTokenMintBulkRequest':
        return super().__new__(
            cls,
            *_args,
            tokenObjects=tokenObjects,
            playerId=playerId,
            _configuration=_configuration,
            **kwargs,
        )

from stardust_core_sdk.model.sd_token_mint_bulk_token_object import SDTokenMintBulkTokenObject
