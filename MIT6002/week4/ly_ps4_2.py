# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:32:25 2015

@author: LY
"""

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