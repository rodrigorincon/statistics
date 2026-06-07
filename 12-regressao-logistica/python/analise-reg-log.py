import pandas as pd
import numpy as np
import statsmodels.api as sm

idades = [45, 50, 30, 60, 55, 40, 35, 70, 65, 50, 42, 36, 53, 58, 62, 39, 48, 33, 66, 41, 57, 49, 34, 61, 47, 38, 54, 63, 32, 46]
glicose = [85, 120, 75, 140, 110, 90, 80, 160, 150, 100, 95, 82, 115, 135, 145, 87, 102, 78, 155, 98, 128, 106, 81, 138, 104, 89, 118, 148, 77, 112]
diabetes = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]

# REGRESSÃO LOGISTICA COM PANDAS
X = pd.DataFrame({'idade': idades, 'glicose': glicose})
y = pd.DataFrame({'diabetes': diabetes})

X = sm.add_constant(X)
modelo = sm.Logit(y, X)
resultado = modelo.fit()
print(resultado.summary())
# METHOD: MLE (máxima verossimilhança)
# converged: True (o gradiente descendente convergiu para um mínimo, não rodou até o limite de iterações)

# PSEUDO R²: 0.645 (indica que o modelo explica 64,5% da variabilidade dos dados)
# Ele usa a variação de McFadden, que é 1 - Log-Likelohood/LL-Null

# Log-Likelihood: valor da função de log-verossimilhança -> y*ln(sigmoide) + (1-y)*ln(1-sigmoide)
# Log-Likelihood: quanto mais próximo de zero, melhor o ajuste do modelo (por ser a derivada da função de custo, o ponto = 0 é o ideal)
# Log-Likelihood: nosso H1, diz se essas vars independentes explicam suficientemente bem os dados
# Podemos comparar o Log-Likelihood de 2 modelos para ver qual é o melhor

# LL-Null: nosso H0. modelo sem nenhuma var independente, apenas intercepto (linha reta)
# Log-Likelihood precisa ser mais proximo de 0 que LL-Null sempre!!!!

# LLR-P: p-valor do teste de razão de verossimilhança. É o p-valor do Log-Likelihood
# LLR-P < alfa: Indica que o as variáveis usadas são estaticamente significativas em prever os resultados comparado ao LL-Null

print(f'Pseudo R2: {resultado.prsquared}')
print(f'Log-Verossimilhança: {resultado.llf}')
print(f'Log-Null: {resultado.llnull}')

print(f'Valor Qui-Quadrado da log-verossimilhança: {resultado.llr}') # 2 × (llf - llnull)
print(f'P-valor: {resultado.llr_pvalue}')