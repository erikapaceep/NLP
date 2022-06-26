import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction

d1 = [2,0,1,2,0,0]
d2 = [0,3,2,1,1,1]
d3 = [0,0,0,3,0,4]

# compute cosine similarity - input vectors
print("Cosine Similarity")
#print(sum(comedy))
def cosine(s1,s2):
    num = round(np.dot(s1, s2),5)

    den = math.sqrt(sum(i*i for i in s1)) * math.sqrt(sum(i*i for i in s2))
    cos = num/den
    return cos

print(round(cosine(d1, d3),3))
print(round(cosine(d2, d3),3))
#print(round(cosine(comedy, action),2))
