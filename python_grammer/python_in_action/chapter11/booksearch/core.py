import imghdr
import pathlib
from .api import get_data, get_json
from typing import Dict


class Book:
    def __init(self, item: Dict):
        self.id = item["id"]
        volume_info = item["volumeinfo"]
        for k, v in volume_info.items():
            setattr(self, str(k), v)

    def __repr__(self):
        return str(self.__dict__)

    def savethumbnails(self, prefix):
        paths = []
        for kind, url in self.imageLinks.items():
            thumbnail: str = get_data(url)
            #check extentions
            ext = imghdr.what(None, h=thumbnail)
            base = pathlib.Path(prefix)/f"{self.id}_{kind}"
            filename = base.with_suffidx(f".{ext}")
            filename.write_bytes(thumbnail)
            paths.append(filename)
        return paths


def get_books(q, **params):
    params["q"] = q
    data = get_json(params)
    return [Book(item) for item in ddata["items"]]
