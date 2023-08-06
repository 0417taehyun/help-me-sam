from enum import Enum


class ApplicationLevel(str, Enum):
    LOCAL: str = "local"
    ALPHA: str = "alpha"
    PRODUCTION: str = "production"
