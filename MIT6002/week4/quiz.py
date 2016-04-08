# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:25:49 2015

@author: LY
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#for x in range(62):
#    print f(3)

import random


##set line width
#pylab.rcParams['lines.linewidth'] = 6
##set font size for titles 
#pylab.rcParams['axes.titlesize'] = 20
##set font size for labels on axes
#pylab.rcParams['axes.labelsize'] = 20
##set size of numbers on x-axis
#pylab.rcParams['xtick.major.size'] = 5
##set size of numbers on y-axis
#pylab.rcParams['ytick.major.size'] = 5



#
#xVals = []
#yVals = []
#wVals = []
#for i in range(1000):
#    xVals.append(random.random())
#    yVals.append(random.random())
#    wVals.append(random.random())
#xVals = pylab.array(xVals)
#yVals = pylab.array(yVals)
#wVals = pylab.array(wVals)
#xVals = xVals + xVals
#zVals = xVals + yVals
#tVals = xVals + yVals + wVals
#
#
#
#pylab.hist(xVals, bins = 11)
#xmin, xmax = pylab.xlim()
#ymin, ymax = pylab.ylim()
#print 'x-range =', xmin, '-', xmax
#print 'y-range =', ymin, '-', ymax
#
###pylab.figure
##pylab.hist(xVals, bins = 11)
##xmin, xmax = pylab.xlim()
##ymin, ymax = pylab.ylim()
##print 'x-range =', xmin, '-', xmax
##print 'y-range =', ymin, '-', ymax
##
##
###pylab.figure
##pylab.hist(zVals, bins = 11)
##xmin, xmax = pylab.xlim()
##ymin, ymax = pylab.ylim()
##print 'x-range =', xmin, '-', xmax
##print 'y-range =', ymin, '-', ymax
#
#pylab.show()


#def drawing_without_replacement_sim(numTrials):
#    '''
#    Runs numTrials trials of a Monte Carlo simulation
#    of drawing 3 balls out of a bucket containing
#    4 red and 4 green balls. Balls are not replaced once
#    drawn. Returns a float - the fraction of times 3 
#    balls of the same color were drawn in the first 3 draws.
#    '''
#    # Your code here 
#    num_equal = 0
#    nT = numTrials
#    while nT:
#        ball = [ 1, 1, 1, 1, 0, 0, 0, 0]
#        sum_ball = 0
#        for i in range(3):
#            random.shuffle(ball)
#            sum_ball += ball.pop()
#        if sum_ball == 3 or sum_ball == 0 :
#            num_equal += 1
#        nT -= 1
#    return num_equal / (numTrials + 0.0)
#            





    