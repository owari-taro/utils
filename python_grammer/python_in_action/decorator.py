from functools import lru_cache
from time import sleep

@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    return n+1


if __name__=="__main__":
    print(heavy_function(10))
    #second time ,it respond much faster thanks to cache
    print(heavy_function(10))
