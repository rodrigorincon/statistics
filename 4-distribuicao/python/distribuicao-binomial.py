import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# create graphics for binomial distribution with different probs to show the assimetry change
x_axis = np.arange(0, 11) # from 0 to 10
prob_list_to_calc = [0.1, 0.3, 0.5, 0.7, 0.9] # run the distribution with these probabilities

def binomial_distribution(p):
	prob_list = binom.pmf(x_axis, 10, p) # params: 1º desired number of successes, 2º total of attempts, 3º probability of success
	# when we pass an array as 1º param, it calcs the probability for each value and returns an array with the prob for each one
	return prob_list

# Create a figure with 1 row and 5 columns
fig, axs = plt.subplots(nrows=1, ncols=len(prob_list_to_calc), figsize=(15, 4))
axs[0].set_ylabel("Probability")

for idx in range( len(prob_list_to_calc) ):
	prob = prob_list_to_calc[idx]
	prob_list = binomial_distribution(prob)
	# Plot the distribution inside the figure
	axs[idx].bar(x_axis, prob_list)
	axs[idx].set_title(f'Binomial Distribution for p={prob}')
	axs[idx].set_xlabel("Number of Successes")
	axs[idx].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout() # Adjust layout to prevent titles/labels from overlapping
plt.show()
