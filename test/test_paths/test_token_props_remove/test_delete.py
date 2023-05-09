# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import stardust_core_sdk
from stardust_core_sdk.paths.token_props_remove import delete  # noqa: E501
from stardust_core_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTokenPropsRemove(ApiTestMixin, unittest.TestCase):
    """
    TokenPropsRemove unit test stubs
        Remove Token Property  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
