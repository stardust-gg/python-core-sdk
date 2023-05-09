import typing_extensions

from stardust_core_sdk.paths import PathValues
from stardust_core_sdk.apis.paths.game_get import GameGet
from stardust_core_sdk.apis.paths.game_mutate import GameMutate
from stardust_core_sdk.apis.paths.health import Health
from stardust_core_sdk.apis.paths.order_buy import OrderBuy
from stardust_core_sdk.apis.paths.order_cancel import OrderCancel
from stardust_core_sdk.apis.paths.order_create import OrderCreate
from stardust_core_sdk.apis.paths.order_get import OrderGet
from stardust_core_sdk.apis.paths.order_get_all import OrderGetAll
from stardust_core_sdk.apis.paths.player_count import PlayerCount
from stardust_core_sdk.apis.paths.player_create import PlayerCreate
from stardust_core_sdk.apis.paths.player_get import PlayerGet
from stardust_core_sdk.apis.paths.player_get_all import PlayerGetAll
from stardust_core_sdk.apis.paths.player_get_id import PlayerGetId
from stardust_core_sdk.apis.paths.player_get_ids import PlayerGetIds
from stardust_core_sdk.apis.paths.player_get_inventory import PlayerGetInventory
from stardust_core_sdk.apis.paths.player_mutate import PlayerMutate
from stardust_core_sdk.apis.paths.player_remove import PlayerRemove
from stardust_core_sdk.apis.paths.player_wallet_get import PlayerWalletGet
from stardust_core_sdk.apis.paths.player_withdraw import PlayerWithdraw
from stardust_core_sdk.apis.paths.template_count import TemplateCount
from stardust_core_sdk.apis.paths.template_create import TemplateCreate
from stardust_core_sdk.apis.paths.template_get import TemplateGet
from stardust_core_sdk.apis.paths.template_get_all import TemplateGetAll
from stardust_core_sdk.apis.paths.template_get_tokens import TemplateGetTokens
from stardust_core_sdk.apis.paths.template_mutate import TemplateMutate
from stardust_core_sdk.apis.paths.template_props_remove import TemplatePropsRemove
from stardust_core_sdk.apis.paths.template_remove import TemplateRemove
from stardust_core_sdk.apis.paths.token_burn import TokenBurn
from stardust_core_sdk.apis.paths.token_get import TokenGet
from stardust_core_sdk.apis.paths.token_mint_bulk import TokenMintBulk
from stardust_core_sdk.apis.paths.token_mutate import TokenMutate
from stardust_core_sdk.apis.paths.token_props_remove import TokenPropsRemove
from stardust_core_sdk.apis.paths.token_transfer import TokenTransfer
from stardust_core_sdk.apis.paths.token_withdraw import TokenWithdraw

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.GAME_GET: GameGet,
        PathValues.GAME_MUTATE: GameMutate,
        PathValues.HEALTH: Health,
        PathValues.ORDER_BUY: OrderBuy,
        PathValues.ORDER_CANCEL: OrderCancel,
        PathValues.ORDER_CREATE: OrderCreate,
        PathValues.ORDER_GET: OrderGet,
        PathValues.ORDER_GETALL: OrderGetAll,
        PathValues.PLAYER_COUNT: PlayerCount,
        PathValues.PLAYER_CREATE: PlayerCreate,
        PathValues.PLAYER_GET: PlayerGet,
        PathValues.PLAYER_GETALL: PlayerGetAll,
        PathValues.PLAYER_GETID: PlayerGetId,
        PathValues.PLAYER_GETIDS: PlayerGetIds,
        PathValues.PLAYER_GETINVENTORY: PlayerGetInventory,
        PathValues.PLAYER_MUTATE: PlayerMutate,
        PathValues.PLAYER_REMOVE: PlayerRemove,
        PathValues.PLAYER_WALLETGET: PlayerWalletGet,
        PathValues.PLAYER_WITHDRAW: PlayerWithdraw,
        PathValues.TEMPLATE_COUNT: TemplateCount,
        PathValues.TEMPLATE_CREATE: TemplateCreate,
        PathValues.TEMPLATE_GET: TemplateGet,
        PathValues.TEMPLATE_GETALL: TemplateGetAll,
        PathValues.TEMPLATE_GETTOKENS: TemplateGetTokens,
        PathValues.TEMPLATE_MUTATE: TemplateMutate,
        PathValues.TEMPLATE_PROPSREMOVE: TemplatePropsRemove,
        PathValues.TEMPLATE_REMOVE: TemplateRemove,
        PathValues.TOKEN_BURN: TokenBurn,
        PathValues.TOKEN_GET: TokenGet,
        PathValues.TOKEN_MINTBULK: TokenMintBulk,
        PathValues.TOKEN_MUTATE: TokenMutate,
        PathValues.TOKEN_PROPSREMOVE: TokenPropsRemove,
        PathValues.TOKEN_TRANSFER: TokenTransfer,
        PathValues.TOKEN_WITHDRAW: TokenWithdraw,
    }
)

path_to_api = PathToApi(
    {
        PathValues.GAME_GET: GameGet,
        PathValues.GAME_MUTATE: GameMutate,
        PathValues.HEALTH: Health,
        PathValues.ORDER_BUY: OrderBuy,
        PathValues.ORDER_CANCEL: OrderCancel,
        PathValues.ORDER_CREATE: OrderCreate,
        PathValues.ORDER_GET: OrderGet,
        PathValues.ORDER_GETALL: OrderGetAll,
        PathValues.PLAYER_COUNT: PlayerCount,
        PathValues.PLAYER_CREATE: PlayerCreate,
        PathValues.PLAYER_GET: PlayerGet,
        PathValues.PLAYER_GETALL: PlayerGetAll,
        PathValues.PLAYER_GETID: PlayerGetId,
        PathValues.PLAYER_GETIDS: PlayerGetIds,
        PathValues.PLAYER_GETINVENTORY: PlayerGetInventory,
        PathValues.PLAYER_MUTATE: PlayerMutate,
        PathValues.PLAYER_REMOVE: PlayerRemove,
        PathValues.PLAYER_WALLETGET: PlayerWalletGet,
        PathValues.PLAYER_WITHDRAW: PlayerWithdraw,
        PathValues.TEMPLATE_COUNT: TemplateCount,
        PathValues.TEMPLATE_CREATE: TemplateCreate,
        PathValues.TEMPLATE_GET: TemplateGet,
        PathValues.TEMPLATE_GETALL: TemplateGetAll,
        PathValues.TEMPLATE_GETTOKENS: TemplateGetTokens,
        PathValues.TEMPLATE_MUTATE: TemplateMutate,
        PathValues.TEMPLATE_PROPSREMOVE: TemplatePropsRemove,
        PathValues.TEMPLATE_REMOVE: TemplateRemove,
        PathValues.TOKEN_BURN: TokenBurn,
        PathValues.TOKEN_GET: TokenGet,
        PathValues.TOKEN_MINTBULK: TokenMintBulk,
        PathValues.TOKEN_MUTATE: TokenMutate,
        PathValues.TOKEN_PROPSREMOVE: TokenPropsRemove,
        PathValues.TOKEN_TRANSFER: TokenTransfer,
        PathValues.TOKEN_WITHDRAW: TokenWithdraw,
    }
)
