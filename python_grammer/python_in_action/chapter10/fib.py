import sys
import time
import os


def elapsed_time(f: function):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}")
        print(time.time()-st)
        return v
    return wrapper


def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1)+fib(n-2)

# TODO:write recursive ver


def fibonacci(n: int) -> int:
    """fibonacci:a(n)=a(n-1)+a(n-2)"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b+a
    else:
        return a


def get_sequential(nums: int):
    for num in nums:
        print(fibonacci(num))


def main():
    n = int(sys.argv[1])
    nums = [n]*os.cpu_count()
    get_sequential(nums)


# def main():
   # n = int(sys.argv[1])
    # print(fibonacci(n))


if __name__ == "__main__":
 #   main()
    print(fib(3))
    print(fib(10))
