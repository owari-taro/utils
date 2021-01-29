import json
from typing import Dict, Any, IO
SIMPLE_TYPE = (int, str, bool)


def write_dict_summary(dict_: Dict, writer: IO, indent: int = 0):
    prefix = ","*indent
    for key in dict_.keys():
        value = dict_[key]
        type_ = type(value)
        if type_ in SIMPLE_TYPE:
            writer.write(prefix+f"{key},{value}\n")
        elif type_ is dict:
            writer.write(prefix+f"{key}\n")
            #indent = indent + 1
            print(f"{key=},{indent=}")
            write_dict_summary(value, writer, indent+1)
        elif type_ is list:
            writer.write(prefix+f"{key}\n")
            write_list_summary(value, writer, indent+1)


def write_list_summary(list_, writer, indent):
    prefix = ","*indent
    for ele in list_:
        if ele in SIMPLE_TYPE:
            writer.write(prefix+ele+"\n")
        elif type(ele) is dict:
            write_dict_summary(ele, writer, indent)


with open("tmp_.json", "r", encoding="utf-8")as reader:
    json_ = json.load(reader)
    ec2_ = json_["Reservations"][0]["Instances"][0]
    with open("tmp.csv", "w", encoding="utf-8")as writer:
        write_dict_summary(ec2_, writer)
