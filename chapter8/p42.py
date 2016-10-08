#/usr/bin/env python

import sys
from operator import itemgetter


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def read_file():
    get_list=[]
    with open("input_data/p42.txt", 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            get_list.append(line.split(','))
    
    sort_list = sorted(get_list, key=itemgetter(2))
    return sort_list


def get_max_length(name_list):
    str_len = {"Last_len":0, "First_len":0, "Salary":0}
    for name in name_list:
        if str_len.get("Last_len") < len(name[0]):
            str_len["Last_len"] = len(name[0])

        if str_len.get("First_len") < len(name[1]):
            str_len["First_len"] = len(name[1])
    return str_len    


def list_print(name_list, max_len):
    gap = 0
    space = " "
    print("Last     First    Salary\n------------------------")
    for people in name_list:
        if len(people[0]) <= max_len.get("Last_len"):
            gap = max_len.get("Last_len") - len(people[0]) + 1
            message = (people[0] + space*gap)

        if len(people[1]) <= max_len.get("First_len"):
            gap = max_len.get("First_len") - len(people[1]) + 1
            message += (people[1] + space*gap)
        
        message += people[2]
        print(message)
        message = ""


if __name__ == "__main__":
    name_list = read_file()
    max_len = get_max_length(name_list)
    list_print(name_list, max_len)

