import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
from statsmodels.formula.api import ols
from scipy.stats import shapiro
from scipy.stats import levene

segunda = [276,323,298,256,277,309,312,265,311]
terca = [243,279,301,285,274,243,228,298,255]
quarta = [288,292,310,267,243,293,255,273]
quinta = [254,279,241,227,278,276,256,262]

# FORMATING DATA TO GET THE RESIDUALS (TO CHECK NORMALITY)
df = pd.DataFrame({
    'valores': np.array(segunda + terca + quarta + quinta),
    'labels': ['segunda']*len(segunda) + ['terca']*len(terca) + ['quarta']*len(quarta) + ['quinta']*len(quinta)
})
model = ols('valores ~ C(labels)', data=df).fit() # run steps 1, 2 and 3 (just don't run F test)

residuals = model.resid # residuo = diferença entre a amostra e a média de seu grupo. 
# resíduo representa a variação não explicada por essa variável, podendo ser causadas por outras ou só aleatoriedade
# Tenho 1 resíduo pra cada amostra
print("RESIDUALS:\n", residuals, "\n--------------------------")

### CALCULATING RESIDUALS MANUALLY
media_segunda = np.mean(segunda)
media_terca = np.mean(terca)
media_quarta = np.mean(quarta)
media_quinta = np.mean(quinta)
residuos_segunda = [x - media_segunda for x in segunda]
residuos_terca = [x - media_terca for x in terca]
residuos_quarta = [x - media_quarta for x in quarta]
residuos_quinta = [x - media_quinta for x in quinta]

my_residual = np.array(residuos_segunda + residuos_terca + residuos_quarta + residuos_quinta)
print("RESIDUALS 2:\n",my_residual, "\n--------------------------")

### CHECK NORMALITY OR RESIDUALS
stats, shap_p_value = shapiro(residuals)
print(f"Normallity results: \nShapiro-stats: {stats}, P-value: {shap_p_value} \n")
if shap_p_value < 0.05:
  print("Residuals are not normal, we can't run ANOVA")
else:
  print("Residuals are normal, we can run ANOVA")
print("--------------------------")

### CHECK HOMOGENEITY OF VARIANCES
stats, levene_p_value = levene(segunda, terca, quarta, quinta)
print(f"Homogeneity variances results: \nLevene-stats: {stats}, P-value: {levene_p_value} \n")
if levene_p_value < 0.05:
  print("Variances are not similar, we can't run ANOVA")
else:
  print("Variances are similar, we can run ANOVA")
print("--------------------------")

### RUN ANOVA IF ALL PREMISSAS ARE OK
if(levene_p_value >= 0.05 and shap_p_value >= 0.05):
  f_stat, p_value = f_oneway(segunda, terca, quarta, quinta)
  print(f"Anova results: \nF-statistic: {f_stat}, P-value: {p_value} \n")
  if p_value < 0.05:
    print("Reject Ho. At least 1 group is different from the others")
  else:
    print("Don't reject Ho. Al groups are similar")
