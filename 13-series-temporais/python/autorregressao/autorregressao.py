import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

# CRIA UMA SERIE TEMPORAL ESTACIONARIA -----------------------------
np.random.seed(42)
tamanho_dados = 100
X_dados = np.arange(0, 100)
dados_estacionarios = np.sin(np.linspace(0, 20, tamanho_dados)) + np.random.normal(0, 0.1, tamanho_dados)
plt.plot(dados_estacionarios)
plt.show()

# SEPARA OS DADOS EM TREINO E TESTE PARA TESTAR A AUTO REGRESSÃO -----------------------------
ponto_corte = 90
X_treino = X_dados[:ponto_corte]
dados_treino = dados_estacionarios[:ponto_corte]

X_teste = X_dados[ponto_corte:]
dados_teste = dados_estacionarios[ponto_corte:]

# executa a auto regressão com lag=15 -----------------------------
lag = 15
modelo = AutoReg(dados_treino, lags=lag)
resultado = modelo.fit()

# executa a previsao e calcula o erro delas
previsoes = resultado.predict(start=len(X_treino), end=len(X_treino)+len(X_teste)-1)
MSE = mean_squared_error(dados_teste, previsoes)
RMSE = np.sqrt(MSE)

print(f'LAG: {lag}, AIC: {resultado.aic:.2f}, ERRO: {RMSE:.4f}')

plt.plot(X_dados, dados_estacionarios, color='blue', label='dados verdadeiros')
plt.plot(X_teste, previsoes, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show()

# encontrando o melhor lag -----------------------------
melhor_lag_segundo_aic = 0
menor_aic = 999_999_999
erro_do_menor_aic = 0

melhor_lag_segundo_erro = 0
menor_erro = 999_999_999
aic_do_menor_erro = 0

for i in range(1, len(X_treino)//2-1):
    modelo = AutoReg(dados_treino, i)
    result = modelo.fit()
    aic = result.aic
    dados_pred = result.predict(start=len(dados_treino), end=len(dados_treino)+len(dados_teste)-1)
    MSE = mean_squared_error(dados_teste, dados_pred)
    RMSE = np.sqrt(MSE)
    if(aic < menor_aic):
        menor_aic = aic
        melhor_lag_segundo_aic = i
        erro_do_menor_aic = RMSE
    if(RMSE < menor_erro):
        menor_erro = RMSE
        melhor_lag_segundo_erro = i
        aic_do_menor_erro = aic
    print(f'I = {i}, AIC = {aic:.2f} ERRO: {RMSE:.4f}')

print(f'MELHOR LAG PELO AIC FOI {melhor_lag_segundo_aic}. AIC = {menor_aic}. ERRO = {erro_do_menor_aic}')
print(f'MELHOR LAG PELO ERRO FOI {melhor_lag_segundo_erro}. ERRO = {menor_erro}. AIC = {aic_do_menor_erro}')

# ANALISE DA REGRESSAO COM O LAG DADO PELO MENOR AIC -----------------------------
modelo = AutoReg(dados_treino, melhor_lag_segundo_aic)
resultado = modelo.fit()
dados_pred = resultado.predict(start=len(dados_treino), end=len(dados_treino)+len(dados_teste)-1)

print(f'LAG: {melhor_lag_segundo_aic}, AIC: {resultado.aic:.2f}, ERRO: {erro_do_menor_aic:.4f}')

plt.plot(X_dados, dados_estacionarios, color='blue', label='dados verdadeiros')
plt.plot(X_teste, previsoes, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show()

# ANALISE DA REGRESSAO COM O LAG DADO PELO MENOR ERRO -----------------------------
modelo = AutoReg(dados_treino, melhor_lag_segundo_erro)
resultado = modelo.fit()
dados_pred = resultado.predict(start=len(dados_treino), end=len(dados_treino)+len(dados_teste)-1)

print(f'LAG: {melhor_lag_segundo_erro}, AIC: {resultado.aic:.2f}, ERRO: {menor_erro:.4f}')

plt.plot(X_dados, dados_estacionarios, color='blue', label='dados verdadeiros')
plt.plot(X_teste, previsoes, color='orange', label='dados previstos')
plt.legend(loc="upper left") 
plt.show()