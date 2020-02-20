from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from random import uniform
from hashlib import md5
from pathib import Path
from urllib import request
import time


def test_function():
    return uniform(0, 1000)


def download(url):
    req = request.Request(url)
    name = md5(url.encode("utf-8"))
    file_path = f"./{name}"
    with request.urlopen(req)as res:
        Path(file_path).write_bytes(res.read())
        return url, file_pa


if __name__ == "__main__":

    future = ThreadPoolExecutor().submit(test_function)
    print(isinstance(future, Future))
    print(future.result())
    print(future.done())
    ########################################

