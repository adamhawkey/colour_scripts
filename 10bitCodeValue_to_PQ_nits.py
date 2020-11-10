#!/usr/bin/python

# script to enter a 10 bit code value and return the corresponding NITS value in PQ space
# "A Perceptual EOTF for Extended Dynamic Range Imagery"

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