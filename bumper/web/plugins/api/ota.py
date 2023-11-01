"""Ota plugin module."""
import logging
from collections.abc import Iterable

from aiohttp import web
from aiohttp.web_exceptions import HTTPInternalServerError
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import AbstractRouteDef

from bumper.utils import utils
from bumper.web.response_utils import get_success_response_v3

from .. import WebserverPlugin

_LOGGER = logging.getLogger(__name__)


class OtaPlugin(WebserverPlugin):
    """Ota plugin."""

    @property
    def routes(self) -> Iterable[AbstractRouteDef]:
        """Plugin routes."""
        return [
            web.route(
                "*",
                "/ota/products/wukong/class/{class}/firmware/latest.json",
                _handle_products_firmware_latest,
            ),
        ]


async def _handle_products_firmware_latest(_: Request) -> Response:
    # TODO: check what's needed to be implemented
    _LOGGER.warning("!!! POSSIBLE THIS API IS NOT (FULL) IMPLEMENTED :: _handle_products_firmware_latest !!!")
    try:
        # device_class = request.match_info.get("class")
        # did = request.query.get("did")
        return get_success_response_v3(None)
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError
