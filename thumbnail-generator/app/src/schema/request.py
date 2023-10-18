from typing import TypedDict


class AWSS3Bucket(TypedDict):
    name: str


class AWSS3Object(TypedDict):
    key: str


class AWSS3(TypedDict):
    bucket: AWSS3Bucket
    object: AWSS3Object


class AWSS3Record(TypedDict):
    s3: AWSS3


class AWSLambdaEvent(TypedDict):
    Records: list[AWSS3Record]


class AWSLambdaContext(TypedDict):
    pass
