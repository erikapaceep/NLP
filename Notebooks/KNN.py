import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fractions import Fraction
import copy

classes = ['P','N']
d1 = 'Shipment of gold arrived in a truck'
d2 = 'Shipment of gold damaged in a fire'
q = 'Delivery of silver arrived in a silver truck'

collection = [d1,d2,q]
n = len(collection)

#// Term IDF Weights
dic = dict()
for i in collection:
    i = i.lower()
    s = set(i.split(" "))
    for j in s:
        if j not in dic.keys():
            dic[j] = 1
        else:
            dic[j] += 1

idf_dict = dict()
for i in dic.keys():
    key = "idf "+str(i) + " = " + "log(" + str(n) +"/"+str(dic[i]) +")"
    idf_dict[key] = round(math.log10(n/dic[i]),3)
print('idf_dict:',idf_dict)

idf = dict()
for i in dic.keys():
    idf[i] = round(math.log10(n/dic[i]),3)
print(list(d1.split(" ")))

#// TF×IDF Document Vectors
def tf_idf(doc):
    tf_idf = dict()
    for i in idf.keys():
        x=0
        d1 = doc.lower()
        d1_str = list(d1.split(" "))
        tf_idf[i]=0
        for j in d1_str:
            if i ==j:
                tf_idf[i] += idf[i]
            else:
                continue
    return tf_idf

d1_tdf_if = tf_idf(d1)
d2_tdf_if = tf_idf(d2)
q_tdf_if = tf_idf(q)

print(d1_tdf_if)
print(d2_tdf_if)
print(q_tdf_if)

d1_list=list(d1_tdf_if.values())
d2_list=list(d2_tdf_if.values())
q_list=list(q_tdf_if.values())

#cosine
def cosine(s1,s2):
    num = round(np.dot(s1, s2),5)

    den = math.sqrt(sum(i*i for i in s1)) * math.sqrt(sum(i*i for i in s2))
    cos = num/den
    return cos

print('cosine similarity:',round(cosine(d1_list, q_list),3))
print('cosine similarity:',round(cosine(d2_list, q_list),3))
