import os
from slack_sdk import WebClient

client = WebClient(os.environ.get("SLACK_API_TOKEN"))


def delete_message(channel, message_ts):
    client.chat_delete(channel=channel, ts=message_ts)
