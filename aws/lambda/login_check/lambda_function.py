from requests import post
from requests.auth import HTTPBasicAuth
from retrying import retry
import traceback
import time
URL = ""
ID = ""
PASSWORD = ""


@retry(stop_max_attempt_number=3, wait_fixed=2000)
def login_check(url: str = URL, id: str = ID, password: str = PASSWORD) -> None:
    """
    basic認証できるかの確認する
    3回リトライし、リトライごとに1s待つ
    Parameters
    ----------
    url : str, optional
        [description], by default URL
    id : str, optional
        [description], by default ID
    password : str, optional
        [description], by default PASSWORD

    Raises
    ------
    Exception
        [description]
    """

    start = time.time()
    try:

        response = post(
            url, timeout=10,
            auth=HTTPBasicAuth(id, password)
        )
        elapsed = time.time()-start
        if response.status_code == 200:
            print(f"status check is ok. URL:{url}  time:{elapsed}")
        else:
            print(f"status is {response.status_code}.URL:{url} time:{elapsed}")

    except Exception:
        print(traceback.format_exc())
        raise Exception


if __name__ == "__main__":
    login_check()
