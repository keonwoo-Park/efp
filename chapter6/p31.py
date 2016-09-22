#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

START_INTENSITY = 0.55
END_INTENSITY = 0.95

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def targetHR_table(age, HR):
    print("\nResting Pulse: %d Age: %d"%(HR, age))
    print("Intensity| Rate\n---------|--------")

    intensity = START_INTENSITY
    while intensity <= END_INTENSITY:
        targetHeartRate = round( (((220 - age) - HR) * intensity)) + HR
        print("%d%% \t | %d bpm"%(intensity*100, targetHeartRate))
        intensity += 0.05
        intensity = round(intensity, 3)


if __name__ == "__main__":
    while True:
        input_age = version_input("Enter your age: ")
        input_HR = version_input("Enter your HeartRate: ")

        try:
            age = int(input_age)
            HR = int(input_HR)
        except ValueError:
            print("Please enter correct Integer.")
        else:
            break

    targetHR_table(age, HR)

