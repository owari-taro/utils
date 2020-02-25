import sys
import time


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


#def main():
   # n = int(sys.argv[1])
    #print(fibonacci(n))


if __name__ == "__main__":
 #   main()
    print(fib(3))
    print(fib(10))