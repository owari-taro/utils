import csv
import os
from typing import Set, List
# csvファイルの説明のindex
INDEX = 10


def merge_csv_files(dir_name: str, output_csv_name: str):
    """csvファイルをmergeする。ただし重複行は無視する"""
    fnames: List = os.listdir(dir_name)
    # sort
    fnames: List[str] = sorted(fnames, key=lambda x: (len(x), str(x)))
    print(fnames)
    # 説明のset,重複があるかを判断するのに使う
    explanation_set: Set = set()
    with open(output_csv_name, "w", encoding="shift-jis", newline="")as writer:
        csv_writer = csv.writer(writer)
        for fname in fnames:
            if not fname.endswith(".csv"):
                continue
            with open(os.path.join(dir_name, fname), "r", encoding="shift-jis") as reader:
                reader.readline()
                csv_reader = csv.reader(reader)
                for ele in csv_reader:
                    if not ele[INDEX] in explanation_set:
                        print(ele[INDEX])
                        explanation_set.add(ele[INDEX])
                        csv_writer.writerow(ele)


if __name__ == "__main__":
    merge_csv_files("1213", "merged1213.csv")
