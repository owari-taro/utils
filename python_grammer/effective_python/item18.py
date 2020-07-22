from typing import Hashable


def open_picture(fname: str):
    try:
        return open(fname, "a+b")
    except OsError:
        print(f"failed to open a file:{}")
        raise


class Picture(dict):
    def __missing__(self, key: Hashable):
        """
        you can set default value with this method when key is not in the dictionary obj

        Parameters
        ----------
        key : Hashable
            [description]

        Returns
        -------
        [type]
            [description]
        """        
        value = open_picture(key):
        self[key] = value
        return value
