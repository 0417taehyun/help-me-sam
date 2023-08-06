from src.custom import AWSS3ObjectModel
from src.service.api import SlackAPIService


class MessageService:
    def __init__(self, slack_client: SlackAPIService) -> None:
        self.slack_client: SlackAPIService = slack_client

    def _create_upload_message(self, aws_s3_object_model: AWSS3ObjectModel) -> str:
        return f"{aws_s3_object_model.bucket_name} 버킷에 업로드된 {aws_s3_object_model.object_key} 이름의 영상 썸네일 이미지 업로드 완료!"

    def send_message_with_file(self, channel: str, file: bytes, aws_s3_object_model: AWSS3ObjectModel) -> None:
        upload_message: str = self._create_upload_message(aws_s3_object_model=aws_s3_object_model)
        self.slack_client.upload_file(channel=channel, text=upload_message, file=file)
