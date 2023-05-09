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


class SDOrderGetAllResponses(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['SDOrderGetAllResponse']:
            return SDOrderGetAllResponse

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['SDOrderGetAllResponse'], typing.List['SDOrderGetAllResponse']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SDOrderGetAllResponses':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'SDOrderGetAllResponse':
        return super().__getitem__(i)

from stardust_core_sdk.model.sd_order_get_all_response import SDOrderGetAllResponse
