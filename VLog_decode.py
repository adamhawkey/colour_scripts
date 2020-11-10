#!/usr/bin/python
# decoding Panasonic VLog into PQ
import numpy as np
import colour
from colour.utilities import Structure, as_numeric

"""  This is a mess.  Have fun """

T=int(input("Enter a 10 bit value (0-1023): "))
Tlin=colour.models.log_decoding_VLog(T)
print(T)
print(Tlin)


"""
=IF(H16<$I$3,(H16-0.125)/5.6,power(10,((H16-$I$6)/$I$5)-$I$4))
"""



""" returns PQ Nits from 10 bit code value
# N=float(input("Enter a value: "))
T=int(input("Enter a value: "))
N=T/1023

m1=(2610/4096)/4
m2=(2523/4096)*128
c1=3424/4096
c2=(2413/4096)*32
c3=(2392/4096)*32
C=10000

print(N,N/1023)

L=((N**(1/m2)-c1)/(c2-c3*N**(1/m2)))**(1/m1)

print('Resulting Luminance in cd/m^2')
print(L*C)
"""
