import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# data following normal distribution
normal_points = np.random.normal(0, 1, 100) 

# data following exponential distribution
exp_points = np.random.exponential(scale=5.0, size=100)

# Create the Q-Q plot, first line showing distributions in a normal graphic and second line showing in a exponential graphic
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 6))

stats.probplot(normal_points, dist="norm", plot=axs[0][0]) # define the red line as normal distribution
stats.probplot(exp_points, dist="norm", plot=axs[0][1]) # show not match between data and distribution

stats.probplot(normal_points, dist=stats.expon, plot=axs[1][0]) # show not match between data and distribution
stats.probplot(exp_points, dist=stats.expon, plot=axs[1][1])

axs[0][0].set_title("Normal data in Normal Distribution")
axs[0][1].set_title("Exponential data in Normal Distribution")
axs[1][0].set_title("Normal data in Exponential Distribution")
axs[1][1].set_title("Exponential data in Exponential Distribution")

plt.tight_layout()
plt.show()
