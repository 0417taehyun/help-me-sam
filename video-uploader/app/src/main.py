import json

from pydantic import HttpUrl

from src.constant import HTTPStatusCode, HTTPContentType
from src.service import UploadService
from src.schema import AWSLambdaEvent, AWSLambdaContext, HTTPResponse


def lambda_handler(event: AWSLambdaEvent, context: AWSLambdaContext) -> None:
    try:
        url: HttpUrl = UploadService.get_upload_url()
        return HTTPResponse(
            statusCode=HTTPStatusCode.OK.value,
            headers={"Content-Type": HTTPContentType.JSON.value},
            body=json.dumps({"detail": url}),
        )

    except Exception as error:
        return HTTPResponse(
            statusCode=HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
            headers={"Content-Type": HTTPContentType.JSON.value},
            body=json.dumps({"detail": str(error)}),
        )
