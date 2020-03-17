"""


TODO:https://rcmdnk.com/blog/2017/04/22/blog-octopress-github/

"""
import csv
import os
from typing import List
import requests
import time
from typing import Dict
from dataclasses import dataclass
from config import ID, SECRET, TARGET_DICT
API_DOMAIN = "https://api.github.com/repos"
QUERY_PARAM = "?client_id={ID}&client_secret={SECRET}"


@dataclass
class Response:
    name: str
    version: str
    release_date: datetime

    # printした時のformat指定のメソッド↓
    def __repr__(self):
        return f"ver:{self.version},release_date:{self.release_date}\n"


def get_release_info(respository_path: str, name: str) -> Dict:
    """
    get release-infomatrion from github api!
    official document : https://developer.github.com/v3/git/tags/
    ----------
    repository_path : str   {author}/{name}
    Returns
    -------
    Dict
        response from github-api
    """
    def helper(url: str, verion_name: str) -> datetime:
        """
        get release date from github api!
        Parameters
        ----------
        url : [type]
            [description]

        Returns
        -------
        datetime
            [description]
        """
        res = requests.get(url+QUERY_PARAM).json()
        # T以降は時刻情報はいらないので取り除くex:2018-04-18T15:00:44Z
        date_str = res["commit"]["committer"]["date"].split("T")[0]
        release_date = datetime.strptime(date_str, "%Y-%m-%d")

        return Response(name, verion_name, release_date)

    # ex:https://api.github.com/repos/fuel/fuel/tags
    url = f"{API_DOMAIN}/{respository_path}/tags"
    response = requests.get(url+QUERY_PARAM)
    print(response.json())
    ver_list = []
    count = 0
    for ele in response.json():
        count += 1
        # github-APIのリクエスト制限を回避するための一次的処置
        if count == 5:
            break
        print(ele["commit"]["url"])
        ver_list.append(helper(ele["commit"]["url"], ele["name"]))
    # release_dateでsort
    if len(ver_list):
        ver_list = sorted(ver_list, key=lambda x: x.release_date, reverse=True)
        return ver_list[0]
    return None


def main():
    """
    github_repositoryから最新のverを取得
    """
    with open("tmp.csv", "w", encoding="utf-8", newline="")as writer:
        csv_writer = csv.writer(writer)
        csv_writer.writerow(["name", "version", "release-date"])
        for key in TARGET_DICT.keys():
            res = get_release_info(TARGET_DICT[key], key)
            if res:
                csv_writer.writerow(
                    [res.name, res.version, res.release_date.strftime("%Y/%m/%d")
                     ])


if __name__ == "__main__":
    # /fuel/fuel/releases
    # https://api.github.com/repos/dillonkearns/mobster/releases/latest
    url = " /repos/:owner/:repo/releases/latest"
    print("")
    # https://api.github.com/repos/fuel/fuel
    main()
