import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import t

normal_x_axis = np.linspace(-2, 2, 100)
normal_values = norm.pdf(normal_x_axis)

t_x_axis = np.linspace(-2, 2, 10)
t_values = t.pdf(t_x_axis, len(t_x_axis)-1 )

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(normal_x_axis, normal_values, label='Distribuição Normal', color='red')
plt.plot(t_x_axis, t_values, label='Distribuição T', color='blue')
plt.legend()
plt.xlabel("Value")
plt.ylabel("Probability")
plt.title('Normal and T Distributions')
plt.show()


