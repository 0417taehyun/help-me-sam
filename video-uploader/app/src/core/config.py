from functools import lru_cache

from pydantic import BaseSettings


class AWSSettings(BaseSettings):
    AWS_REGION_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_ENDPOINT_URL: str


class ApplicationSettings(AWSSettings):
    pass


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
