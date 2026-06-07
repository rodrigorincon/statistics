import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

# VARs INDEPENDENTES X E VAR DEPENDENTE Y
data = pd.DataFrame({
    'idade': np.random.randint(30, 80, size=100), # X1
    'colesterol': np.random.randint(150, 300, size=100), # X2
    'infarto': np.random.choice([0, 1], size=100) # Y
})

# Adiciona uma coluna X_log para cada var independente, aonde o valor é X*ln(X)
vars_log = []
for col_name in data.columns[:-1]:
    if (data[col_name] <= 0).any():
        print(f"##### ERRO: Coluna '{col_name}' possui valores não positivos e não posso executar o teste")
        sys.exit(0)

    data[f'{col_name}_ln'] = data[col_name] * np.log(data[col_name])
    vars_log.append(f'{col_name}_ln')

# Nossas vars X são tanto as vars originais (idade e colesterol) quanto a versão log delas
X = data.drop('infarto', axis=1)

# Executa o teste
X = sm.add_constant(X) # Add the intercept term
y = data['infarto']

# Executa a regressão linear generalizada (GLM) com a família Binomial (Regressão Logística)
logit_model = sm.GLM(y, X, family=sm.families.Binomial())
logit_results = logit_model.fit()

# Pega os p-valores apenas dos coeficientes com log
for col_name in vars_log:
    p_value = logit_results.pvalues[col_name]
    if p_value >= 0.05:
        print(f'Var {col_name} PASSOU')
    else:
        print(f'Var {col_name} NÃO TEM LOGIT LINEAR')