from enum import Enum


class AWSService(str, Enum):
    S3: str = "s3"


class AWSS3ClientMethod(str, Enum):
    PUT_OBJECT: str = "put_object"
    