import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parameters: degrees of freedom
df = 10 
ho_x = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 100)
ho_y = t.pdf(ho_x, df)

ha_x = np.linspace(t.ppf(0.001, df)+5, t.ppf(0.999, df)+5, 100)
ha_y = t.pdf(ho_x, df)

alpha = 0.05
t_crit = t.ppf(1 - alpha/2, df) # t for alpha

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(ho_x, ho_y, label=f'Ho curve')
plt.plot(ha_x, ha_y, label=f'Ha curve')
plt.title('t-Distribution Curve')
plt.xlabel('t-value')
plt.ylabel('Density')
plt.legend()

# Shade alpha region
x_left = np.linspace(-4, -t_crit, 100)
x_right = np.linspace(t_crit, 4, 100)
plt.fill_between(x_left, t.pdf(x_left, df), color='red', alpha=0.5, label='Alpha region')
plt.fill_between(x_right, t.pdf(x_right, df), color='red', alpha=0.5)
# Add critical value lines
plt.axvline(-t_crit, color='red', linestyle='--')
plt.axvline(t_crit, color='red', linestyle='--')

plt.grid(True)
plt.show()
