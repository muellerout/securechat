from celery import shared_task
from dlptool.core import detect_data_leaks
from slack.models import DataLeak, Regex
import slackapi
import os
from const import DLPTOOL_INPUT_FILE_PATH


@shared_task
def process_data_leak(message_text, channel, message_ts, regexs):
    with open(DLPTOOL_INPUT_FILE_PATH, "w") as inputfile:
        filepath = os.path.abspath(inputfile.name)

        inputfile.write(message_text)

    if catching_regex := detect_data_leaks(filepath, regexs):
        DataLeak.objects.create(
            message=message_text, catching_regex=Regex.objects.get(entry=catching_regex)
        )

        slackapi.delete_message(channel=channel, message_ts=message_ts)
