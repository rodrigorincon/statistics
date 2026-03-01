import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# create graphics for binomial distribution with different probs and different N to show the it approximates to normal when N increases independent of the prob
num_attempt_list = [10, 20, 30, 40]
prob_list_to_calc = [0.2, 0.5, 0.8] # run the distribution with these probabilities

def binomial_distribution(p, num_attempts):
	x_axis = np.arange(0, num_attempts-1)
	prob_list = binom.pmf(x_axis, num_attempts, p) # params: 1º desired number of successes, 2º total of attempts, 3º probability of success
	# when we pass an array as 1º param, it calcs the probability for each value and returns an array with the prob for each one
	return prob_list

# Create a figure with 3 row and 4 columns
fig, axs = plt.subplots(nrows=len(prob_list_to_calc), ncols=len(num_attempt_list), figsize=(20, 7))

for row_idx in range( len(prob_list_to_calc) ):
	#axs[row_idx].set_ylabel("Probability")
	prob = prob_list_to_calc[row_idx]
	for col_idx in range(len(num_attempt_list)):
		num_attempt = num_attempt_list[col_idx]
		prob_list = binomial_distribution(prob, num_attempt)
		# Plot the distribution inside the figure
		x_axis = np.arange(0, num_attempt-1)
		axs[row_idx][col_idx].bar(x_axis, prob_list)
		axs[row_idx][col_idx].set_title(f'Binomial Distribution for p={prob} and N={num_attempt}')
		axs[row_idx][col_idx].set_xlabel("Number of Successes")
		axs[row_idx][col_idx].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout() # Adjust layout to prevent titles/labels from overlapping
plt.show()
