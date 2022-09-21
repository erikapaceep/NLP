import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction

list_probability = [0.0526,0.0526,0.105,0.105,0.105,0.105]
print(len(list_probability))
# compute cosine similarity - input vectors

p = 1
print("Perplexity = (", )
for i in list_probability:
    p *= 1/i
    print("1/",i,"*")
print(")^(1/",len(list_probability),')')
print("=",p**(1/len(list_probability)))


#print(round(cosine(comedy, action),2))
