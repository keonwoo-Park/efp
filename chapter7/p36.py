#/usr/bin/env python

import sys
import math


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def calculate(response_list):
    total = 0
    deviation=0
    total = sum(response_list)
    average = total / len(response_list)
    min_number = min(response_list)
    max_number = max(response_list)


    for factor in response_list:
        deviation += pow((factor - average), 2)

    standard_deviation = math.sqrt(deviation / len(response_list))

    print("The average is %d." % average)
    print("The minimum is %d." % min_number)
    print("The maximum is %d." % max_number)
    print("The standard deviation is %.2f." % standard_deviation)



if __name__ == "__main__":
    response_list=[]
    while True:
        number_str = version_input("Enter a number: ")
        if number_str == "done":
            break
        try:
            number = int(number_str)
        except ValueError:
            print("Please enter correct integer number.")
        else:
            response_list.append(number)

    
    print(response_list)
    calculate(response_list)
