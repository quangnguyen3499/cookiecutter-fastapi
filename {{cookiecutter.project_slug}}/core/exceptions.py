from typing import Any

from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel


class ExceptionModel(BaseModel):
    detail: str = ""


class ChatbotException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Chatbot Error"

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail, **kwargs)


class OpenAITimeoutException(ChatbotException):
    status_code = status.HTTP_504_GATEWAY_TIMEOUT
    detail = "OpenAI API Request timed out"


class OpenAIException(ChatbotException):
    status_code = status.HTTP_502_BAD_GATEWAY
    detail = "OpenAI API Server error"


class CustomBaseException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server Error"


class PermissionDenied(CustomBaseException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Permission denied"


class NotFound(CustomBaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Not Found"


class BadRequest(CustomBaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad Request"


class NotAuthenticated(CustomBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not authenticated"
