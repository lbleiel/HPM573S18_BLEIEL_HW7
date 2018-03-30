## PROBLEM 1 ##

import SurvivalModelClasses as Cls

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)
print('Problem 1:')
# print the patient survival time
print('Percentage of patients survived beyond 5 years):', myCohort.get_5yr_survtime())

## PROBLEM 2 ##
print('Problem 2:')
print('Type of distribution: BINOMIAL')
print('Parameters: N = number of participants (trials)')
print('q is the probability of 5 year survival [0,1]')
print('(1 = survives 5 years, 0 = does not survive 5 years)')


