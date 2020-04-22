import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper() -> str:
        return func().upper()
    return wrapper


def hoge(func):
    """without functools"""
    def wrapper() -> str:
        """wrapper hogehoge"""
        return func().upper()
    return wrapper


@uppercase
def greet():
    """return greeting message
    """
    return "Hello"


greet.__name__
greet.__doc__


@hoge
def hoge_greet():
    """return greeting message"""
    return "Hello"


hoge_greet.__name__
# not display decorated func's docstrings
hoge_greet.__doc__
