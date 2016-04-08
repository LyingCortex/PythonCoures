# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:31:04 2015

@author: LY
"""


a = [-6, -6, -4, -4, 2, 2, 2]
C1 = [2, 2, -6, -6] 
C2 = [-4, -4, 2]
C1 = [2, 2, 2]
C2 = [-6, -6, -4, -4]


def my_variance(a_list):
    a_mean = sum(a_list) * 1.0 / len(a_list)
    return sum((a - a_mean)**2 for a in a_list)
    
print my_variance(C1)
print my_variance(C2)
print my_variance(C1) + my_variance(C2)