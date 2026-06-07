import pandas as pd
import numpy as np
import statsmodels.api as sm

idades = [45, 50, 30, 60, 55, 40, 35, 70, 65, 50, 42, 36, 53, 58, 62, 39, 48, 33, 66, 41, 57, 49, 34, 61, 47, 38, 54, 63, 32, 46]
glicose = [85, 120, 75, 140, 110, 90, 80, 160, 150, 100, 95, 82, 115, 135, 145, 87, 102, 78, 155, 98, 128, 106, 81, 138, 104, 89, 118, 148, 77, 112]
diabetes = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]

# REGRESSÃO LOGISTICA COM NUMPY
X = np.array([idades, glicose]).T
y = np.array([diabetes]).T

X = sm.add_constant(X)
modelo = sm.Logit(y, X)
resultado = modelo.fit()
print(resultado.summary())

# PREVISÃO
novo_valor_idade = 60
novo_valor_glicose = 130
novo_X = pd.DataFrame({'const': [1], 'idade': [novo_valor_idade], 'glicose': [novo_valor_glicose]})
prob_prevista = resultado.predict(novo_X)
print(f'\nA probabilidade prevista de ser diabético é: {prob_prevista[0]:.2f}\n\n\n')


# REGRESSÃO LOGISTICA COM PANDAS
X = pd.DataFrame({'idade': idades, 'glicose': glicose})
y = pd.DataFrame({'diabetes': diabetes})

X = sm.add_constant(X)
modelo = sm.Logit(y, X)
resultado = modelo.fit()
print(resultado.summary())

# PREVISÃO
novo_valor_idade = 60
novo_valor_glicose = 130
novo_X = pd.DataFrame({'const': [1], 'idade': [novo_valor_idade], 'glicose': [novo_valor_glicose]})
prob_prevista = resultado.predict(novo_X)
print(f'\nA probabilidade prevista de ser diabético é: {prob_prevista[0]:.2f}') 