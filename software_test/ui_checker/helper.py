import requests
from enum import Enum
from typing import Dict
import yaml
TOKEN = ""
CHANNEL_ID = ""


class Browser(Enum):
    CHROME = "chrome"
    IE = "ie"
    EDGE = "edge"


class Action(Enum):
    CLICK = "click"
    INPUT = "input"
    SELECT = "select"
    SCREENSHOT = "screenshot"


def load_yaml(fname: str) -> Dict:
    with open(fname, "r", encoding="utf-8")as reader:
        obj = yaml.safe_load(reader)
        return obj


def upload_image_to_slack(fname: str, token: str = TOKEN, channel_id: str = CHANNEL_ID) -> None:
    files = {'file': open(fname, 'rb')}
    param = {'token': token, 'channels': channel_id}
    res = requests.post(
        url="https://slack.com/api/files.upload", params=param, files=files)
    print(res)


if __name__ == "__main__":
    print("click")
    print(Action.INPUT)
    hoge = load_yaml("hoge.yaml")
    print(hoge["page2"]["url"] is None)
