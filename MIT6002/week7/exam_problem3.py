import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    if CURRENTRABBITPOP > 10 :
        p_rabit_reproduction = 1 - CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
        CURRENTRABBITPOP = CURRENTRABBITPOP * ( 1 + p_rabit_reproduction )
        p_fox_eat_rabit = CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
        CURRENTRABBITPOP = CURRENTRABBITPOP * (1 - p_fox_eat_rabit)
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if CURRENTFOXPOP > 10:
        p_fox_eat_rabit = CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
        fox_eat = CURRENTFOXPOP * p_fox_eat_rabit
    
        fox_eat_a = fox_eat * ( 1 + 1.0 / 3)
        fox_eat_b = ( CURRENTFOXPOP - fox_eat) * ( 1 - 0.1)
        CURRENTFOXPOP = fox_eat_a + fox_eat_b
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    for  i in xrange(numSteps):
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)


aa = runSimulation(200)
pylab.plot(list(range(200)), aa[0])
pylab.plot(list(range(200)), aa[1])
