import types


@types.coroutine
def read_data():
    def inner(n):
        try:
            print(f"printing from read_data:{n=}")
            callback = gen.send(n*2)
        except StopIteration:
            pass


async def process():
    try:
        while True:
            data = await read_data()
            print(f"printing from process():{data}")
    finally:
        print(f"processing done")

gen = process()
callback.send(None)


def main():
    for i in range(5):
        print(f"printing from main():{i}")
        callback(i)


if __name__ == "__main__":
    main()
