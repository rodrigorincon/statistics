import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

# IMPORTACAO E VISUALIZACAO DOS DADOS -----------------------------
dados = pd.read_csv('../AirPassengers.csv')
print(dados.head())
print(dados.tail()) # ver as ultimas datas

dados.plot()
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Passageiros')
plt.tight_layout()
plt.show()

# SEPARA OS DADOS EM TREINO E TESTE PARA TESTAR A AUTO REGRESSÃO -----------------------------

# usa de 1949 até 1958 como treino e 1959 e 1960 como teste
datas_treino = dados[dados.Month < '1959-01-01' ].Month.values
X_treino = dados[dados.Month < '1959-01-01' ]['#Passengers'].values

datas_teste = dados[dados.Month >= '1959-01-01' ].Month.values
X_teste = dados[dados.Month >= '1959-01-01' ]['#Passengers'].values

# FAZ A AUTO REGRESSAO CONSIDERANDO SÓ OS DADOS DE TREINO -----------------------------
modelo = AutoReg(X_treino, 1) # AR(1), considera só o último dado pra prever o próximo
resultado = modelo.fit()
print(resultado.summary(), '\n')
print(f'AIC com AR(1) = {resultado.aic:.2f}')

# TENTA PREVER OS DADOS USANDO SÓ O ULTIMO VALOR COMO REFERENCIA -----------------------------
X_pred = resultado.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)
print('Valores preditos pros anos 1959 e 1960\n', X_pred)

plt.plot(datas_treino, X_treino, color='blue', label='dados de treino')
plt.plot(datas_teste, X_teste, color='green', label='dados verdadeiros')
plt.plot(datas_teste, X_pred, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show() # pessima previsão, passou longe. Previsão fez uma curva suave descendo

MSE = mean_squared_error(X_teste, X_pred)
RMSE = np.sqrt(MSE)
print(f'raiz dos erros ao quadrado com AR(1): {RMSE:.2f}')

# usando um lag maior (no caso 12, pegando o ano todo) -----------------------------
modelo = AutoReg(X_treino, 12) # considera o ano todo
resultado = modelo.fit()
print(resultado.summary(), '\n')
print(f'AIC com AR(12) = {resultado.aic:.2f}')

X_pred = resultado.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)

plt.plot(datas_treino, X_treino, color='blue', label='dados de treino')
plt.plot(datas_teste, X_teste, color='green', label='dados verdadeiros')
plt.plot(datas_teste, X_pred, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show()

MSE = mean_squared_error(X_teste, X_pred)
RMSE = np.sqrt(MSE)
print(f'raiz dos erros ao quadrado com AR(12): {RMSE:.2f}')

# encontrando o melhor lag -----------------------------
melhor_lag_segundo_aic = 0
melhor_aic = 999_999_999

melhor_lag_segundo_erro = 0
melhor_erro = 999_999_999

for i in range(1, len(X_treino)//2-1):
    modelo = AutoReg(X_treino, i)
    result = modelo.fit()
    aic = result.aic
    if(aic < melhor_aic):
        melhor_aic = aic
        melhor_lag_segundo_aic = i
    X_pred = result.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)
    MSE = mean_squared_error(X_teste, X_pred)
    RMSE = np.sqrt(MSE)
    if(RMSE < melhor_erro):
        melhor_erro = RMSE
        melhor_lag_segundo_erro = i
    print(f'I = {i}, AIC = {aic:.2f} ERRO: {RMSE:.2f}')

print(f'MELHOR LAG PELO AIC FOI {melhor_lag_segundo_aic}. AIC = {melhor_aic}')
print(f'MELHOR LAG PELO ERRO FOI {melhor_lag_segundo_erro}. ERRO = {melhor_erro}')

# ANALISE DA REGRESSAO COM O LAG DADO PELO MENOR AIC -----------------------------
modelo = AutoReg(X_treino, melhor_lag_segundo_aic)
resultado = modelo.fit()
print(resultado.summary(), '\n')

X_pred = resultado.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)

plt.plot(datas_treino, X_treino, color='blue', label='dados de treino')
plt.plot(datas_teste, X_teste, color='green', label='dados verdadeiros')
plt.plot(datas_teste, X_pred, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show() # manteve o padrao da sazonalidade, mas explodiu ele muito mais que o normal

# ANALISE DA REGRESSAO COM O LAG DADO PELO MENOR ERRO -----------------------------
modelo = AutoReg(X_treino, melhor_lag_segundo_erro)
resultado = modelo.fit()
print(resultado.summary(), '\n')

X_pred = resultado.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)

plt.plot(datas_treino, X_treino, color='blue', label='dados de treino')
plt.plot(datas_teste, X_teste, color='green', label='dados verdadeiros')
plt.plot(datas_teste, X_pred, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show() # claramente o melhor resultado foi o com menor erro, nao o com menor AIC