import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, root_mean_squared_error

serie = pd.Series([10, 12, 13, 15, 18, 20, 21, 23, 25, 28])

# Calculando média móvel com janelas de 3 e 5
ma3 = serie.rolling(window=3).mean()
ma5 = serie.rolling(window=5).mean()
print(ma3.values, '\n')
print(ma5.values, '\n')

# A janela gera valores NaN no começo dos arrays, irei remove-los
m3 = ma3.dropna().values
m5 = ma5.dropna().values

# Cria uma copia dos dados reais descartando os dados mais antigos, que não tem previsões para suas posições
real3 = serie.iloc[2:].values
real5 = serie.iloc[4:].values

print('---------- PREVISOES COM JANELA = 3')
print('ORIGINAL')
print(real3)
print('PREVISTO')
print(m3.round())
print('ERROS')
print( (real3 - m3).round() , '\n')

print('---------- PREVISOES COM JANELA = 5')
print('ORIGINAL')
print(real5)
print('PREVISTO')
print(m5.round())
print('ERROS')
print( (real5 - m5).round() , '\n')

# Calculando as métricas MAE, MAPE e RMSE
metricas = {
    "Média Móvel 3": {
        "MAE": mean_absolute_error(real3, m3),
        "MAPE": mean_absolute_percentage_error(real3, m3),
        "RMSE": root_mean_squared_error(real3, m3)
    },
    "Média Móvel 5": {
        "MAE": mean_absolute_error(real5, m5),
        "MAPE": mean_absolute_percentage_error(real5, m5),
        "RMSE": root_mean_squared_error(real5, m5)
    }
}

print(pd.DataFrame(metricas))
# as 2 séries tem MAE e RMSE parecidas, indicando que nenhuma tem outliers nos erros
# todas as 3 métricas da média 3 são menores que as da média 5, logo a janela 3 erra menos

# comparamos MAE com RMSE para ver se tem outliers
def check_outliers(mae, rmse, lag):
    dispersao = rmse/mae
    print('Dispersão da janela', lag, ': ', round(dispersao, 4))
    if(dispersao < 1.2):
        print('Sem outliers nos erros')
    elif(dispersao >= 1.2 and dispersao <= 1.5):
        print('Dispersão moderada, mas ainda OK')
    else:
        print('Tem outliers nos erros. Modelo comete erros muito grandes')
        

check_outliers(metricas['Média Móvel 3']['MAE'], metricas['Média Móvel 3']['RMSE'], 3)
check_outliers(metricas['Média Móvel 5']['MAE'], metricas['Média Móvel 5']['RMSE'], 5)