from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from random import uniform
from hashlib import md5
from pathlib import Path
from urllib import request
import time
from create_decorator import elapsed_time
from typing import List, Any


def test_function():
    return uniform(0, 1000)


def download(url):
    req = request.Request(url)
    name = md5(url.encode("utf-8")).hexdigest()
    file_path = f"./{name}"
    with request.urlopen(req)as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


@elapsed_time
def sequential(urls: List):
    for url in urls:
        try:
            download(url)
        except Exception as err:
            print(url)
            print(err)

if __name__ == "__main__":
    download("https://www.google.com")
    urls = ["https://www.google.com", "https://www.amazon.co.jp/", "http://gmail.com/",
            "https://toyota.jp/index.html", "https://twitter.com/junsaito0529"]
    sequential(urls)