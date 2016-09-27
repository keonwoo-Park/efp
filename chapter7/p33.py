#- coding:utf-8 -*-
#!/usr/bin/env python

import sys
import random

ANSWER_LIST=['Yes','No','Maybe','Ask again later']

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


if __name__ == "__main__":

    question = version_input("What's your question?")
    random_num = random.randint(0, len(ANSWER_LIST)-1)
    answer = ANSWER_LIST[random_num]
    print(answer)
