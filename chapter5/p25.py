#- coding:utf-8 -*-
#!/usr/bin/env python

import sys
import re


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def passwordValidator(password):
    check_int = False
    check_str = False
    check_spe = False
    length = len(password)
    
    for ch in password:
        ascii_num = ord(ch)
        if ascii_num >= 48 and ascii_num <= 57:
            check_int = True
        elif (ascii_num >= 65 and ascii_num <=90) or (ascii_num >=97 and ascii_num <= 122):
            check_str = True
        elif (ascii_num >= 33 and ascii_num <=47) or (ascii_num >=58 and ascii_num <=64) or (ascii_num >= 91 and ascii_num <= 96) or (ascii_num >=123 and ascii_num <= 126):
            check_spe = True
        else:
            print("input value not ascii range.")
            sys.exit()

    if length <= 8:
        if check_int == True and check_str == False and check_spe == False:
            return "very weak"
        elif check_str == True and check_int == False and check_spe == False:
            return "weak"
        else:
            return "nothing"
    else:
        if check_int == True and check_str == True and check_spe == False:
            return "strong"
        elif check_str == True and check_int == True and check_spe == True:
            return "very strong"
        else:
            return "nothing"
        

if __name__ == "__main__":
    password = version_input("input password : ")
    return_value = passwordValidator(password)

    print("The password \'%s\' is a %s."%(password, return_value))
