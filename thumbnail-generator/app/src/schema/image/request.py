import secrets
from dataclasses import dataclass

from src.constant import MediaFormat
from src.schema.request import AWSS3Record, AWSS3


@dataclass(frozen=True)
class Image:
    bucket_name: str
    video_object_key: str

    @property
    def image_object_key(self) -> str:
        return self.video_object_key.replace(MediaFormat.MP4.value, MediaFormat.JPEG.value)
    

@dataclass
class AWSS3Records:
    records: list[AWSS3Record]

    @property
    def images(self) -> list[Image]:
        images: list[Image] = []
        for record in self.records:
            s3_information: AWSS3 = record.get("s3")
            image: Image = Image(
                bucket_name=s3_information.get("bucket").get("name"),
                video_object_key=s3_information.get("object").get("key")
            )
            images.append(image)

        return images
    