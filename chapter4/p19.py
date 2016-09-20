#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

height_int = 0
weight_int = 0

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(height, weight):
    global height_int
    global weight_int

    try:
        height_int = int(height)
        weight_int = int(weight)
        if height_int < 0 or weight_int < 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    height = version_input("Your height: ")
    weight = version_input("Your Weight: ")

    if type_checking(height, weight) == False:
        print("Plese enter correct integer or enter an integer greater than 0.")
        sys.exit()

    inch = height_int * 0.393701
    pound = weight_int * 2.20462
    BMI = (pound / (inch * inch)) * 703
    print("Your BMI is %.1f." % BMI)
    
    if BMI >= 18.5 and BMI <= 25:
        print("You are within the ideal weight range.")
    else:
        print("You are overweight. You should see your doctor.")

