import pandas as pd
import matplotlib.pylab as plt
## pip install pmdarima
from pmdarima.arima import auto_arima

# carrega os dados e visualiza
data = pd.read_csv('../AirPassengers.csv', parse_dates=['Month'], index_col='Month')
print(data.head())

plt.plot(data)
plt.show()

# auto_arima encontra os melhores p, q e d sozinho, ñ preciso rodar mil modelos e compará-los. Ele ja faz tudo isso sozinho
# (opcional) posso passar valores iniciais de p, q e d pra facilitar a convergir e definir também valores máximos pra eles
# seasonal informa que existe sazonalidade e a função irá rodar SARIMA pra tratar a sazonalidade
# m = qual o periodo de sazonalidade dos dados. Como cada dado é 1 mes e a sazonalidade é anual, m=12
# trace é para imprimir cada combinação
# stepwise se deve testar TODAS as combinações ou não (caso true ele vai dar saltos maiores pulando combinações que julga ñ dar um resultado melhor que os que ja tem)
modelo = auto_arima(data, start_p=1,start_q=1,start_d=0, max_p=6, max_q=6, 
                    seasonal=True, m=12, trace=True, stepwise=True)

print('AIC do melhor modelo: ', round(modelo.aic(), 3)) # 1012.991 com stepwise False / 1019.178 com stepwise True (modo rápido perdeu o melhor modelo)

###### TESTE DO MODELO --------------------------
train = data.loc['1949-01-01':'1959-12-01']
test = data.loc['1960-01-01':]
result = modelo.fit(train)
print('\n RESULTADO DO TREINO --------------------- ')
print(result.summary(), '\n\n')
print(f'melhor p = {result.order[0]} melhor d = {result.order[1]} melhor q = {result.order[2]}')
print(f'Parametros Ssazonais \nmelhor P = {result.seasonal_order[0]} melhor D = {result.seasonal_order[1]} melhor Q = {result.seasonal_order[2]} melhor s = {result.seasonal_order[0]}')
print('Params')
print(result.params())


# prever dados dos proximos 12 meses
previsoes = modelo.predict(n_periods=12)
print('PREVISOES')
print(previsoes)

## plotando os valores previstos com os reais
plt.plot(data, label='Original', color='blue')
plt.plot(previsoes, label='Teste', color='orange')
plt.legend(loc="upper left")
plt.show()

# plotando só a parte comum aos 2 para ver mais de perto quão próximo foi
plt.plot(test, label='Original', color='blue')
plt.plot(previsoes, label='Teste', color='orange')
plt.legend(loc="upper left")
plt.show()
