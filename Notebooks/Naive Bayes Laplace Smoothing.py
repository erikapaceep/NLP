import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fractions import Fraction


def naive_bayes_laplace_smoothing(classes, collection):
    """
    The function applies naive bayes algorithm with laplace smoothing
    :param classes (binary): each sentence will have a lable
    :param collection: the collection of sentences the naive bayes with ls is going to be trained on
    :return: the function will return the class that is more likely to be associated with a test given test sentence
    """
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


    #constructing the unigram LM //Add one smoothing
    class1_dict = dict()
    class1_lst=list()
    for i in unique_lst:

        count = 0
        for j in class1:
            if i == j:
                count +=1
        class1_lst.append(count)

    for i,c in enumerate(unique_lst):
        #print(unique_lst[i],class1_lst[i]+1,(len(class1) + len(unique_lst)))
        class1_dict[c]=round((class1_lst[i]+1)/(len(class1) + len(unique_lst)),3)


    class2_dict = dict()
    class2_lst=list()
    for i in unique_lst:
        count = 0
        for j in class2:
            if i == j:
                count +=1
        class2_lst.append(count)

    for i,c in enumerate(unique_lst):
        class2_dict[c]=round((class2_lst[i]+1)/(len(class2) + len(unique_lst)),3)

    #likelihood
    p1=1
    likelihood_class1 = 1
    for i in test:
        if i in class1_dict.keys():
            p1 = class1_dict[i]

        likelihood_class1 *= p1

    p2=1
    likelihood_class2 = 1
    for i in test:
        if i in class2_dict.keys():
            p2 = class2_dict[i]

        likelihood_class2 *= p2


    #Posterior probability
    posterior_class1 = likelihood_class1*prior_ham
    posterior_class2 = likelihood_class2*prior_spam
    if posterior_class1 > posterior_class2:
        result = classes[0]
    else:
        result = classes[1]
    return (f"test sentence belong to class: {result} \n "
    f"posterior probability for class {classes[0]} is: {round(posterior_class1,5)} \n "
    f"posterior probability for class {classes[1]} is: {round(posterior_class2, 5)} \n ")

if __name__ == "__main__":
    classes = ['P','N']
    d1 = ['P','save','money','back']
    d2 = ['P','save','money','no','fees']
    d3 = ['N','future','no','school','fees']
    d4 = ['N','back','to','school']
    d5 = ['N','back','to','the','future']
    collection = [d1,d2,d3,d4,d5]
    test = ['save', 'fees', 'annual', 'fees']
    print(naive_bayes_laplace_smoothing(classes, collection))

