import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

np.random.seed(42)
# dados NÃO  estacionarios
values = pd.Series( np.cumsum( np.random.normal(scale=2, size=100) ) + np.linspace(0, 30, 100) )

# coeficientes do nosso ARIMA(2, 1, 1)
p = 2
q = 1
d = 1

model = ARIMA(values, order=(p, d, q)).fit(method='innovations_mle') 
# opções de metodos de estimativa: 
# 'statespace' = Filtro de Kalman
# 'innovations_mle' = maxima verossimilhanca
# 'hannan_rissanen'
# 'burg' = Levinson-Durbin, bom para series pequenas
# 'innovations' = exclusiva para ARMA
# 'yule_walker' = exclusivo para modelos AR

print(model.summary())

# prevê os proximos 5 dias
forecast = model.forecast(steps=5)
print("\nForecasted Values:")
print(forecast)
