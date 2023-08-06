from tempfile import NamedTemporaryFile

from src.constant import MediaFormat
from src.custom import AWSS3ObjectModel
from src.service.api import AWSS3APIService
from src.util import ThumbnailImageExtractor


class ImageService:
    def __init__(self, aws_s3_client: AWSS3APIService) -> None:
        self.aws_s3_client: AWSS3APIService = aws_s3_client

    def _create_image_object_key(self, object_key: str) -> str:
        return object_key.replace(MediaFormat.MP4.value, MediaFormat.JPEG.value)

    def generate_thumbnail(self, aws_s3_object_model: AWSS3ObjectModel) -> bytes:
        with NamedTemporaryFile(delete=True, suffix=f".{MediaFormat.MP4.value}") as video_file:
            self.aws_s3_client.download_object(
                bucket_name=aws_s3_object_model.bucket_name,
                object_key=aws_s3_object_model.object_key,
                file_name=video_file.name,
            )

            with NamedTemporaryFile(delete=True, suffix=f".{MediaFormat.JPEG.value}") as image_file:
                ThumbnailImageExtractor.run(video_file_name=video_file.name, image_file_name=image_file.name)
                image_file_object_key: str = self._create_image_object_key(object_key=aws_s3_object_model.object_key)
                self.aws_s3_client.upload_object(
                    bucket_name=aws_s3_object_model.bucket_name,
                    object_key=image_file_object_key,
                    file_name=image_file.name,
                )
                image_file.seek(0)
                image_file_content: bytes = image_file.read()
                return image_file_content
