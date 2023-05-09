# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stardust_core_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    GAME_GET = "/game/get"
    GAME_MUTATE = "/game/mutate"
    HEALTH = "/health"
    ORDER_BUY = "/order/buy"
    ORDER_CANCEL = "/order/cancel"
    ORDER_CREATE = "/order/create"
    ORDER_GET = "/order/get"
    ORDER_GETALL = "/order/get-all"
    PLAYER_COUNT = "/player/count"
    PLAYER_CREATE = "/player/create"
    PLAYER_GET = "/player/get"
    PLAYER_GETALL = "/player/get-all"
    PLAYER_GETID = "/player/get-id"
    PLAYER_GETIDS = "/player/get-ids"
    PLAYER_GETINVENTORY = "/player/get-inventory"
    PLAYER_MUTATE = "/player/mutate"
    PLAYER_REMOVE = "/player/remove"
    PLAYER_WALLETGET = "/player/wallet-get"
    PLAYER_WITHDRAW = "/player/withdraw"
    TEMPLATE_COUNT = "/template/count"
    TEMPLATE_CREATE = "/template/create"
    TEMPLATE_GET = "/template/get"
    TEMPLATE_GETALL = "/template/get-all"
    TEMPLATE_GETTOKENS = "/template/get-tokens"
    TEMPLATE_MUTATE = "/template/mutate"
    TEMPLATE_PROPSREMOVE = "/template/props-remove"
    TEMPLATE_REMOVE = "/template/remove"
    TOKEN_BURN = "/token/burn"
    TOKEN_GET = "/token/get"
    TOKEN_MINTBULK = "/token/mint-bulk"
    TOKEN_MUTATE = "/token/mutate"
    TOKEN_PROPSREMOVE = "/token/props-remove"
    TOKEN_TRANSFER = "/token/transfer"
    TOKEN_WITHDRAW = "/token/withdraw"
