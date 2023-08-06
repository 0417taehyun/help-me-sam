from typing import TypedDict


class HTTPResponse(TypedDict):
    statusCode: int
    headers: dict[str, str]
    body: str
