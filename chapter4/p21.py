#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

month_int = 0

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(monty):
    global month_int

    try:
        month_int = int(month)
        if month_int < 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    dic = {1:"Janury", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"Agust", 9:"September", 10:"October", 11:"November", 12:"December"}
    month = version_input("Please enter the number of the month: ")

    if type_checking(month) == False:
        print("Please enter correct integer or enter an integer greater than 0.")
        sys.exit()

    if month_int > 12 :
        print("please enter month 1~12 range.")
        sys.exit()

    print("The name of the month is %s"%dic.get(month_int) )
    
