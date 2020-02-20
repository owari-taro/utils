from functools import lru_cache
from time import sleep
from dataclasses import dataclass


@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    return n+1


@dataclass(frozen=True)
class Fruit:
    name: str
    price: int = 0


if __name__ == "__main__":
    print(heavy_function(10))
    # second time ,it respond much faster thanks to cache
    print(heavy_function(10))
    fruit = Fruit("aaa", 123)
    print(fruit.name)
    fruit.name = "apple"
