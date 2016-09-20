#- coding:utf-8 -*-
#!/usr/bin/env python

import sys


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def isAnagram(word1, word2):
    sort1 = sorted(word1)
    sort2 = sorted(word2)

    if sort1 == sort2 and len(sort1) == len(sort2):
        return True

    return False


if __name__ == "__main__":
    print("Enter two strings and I'll tell you if they are anagrams:")
    word1 = version_input("Enter the first string: ")
    word2 = version_input("Enter the second string: ")

    if isAnagram(word1, word2) == True:
        print("\"%s\" and \"%s\" are anagrams."%(word1, word2))
    else:
        print("not anagrams!")

