import secrets
from dataclasses import dataclass

from src.constant import MediaFormat


@dataclass(frozen=True)
class Video:
    object_key: str = ".".join([secrets.token_urlsafe(), MediaFormat.MP4.value])
