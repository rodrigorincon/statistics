import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

media_list = [5, 10, 20, 30]

# Create a figure with 1 row and 5 columns
fig, axs = plt.subplots(nrows=1, ncols=len(media_list), figsize=(15, 4))
axs[0].set_ylabel("Probability")

for idx in range( len(media_list) ):
	media = media_list[idx]
	x_axis = list(range(100))
	prob_list = poisson.pmf(x_axis, media) # when we pass an array as 1º param, it calcs the probability for each value and returns an array with the prob for each one

	# remove the 0 results from the list to avoid unecessary long tails
	prob_list = [result for result in prob_list if result > 0.0001]
	x_axis = list(range(len(prob_list)))

	# Plot the distribution inside the figure
	axs[idx].plot(x_axis, prob_list)
	axs[idx].set_title(f'Poisson Distribution for media={media}')
	axs[idx].set_xlabel("Number of Successes")
	axs[idx].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout() # Adjust layout to prevent titles/labels from overlapping
plt.show()
