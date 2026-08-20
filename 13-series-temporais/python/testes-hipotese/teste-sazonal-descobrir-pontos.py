import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf

# Criando uma série temporal senoidal com uma pitada de aleatoriedade. Cada valor representa 1 mes
datas = pd.date_range(start="2020-01-01", end="2024-12-01", freq="MS")
valores = np.sin(np.linspace(0, 20 * np.pi, len(datas))) + np.random.normal(0, 0.2, len(datas))
serie = pd.Series(valores, index=datas)
print(serie, '\n')
plt.plot(serie)
plt.show()

plot_pacf(serie.dropna()) # lags default = [0, 1, 2... len(serie)]
plt.title('Gráfico de auto correlação parcial')
plt.show()
# o grafico mostra a auto correlação parcial, variando de -1 a 1. Quanto mais longe do 0, maior a auto-correlação com os dados anteriores
# o que estiver fora da caixa azul deve ser usado como ponte de corte
