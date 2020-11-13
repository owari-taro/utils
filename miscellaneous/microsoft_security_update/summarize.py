import csv
import sys
from datetime import datetime
from helper import convert_xlsx_into_csv
import os
OUTPUT_DIR="OUTPUT"

class Element:
    def __init__(self,article_id:int,product:str,download:str):
        self.article_id=article_id
        self.cve_list=[]
        self.product=product
        self.impact_set=set()
        self.download=download
        self.score=set()
    def get_cve_str(self):
        output_str=""
        for ele in self.cve_list:
            output_str+=str(ele)+"\n"
        return output_str

def load_file(fname:str)->None:
    """microsoft updateを読み込んで結果をまとめたcsvを出力"""
    element_dict={}
    with open(fname,"r",encoding="utf-8")as reader:
        csv_reader=csv.reader(reader)
        #headerはパス
        header=next(reader)
        for row in csv_reader:
            print(row)
            article_id=row[5]
            product=row[1]
            cve_id=row[-2]
            impact=row[4]
            download=row[6]
            score=row[-1]
            element_dict.setdefault(article_id,Element(article_id,product,download))
            element_dict[article_id].score.add(score)
            element_dict[article_id].cve_list.append(cve_id)
            element_dict[article_id].impact_set.add(impact)
    now=datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    output_fname=os.path.join(OUTPUT_DIR,"test_{}.csv".format(now))
    write_csv(output_fname,list(element_dict.values()))

def write_csv(fname,output_list):
    with open(fname,"w",encoding="utf-8")as writer:
        csv_writer=csv.writer(writer,lineterminator="\n")
        csv_writer.writerow(["article_id","cve","product","impact","download","base_score"])
        for ele in output_list:
            csv_writer.writerow([ele.article_id,ele.get_cve_str(),ele.product,str(ele.impact_set),ele.download,max(ele.score)])
        


if __name__=="__main__":
    args=sys.argv
    xlsx_fname=args[1]
    csv_fname=convert_xlsx_into_csv(xlsx_fname)
    load_file(csv_fname)
