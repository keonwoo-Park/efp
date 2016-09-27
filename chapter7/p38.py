#/usr/bin/env python

import sys


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def change_list_type(number_str_list):
    number_list=[]
    for num in number_str_list:
        try:
            number_list.append(int(num))
        except ValueError:
            print("Please enter only numbers.")
            sys.exit()
    return number_list


def filterEvenNumber(number):
    result_list=[]
    for num in number:
        if (num % 2) == 0:
            result_list.append(num)
    return result_list


def print_result(result):
    print("The even numbers are"),
    for num in result:
        print("%d " % num),
    

if __name__ == "__main__":
    input_list = version_input("Enter a list of numbers, separated by spaces:" )
    number_str_list = (input_list.split())
    number = change_list_type(number_str_list)

    result = filterEvenNumber(number)
    print_result(result)

