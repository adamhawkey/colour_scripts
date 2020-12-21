#!/usr/bin/python3

# script to enter a 10 bit code value and return the corresponding NITS value in PQ space
# "A Perceptual EOTF for Extended Dynamic Range Imagery"

# This script was broken and wouldn't correctly divide int and float.  Turns out I was using the python2.7 OS install.

T = int(input("Enter a 10 bit value: "))
N = (T/(2**10))
print(T)

# New Constants with old versions from 2014:
m1 = 1305 / 8192    #(2610/4096)/4
m2 = 2523 / 32      #(2523/4096)*128
c2 = 2413 / 128     #(2413/4096)*32
c3 = 2392 / 128     #(2392/4096)*32
c1 = c3 - c2 + 1    #3424/4096
C=10000

L=((N**(1/m2)-c1)/(c2-c3*N**(1/m2)))**(1/m1)

print('10 bit value:  {}'.format(T))
print('Nits / cd/m^2: {}'.format(L*C))
