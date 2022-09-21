import numpy as np
import math
from scipy.stats import entropy
from fractions import Fraction

posting_list = [3, 515, 520]

#Variable Byte (VB) Code
x=0
binary = bin(x)[2:]
if len(binary)<=7:
    binary = str(1)+ str(0)*(7-len(binary)) + binary
elif len(binary) <= 14:
    binary = str(0) + str(0)*(7-len(binary[0:len(binary)-7])) + binary[0:len(binary)-7] + " " + str(1) + binary[len(binary)-7:len(binary)]
elif len(binary) <= 21:
    binary = str(0) + str(0)*(7-len(binary[0:len(binary)-14])) + binary[0:len(binary)-14] + " " +\
             str(0) + binary[len(binary)-14:len(binary)-7] + " "+\
             str(1) + binary[len(binary)-7:len(binary)]
print(binary)

#Variable Byte (VB) Code
gap_list = []
VB_gap_list = []
for i in range(0,len(posting_list)):
    if i == 0:
        gap_list.append(posting_list[i])
    else:
        gap_list.append(posting_list[i]-posting_list[i-1])
print(gap_list)
for x in gap_list:
    binary = bin(x)[2:]
    if len(binary)<=7:
        binary = str(1)+ str(0)*(7-len(binary)) + binary
    elif len(binary) <= 14:
        binary = str(0) + str(0)*(7-len(binary[0:len(binary)-7])) + binary[0:len(binary)-7] + " " + str(1) + binary[len(binary)-7:len(binary)]
    elif len(binary) <= 21:
        binary = str(0) + str(0)*(7-len(binary[0:len(binary)-14])) + binary[0:len(binary)-14] + " " +\
                 str(0) + binary[len(binary)-14:len(binary)-7] + " "+\
                 str(1) + binary[len(binary)-7:len(binary)]
    print("Variable Byte (VB) Code for", x ,":",binary)
    VB_gap_list.append(binary)
print("VB code for the posting list :",VB_gap_list)
#gamma code for single number

offset = bin(x)[3:]
length = str(1)*len(offset) +str(0)
print(length, offset)

#gamma code for gap list
gamma_code = []
for x in gap_list:
    offset = bin(x)[3:]
    length = str(1)*len(offset) + str(0)
    print("gamma code for",x, ":", length, offset)
    gcode = length + offset
    gamma_code.append(gcode)
print("gamma code is :",gamma_code)

unary = str(1)*x + str(0)
print("unary code is",x,":", unary)
