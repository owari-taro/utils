import boto3
import json
import logging
import os

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + str(message))

    # イベント種別
    EventType = message[0]['EventType']
    # コンピュータ名
    Hostname = message[0]['Hostname']
    # 変更監視ルール
    Reason = message[0]['Reason']

    if EventType == 'IntegrityEvent':
        slackColor = 'warning'

    # 変更監視イベントの出力
    if EventType == 'IntegrityEvent':
        ENCRYPTED_HOOK_URL = os.environ['kmsEncryptedHookUrl']
        SLACK_CHANNEL = '#security'
    HOOK_URL = "https://" + boto3.client('kms').decrypt(
        CiphertextBlob=b64decode(ENCRYPTED_HOOK_URL))['Plaintext'].decode('utf-8')
    slack_message = {
        'channel': SLACK_CHANNEL,
        'attachments': [
            {
                'fallback': 'DeepSecurity IntegrityEvent Alarm : ' + EventType,
                'color': slackColor,
                'title': 'DeepSecurity IntegrityEvent Alarm : ' + EventType,
                'fields': [
                    {
                        'title': 'イベント種別' + ':',
                        'value': EventType
                    },
                    {
                        'title': 'コンピュータ名' + ':',
                        'value': Hostname
                    },
                    {
                        'title': '変更監視ルール' + ':',
                        'value': Reason
                    }
                ],
                "footer": "Send from Amazon SNS"

            }
        ]
    }

    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
