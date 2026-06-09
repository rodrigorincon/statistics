import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

idades = [45, 50, 30, 60, 55, 40, 35, 70, 65, 50, 42, 36, 53, 58, 62, 39, 48, 33, 66, 41, 57, 49, 34, 61, 47, 38, 54, 63, 32, 46]
glicose = [85, 120, 75, 140, 110, 90, 80, 160, 150, 100, 95, 82, 115, 135, 145, 87, 102, 78, 155, 98, 128, 106, 81, 138, 104, 89, 118, 148, 77, 112]
pressao = [22, 25, 15, 30, 27, 20, 17, 35, 32, 25, 21, 18, 26, 29, 31, 19, 24, 16, 33, 20, 28, 24, 17, 30, 23, 19, 27, 31, 16, 23]
diabetes = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]

# REGRESSÃO LOGISTICA
X_sem_intercepto = pd.DataFrame({'idade': idades, 'glicose': glicose, 'pressao': pressao})
y = pd.DataFrame({'diabetes': diabetes})

X = sm.add_constant(X_sem_intercepto)
modelo = sm.Logit(y, X)
resultado = modelo.fit()
print(resultado.summary(), '\n\n')

####### BOX TIDWELL
def box_tidwell(original_x, original_y):
  if( (original_x <= 0).any().any()):
    raise ValueError(f"##### ERRO: Alguma coluna possui valores não positivos e não posso executar o teste")
  
  data_x = pd.DataFrame(original_x)
  # Adiciona uma coluna X_log para cada var independente, aonde o valor é X*ln(X)
  for col_name in data_x.columns:
    data_x[f'{col_name}_ln'] = data_x[col_name] * np.log(data_x[col_name])
  
  # Executa o teste
  X_box = sm.add_constant(data_x) # Add the intercept term
  # Executa a regressão linear generalizada (GLM) com a família Binomial (Regressão Logística)
  logit_results = sm.GLM(original_y, X_box, family=sm.families.Binomial()).fit()

  return (logit_results.pvalues[1:] >= 0.05).all() # pula o p-valor do intercepto

if(box_tidwell(X_sem_intercepto, y)):
  print("Passou no teste de Linearidade do Logit")
else:
  print("Não passou no teste de Linearidade do Logit")

####### VIF
# A função recebe uma matriz só com as vars independentes (X), aonde cada linha é um ponto
# O 2º parametro é a coluna da variavel que estamos analisando (para ser pulada pelo método)

vif_idade = variance_inflation_factor(X_sem_intercepto, 0)
vif_glicose = variance_inflation_factor(X_sem_intercepto, 1)
vif_pressao = variance_inflation_factor(X_sem_intercepto, 2)
print(f'VIF idade: {vif_idade:.2f}. VIF glicose: {vif_glicose:.2f}. VIF pressao: {vif_pressao:.2f}')
if(vif_idade >= 10 or vif_glicose >= 10 or vif_pressao >= 10):
  print("NÃO PASSOU no teste de multicolinearidade")
elif(vif_idade >= 5 or vif_glicose >= 5 or vif_pressao >= 5):
  print("Alerta Amarelo na multicolinearidade")

####### WALD
p_values = resultado.pvalues[1:] # ignora o intercepto
for i in range(len(p_values)):
  p_value = p_values.iloc[i]
  if(p_value > 0.05):
    print(f'Variavel {X_sem_intercepto.columns[i]} NÃO PASSOU no teste do coeficiente. P-valor = {p_value:.4f}')

####### RAZAO DE VEROSSIMILHANCA
if(resultado.llr_pvalue > 0.05):
  print("NÃO PASSOU no teste de significância do teste como um todo")