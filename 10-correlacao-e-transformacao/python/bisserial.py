#import pingouin as pg

# OBS: scipy and most commom libs dont have the regular bisserial function
# to run it we need to use this other lib (pingouin) or install R libs inside python

# Binary variable (0 or 1)
x = [0, 0, 0, 1, 1, 1, 1]
# Continuous variable
y = [10, 12, 9, 25, 30, 28, 22]

# regular bisserial, when the continuous var follows a normal distribution and the category is artificial
res = pg.biserial(x, y)
print(res)

# doing it manually

import numpy as np
from scipy.stats import norm

def biserial_correlation(binary_var, continuous_var):
    y = binary_var
    x = continuous_var
    
    # Calculate means for the two groups
    mean0 = np.mean(x[y == 0])
    mean1 = np.mean(x[y == 1])
    
    # Calculate standard deviation
    sd = np.std(x, ddof=1)
    
    # Proportion of cases in each group
    p = np.mean(y)
    q = 1 - p
    
    # Ordinate of the normal distribution
    h = norm.pdf(norm.ppf(p))
    
    # Biserial formula
    return ((mean1 - mean0) / sd) * (p * q / h)

x = np.random.normal(0, 1, 100)  # Continuous
y = (x + np.random.normal(0, 0.5, 100) > 0).astype(int) # Binary (category A as 1 and category B is 0)
print(biserial_correlation(y, x))
