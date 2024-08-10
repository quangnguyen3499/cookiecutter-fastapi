from enum import Enum


# System
class Environment(str, Enum):
    TESTING = "TESTING"
    LOCAL = "LOCAL"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"

    @property
    def is_deployed(self) -> bool:
        return self in (self.DEVELOPMENT, self.PRODUCTION)


class ResponseDataType(Enum):
    OBJECT = "Object"
    ARRAY = "Array"


# Chat
class MessageType(Enum):
    INFO = "info"
    ERROR = "error"
    SUGGEST = "suggest"
    RESTART = "restart"
    END = "end"
