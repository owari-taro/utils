from operator import mul
from functools import reduce


try:
    while True:
        line=input("please enter a list of integer separted bty commas")
        try:
            num=list(map(int,line.split(",")))
        except ValueError:
            print("error enter only integers separated by commas")
            continue
        print("sum of input integers",sum(nums))
        print("product of input integers",reduce(mul,nums,1))
except KeyboardInterrupt:
    print("finished!!")