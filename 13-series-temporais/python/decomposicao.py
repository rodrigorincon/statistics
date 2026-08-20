import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose, STL

df = pd.read_csv('all_stocks_5yr.csv')
print(df.head(), '\n')
print('Tipo da var data: ', df.date.dtypes)
df.date = pd.to_datetime(df.date)
print('Novo tipo da var data: ', df.date.dtypes)

df_apple = df[df.Name == 'AAPL'].set_index('date')
print('Data frame da Apple')
print(df_apple.head(), '\n')

ts = df_apple['close']
ts.plot(title='Preco de fechamento das acoes da Apple')
plt.show()

# DECOMPOSICAO ADITIVA E MULTIPLICATIVA LADO A LADO
addit_decomp = seasonal_decompose(ts, model='additive', period=252) # numero de dias uteis no ano
mult_decomp = seasonal_decompose(ts, model='multiplicative', period=252) # numero de dias uteis no ano

# para forçar os graficos de aditivos emultiplicativo a usarem os mesmos limites e podermos comparar os 2 lado a lado
min_orig = min(addit_decomp.observed.min(), mult_decomp.observed.min())
max_orig = max(addit_decomp.observed.max(), mult_decomp.observed.max())

min_tend = min(addit_decomp.trend.min(), mult_decomp.trend.min())
max_tend = max(addit_decomp.trend.max(), mult_decomp.trend.max())

min_sazon = min(addit_decomp.seasonal.min(), mult_decomp.seasonal.min())
max_sazon = max(addit_decomp.seasonal.max(), mult_decomp.seasonal.max())

min_resid = min(addit_decomp.resid.min(), mult_decomp.resid.min())
max_resid = max(addit_decomp.resid.max(), mult_decomp.resid.max())

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 8))
axes[0,0].plot(addit_decomp.observed, color="blue")
axes[0,0].set(ylabel="Original")
axes[0,0].set_ylim(min_orig,max_orig)
axes[1,0].plot(addit_decomp.trend, color="blue")
axes[1,0].set(ylabel="Tendência")
axes[1,0].set_ylim(min_tend, max_tend)
axes[2,0].plot(addit_decomp.seasonal, color="blue")
axes[2,0].set(ylabel="Sazonalidade")
axes[2,0].set_ylim(min_sazon, max_sazon)
axes[3,0].plot(addit_decomp.resid, color="blue")
axes[3,0].set(ylabel="Resíduos")
axes[3,0].set_ylim(min_resid, max_resid)
axes[0,0].set_title("Aditivo")

axes[0,1].plot(mult_decomp.observed, color="blue")
axes[0,1].set_ylim(min_orig,max_orig)
axes[1,1].plot(mult_decomp.trend, color="blue")
axes[1,1].set_ylim(min_tend, max_tend)
axes[2,1].plot(mult_decomp.seasonal, color="blue")
axes[2,1].set_ylim(min_sazon, max_sazon)
axes[3,1].plot(mult_decomp.resid, color="blue")
axes[3,1].set_ylim(min_resid, max_resid)
axes[0,1].set_title("Multiplicativo")

plt.tight_layout()
plt.show()
# sazonalidade e residuos do multiplicativo variam quase nada enquanto no aditvo tao bem mais espalhados
# o que indica que o aditivo é melhor para esses dados

# plotando cada um separadamente para conseguir ver melhor. Atente-se que os valore sno eixo-y mudam entre os aditivos e multiplicativos
addit_decomp.plot()
plt.xticks(rotation=45)
plt.show()

mult_decomp.plot()
plt.xticks(rotation=45)
plt.show()

#### DECOMPOSICAO VIA STL
stl_result = STL(ts, period=252, robust=True).fit()
stl_result.plot()
plt.xticks(rotation=45)
plt.show()
# curva de tendencia mais suave, indicando que deve ser a melhor opcao