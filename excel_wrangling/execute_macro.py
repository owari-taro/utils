"""
pythonをインストールしたら↓のコマンドで必用なライブラリーをインストールしてください

>pip install openpyxl

"""

import concurrent.futures as futures
from functools import wraps
import win32com.client
import os
import openpyxl as px
import os
from typing import List
import time
from retrying import retry
CURRENT_DIR = os.getcwd()

# 一旦マクロとテキストファイルの対応表を作って対処。あまりスマートではないが・・・・
config = {}


def check_file(macro_fname: str, fname_list: List):
    """マクロに対応するtxtファイルが存在するか否かを確認する！！"""
    target = config[macro_fname]
    print(target)
    for fname in fname_list:
        if fname.endswith(target):
            print("対象ファイルあり")
            return True
    print("########################################################s")
    print(f"{macro_fname}")
    print("########################################################")
    print("対象のファイルがないからパス!!!!!!!!!!!!!!!")
    return False


def elapsed_time(func):
    """処理時間計測のための関数
           デコレーターとして使う。デコレーターは対象の関数のdefの上に [@elapsed_time]のようにして使う.
           ↓のexecute_macroで使用している
    """
    @wraps(func)
    def new_function(*args, **kwargs):
        start = time.time()
        print("running fuction", func.__name__)
        res = func(*args, **kwargs)
        print("elapset time:", time.time()-start)
        return res
    return new_function


@elapsed_time
@retry(stop_max_attempt_number=3)
def execute_macro(fname: str, macro_name: str):
    # open file and execute a excel-macro
    print("{}を実行".format(macro_name))
    excel = win32com.client.Dispatch("Excel.Application")  # インスタンス生成
    excel.Visible = False  # エクセルを表示する設定（Falseにすれば非表示で実行される）
    excel.Workbooks.Open(Filename=os.path.join(
        CURRENT_DIR, fname), ReadOnly=False)  # ブックを読み取り専用で開く
    excel.Application.Run(macro_name)  # マクロ名を指定して実行（引数なしの場合マクロ名のみで実行可能）
    # ブックを保存して閉じる（SaveChangesを0にすると保存せず閉じる）
    excel.Workbooks(1).Close(SaveChanges=1)
    excel.Application.Quit()  # 終了


def main():
    fname_list = os.listdir()
    print("########################")
    for fname in fname_list:
        try:
            if fname.endswith(".xlsm") and check_file(fname, fname_list):
                print("################################################")
                print(fname)
                print("###############################################")
                execute_macro(fname, "バッチログコピー")
                execute_macro(fname, "ボタン2_Click")
                print("\n\n")

        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()
