import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fractions import Fraction

classes = ['P','N']
d1 = ['P','save','money','back']
d2 = ['P','save','money','no','fees']
d3 = ['N','future','no','school','fees']
d4 = ['N','back','to','school']
d5 = ['N','back','to','the','future']

collection = [d1,d2,d3,d4,d5]

test = ['save', 'fees', 'annual', 'fees']

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
print(prior_ham)
print(prior_spam)
print('check',prior_ham + prior_spam)
print('class1',class1)
print('class2',class2)
print('unique',unique_lst)

#constructing the unigram LM //Add one smoothing
class1_dict = dict()
class1_lst=list()
for i in unique_lst:
    print(i)
    count = 0
    for j in class1:
        if i == j:
            count +=1
    class1_lst.append(count)
#print(class1_lst)
for i,c in enumerate(unique_lst):
    #print(unique_lst[i],class1_lst[i]+1,(len(class1) + len(unique_lst)))
    class1_dict[c]=round((class1_lst[i]+1)/(len(class1) + len(unique_lst)),3)
print('class 1 likelihood1:',class1_dict)

class2_dict = dict()
class2_lst=list()
for i in unique_lst:
    count = 0
    for j in class2:
        if i == j:
            count +=1
    class2_lst.append(count)
print('class2',class2_lst)
for i,c in enumerate(unique_lst):
    print(class2_lst[i]+1,len(class2) + len(unique_lst))
    class2_dict[c]=round((class2_lst[i]+1)/(len(class2) + len(unique_lst)),3)
print('class list 2',class2_lst)
print('class 2 likelihood1:',class2_dict)

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
print(likelihood_class2)

#Posterior probability
posterior_class1 = likelihood_class1*prior_ham
posterior_class2 = likelihood_class2*prior_spam

print("posterior probability class 1:", round(posterior_class1,5))
print("posterior probability class 2:", round(posterior_class2,5))