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


class SDPlayerGetIdsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the data output json model, i.e. {"uniqueId": "playerId"} 
    """


    class MetaOapg:
        required = {
            "uniqueId",
            "playerId",
        }
        
        class properties:
            playerId = schemas.StrSchema
            uniqueId = schemas.StrSchema
            __annotations__ = {
                "playerId": playerId,
                "uniqueId": uniqueId,
            }
    
    uniqueId: MetaOapg.properties.uniqueId
    playerId: MetaOapg.properties.playerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uniqueId"]) -> MetaOapg.properties.uniqueId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["playerId", "uniqueId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uniqueId"]) -> MetaOapg.properties.uniqueId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playerId", "uniqueId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uniqueId: typing.Union[MetaOapg.properties.uniqueId, str, ],
        playerId: typing.Union[MetaOapg.properties.playerId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDPlayerGetIdsResponse':
        return super().__new__(
            cls,
            *_args,
            uniqueId=uniqueId,
            playerId=playerId,
            _configuration=_configuration,
            **kwargs,
        )
