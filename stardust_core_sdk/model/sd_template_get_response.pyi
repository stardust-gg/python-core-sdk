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


class SDTemplateGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gameId",
            "cap",
            "totalSupply",
            "name",
            "_id",
            "type",
            "props",
        }
        
        class properties:
            
            
            class gameId(
                schemas.IntSchema
            ):
                pass
            
            
            class _id(
                schemas.IntSchema
            ):
                pass
            cap = schemas.StrSchema
            totalSupply = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FT(cls):
                    return cls("FT")
                
                @schemas.classproperty
                def NFT(cls):
                    return cls("NFT")
            
            
            class props(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "immutable",
                        "mutable",
                        "$mutable",
                    }
                    
                    class properties:
                        immutable = schemas.DictSchema
                        mutable = schemas.DictSchema
                        mutable = schemas.DictSchema
                        __annotations__ = {
                            "immutable": immutable,
                            "mutable": mutable,
                            "$mutable": mutable,
                        }
                
                immutable: MetaOapg.properties.immutable
                mutable: MetaOapg.properties.mutable
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["immutable"]) -> MetaOapg.properties.immutable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["$mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["immutable", "mutable", "$mutable", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["immutable"]) -> MetaOapg.properties.immutable: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["$mutable"]) -> MetaOapg.properties.mutable: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["immutable", "mutable", "$mutable", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    immutable: typing.Union[MetaOapg.properties.immutable, dict, frozendict.frozendict, ],
                    mutable: typing.Union[MetaOapg.properties.mutable, dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'props':
                    return super().__new__(
                        cls,
                        *_args,
                        immutable=immutable,
                        mutable=mutable,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class contractType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ERC721(cls):
                    return cls("ERC721")
                
                @schemas.classproperty
                def INTERNALMINT(cls):
                    return cls("internal-mint")
                
                @schemas.classproperty
                def EXTERNALNOMINT(cls):
                    return cls("external-no-mint")
            publicContractMetadata = schemas.DictSchema
            publicTokenMetadata = schemas.DictSchema
            
            
            class fees(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                feePercentage = schemas.IntSchema
                                feeType = schemas.StrSchema
                                __annotations__ = {
                                    "feePercentage": feePercentage,
                                    "feeType": feeType,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["feePercentage"]) -> MetaOapg.properties.feePercentage: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["feeType"]) -> MetaOapg.properties.feeType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["feePercentage", "feeType", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["feePercentage"]) -> typing.Union[MetaOapg.properties.feePercentage, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["feeType"]) -> typing.Union[MetaOapg.properties.feeType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["feePercentage", "feeType", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            feePercentage: typing.Union[MetaOapg.properties.feePercentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            feeType: typing.Union[MetaOapg.properties.feeType, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                feePercentage=feePercentage,
                                feeType=feeType,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fees':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "gameId": gameId,
                "_id": _id,
                "cap": cap,
                "totalSupply": totalSupply,
                "name": name,
                "type": type,
                "props": props,
                "contractType": contractType,
                "publicContractMetadata": publicContractMetadata,
                "publicTokenMetadata": publicTokenMetadata,
                "fees": fees,
            }
    
    gameId: MetaOapg.properties.gameId
    cap: MetaOapg.properties.cap
    totalSupply: MetaOapg.properties.totalSupply
    name: MetaOapg.properties.name
    _id: MetaOapg.properties._id
    type: MetaOapg.properties.type
    props: MetaOapg.properties.props
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gameId"]) -> MetaOapg.properties.gameId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cap"]) -> MetaOapg.properties.cap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalSupply"]) -> MetaOapg.properties.totalSupply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["props"]) -> MetaOapg.properties.props: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractType"]) -> MetaOapg.properties.contractType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicContractMetadata"]) -> MetaOapg.properties.publicContractMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicTokenMetadata"]) -> MetaOapg.properties.publicTokenMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fees"]) -> MetaOapg.properties.fees: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gameId", "_id", "cap", "totalSupply", "name", "type", "props", "contractType", "publicContractMetadata", "publicTokenMetadata", "fees", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gameId"]) -> MetaOapg.properties.gameId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cap"]) -> MetaOapg.properties.cap: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalSupply"]) -> MetaOapg.properties.totalSupply: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["props"]) -> MetaOapg.properties.props: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractType"]) -> typing.Union[MetaOapg.properties.contractType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicContractMetadata"]) -> typing.Union[MetaOapg.properties.publicContractMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicTokenMetadata"]) -> typing.Union[MetaOapg.properties.publicTokenMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fees"]) -> typing.Union[MetaOapg.properties.fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gameId", "_id", "cap", "totalSupply", "name", "type", "props", "contractType", "publicContractMetadata", "publicTokenMetadata", "fees", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gameId: typing.Union[MetaOapg.properties.gameId, decimal.Decimal, int, ],
        cap: typing.Union[MetaOapg.properties.cap, str, ],
        totalSupply: typing.Union[MetaOapg.properties.totalSupply, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        _id: typing.Union[MetaOapg.properties._id, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        props: typing.Union[MetaOapg.properties.props, dict, frozendict.frozendict, ],
        contractType: typing.Union[MetaOapg.properties.contractType, str, schemas.Unset] = schemas.unset,
        publicContractMetadata: typing.Union[MetaOapg.properties.publicContractMetadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        publicTokenMetadata: typing.Union[MetaOapg.properties.publicTokenMetadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        fees: typing.Union[MetaOapg.properties.fees, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SDTemplateGetResponse':
        return super().__new__(
            cls,
            *_args,
            gameId=gameId,
            cap=cap,
            totalSupply=totalSupply,
            name=name,
            _id=_id,
            type=type,
            props=props,
            contractType=contractType,
            publicContractMetadata=publicContractMetadata,
            publicTokenMetadata=publicTokenMetadata,
            fees=fees,
            _configuration=_configuration,
            **kwargs,
        )
