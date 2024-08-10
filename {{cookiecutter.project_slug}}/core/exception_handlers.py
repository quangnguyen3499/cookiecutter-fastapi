import json

import openai
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.chat.schemas import AIResponse
from core.constants import ERROR_RESPONSE
from core.constants import ERROR_TIMEOUT_RESPONSE
from core.enumerate import MessageType
from core.exceptions import ChatbotException
from core.exceptions import CustomBaseException


def unexpected_exception_handler(request: Request, exc: CustomBaseException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": jsonable_encoder(exc.detail)},
    )


def openai_request_error_handler(request: Request = None, exc: openai.OpenAIError = None) -> str:
    return json.dumps(
        [
            AIResponse(
                type=MessageType.ERROR.value,
                content=ERROR_RESPONSE,
                code=status.HTTP_502_BAD_GATEWAY,
            ).model_dump(),
        ],
    )


def openai_timeout_error_handler(
    request: Request = None,
    exc: openai.APITimeoutError = None,
) -> str:
    return json.dumps(
        [
            AIResponse(
                type=MessageType.ERROR.value,
                content=ERROR_TIMEOUT_RESPONSE,
                code=status.HTTP_504_GATEWAY_TIMEOUT,
            ).model_dump(),
        ],
    )


def chatbot_exception_error_handler(request: Request = None, exc: ChatbotException = None) -> str:
    return json.dumps(
        [
            AIResponse(
                type=MessageType.ERROR.value,
                content=ERROR_RESPONSE,
                code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ).model_dump(),
        ],
    )
