import attr
from typing import Iterable, List  # E,List,Union
FILE_PATH = "item31_data.txt"


@attr.s
class ReadVisit:
    file_path: str = attr.ib(default=FILE_PATH)

    def __iter__(self):
        print("__iter__ is called")
        print(self.file_path)
        with open(self.file_path, "r", encoding="utf-8")as reader:
            for line in reader:
                yield int(line)


def normalize(numbers: Iterable) -> List:
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

def read_visits(file_path=FILE_PATH):
    with open(file_path, "r", encoding="utf-8")as reader:
        for line in reader:
            yield int(line)


if __name__ == "__main__":
    hoge = ReadVisit()
    print(iter(hoge) is hoge)
    tmp=read_visits()
    print(iter(tmp) is tmp)
    # for ele in hoge:
    #   print(ele)
    #res = normalize(hoge)
    # print(res)
