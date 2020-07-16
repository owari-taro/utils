from selenium import webdriver
from datetime import datetime
import os
# import attr
from typing import List, Dict
from helper import Action, load_yaml, Browser, upload_image
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
YAML_FNAME = "hoge.yaml"


# @attr.s
class UIChecker:
    def __init__(self):
        # save_dir = attr.ib(init=None)
        #driver is set at exe method
        self.driver = None  # webdriver.Chrome(DRIVER_PATH)
        self.count = 0
        today = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.save_dir = f"screenshots/{today}"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    # def __attrs_post_init__(self):
        # self.driver = webdriver.chrome(self.driver_path)
        # self.driver.implicitly_wait(30)
        # today = datetime.now().strftime()
        # self.save_dir = f"/tmp/{today}"

    def exe(self, yaml_fname: str = YAML_FNAME):
        """
        load a yamle file which is written how selenium works,
        then activate selenium accordingly.

        Parameters
        ----------
        yaml_fname : str, optional
            [description], by default YAML_FNAME
        """        
        yaml: Dict = load_yaml(yaml_fname)
        settings = yaml.pop("settings")
        self.set_browser_driver(
            settings[0]["browser"], settings[0]["driver_path"])

        for each_page in yaml["screen_transition"]:
            print(each_page)
            self.check_page(each_page)

    def set_browser_driver(self, browser: str, driver_path: str) -> None:

        if browser == Browser.CHROME.value:
            self.driver = webdriver.Chrome(driver_path)
        else:
            raise NotImplementedError
        self.driver.implicitly_wait(30)

    def click(self, css_selector: str) -> None:
        button = self.driver.find_element_by_css_selector(css_selector)
        button.click()
        # NotImplemented

    def check_page(self, page_info: Dict) -> None:
        """[summary]

        Parameters
        ----------
        pag_info : Dict
            yamlに書かれたページごとの対象selectorなどが書かれたdict
        """
        self.page_name = page_info["page_name"]
        if page_info["url"]:
            self.driver.get(page_info["url"])
        print(page_info["page_name"])
        for action in page_info["actions"]:
            # 入力、クリックなどの動作を順に行う
            self.__action(action)

    def __action(self, action: Dict) -> None:
        if action["type"] == Action.CLICK.value:
            self.click(action["selector"])
        elif action["type"] == Action.INPUT.value:
            # inputは複数入可能なのでfor-loop
            self.input_form(action["selector"], action["value"])
        elif action["type"] == Action.SCREENSHOT.value:
            self.screenshot()
        else:
            NotImplemented

    def input_form(self, css_selector: str, content: str) -> None:
        form = self.driver.find_element_by_css_selector(css_selector)
        form.send_keys(content)

    def screenshot(self) -> None:
        self.count += 1
        fname: str = os.path.join(
            self.save_dir, f"{self.count}_{self.page_name}.png")
        print("screenshot:{}".format(fname))
        self.driver.save_screenshot(fname)
        upload_image(fname)


if __name__ == "__main__":
    checker = UIChecker()
    checker.exe()
