from boto3 import client
from src.constant import ApplicationLevel, AWSService
from src.core import get_settings


class AWSClientFactory:
    @staticmethod
    def create(aws_service: AWSService) -> client:
        if get_settings().LEVEL == ApplicationLevel.LOCAL.value:
            return client(
                service_name=aws_service.value,
                region_name=get_settings().AWS_REGION_NAME,
                aws_access_key_id=get_settings().AWS_ACCESS_KEY_ID,
                aws_secret_access_key=get_settings().AWS_SECRET_ACCESS_KEY,
                endpoint_url=get_settings().AWS_ENDPOINT_URL,
            )

        return client(service_name=aws_service.value)


class AWSS3APIService:
    def __init__(self, aws_client: client) -> None:
        self.client: client = aws_client

    def upload_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        self.client.upload_file(Bucket=bucket_name, Key=object_key, Filename=file_name)

    def download_object(self, bucket_name: str, object_key: str, file_name: str) -> None:
        self.client.download_file(Bucket=bucket_name, Key=object_key, Filename=file_name)
