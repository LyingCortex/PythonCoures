# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
# 
numViruses = 100
maxPop = 1000
maxBirthProb = 0.1
clearProb = 0.05
resistances = {'guttagonol': False, 'grimpex': False}
mutProb = 0.005 




#def simulation(numViruses, maxPop, maxBirthProb, clearProb, resistances,
#                       mutProb, step1, step2):
#    
#    
#    num = []
#    viruses = []
#    for i in range(numViruses):
#        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
#    patient = TreatedPatient(viruses, maxPop)
#    len_resistances = len(resistances)
#    for i in range(step1):
#        patient.update()
#        
#    for j in range(len_resistances):        
#        patient.addPrescription(resistances.keys()[j])
#    for i in range(step2):
#        patient.update()
#    for j in range(len_resistances):
#            num.append(patient.getTotalPop())
#    return num
#    
       
#def simulationDelayedTreatment(numTrials):
#    """
#    Runs simulations and make histograms for problem 1.
#
#    Runs numTrials simulations to show the relationship between delayed
#    treatment and patient outcome using a histogram.
#
#    Histograms of final total virus populations are displayed for delays of 300,
#    150, 75, 0 timesteps (followed by an additional 150 timesteps of
#    simulation).
#
#    numTrials: number of simulation runs to execute (an integer)
#    """
#    
#    # TODO
#    
#    step1 = [300, 150, 75, 0]
#    result = [[] for i in range(len(step1))]
#    step2 = 150
#    while numTrials:
#        for i in range(len(step1)):
#            result[i].append(simulation(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, step1[i], step2)[0])
#        numTrials -= 1
#    
#    for i in range(len(step1)):
#        pylab.subplot(2,2,i)
#        pylab.hist(result[i], bins = 10)
#        pylab.title(str(step1[i]))
#        
#        
#        
#simulationDelayedTreatment(300)        



def simulation(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, step1):
    
    
    
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    patient = TreatedPatient(viruses, maxPop)
    
    for i in range(150):
        patient.update()
        
    patient.addPrescription(resistances.keys()[0])  
    
    for i in range(step1):
        patient.update()
        
          
    patient.addPrescription(resistances.keys()[1])
    
    for i in range(150):
        patient.update()
    
    return patient.getTotalPop()
    
          




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    step1 = [300, 150, 75, 0]
    result = [[] for i in range(len(step1))]
    
    while numTrials:
        for i in range(len(step1)):
            result[i].append(simulation(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, step1[i]))
        numTrials -= 1
    
    for i in range(len(step1)):
        pylab.subplot(2,2,i)
        pylab.hist(result[i], bins = 10)
        pylab.title(str(step1[i]))
        
        
        
simulationTwoDrugsDelayedTreatment(100)            
    
  


    











