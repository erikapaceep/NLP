import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction

s1 = "<s> <s> This is the rat that ate the malt that lay in the house that Jack built </s>"
s2 = "mary"

def count_unique_word(string):
    s1_split = set(s1.split(" "))
    return s1_split

print('vocabulary size including <s>,</s>:', count_unique_word(s1))
print(len(count_unique_word(s1)))

def bigram(string):
    s1_list = []
    s1_split = list(s1.split(" "))
    for i in range(0,len(s1_split)-1):
        x = s1_split[i] + " " +s1_split[i+1]
        s1_list.append(x)
    return s1_list
print(bigram(s1))


def trigram(string):
    s1_list = []
    for i in range(0,len(string)):
        if i == 0:
            x = "$" + "$" + string[i]
            s1_list.append(x)
        if i == 1:
            x = "$" + string[i-1]+string[i]
            s1_list.append(x)
        if i < len(string)-2:
            x = string[i]+string[i+1]+string[i+2]
            s1_list.append(x)
        if i == len(string)-1:
            x = string[i]+"$"+"$"
            s1_list.append(x)
        if i == len(string)-2:
            x = string[i]+string[i+1]+"$"
            s1_list.append(x)
    return s1_list

print(trigram(s1))
print(bigram(s2))

def intersection(lst1,lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def union(lst1,lst2):
    lst4 = list(set(lst1)|set(lst2))
    return lst4

print(intersection((bigram(s1)),bigram(s2)))
print(union((bigram(s1)),bigram(s2)))

jaccard = len(intersection((bigram(s1)),bigram(s2)))/len(union((bigram(s1)),bigram(s2)))
print("Jaccard coefficient = ",len(intersection((bigram(s1)),bigram(s2)))/len(union((bigram(s1)),bigram(s2))))
print(round(jaccard,3))