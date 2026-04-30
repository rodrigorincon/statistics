import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

segunda = [276,323,298,256,277,309,312,265,311]
terca = [243,279,301,285,274,243,228,298,255]
quarta = [288,292,310,267,243,293,255,273]
quinta = [254,279,241,227,278,276,256,262]

f_stat, p_value = f_oneway(segunda, terca, quarta, quinta)
print(f"F-statistic: {f_stat}, P-value: {p_value} \n")
if p_value < 0.05:
  print("Reject Ho")
else:
  print("Don't reject Ho")

##### ANOVA is significant, let's do Tukey's HSD test

# for post-hoc test we need to create an array with all the data and another array with the group labels
data = np.array(segunda + terca + quarta + quinta)
labels = np.array(['segunda']*len(segunda) + ['terca']*len(terca) + ['quarta']*len(quarta) + ['quinta']*len(quinta))

tukey = pairwise_tukeyhsd(data, labels, alpha=0.05)
print(tukey)

rejected_lines = [line for line in tukey._results_table.data[1:] if line[-1]  ]
for line in rejected_lines:
  print("Significant difference between", line[0], "and", line[1], ".", line[0], " has between ", line[4], " and ", line[5], " less people than ", line[1])