from functools import wraps

def decol(f):
    print("decol colled")

    def wrapper():
        print("before exec")
        v = f()
        print("after exec")
        return v
    return wrapper


def document_it(func):
    """you can try this for debugging by decorator"""
    @wraps(func)
    #↑whithout this,decorated function's name is recognized as 'new_function'
    def new_function(*args, **kwargs):
        print("running fuction", func.__name__)
        print("positinal arguments", args)
        print("keyword arguments", kwargs)
        res = func(*args, **kwargs)
        print("result:", res)
        return res
    return new_function


@document_it
def add_ints(a, b):
    return a+b


@decol
# functional decorator ,decol get func as an argument and //////
def func():
    print("exec")
    return 1


if __name__ == "__main__":
    add_ints(a=321, b=321)
    add_ints(123, 321)
    print(add_ints.__name__)