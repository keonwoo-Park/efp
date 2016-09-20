#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

age_int = 0

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(age):
    global age_int
    try:
        age_int = int(age)
        if age_int < 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    age = version_input("What is your age? ")
    if type_checking(age) == False:
        print("Plese enter correct integer or enter an integer greater than 0.")
        sys.exit()

    message = "You are old enough to legally drive." if age_int >= 16 else "You are not enough to legally drive."
    print(message)

