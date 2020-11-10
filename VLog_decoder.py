#!/usr/bin/env python
# -*- coding: utf-8 -*-

import colour
from colour.utilities import Structure, as_numeric

# Maximum Nit value
C=10000

VLog=int(input("10 bit Vlog value (0-1023): "))

linLight=colour.log_decoding_curve(VLog/1023, curve='V-Log')
print('\n''Linear-Light: \t{}\n'.format(linLight))

toVLog=colour.log_encoding_curve(linLight, curve='V-Log')
print('To VLog:\t{}\n'.format(int(toVLog*1023)))

toLogC=colour.log_encoding_curve(linLight, curve='Alexa Log C')
print('To LogC:\t{}\n'.format(int(toLogC*1023)))

toSLog3=colour.log_encoding_curve(linLight, curve='S-Log3')
print('To SLog 3:\t{}\n'.format(int(toSLog3*1023)))

to709=colour.models.oetf(linLight, function='BT.709')
print('using oetf_BT709: \t{}'.format(to709))

toPQ=colour.models.oetf(linLight, function='ST 2084')
print('using oetf_ST2084: \t{}'.format(toPQ))


"""
mg=.18

print(colour.models.oetf_ST2084(mg))
print(int(colour.models.oetf_ST2084(VLog)))

# print('with a 10 bit code value of:\t{}\n'.format(int(colour.models.oetf_ST2084(Nits)*1023)))


toPQ=colour.eotf_ST2084(linLight)
print('then, using colour.eotf_ST2084:\t{}\n'.format(toPQ))
"""

"""
Nits=float(input("Enter a value in Nits: "))

T=int(input("Enter a 10 bit value (0-1023): "))

N=T/1023

		
print('\n''With an input of {} Nits, one can derive the following:\n'.format(Nits))

print('using colour.oetf_ST2084:\t{}\n'.format(colour.models.oetf_ST2084(Nits)))
print('with a 10 bit code value of:\t{}\n'.format(int(colour.models.oetf_ST2084(Nits)*1023)))

print('using colour.eotf_ST2084:\t{}\n'.format(colour.eotf_ST2084(N)))

linLight=colour.oetf_ST2084(N)

print(N)
print(PQ_EOTF)
print(linLight)
"""
