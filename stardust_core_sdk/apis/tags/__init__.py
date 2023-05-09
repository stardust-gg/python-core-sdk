# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stardust_core_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    GAME_ENDPOINTS = "Game Endpoints"
    HEALTH_ENDPOINTS = "Health Endpoints"
    ORDER_ENDPOINTS = "Order Endpoints"
    PLAYER_ENDPOINTS = "Player Endpoints"
    TEMPLATE_ENDPOINTS = "Template Endpoints"
    TOKEN_ENDPOINTS = "Token Endpoints"
