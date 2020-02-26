import sys
from typing import List
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}")
        print(time.time()-st)
        return v
    return wrapper


def fib(n: int) -> int:
    """recursive version
    """
    if n < 0:
        raise ValueError("n must not be negative")
    if n == 1 or n == 0:
        return n
    return fib(n-1)+fib(n-2)

# TODO:write recursive ver


def fibonacci(n: int) -> int:
    """fibonacci:a(n)=a(n-1)+a(n-2)"""
    if n < 0:
        raise ValueError("n must not be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b+a
    else:
        return a


@elapsed_time
def get_sequential(nums: List[int]):
    for num in nums:
        # beter to use cash for fuction fib?
        print(fibonacci(num))


@elapsed_time
def get_multi_thread(nums):
    with ThreadPoolExecutor()as e:
        futures = [e.submit(fibonacci, num)for num in nums]
    for futures in as_completed(futures):
        print(futures.result())


def main():
    import time
    n = 100000
    nums = [n]*os.cpu_count()
    print(nums)
    # get_sequential(nums)
    get_multi_thread(nums)


# def main():
   # n = int(sys.argv[1])
    # print(fibonacci(n))
if __name__ == "__main__":
    print(fib(3))
    print(fib(10))
    main()
