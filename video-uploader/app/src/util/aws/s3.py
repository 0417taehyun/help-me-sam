from abc import ABC, abstractmethod

from boto3 import client
from pydantic import HttpUrl

from src.constant import AWSS3ClientMethod


class AWSS3APIInterface(ABC):
    @abstractmethod
    def generate_presigned_url(self, bucket_name: str, object_key: str) -> HttpUrl:
        ...


class FakeAWSS3API(AWSS3APIInterface):
    def generate_presigned_url(self, bucket_name: str, object_key: str) -> HttpUrl:
        return


class AWSS3API(AWSS3APIInterface):
    def __init__(self, client: client) -> None:
        self.client: client = client

    def generate_presigned_url(self, bucket_name: str, object_key: str) -> HttpUrl:
        return self.client.generate_presigned_url(
            ClientMethod=AWSS3ClientMethod.PUT_OBJECT.value,
            Params={"Bucket": bucket_name, "Key": object_key}
        )
