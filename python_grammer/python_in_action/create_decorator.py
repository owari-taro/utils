from functools import wraps
import time


def decol(f):
    print("decol colled")

    def wrapper():
        print("before exec")
        v = f()
        print("after exec")
        return v
    return wrapper


def elapsed_time(func):
    """used as decorator to display elapsed time"""
    @wraps(func)
    def new_function(*args, **kwargs):
        start = time.time()
        print("running fuction", func.__name__)
        res = func(*args, **kwargs)
        print("elapset time:",time.time()-start)
        return res
    return new_function


def document_it(func):
    """you can try this for debugging by decorator"""
    @wraps(func)
    # ↑whithout this,decorated function's name is recognized as 'new_function'
    def new_function(*args, **kwargs):
        print("running fuction", func.__name__)
        print("positinal arguments", args)
        print("keyword arguments", kwargs)
        res = func(*args, **kwargs)
        print("result:", res)
        return res
    return new_function


@elapsed_time
# document_it
def add_ints(a, b):
    return a+b


# @decol
# functional decorator ,decol get func as an argument and //////
def func():
    print("exec")
    return 1


if __name__ == "__main__":
    add_ints(a=321, b=321)
    add_ints(123, 321)
    print(add_ints.__name__)
