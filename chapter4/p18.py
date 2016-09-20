#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

temperature_int = 0

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def type_checking(temperature):
    global temperature_int
    try:
        temperature_int = int(temperature)
        if temperature_int < 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.")
    choice = version_input("Your choice: ")
    temperature = version_input("Please enter the temperature in Fahrenheit: ")

    if type_checking(temperature) == False:
        print("Plese enter correct integer or enter an integer greater than 0.")
        sys.exit()

    if choice == "C" or choice =="c":
        exchange_temperature = (temperature_int - 32)*5/9
        print("The temperature in Celsius is %d."% exchange_temperature)
    elif choice == "F" or choice =="f":
        exchange_temperature = (temperature_int * 9 /5)+32
        print("The temperature in Fahrenheit is %d."% exchange_temperature)
    else:
        print("Please enter C or F.")
