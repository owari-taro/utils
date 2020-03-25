class ContextManager:
    def __enter__(self):
        print("__enter was called")

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ was called")
        print(f"{exc_type=}")
        print(f"{exc_value=}")
        print(f"{traceback=}")


with ContextManager():
    print("insitde the block")
