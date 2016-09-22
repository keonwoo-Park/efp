#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":

    while True:
        input_rate = version_input("What is the rate of return? ")
        try:
            rate = int(input_rate)
            if rate == 0:
                print("Rate %d is not use."%rate)
            else:
                years = 72/rate
                print("It will take %d years to double your initial investment." % years)
                break
        except ValueError:
            print("Sorry. That's not a valid input.")

