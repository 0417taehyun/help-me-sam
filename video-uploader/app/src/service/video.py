from pydantic import HttpUrl

from src.schema import Video
from src.util import AWSS3APIInterface


class VideoService:
    _AWS_BUCKET_NAME: str = "help-me-sam"

    def __init__(self, aws_s3_api: AWSS3APIInterface) -> None:
        self.aws_s3_api: AWSS3APIInterface = aws_s3_api

    def get_upload_url(self, video: Video) -> HttpUrl:
        return self.aws_s3_api.generate_presigned_url(
            bucket_name=VideoService._AWS_BUCKET_NAME,
            object_key=video.object_key
        )

