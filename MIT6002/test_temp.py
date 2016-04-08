# -*- coding: utf-8 -*-
'''
from math import *
import numpy as np
import pylab as pl
from scipy import interpolate 


c=300
f = 2.45
wl =  c / f
k= 2*pi/wl
w=37.26
dL=0.7386062849627408
e = 4.4
L=c/f/(e**0.5)/2-dL*2
def f(x):
    return (sin(k*w/2*cos(x))/cos(x))**2*sin(x)**3
    
I, err = integrate.quad(f, 0, pi)
print 'I = '+str(I)

G =I/120/(pi**2)
print 'G = ' + str(G)

Z = (cos(k/((e)**0.5)*w/2))**2/2/G
Z1 = (cos(pi/L*w/2))**2/2/G
print 'Z1 = ' + str(Z1)

print wl*((90/50)**0.5)
print wl*((90/80)**0.5)
'''
a1 =39.2


a=6.3

f = list(range(18,41))

wl = [300.0/ ff for ff in f]

ro = [a1**2 /3/w for w in wl]