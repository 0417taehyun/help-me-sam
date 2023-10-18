from abc import ABC, abstractmethod

from boto3 import client


class AWSS3APIInterface(ABC):
    @abstractmethod
    def upload_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        ...

    @abstractmethod
    def download_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        ...


class FakeAWSS3API(AWSS3APIInterface):
    def upload_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        return

    def download_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        pass


class AWSS3API(AWSS3APIInterface):
    def __init__(self, client: client) -> None:
        self.client: client = client

    def upload_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        self.client.upload_file(Bucket=bucket_name, Key=object_key, Filename=file_name)
        
    def download_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        self.client.download_file(Bucket=bucket_name, Key=object_key, Filename=file_name)        
