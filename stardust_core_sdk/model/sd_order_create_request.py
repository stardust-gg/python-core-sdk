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


class SDOrderCreateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tokensRequested",
            "offeredBy",
            "tokensOffered",
        }
        
        class properties:
            offeredBy = schemas.StrSchema
            
            
            class tokensOffered(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SDOrderCreateTokens']:
                        return SDOrderCreateTokens
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SDOrderCreateTokens'], typing.List['SDOrderCreateTokens']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tokensOffered':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SDOrderCreateTokens':
                    return super().__getitem__(i)
            
            
            class tokensRequested(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SDOrderCreateTokens']:
                        return SDOrderCreateTokens
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SDOrderCreateTokens'], typing.List['SDOrderCreateTokens']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tokensRequested':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SDOrderCreateTokens':
                    return super().__getitem__(i)
            __annotations__ = {
                "offeredBy": offeredBy,
                "tokensOffered": tokensOffered,
                "tokensRequested": tokensRequested,
            }
    
    tokensRequested: MetaOapg.properties.tokensRequested
    offeredBy: MetaOapg.properties.offeredBy
    tokensOffered: MetaOapg.properties.tokensOffered
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offeredBy"]) -> MetaOapg.properties.offeredBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokensOffered"]) -> MetaOapg.properties.tokensOffered: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokensRequested"]) -> MetaOapg.properties.tokensRequested: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["offeredBy", "tokensOffered", "tokensRequested", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offeredBy"]) -> MetaOapg.properties.offeredBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokensOffered"]) -> MetaOapg.properties.tokensOffered: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokensRequested"]) -> MetaOapg.properties.tokensRequested: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["offeredBy", "tokensOffered", "tokensRequested", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tokensRequested: typing.Union[MetaOapg.properties.tokensRequested, list, tuple, ],
        offeredBy: typing.Union[MetaOapg.properties.offeredBy, str, ],
        tokensOffered: typing.Union[MetaOapg.properties.tokensOffered, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDOrderCreateRequest':
        return super().__new__(
            cls,
            *_args,
            tokensRequested=tokensRequested,
            offeredBy=offeredBy,
            tokensOffered=tokensOffered,
            _configuration=_configuration,
            **kwargs,
        )

from stardust_core_sdk.model.sd_order_create_tokens import SDOrderCreateTokens
