from enum import Enum
from typing import Dict
import yaml


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


if __name__ == "__main__":
    print("click")
    print(Action.INPUT)
    hoge = load_yaml("hoge.yaml")
    print(hoge["page2"]["url"])
