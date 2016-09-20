#- coding:utf-8 -*-
#!/usr/bin/env python

import sys


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":
    first_str = version_input("Enter the first number: ")
    second_str = version_input("Enter the second number: ")
    third_str = version_input("Enter the third number: ")

    try:
        first = int(first_str)
        second = int(second_str)
        third = int(third_str)
    except ValueError:
        print("Please enter correct integer.")
        sys.exit()

    if first == second or first == third or second == third:
        sys.exit()
    
    if first > second and first > third:
        larger = first
    elif second > first and second > third:
        larger = second
    elif third > first and third > second:
        larger = third
    
    print("The largest number is %d."%larger)


