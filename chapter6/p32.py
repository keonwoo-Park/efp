#- coding:utf-8 -*-
#!/usr/bin/env python

import sys
import random

START_RANGE = 1

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_range(level):
    if level == 1:
        end_range = 10
    elif level == 2:
        end_range = 100
    elif level == 3:
        end_range = 1000
    else:
        print("Please enter 1~3 ranges!")
        sys.exit()
    return end_range


def print_message(find_count):
    message = "You got it in %d guesses!\n" % find_count
    if find_count == 1:
        message += "You're a mind reader!"
    elif find_count >= 2 and find_count <= 4:
        message += "Most impressive."
    elif find_count >= 5 and find_count <= 6:
        message += "You can do better than that."
    else:
        message += "Better luck next time."
    
    print(message)


if __name__ == "__main__":
    print("Let's play Guess the Number.")
    input_level = version_input("Pick a difficulty level(1, 2, or 3): ")
    try:
        level = int(input_level)
    except ValueError:
        print("Please enter correct Integer.")
        sys.exit()

    end_range = get_range(level)
    computer_number = random.randint(START_RANGE,end_range)
    message = "I have my number. What's your guess? "

    wrong_count = 0
    find_count = 0
    while True:
        input_number = version_input(message)
        try:
            number = int(input_number)
        except ValueError:
            print("Please enter correct Integer.")
            wrong_count += 1
            continue
        
        if START_RANGE > number or end_range < number:
            print("Please enter correct input ranges(%d~%d)"%(START_RANGE, end_range))
            wrong_count += 1
            continue

        find_count += 1
        if computer_number == number:
            print_message(find_count)
            ans = version_input("Play again?(y/n) ")
            if ans.lower() == 'n':
                print("goodbye!")
                break
            elif ans.lower() == 'y':
                wrong_count = 0
                find_count = 0
                number = 0
                computer_number = random.randint(START_RANGE,end_range)
                message = "\nI have my number. What's your guess? "
                continue
            else:
                print("Your input wrong and exit program!")
                sys.exit()
        elif computer_number > number:
            message = "Too low. Guess again: "
        elif computer_number < number:
            message = "Too high. Guess again: "

