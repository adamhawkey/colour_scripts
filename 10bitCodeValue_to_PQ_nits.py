#!/usr/bin/env python3

# script to enter a 10 bit code value and return the corresponding NITS value in PQ space
# "A Perceptual EOTF for Extended Dynamic Range Imagery"

bit10 = int(input("Enter a 10 bit code value: "))
N = bit10/(2**10-1)  #instead of dividing by 1023, using 2^10-1 instead.

'''
# original calculations in 2015
m1 = (2610/4096)/4
m2 = (2523/4096)*128
c1 = 3424/4096
c2 = (2413/4096)*32
c3 = (2392/4096)*32
'''
#updated calculations which have the same result, but may have been simplified since I last looked.
m1 = 1305 / 8192
m2 = 2523 / 32
c2 = 2413 / 128 
c3 = 2392 / 128
c1 = c3 - c2 + 1

C = 10000

L=((N**(1/m2)-c1)/(c2-c3*N**(1/m2)))**(1/m1)

print('10 bit value:')
print(bit10)

bit8 = bit10/(2**10-1) * (2**8-1)
print('8 bit value:')
print(bit8)

bit12 = bit10/(2**10-1) * (2**12-1)
print('12 bit value:')
print(bit12)

bit16 = bit10/(2**10-1) * (2**16-1)
print('16 bit value:')
print(bit16)

print('Luminance in PQ cd/m^2 (Nits):')
print(L*C)