import attr
from typing import Iterable  # E,List,Union


@attr.s
class ReadVisit:
    file_path: str = attr.ib(default="item31_data.txt")
    def __iter__(self):
        print("__iter__ is called")
        print(self.file_path)
        with open(self.file_path, "r", encoding="utf-8")as reader:
            for line in reader:
                yield int(line)


def normalize(numbers: Iterable):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


if __name__ == "__main__":
    hoge = ReadVisit()
    #for ele in hoge:
     #   print(ele)
    res=normalize(hoge)
    print(res)