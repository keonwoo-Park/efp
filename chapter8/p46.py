#usr/bin/env python

import sys
from operator import itemgetter


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_data():
    frequency = dict()
    with open("input_data/p46.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line: 
                break 
    
            words = line.split()
            for word in words:
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1          
     
    return frequency


if __name__ == "__main__":
    input_data = get_data()
    order_data = sorted(input_data.items(), key=itemgetter(1), reverse=True)
 
    paint = '*'
    for word in order_data:
        print("%s:%s" % (word[0], paint*word[1]))

