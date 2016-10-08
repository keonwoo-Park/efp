#/usr/bin/env python

import sys
from operator import itemgetter


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def read_file():
    name_list=[]
    with open("input_data/p41.txt", 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            name_list.append(line.split(','))
    
    sort_list = sorted(name_list, key=itemgetter(0))   
    return sort_list


def write_file(sorted_list):
    with open("result_data/p41-result.txt", "w") as f:
        f.write("Total of %d names\n" % len(sorted_list))
        f.write("-----------------\n")
        for info in sorted_list:
            name = "%s,%s\n" % (info[0], info[1])
            f.write(name)


if __name__ == "__main__":
    sorted_list = read_file()
    write_file(sorted_list)
