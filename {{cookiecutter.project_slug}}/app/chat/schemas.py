from typing import List
from typing import Union

from core.enumerate import MessageType
from pydantic import BaseModel
from pydantic import Field
from starlette import status


class BaseMessage(BaseModel):
    type: str = MessageType.INFO
    content: str = Field("", alias="message")


class AIResponse(BaseMessage):
    content: Union[str, List] = ""
    code: int = status.HTTP_200_OK
