#- coding:utf-8 -*-
#!/usr/bin/env python

import sys

EMPLOYEES=[]

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def employees_print():
    print("\nThere are %d employees:" % len(EMPLOYEES))
    for name in EMPLOYEES:
        print(name)


def del_employee(delete_name):
    if (delete_name in EMPLOYEES) == True:
        EMPLOYEES.remove(delete_name)
    else:
        print("%s is not on the list." % delete_name)
        sys.exit()


def file_action(message):
    global EMPLOYEES
    if message == "read":
        with open("employees.txt", 'r') as f:
            EMPLOYEES = f.read().split()
    else:
        with open("employees.txt", 'w') as f:
            for name in EMPLOYEES:
                f.write("%s\n" % name)


if __name__ == "__main__":
    file_action("read")
    employees_print()
    delete_name = version_input("Enter an employee name to remove: ")
    del_employee(delete_name)
    employees_print()
    file_action("write")
