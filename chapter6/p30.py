#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def multiplication_table(first_factor, second_factor):
    for first_num in range(0, first_factor+1):
        for second_num in range(0, second_factor+1):
            print("%d x %d = %d"%(first_num, second_num, first_num*second_num))



if __name__ == "__main__":
    
    input_first_factor = version_input("Enter first factor: ")
    input_second_factor = version_input("Enter second factor: ")

    try:
        first_factor = int(input_first_factor)
        second_factor = int(input_second_factor)
    except ValueError:
        print("Please enter correct Integer.")
        sys.exit()

    multiplication_table(first_factor, second_factor)

