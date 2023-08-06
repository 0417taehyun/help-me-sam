from typing import Optional, TypedDict


class AWSS3UserIdentity(TypedDict):
    principalId: str


class AWSS3Bucket(TypedDict):
    name: str
    ownerIdentity: AWSS3UserIdentity
    arn: str


class AWSS3Object(TypedDict):
    key: str
    size: int
    eTag: str
    sequencer: str


class AWSS3(TypedDict):
    s3SchemaVersion: str
    configurationId: str
    bucket: AWSS3Bucket
    object: AWSS3Object


class AWSS3RequestParameters(TypedDict):
    sourceIPAddress: str


AWSS3ResponseElements = TypedDict("AWSS3ResponseElements", {"x-amz-request-id": str, "x-amz-id-2": str})


class AWSS3Record(TypedDict):
    eventVersion: str
    eventSource: str
    awsRegion: str
    eventTime: str
    eventName: Optional[dict]
    userIdentity: AWSS3UserIdentity
    requestParameters: AWSS3RequestParameters
    responseElements: AWSS3ResponseElements
    s3: AWSS3


class AWSLambdaEvent(TypedDict):
    Records: list[AWSS3Record]


class AWSLambdaContext(TypedDict):
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    function_name: str
    memory_limit_in_mb: int
    function_version: str
    invoked_function_arn: str
    identity: Optional[dict]
    client_context: Optional[dict]
