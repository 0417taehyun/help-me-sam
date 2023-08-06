from enum import Enum


class HTTPContentType(str, Enum):
    JSON: str = "application/json"


class HTTPStatusCode(Enum):
    OK: int = 200
    INTERNAL_SERVER_ERROR: int = 500
