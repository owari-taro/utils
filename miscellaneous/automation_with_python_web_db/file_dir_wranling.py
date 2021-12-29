from os.path import abspath, dirname, join
#linux and windows  show each different print-statement
print("".join([dirname(abspath(__file__)), "/", "tmp"]))


from pathlib import Path

print(Path(__file__).resolve().parent.joinpath("tmp"))

print(Path("symbolic/./test.txt").resolve())+