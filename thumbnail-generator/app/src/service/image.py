import subprocess
from tempfile import NamedTemporaryFile

from src.constant import MediaFormat
from src.schema import Image
from src.util import AWSS3APIInterface


class ImagerService:
    def __init__(self, aws_s3_api: AWSS3APIInterface) -> None:
        self.aws_s3_api: AWSS3APIInterface = aws_s3_api

    def _extract(self, video_file_name: str, image_file_name: str) -> None:
        subprocess.run(["./ffmpeg", "-y", "-ss", "00:00:10", "-i", video_file_name, "-vframes", "1", image_file_name])        

    def upload_image(self, image: Image) -> None:
        with NamedTemporaryFile(delete=True, suffix=f".{MediaFormat.MP4.value}") as video_file:
            self.aws_s3_api.download_object(
                bucket_name=image.bucket_name,
                object_key=image.video_object_key,
                file_name=video_file.name,
            )

            with NamedTemporaryFile(delete=True, suffix=f".{MediaFormat.JPEG.value}") as image_file:
                self._extract(video_file_name=video_file.name, image_file_name=image_file.name)
                self.aws_s3_api.upload_object(
                    bucket_name=image.bucket_name,
                    object_key=image.image_object_key,
                    file_name=image_file.name,
                )
