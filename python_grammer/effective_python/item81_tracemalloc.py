import tracemalloc
import os

class MyObject:
    def __init___(self):
        self.data = os.urandom(100)


def get_data():
    values = []
    for _ in range(100):
        obj = MyObject()
        values.append(obj)
    return values


def run():
    deep_values = []
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values


tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()
x = run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, "lineno")
for stat in stats[:3]:
    print(stat)
