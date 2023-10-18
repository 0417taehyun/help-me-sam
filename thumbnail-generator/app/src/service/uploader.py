from tempfile import NamedTemporaryFile

from boto3 import client

from src.constant import AWSService
from src.core import get_settings
from src.schema import AWSLambdaEvent, AWSS3Records, Image
from src.service.image import ImagerService
from src.util import AWSS3API


class UploadService:
    @staticmethod
    def generate_thumbnail(aws_s3_event: AWSLambdaEvent) -> bytes:
        images: list[Image] = AWSS3Records(records=aws_s3_event.get("Records")).images
        aws_s3_client: client = client(
            service_name=AWSService.S3.value,
            aws_access_key_id=get_settings().AWS_ACCESS_KEY_ID,
            aws_secret_access_key=get_settings().AWS_SECRET_ACCESS_KEY,
            region_name=get_settings().AWS_REGION_NAME,
            endpoint_url=get_settings().AWS_ENDPOINT_URL
        )
        aws_s3_api: AWSS3API = AWSS3API(client=aws_s3_client)
        image_service: ImagerService = ImagerService(aws_s3_api=aws_s3_api)
        for image in images:
            image_service.upload_image(image=image)
            