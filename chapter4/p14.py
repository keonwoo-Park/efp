#*- coding:utf-8 -*-
#!/usr/bin/env python

import sys
TAX_RATE = float(5.5)
WI_STATE = 'WI'
amount_int = 0
compare_list=['WI','wi','Wi','wI']

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(amount):
    global amount_int
    try:
        amount_int = int(amount)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    amount = version_input("What is the order amount?")
    state = version_input("What is the state?")
    
    if type_checking(amount) == False:
        print("Please enter the correct type!!")
        sys.exit()

    tax = round((amount_int * (TAX_RATE/100)), 2)
    total = round((amount_int + tax), 2)

    for name in compare_list:
        if state == name:
            print("The subtoatl is $%.2f\nThe tax is $%.2f\nThe total is $%.2f" % (float(amount), tax, total))
            sys.exit()

    print("The total is $%.2f" % total)

