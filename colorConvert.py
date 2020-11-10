#!/usr/bin/env python
# -*- coding: utf-8 -*-

import colour

Nits=float(input("Enter a value in Nits: "))

T=int(input("Enter a 10 bit value (0-1023): "))

N=T/1023

		
print('\n''With an input of {} Nits, one can derive the following:\n'.format(Nits))

PQ_OETF=colour.models.oetf_ST2084(Nits)
print('using colour.models.oetf_ST2084:\t{}\n'.format(PQ_OETF))
print('with a 10 bit code value of:\t{}\n'.format(int(colour.models.oetf_ST2084(Nits)*1023)))

print('using colour.eotf_ST2084:\t{}\n'.format(colour.eotf_ST2084(N)))


"""
linLight=colour.oetf_ST2084(N)

print(N)
print(PQ_EOTF)
print(linLight)

message_box('Resulting Luminance in cd/m^2 calculated traditionally '
			'with L=((N**(1/m2)-c1)/(c2-c3*N**(1/m2)))**(1/m1)'
			'\n\t{0}'.format(PQ_EOTF*C))

message_box('using colour.eotf_ST2084:'
			'\n\t{0}'.format(colour.eotf_ST2084(N)))
						
message_box('using colour.oetf_ST2084:'
			'\n\t{0}'.format(colour.oetf_ST2084(N)))

message_box(('Encoding to video component signal value using "BT.709" OETF '
             'and given linear-light value:\n'
             '\n\t{0}'.format(colour.models.oetf_BT709(N))))

print(colour.oetf(linLight, function='BT.709'))

print(colour.oetf(linLight, function='ITU-R BT.1886'))
print(colour.models.oetf_BT1886(linLight))
"""