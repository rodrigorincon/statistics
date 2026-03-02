import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

x_axis = np.linspace(0, 15, 100)
lambdas = [0.5, 1, 1.5]

exponential_curves = [ expon.pdf(x_axis, scale=1/my_lambda) for my_lambda in lambdas]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_axis, exponential_curves[0], label='lambda = 0.5', color='red')
plt.plot(x_axis, exponential_curves[1], label='lambda = 1', color='blue')
plt.plot(x_axis, exponential_curves[2], label='lambda = 1.5', color='green')
plt.legend()
plt.xlabel("Value")
plt.ylabel("Probability")
plt.title('Exponential Distributions')
plt.show()


