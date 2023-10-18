import json

from src.constant import HTTPStatusCode, HTTPContentType
from src.schema import AWSLambdaEvent, AWSLambdaContext, HTTPResponse
from src.service import UploadService


def lambda_handler(event: AWSLambdaEvent, context: AWSLambdaContext) -> None:
    try:
        UploadService.generate_thumbnail(aws_s3_event=event)
        return HTTPResponse(
            statusCode=HTTPStatusCode.OK.value,
            headers={"Content-Type": HTTPContentType.JSON.value},
            body=json.dumps({"detail": "success"}),
        )

    except Exception as error:
        return HTTPResponse(
            statusCode=HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
            headers={"Content-Type": HTTPContentType.JSON.value},
            body=json.dumps({"detail": str(error)}),
        )
