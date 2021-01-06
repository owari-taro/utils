# coding: utf-8
import os
import csv
import openpyxl
DIR="tmp_csv"
from datetime import datetime

#xlsxをcsvファイルに変換するための関数
def convert_xlsx_into_csv(xlsx_fname):
    now=datetime.utcnow()
    # ブックを読み込みます。
    filepath = os.path.join(xlsx_fname)
    book = openpyxl.load_workbook(filepath, read_only=True, keep_vba=False)
    #(xlsxをcsv変換したファイルの)保存用dirが存在しなければ作成する
    if not os.path.exists("tmp_csv"):
        os.makedirs(DIR)

    # シートでループ
    for sheet in book.worksheets:
        sheet_name = sheet.title  # シート名を取得
        fname="tmp_{}".format(int(now.timestamp()))+".csv"
        fname=os.path.join(DIR,fname)
        with open(fname, 'w', encoding='utf-8',newline="") as writer:
            writer = csv.writer(writer)

            for cols in sheet.rows:
                writer.writerow([str(col.value or '') for col in cols])
        return fname

if __name__ == '__main__':
    convert_xlsx_into_csv("test.xlsx")