import typing_extensions

from stardust_core_sdk.apis.tags import TagValues
from stardust_core_sdk.apis.tags.game_endpoints_api import GameEndpointsApi
from stardust_core_sdk.apis.tags.health_endpoints_api import HealthEndpointsApi
from stardust_core_sdk.apis.tags.order_endpoints_api import OrderEndpointsApi
from stardust_core_sdk.apis.tags.player_endpoints_api import PlayerEndpointsApi
from stardust_core_sdk.apis.tags.template_endpoints_api import TemplateEndpointsApi
from stardust_core_sdk.apis.tags.token_endpoints_api import TokenEndpointsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.GAME_ENDPOINTS: GameEndpointsApi,
        TagValues.HEALTH_ENDPOINTS: HealthEndpointsApi,
        TagValues.ORDER_ENDPOINTS: OrderEndpointsApi,
        TagValues.PLAYER_ENDPOINTS: PlayerEndpointsApi,
        TagValues.TEMPLATE_ENDPOINTS: TemplateEndpointsApi,
        TagValues.TOKEN_ENDPOINTS: TokenEndpointsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.GAME_ENDPOINTS: GameEndpointsApi,
        TagValues.HEALTH_ENDPOINTS: HealthEndpointsApi,
        TagValues.ORDER_ENDPOINTS: OrderEndpointsApi,
        TagValues.PLAYER_ENDPOINTS: PlayerEndpointsApi,
        TagValues.TEMPLATE_ENDPOINTS: TemplateEndpointsApi,
        TagValues.TOKEN_ENDPOINTS: TokenEndpointsApi,
    }
)
