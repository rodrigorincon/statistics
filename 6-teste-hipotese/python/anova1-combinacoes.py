import numpy as np
from scipy.stats import f_oneway

def print_stats(combination_text, *groups):
  for group in groups:
    print("mean =", np.mean(group), "variance =", np.var(group, ddof=1))
  f_stat, p_value = f_oneway(groups[0], groups[1], groups[2])
  print(f"F-statistic: {f_stat}, P-value: {p_value} \n")
  if p_value < 0.05:
    print(combination_text, "-> Reject Ho")
  else:
    print(combination_text, "-> Don't reject Ho")


# close averages, low variances
print("---------------------")
group1 = [4,5,5,5,5,6,6,6,7,7] # mean=5.6, vari=0.93
group2 = [4,4,5,5,6,6,6,6,6,6] # mean=5.4, vari=0.71
group3 = [4,4,5,5,5,6,6,6,6,6] # mean=5.3, vari=0.68
print_stats("close averages, low variances", group1, group2, group3) # Don't reject Ho

# close averages, high variances
print("---------------------")
group1 = [1,2,3,5,5,6,7,8,9,10] # mean=5.6, vari=8.93
group2 = [1,2,3,4,6,6,6,7,9,11] # mean=5.5, vari=9.61
group3 = [1,3,3,5,5,5,6,7,9,10] # mean=5.4, vari=7.6
print_stats("close averages, high variances", group1, group2, group3) # Don't reject Ho

# distant averages, low variances
print("---------------------")
group1 = [1,1,1,2,2,2,2,3,3,3] # mean=2, vari=0.67
group2 = [3,3,4,4,4,4,4,5,5,5] # mean=4.1, vari=0.54
group3 = [8,8,8,8,8,9,9,9,9,10] # mean=8.6, vari=0.48
print_stats("distant averages, low variances", group1, group2, group3) # Reject Ho

# distant averages, high variances
print("---------------------")
group1 = [1,1,1,1,1,1,1,1,1,20] # mean=2.9, vari=36.1
group2 = [6,6,6,7,8,8,11,13,15,15] # mean=9.5, vari=13.61
group3 = [2,2,2,3,4,6,6,6,9,10] # mean=5, vari=8.44
print_stats("distant averages, high variances", group1, group2, group3) # Reject Ho