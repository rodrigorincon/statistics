import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Dados: X de 10 a 50, y = 3X + 10 + ruído
X = np.linspace(10, 50, 100)
y = 3 * X + 10 + np.random.normal(0, 15, 100)
dados = pd.DataFrame({'X': X, 'y': y})

# Ajustando o modelo OLS
regressao = sm.OLS(y, X).fit()

# Calculando os valores pros mesmos dados seguindo a reta da regressão e calculando os intervalos de predição
previsoes = regressao.get_prediction(dados[['X']])
intervalos = previsoes.summary_frame()

media_estimada = intervalos['mean']
intervalo_conf = intervalos[['mean_ci_lower', 'mean_ci_upper']]
intervalo_pred = intervalos[['obs_ci_lower', 'obs_ci_upper']]

# Plotando os dados, a reta de regressão e os intervalos
plt.figure(figsize=(10, 6))
plt.scatter(dados['X'], dados['y'], label='Dados Observados', color='black', alpha=0.5)
plt.plot(dados['X'], media_estimada, color='blue', label='Reta de Regressão (OLS)')

# Intervalo de Confiança (Média estimada)
plt.fill_between(dados['X'], intervalo_conf['mean_ci_lower'], intervalo_conf['mean_ci_upper'], 
                 color='blue', alpha=0.2, label='Intervalo de Confiança')

# Intervalo de Predição (Novas observações)
plt.fill_between(dados['X'], intervalo_pred['obs_ci_lower'], intervalo_pred['obs_ci_upper'], 
                 color='red', alpha=0.1, label='Intervalo de Predição')

plt.xlabel('Variável Independente (X)')
plt.ylabel('Variável Dependente (y)')
plt.legend()
plt.title('Regressão OLS: Intervalos de Confiança e Predição')
plt.show()
