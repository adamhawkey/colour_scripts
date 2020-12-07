#!/usr/bin/env python3

# Luminance calculation of Perceptual Quantizer (PQ) EOTF
# From the SMPTE / Dolby presentation
# "A Perceptual EOTF for Extended Dynamic Range Imagery"

N = float(input("Enter a float value: "))

m1 = (2610/4096)/4
m2 = (2523/4096)*128
c1 = 3424/4096
c2 = (2413/4096)*32
c3 = (2392/4096)*32
C = 10000

print(N)

L=((N**(1/m2)-c1)/(c2-c3*N**(1/m2)))**(1/m1)

print(N**(1/m2)-c1)
print(c2-c3*N**(1/m2))

print(L)
