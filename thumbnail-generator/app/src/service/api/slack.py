from typing import IO

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
from src.core import get_settings


class SlackAPIService:
    def __init__(self) -> None:
        self.client: WebClient = WebClient(token=get_settings().SLACK_BOT_TOKEN)

    def upload_file(self, channel: str, text: str, file: bytes) -> None:
        response: SlackResponse = self.client.files_upload_v2(file=file, channel=channel, initial_comment=text)
        if not response.get("ok"):
            raise Exception(str(response.get("error")))
