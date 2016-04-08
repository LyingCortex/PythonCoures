import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()

    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    result_longest_run = []
    
    while numTrials:
        run = []
        for i in range(numRolls):
            run.append(die.roll())
            
        longest = 0
        i = 0                
        while i < numRolls:
            distance = 1
            j = i + 1
            label = 1
            while j < numRolls :
                if run[j] == run[i]:
                    distance += 1
                    j += 1
                else:
                    i = j
                    label = 0
                    if longest <  distance:
                        longest = distance
                    break
            if longest <  distance:
                longest = distance
            if label:
                i += 1
        result_longest_run.append(longest) 
        
        numTrials -= 1
    makeHistogram(result_longest_run, 10, 'x', 'y', title= 'hi')
    mean, std = getMeanAndStd(result_longest_run)
    return mean
            
    
    
    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)