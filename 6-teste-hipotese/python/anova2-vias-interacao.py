from itertools import chain
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
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
modelo = smf.ols('Salario ~ Area + Formacao + Area:Formacao', data=salarios).fit()
# run steps 1, 2 and 3 (just don't run F test)
# that's why we can get the residual
# we can get the sum of variances or their divided by free degrees
# syntax: group1:group2 (analize the interation between the both groups)
print(modelo.summary(), '\n-----------------------------\n')


### RUN ANOVA IF ALL PREMISSAS ARE OK
anova_table = sm.stats.anova_lm(modelo, typ=2)
print(anova_table, '\n--------------')

p_values = anova_table['PR(>F)'].dropna().tolist()
if(p_values[-1] < 0.05): # verifico o p-valor da interação primeiro
  print("Rejeito Ho: uma var influencia a outra e preciso fazer uma análise de regressão para tirar melhores informações")
else:
  print("Aceitei Ho: as vars são independentes. Portanto vamos checar os grupos")
  if(p_values[0] < 0.05): # SEGUE A ORDEM USADA NO smf.ols
    print("Há diferenças entre os grupos de Area")
  else:
    print("Os grupos de Area são similares")
  
  if(p_values[1] < 0.05):
    print("Há diferenças entre os grupos de Formacao")
  else:
    print("Os grupos de Formação são similares")