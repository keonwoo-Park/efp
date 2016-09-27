#/usr/bin/env python

import sys
import math


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def calculate(response_list):
    total = 0
    deviation=0
    print("len : %d" % len(response_list))
    total = sum(response_list)
    average = total / len(response_list)
    min_number = min(response_list)
    max_number = max(response_list)


    for factor in response_list:
        print(pow((factor - average), 2))
        deviation += pow((factor - average), 2)
        print("deviatoin %d"%deviation)

    tt = deviation / len(response_list)

    standard_deviation = tt**0.5
   # standard_deviation = math.sqrt(deviation / len(response_list))


    print("The average is %d." % average)
    print("The minimum is %d." % min_number)
    print("The maximum is %d." % max_number)
    print("The standard deviation is %.2f." % standard_deviation)






'''
    for factor in response_list:
        total += factor


    
    for factor in response_list:

        #deviation += pow((factor - total), 2)
        deviation += ((factor - average)**2)
        print("factor : %d"%factor)
        print("chaee: %d"%(factor-average))
        print("jecoq : %d"%((factor-average)**2))
        print("deviation : %d"%deviation)
    standard_deviation = math.sqrt(deviation / len(response_list)) 
    print("av : %d"%(deviation/len(response_list)))



    
'''

if __name__ == "__main__":
    response_list=[]
    while True:
        number_str = version_input("Enter a number: ")
        if number_str == "done":
            break
        try:
            number = int(number_str)
        except ValueError:
            print("Please enter correct integer number.")
        else:
            response_list.append(number)

    
    print(response_list)
    calculate(response_list)
