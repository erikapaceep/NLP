import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fractions import Fraction



def naive_bayes(collection, classes):
    p_ham = 0
    p_spam =0
    unique = set()
    class1 = list()
    class2 = list()
    for i in collection:
        if i[0]==classes[0]:
            p_ham +=1
            for word in i[1:len(i)]:
                class1.append(word)
        else:
            p_spam +=1
            for word in i[1:len(i)]:
                class2.append(word)
        for word in i[1:len(i)]:
            unique.add(word)
    unique_lst = list(unique)
    #prior prbability
    prior_ham=p_ham/len(collection)
    prior_spam=p_spam/len(collection)

    print('check',prior_ham + prior_spam)
    print('class1',class1)
    print('class2',class2)
    print('unique',unique_lst)
    #constructing the unigram LM //Add one smoothing
    class1_dict = dict()
    class1_lst=list()
    for i in unique_lst:
        count = 1
        for j in class1:
            if i == j:
                count +=1
        class1_lst.append(count)
    print(class1_lst)
    for i,c in enumerate(unique_lst):
        class1_dict[c]=round(class1_lst[i]/sum(class1_lst),3)
    print(class1_dict)

    class2_dict = dict()
    class2_lst=list()
    for i in unique_lst:
        count = 1
        for j in class2:
            if i == j:
                count +=1
        class2_lst.append(count)
    print(class2_lst)
    for i,c in enumerate(unique_lst):
        class2_dict[c]=round(class2_lst[i]/sum(class2_lst),3)
    print(class2_dict)

    #likelihood
    likelihood_class1 = 1
    for i in test:
        if i in class1_dict.keys():
            p1 = class1_dict[i]

        likelihood_class1 *= p1


    likelihood_class2 = 1
    for i in test:
        if i in class2_dict.keys():
            p2 = class2_dict[i]

        likelihood_class2 *= p2
    print(likelihood_class2)

    #Posterior probability
    posterior_class1 = likelihood_class1*prior_ham
    posterior_class2 = likelihood_class2*prior_spam

    if posterior_class1 > posterior_class2:
        result = classes[0]
    else:
        result = classes[1]
    return (f"test sentence belong to class: {result} \n "
            f"posterior probability for class {classes[0]} is: {round(posterior_class1, 5)} \n "
            f"posterior probability for class {classes[1]} is: {round(posterior_class2, 5)} \n ")

if __name__ == "__main__":
    classes = ['P','N']
    d1 = ['P','easy','read']
    d2 = ['P','easy','read','funny']
    d3 = ['N','hard','read']
    d4 = ['N','hard', 'read', 'dull']
    d5 = ['N','hard', 'hard', 'dull']
    d6 = ['N','hard', 'funny']
    collection = [d1,d2,d3,d4,d5,d6]
    test = ['Very', 'good', 'read', 'hard', 'read']
    print(naive_bayes(classes, collection))