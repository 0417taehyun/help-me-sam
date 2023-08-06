import json

from boto3 import client
from src.constant import AWSService, HTTPContentType, HTTPStatusCode
from src.core import get_settings
from src.custom import AWSLambdaContext, AWSLambdaEvent, AWSS3ObjectModel, HTTPResponse
from src.service import AWSClientFactory, AWSS3APIService, ImageService, MessageService, SlackAPIService
from src.util import AWSEventParser


def lambda_handler(event: AWSLambdaEvent, context: AWSLambdaContext) -> None:
    aws_client: client = AWSClientFactory.create(aws_service=AWSService.S3)
    aws_s3_client: AWSS3APIService = AWSS3APIService(aws_client=aws_client)
    slack_clinet: SlackAPIService = SlackAPIService()
    image_service: ImageService = ImageService(aws_s3_client=aws_s3_client)
    message_service: MessageService = MessageService(slack_client=slack_clinet)

    try:
        aws_s3_object_model: AWSS3ObjectModel = AWSEventParser.create_aws_s3_object_model(event=event)
        image_file: bytes = image_service.generate_thumbnail(aws_s3_object_model=aws_s3_object_model)
        message_service.send_message_with_file(
            channel=get_settings().SLACK_CHANNEL_ID, file=image_file, aws_s3_object_model=aws_s3_object_model
        )
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
