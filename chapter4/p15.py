#*- coding:utf-8 -*-
#!/usr/bin/env python

import sys
import getpass
ID="admin"
PW="R/wp.no1"

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def checking_info(user_id, password):
    if ID == user_id:
        return True if PW==password else False
    else:
        print("Please enter a valid ID.");
        sys.exit()


if __name__ == "__main__":
    user_id = version_input("What is the ID :")
    password = getpass.getpass("What is the password :")

    if checking_info(user_id, password) == False:
        print("That password is incorrect.")
    else:
        print("Welcome!") 
