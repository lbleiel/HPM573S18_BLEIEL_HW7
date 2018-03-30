from scipy.stats import binom
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)

p = .5
n = 573 # number of trials
k = 400 # number of successes


likelihood = binom.pmf(k, n, p, loc = 0)
print('The likelihood is:', likelihood)
