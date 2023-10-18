from boto3 import client
from pydantic import HttpUrl

from src.constant import AWSService
from src.core import get_settings
from src.schema import AWSLambdaEvent, Video
from src.service.video import VideoService
from src.util import AWSS3API


class UploadService:
    @staticmethod
    def get_upload_url() -> HttpUrl:
        video: Video = Video()
        aws_s3_client: client = client(
            service_name=AWSService.S3.value,
            aws_access_key_id=get_settings().AWS_ACCESS_KEY_ID,
            aws_secret_access_key=get_settings().AWS_SECRET_ACCESS_KEY,
            region_name=get_settings().AWS_REGION_NAME,
            endpoint_url=get_settings().AWS_ENDPOINT_URL
        )
        aws_s3_api: AWSS3API = AWSS3API(client=aws_s3_client)
        video_service: VideoService = VideoService(aws_s3_api=aws_s3_api)
        return video_service.get_upload_url(video=video, aws_s3_api=aws_s3_api)
        
