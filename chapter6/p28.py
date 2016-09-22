#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":
    total = 0

    count_str = version_input("Enter root count: ")
    try:
        count = int(count_str)
    except ValueError:
        print("Please enter correct interger.")
        sys.exit()

    for num in range(0, count):
        input_number = version_input("Enter a number: ")
        try:
            number = int(input_number)
        except ValueError:
            print("%s is not Integer."%input_number)
            continue
        total = total + number        

    print("The total is %d."%total)
