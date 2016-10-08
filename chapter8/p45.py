#usr/bin/env python

import sys

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_data():
    with open("input_data/p45.txt", 'r') as f:
        data = f.read()
    return data


def set_data(output_name, replace_data):
    path = "result_data/" + output_name
    with open(path, 'w') as f:
        f.write(replace_data)



if __name__ == "__main__":
    output_name = version_input("Enter output file name: ")
    input_data = get_data()
    
    count = input_data.count("utilize") 
    replace_data = input_data.replace("utilize", "use")

    set_data(output_name, replace_data)
    print("Replace count: %d" % count)
