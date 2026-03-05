import numpy as np
from scipy.stats import binom, norm

# para dist DISCRETAS
# PMF = prob para um valor P(X=x)
# CDF = prob acumulada P(X<=x)

value_for_5 = binom.pmf(7, 10, 0.6)
value_from_0_to_5 = binom.cdf(7, 10, 0.6)

print("PMF: ", round(value_for_5, 4), " CDF: ", round(value_from_0_to_5, 4))

# para dist CONTINUAS
# PDF = prob para um valor P(X=x)
# CDF = prob acumulada P(X<=x)

value_for_mean = norm.pdf(0)
value_from_minus_inf_to_mean = norm.cdf(0)

print("PDF: ", round(value_for_mean, 4), " CDF: ", round(value_from_minus_inf_to_mean, 4))
