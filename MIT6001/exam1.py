# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:53:31 2015

@author: LY
"""

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    n_name = newFrob.myName()
    at_name = atMe.myName()
#    print 'newFrob name = ',
#    print n_name
#    print 'atMe name = ',
#    print at_name
    
    if n_name == at_name :
#        print 'equal'
        if atMe.getBefore() == None:
#            print 'hhhhhhhhhhhhhh'
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getAfter() == None:
#            print 'at end'
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            
            at_after = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore = at_after
            at_after.setAfter(newFrob)
#            print 'eeeeeeeeeeeeeeeeeeeee'
        
        
    
        
    elif n_name > at_name:
#        print 'n > at_name'
        at = atMe
        label = 1
        
        
        while at.getAfter():
#            print '00 at_name ',
#            print at.myName()
            if at.getAfter().myName() <= n_name:
#                print '11 at.getAfter_name ',
#                print at.getAfter().myName()
                
                
#                print '22     n_name  '   ,
#                print n_name
                at = at.getAfter()
                
#                print 'wwwwwww'
            else:
                at_next = at.getAfter()
                at_next_b = at_next.getBefore()
                at_next.setBefore(newFrob)
                newFrob.setAfter(at_next)
                newFrob.setBefore(at_next_b)
                at_next_b.setAfter(newFrob)
                label = 0
#                print 'llllllllllllllllllll'
                break
        if label:
            at.setAfter(newFrob)
            newFrob.setBefore(at)
#            print 'large end'
            
    else:
#        print 'new_name < at_name'
        at = atMe
        label1=1
#        print '0    at_name ',
#        print at.myName()
        while at.getBefore():
            if at.getBefore().myName()>=n_name:
#                print '1    at.getBefore_name',
#                print at.getBefore().myName()
#                print 'at name',
#                print at.myName()
#                print '2  new_name',
#                print n_name
                at = at.getBefore()
#                print 'forward'
            else:
                at_before = at.getBefore()
                at_before_n = at_before.getAfter()
                at_before.setAfter(newFrob)
                newFrob.setBefore(at_before)
                newFrob.setAfter(at_before_n)
                at_before_n.setBefore(newFrob)
                label1 = 0
#                print 'mmmmmmmmmmmmmmmmmmm'
                break
        if label1:
            at.setBefore(newFrob)
            newFrob.setAfter(at)
#            print 'less head'



test_list = Frob('eric')
insert(test_list, Frob("eric"))
print '1 -----------------------'
insert(test_list, Frob("chris"))
print '-----------------------'
print '2 -----------------------'
insert(test_list, Frob("john"))
print '-----------------------'
print '-----------------------'
print '3-----------------------'
insert(test_list, Frob("john"))
print '-----------------------'
print '-----------------------'
print '-----------------------'
print '4-----------------------'
insert(test_list, Frob("chris"))
print '-----------------------'
print '-----------------------'
print '-----------------------'
print '-----------------------'
print '5-----------------------'

insert(test_list, Frob("eric"))
print '--------------+++++++++'
insert(test_list, Frob("john"))