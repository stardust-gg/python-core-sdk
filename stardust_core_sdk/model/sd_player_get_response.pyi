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


class SDPlayerGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the data output json model
    """


    class MetaOapg:
        required = {
            "uniqueId",
            "playerId",
        }
        
        class properties:
            playerId = schemas.StrSchema
            uniqueId = schemas.StrSchema
            lastSeen = schemas.StrSchema
            image = schemas.StrSchema
            __annotations__ = {
                "playerId": playerId,
                "uniqueId": uniqueId,
                "lastSeen": lastSeen,
                "image": image,
            }
        additional_properties = schemas.StrSchema
    
    uniqueId: MetaOapg.properties.uniqueId
    playerId: MetaOapg.properties.playerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uniqueId"]) -> MetaOapg.properties.uniqueId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastSeen"]) -> MetaOapg.properties.lastSeen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uniqueId"], typing_extensions.Literal["playerId"], typing_extensions.Literal["lastSeen"], typing_extensions.Literal["image"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uniqueId"]) -> MetaOapg.properties.uniqueId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playerId"]) -> MetaOapg.properties.playerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastSeen"]) -> typing.Union[MetaOapg.properties.lastSeen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uniqueId"], typing_extensions.Literal["playerId"], typing_extensions.Literal["lastSeen"], typing_extensions.Literal["image"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uniqueId: typing.Union[MetaOapg.properties.uniqueId, str, ],
        playerId: typing.Union[MetaOapg.properties.playerId, str, ],
        lastSeen: typing.Union[MetaOapg.properties.lastSeen, str, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
    ) -> 'SDPlayerGetResponse':
        return super().__new__(
            cls,
            *_args,
            uniqueId=uniqueId,
            playerId=playerId,
            lastSeen=lastSeen,
            image=image,
            _configuration=_configuration,
            **kwargs,
        )
