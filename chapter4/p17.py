#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":
    weight_st = version_input("What is your weight? ")
    sex = version_input("What is your sex?")
    #quantity = version_input("How much can you drink?")
    alcohol_quantity_st = version_input("How many you drank cup?") 
    time_st = version_input("When did you drink alcohol?")

    try:
        weight = int(weight_st)
        alcohol_quantity = int(alcohol_quantity_st) 
        time = int(time_st)
    except ValueError:
        print("Please Enter correct integer.")
        sys.exit()

    MAN = 0.73
    GIRL =  0.6

    r = MAN if sex == "man" else GIRL
    BAC = (alcohol_quantity * 5.14 / weight * r ) - .015 * time
    
    if BAC < 0.08:
        print("Your BAC is %.2f\nIt is legal for you to drive."%BAC)
    else:
        print("Your BAC is %.2f\nIt is not legal for you to drive."%BAC)
    
