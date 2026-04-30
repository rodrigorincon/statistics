from itertools import chain
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import shapiro
from scipy.stats import levene
# OBS: doesnt exist a f_twoway in scipy.stats, to do anova with 2 way needs to use statsmodels!

### BUILD THE DATAFRAME
educacao = [{
    'Formacao': 'ensino médio',
    'Salarios': [20,25,22]
  },{
    'Formacao': 'graduação',
    'Salarios': [30, 35, 34]
  },{
    'Formacao': 'mestrado',
    'Salarios': [46, 47, 50]
  },{
    'Formacao': 'doutorado',
    'Salarios': [79, 78, 74]
  }
]

financas = [{
    'Formacao': 'ensino médio',
    'Salarios': [27, 25, 25]
  },{
    'Formacao': 'graduação',
    'Salarios': [44, 46, 48]
  },{
    'Formacao': 'mestrado',
    'Salarios': [50, 58, 56]
  },{
    'Formacao': 'doutorado',
    'Salarios': [90, 92, 95]
  }
]

medicina = [{
    'Formacao': 'ensino médio',
    'Salarios': [26, 24, 25]
  },{
    'Formacao': 'graduação',
    'Salarios': [42, 43, 45]
  },{
    'Formacao': 'mestrado',
    'Salarios': [62, 56, 60]
  },{
    'Formacao': 'doutorado',
    'Salarios': [90, 100, 105]
  }
]

num_salarios_edu = sum([ len(edu["Salarios"]) for edu in educacao])
num_salarios_fin = sum([ len(edu["Salarios"]) for edu in financas])
num_salarios_med = sum([ len(edu["Salarios"]) for edu in medicina])

formation_edu = list(chain.from_iterable([ [edu['Formacao']]*len(edu['Salarios']) for edu in educacao]))
formation_fin = list(chain.from_iterable([ [edu['Formacao']]*len(edu['Salarios']) for edu in financas]))
formation_med = list(chain.from_iterable([ [edu['Formacao']]*len(edu['Salarios']) for edu in medicina]))

list_salaries = [obj["Salarios"] for obj in educacao] + [obj["Salarios"] for obj in financas] + [obj["Salarios"] for obj in medicina]

salarios = pd.DataFrame({
    'Formacao': list(chain.from_iterable([formation_edu, formation_fin, formation_med])),
    'Area': ['Educação']*num_salarios_edu + ['Finanças']*num_salarios_fin + ['Medicina']*num_salarios_med,
    'Salario': list(chain.from_iterable(list_salaries))
})

### MODEL IS USED TO GET RESIDUAL AND TO RUN ANOVA NOW
modelo = smf.ols('Salario ~ Area + Formacao', data=salarios).fit()
# run steps 1, 2 and 3 (just don't run F test)
# that's why we can get the residual
# we can get the sum of variances or their divided by free degrees
# its here where join the groups
# syntax: group1 + group2 (analize both groups)
print(modelo.summary())

### CHECK NORMALITY OR RESIDUALS
residuals = modelo.resid
print('--------------\nResiduals\n',residuals.head(),'\n----------------------')

stats, shap_p_value = shapiro(residuals)
print(f"Normallity results: \nShapiro-stats: {stats}, P-value: {shap_p_value} \n")
if shap_p_value < 0.05:
  print("Residuals are not normal, we can't run ANOVA")
else:
  print("Residuals are normal, we can run ANOVA")
print("--------------------------")

### CHECK HOMOGENEITY OF VARIANCES
grupos = salarios.groupby(['Area', 'Formacao'])['Salario'].apply(list) # agrupa pelos grupos para poder testar o levene
print(grupos)

stats, levene_p_value = levene(*grupos)
print(f"-----------\nHomogeneity variances results: \nLevene-stats: {stats}, P-value: {levene_p_value} \n")
if levene_p_value < 0.05:
  print("Variances are not similar, we can't run ANOVA")
else:
  print("Variances are similar, we can run ANOVA")
print("--------------------------")

### RUN ANOVA IF ALL PREMISSAS ARE OK
if(levene_p_value >= 0.05 and shap_p_value >= 0.05):
  anova_table = sm.stats.anova_lm(modelo, typ=2)
  print(anova_table, '\n--------------')
