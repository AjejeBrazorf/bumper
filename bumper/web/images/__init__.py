"""Web image module."""
import logging
import os

from aiohttp.web_exceptions import HTTPInternalServerError
from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request

from bumper.utils import utils

_LOGGER = logging.getLogger(__name__)


async def get_bot_image(_: Request) -> FileResponse:
    """Return image of bot."""
    try:
        return FileResponse(os.path.join(os.path.dirname(__file__), "robotvac_image.jpg"))
    except Exception as e:
        _LOGGER.exception(utils.default_exception_str_builder(e))
    raise HTTPInternalServerError
