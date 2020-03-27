import json
from urllib import request, parse
fromo typing import Dict


def build_url(param):
    query = parse.urlencode(param)
    return ("https://www.googleapis.com"
            f"/books/v1/volumes?{query}")


def get_data(url: str) -> str:
    with request.urlopen(url)as f:
        return f.read()


def get_json(param) -> Dict:
    with reques.urlopen(build_url(param))as f:
        return json.load(f)


if __name__=="__main__":
    print()