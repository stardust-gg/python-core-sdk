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


class SDPlayerWalletGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the data output json model
    """


    class MetaOapg:
        required = {
            "wallet",
        }
        
        class properties:
            
            
            class wallet(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "address",
                                "blockchain",
                            }
                            
                            class properties:
                                blockchain = schemas.StrSchema
                                address = schemas.StrSchema
                                
                                
                                class monies(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.DictSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                class properties:
                                                    amount = schemas.StrSchema
                                                    currency = schemas.StrSchema
                                                    __annotations__ = {
                                                        "amount": amount,
                                                        "currency": currency,
                                                    }
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                            
                                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "currency", ], str]):
                                                # dict_instance[name] accessor
                                                return super().__getitem__(name)
                                            
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                            
                                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "currency", ], str]):
                                                return super().get_item_oapg(name)
                                            
                                        
                                            def __new__(
                                                cls,
                                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                                amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
                                                currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                            ) -> 'items':
                                                return super().__new__(
                                                    cls,
                                                    *_args,
                                                    amount=amount,
                                                    currency=currency,
                                                    _configuration=_configuration,
                                                    **kwargs,
                                                )
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'monies':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "blockchain": blockchain,
                                    "address": address,
                                    "monies": monies,
                                }
                        
                        address: MetaOapg.properties.address
                        blockchain: MetaOapg.properties.blockchain
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["blockchain"]) -> MetaOapg.properties.blockchain: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["monies"]) -> MetaOapg.properties.monies: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["blockchain", "address", "monies", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["blockchain"]) -> MetaOapg.properties.blockchain: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["monies"]) -> typing.Union[MetaOapg.properties.monies, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["blockchain", "address", "monies", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            address: typing.Union[MetaOapg.properties.address, str, ],
                            blockchain: typing.Union[MetaOapg.properties.blockchain, str, ],
                            monies: typing.Union[MetaOapg.properties.monies, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                address=address,
                                blockchain=blockchain,
                                monies=monies,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wallet':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "wallet": wallet,
            }
    
    wallet: MetaOapg.properties.wallet
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wallet"]) -> MetaOapg.properties.wallet: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["wallet", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wallet"]) -> MetaOapg.properties.wallet: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["wallet", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        wallet: typing.Union[MetaOapg.properties.wallet, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDPlayerWalletGetResponse':
        return super().__new__(
            cls,
            *_args,
            wallet=wallet,
            _configuration=_configuration,
            **kwargs,
        )