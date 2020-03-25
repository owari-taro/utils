from contextlib import contextmanager


class ContextManager:
    def __enter__(self):
        print("__enter was called")

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ was called")
        ##print(f"{exc_type=}")
        #print(f"{exc_value=}")
        #print(f"{traceback=}")


#with ContextManager():
 #   print("insitde the block")


@contextmanager
def point(*kwargs):
    print("__enter__ was called")
    value = kwargs
    try:
        yield value
    except Exception as e:
        print(e)
        raise
    finally:
        print("__exit__ was called")
        print(value)


with point(x=1, z=2)as p:
    print(type(p))
    print(p)
    p["z"] = 3
