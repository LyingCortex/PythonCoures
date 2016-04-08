# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 08:56:35 2015

@author: LY
"""

def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr



# generate all combinations of N items
def powerSet(items):
    N = len(items)
    print ' N = ' + str(N) 
    print '============================'
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        print 'i = ' + str(i) +'  ---> ',
        print dToB(i, N)
        combo = []
        for j in xrange(N):
            print '  j = ' + str(j) + ', ',
            print (i >> j) % 2
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        print combo
        yield combo


items = ['a', 'b', 'c']
a = powerSet(items)
for i in xrange(2**len(items)):
    a.next()
    print '============================'



