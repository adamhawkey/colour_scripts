#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import colour
import numpy
from colour.utilities.verbose import message_box

message_box('Colour Component Transfer Functions (CCTF) Computations')
C = int((input("Enter a % value: "))
C = C/100

message_box(('Encoding to video component signal value using "BT.709" OETF '
             'and given linear-light value:\n'
             '\n\t{0}'.format(C)))
print(colour.models.oetf_BT709(C))
print(colour.oetf(C, function='BT.709'))

print('\n')

N = 0.40900773
message_box(('Decoding to linear-light value using "BT.1886" EOTF and given '
             ' video component signal value:\n'
             '\n\t{0}'.format(N)))
print(colour.eotf_BT1886(N))
print(colour.eotf(N, function='BT.1886'))

print('\n')

N=float(input("Enter a value: "))

#N = 0.40900773
message_box(('Decoding to linear-light value using "PQ" EOTF and given '
             ' video component signal value:\n'
             '\n\t{0}'.format(N)))
print(colour.oetf_ST2084(N))
print(colour.eotf(N, function='ST 2084', L_p=10000))

print('\n')
