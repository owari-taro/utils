from selenium import webdriver
from datetime import datetime
import os
import time
# import attr
from typing import List, Dict
from helper import Action, load_yaml
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
DRIVER_PATH = "drivers/chromedriver.exe"
YAML_FNAME = "hoge.yaml"


# @attr.s
class UIChecker:
    # 各自PCの環境ごとのchromedriveを用意してpathを指定してください
    def __init__(self):
        # save_dir = attr.ib(init=None)
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.implicitly_wait(30)
        self.count = 0
        # today = datetime.now().strftime()
        # self.save_dir = f"/tmp/{today}"

    # def __attrs_post_init__(self):
        # self.driver = webdriver.chrome(self.driver_path)
        # self.driver.implicitly_wait(30)
        # today = datetime.now().strftime()
        # self.save_dir = f"/tmp/{today}"

    def click(self, css_selector: str) -> None:
        button = self.driver.find_element_by_css_selector(css_selector)
        button.click()

    def exe(self):
        target: Dict = load_yaml(YAML_FNAME)
        for key in target.keys():
            self.check_page(target[key])
            # NotImplemented

    def check_page(self, page_info: Dict) -> None:
        """[summary]

        Parameters
        ----------
        pag_info : Dict
            yamlに書かれたページごとの対象selectorなどが書かれたdict
        """
        if page_info["url"]:
            self.driver.get(page_info["url"])
        print(page_info["name"])
        for action in page_info["actions"]:
            # 入力、クリックなどの動作を順に行う
            self.__action(action)

    def __action(self, action: Dict):
        if action["type"] == Action.CLICK.value:
            print("click")
            self.click(action["selector"])
        elif action["type"] == Action.INPUT.value:
            # inputは複数入可能なのでfor-loop
            for key in action["selector"].keys():
                self.input_form(key, action["selector"][key])
        elif action["type"] == Action.SELECT.value:
            print()
        else:
            print()

    def input_form(self, css_selector: str, content: str) -> None:
        # formに入力する
        form = self.driver.find_element_by_css_selector(css_selector)
        form.send_keys(content)

    def save_screenshot(self, name) -> None:
        fname: str = os.path.join(
            self.__save_dir, name+"_"+str(self.__count) + ".png")
        print("screenshot:{}".format(fname))
        self.driver.save_screenshot(fname)
        self.__count += 1


if __name__ == "__main__":
    checker = UIChecker()
    checker.exe()
