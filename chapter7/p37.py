#/usr/bin/env python

import sys
import random

SPECIAL=['!','@','#','$','%','^','&','*','-','~','=','+','/','?','.','<','>','[',']']
NUMBER=[1,2,3,4,5,6,7,8,9,0]
CHAR=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def make_password(count, kind):
    for num in range(count):
        one_word = random.choice(kind)
        password.append(one_word)


def print_password():
    password_str=""
    
    print("Your password is")
    for word in password: 
        password_str += str(word)
    print(password_str)



if __name__ == "__main__":
    password=[]
    length_str = version_input("What's the minimum length?(1-15) ")
    special_str = version_input("How many special characters? ")
    num_str = version_input("How many numbers? ")

    try:
        length = int(length_str)
        special_count = int(special_str)
        num_count = int(num_str)
    except ValueError:
        print("Please enter correct Integer.")
        sys.exit()
    else:
        str_count = length - special_count - num_count
        if str_count <= 0 or str_count > 15:
            print("Please enter correct ranges(1~15)!")
            sys.exit()

    make_password(special_count, SPECIAL)
    make_password(num_count, NUMBER)
    make_password(str_count, CHAR)
    random.shuffle(password)
    
    print_password()    

