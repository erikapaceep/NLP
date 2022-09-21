import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction


def jaccard_coef(string1,string2,ngram):
    """
    This function compute the jaccard coefficient between two strings
    Args:
        The function requires two strings string1 and string2
        The function requires the n-gram which can be unigram, bigram or trigram

    Return:
        The function return the jaccard coefficient between the two strings
    """
    jaccard_coef = len(intersection((ngram(string1)), ngram(string2))) / len(union((ngram(string1)), ngram(string2)))
    return round(jaccard_coef,3)


def count_unique_word(string):
    s1_split = set(s1.split(" "))
    return s1_split



def unigram(string):
    return list(string.lower().split(" "))

def bigram(string):
    s_list = []
    str_split = list(string.split(" "))
    for i in range(0,len(str_split)-1):
        x = str_split[i] + " " + str_split[i+1]
        s_list.append(x)
    return s_list


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


def intersection(lst1,lst2):
    intersection_lst = [value for value in lst1 if value in lst2]
    return intersection_lst

def union(lst1,lst2):
    union_lst = list(set(lst1)|set(lst2))
    return union_lst


if __name__ == "__main__":
    s1 = "What is your name?"
    s2 = "Erika, and what is yours?"
    print(jaccard_coef(s1,s2,unigram))

