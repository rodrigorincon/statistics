import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats

preco = [840000, 822000, 713000, 689000, 685000, 645000, 625000, 620000, 587500, 585000, 583000, 569000, 546000, 540000, 537000, 
516000, 511000, 510000, 495000, 463000, 457000, 451000, 435000, 431700, 414000, 401500, 399000, 380000, 380000, 375900, 372000, 367500,
356500, 330000, 330000, 307500]

m2 = [257, 232, 222, 204, 252, 234, 253, 226, 195, 180, 206, 303, 166, 138, 270, 181, 162, 160, 157, 159, 153, 156, 139, 176, 109, 107, 
128, 124, 118, 211, 93, 118, 132, 126, 136, 78]

df = pd.DataFrame({'preco': preco, 'm2': m2})

X = sm.add_constant(df['m2']) # Adicionar intercepto
y = df['preco']
regressao = sm.OLS(y, X).fit()

# Mostrando como o intervalo de confiança cresce ao aumentar o nível de confiança (diminuir alfa).
intervalo_95 = regressao.conf_int() # intervalo de confiança padrão (95%)
intervalo_90 = regressao.conf_int(alpha=0.10) # intervalo de confiança de 90%
intervalo_99 = regressao.conf_int(alpha=0.01) # intervalo de confiança de 99%

margem_m2_95 = np.round((intervalo_95.loc['m2'][1] - intervalo_95.loc['m2'][0])/2, 2)
margem_m2_90 = np.round((intervalo_90.loc['m2'][1] - intervalo_90.loc['m2'][0])/2, 2)
margem_m2_99 = np.round((intervalo_99.loc['m2'][1] - intervalo_99.loc['m2'][0])/2, 2)

a1 = np.round(regressao.params['m2'], 2)
print(f'A1 com Intervalo de Confiança de 90%: {a1} +- {margem_m2_90}') # 452.88
print(f'A1 com Intervalo de Confiança de 95%: {a1} +- {margem_m2_95}') # 544.30
print(f'A1 com Intervalo de Confiança de 99%: {a1} +- {margem_m2_99}') # 730.75