# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:03:44 2015

@author: LY
"""

def powerSet(items):
    N = len(items)
    print 'N = ',
    print N
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        print ' i= ' + str(i)
        for j in xrange(N):
            # test bit jth of integer i
            print 'j = ' +str(j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        print combo
        print '-------------------'
        yield combo
        
        
        
items = ['a','b']

#a = powerSet(items)
#a.next()
#a.next()
#a.next()
#a.next()






def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        
        for j in xrange(N):
            if(i / (3**j)) % 3 == 1:
                bag1.append(items[j])
            if(i // (3**j)) % 3 == 2:
                bag2.append(items[j])
        combo = (bag1, bag2)
        print combo
        yield combo
                
a = yieldAllCombos(items)
a.next()
print '-----------'
a.next()
print '-----------'
a.next()
print '-----------'
a.next()
print '-----------'
a.next()
print '-----------'
                
    