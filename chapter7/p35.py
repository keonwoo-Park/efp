#!/usr/bin/env python

import sys
import random


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)

def get_list():
    while True:
        name = version_input("Enter a name:")
        if name == "":
            break
        winner_list.append(name)


def people_print():
    print(winner_list)


def select_winner():
    winner_number = random.randrange(0, len(winner_list))
    print("The winner is %s." % winner_list[winner_number])
    winner_list.pop(winner_number)



if __name__ == "__main__":
    while True:
        winner_list=[]
        get_list()
        people_print()
        select_winner() 
        people_print() 
        ans = version_input("Are you want again?(y/n): ")
        if ans.upper() == 'N':
            break
        elif ans.upper() == 'Y':
            continue
        else:
            print("Please enter correct word(y/n).")
            sys.exit()

