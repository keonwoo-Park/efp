#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

Eau_Claire = 0.005
Dunn = 0.004
Illinois = 0.08
Wisconsin = 0.055
amount_int = 0

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(amount):
    global amount_int

    try:
        amount_int = int(amount)
        if amount_int < 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    amount = version_input("What is the order amount?")
    state = version_input("What state do you live in?")

    if type_checking(amount) == False:
        print("Plese enter correct integer or enter an integer greater than 0.")
        sys.exit()
    
    if state == "Wisconsin":
        county = version_input("What county do you live in?")
        if county == "Eau Claire":
            county_tax = Eau_Claire
        else:
            county_tax = Dunn

        tax = round(amount_int * Wisconsin, 2)
        ctax = round(amount_int * county_tax, 2)
        total_tax = round( tax + ctax, 2)
        total = amount_int + total_tax
        message = "The state tax is $%.2f.\nThe county tax is$%.2f.\nThe total tax is $%.2f\nThe total is $%.2f" \
                    %(tax, ctax, total_tax, total)
    elif state == "Illinois":
        tax = round(amount_int * Illinois, 2)
        total = amount_int + tax
        message = "The state tax is $%.2f.\nThe total is $%.2f" %(tax, total)
    else:
        message = "The total is $%.2f" % amount_int

    print(message)






