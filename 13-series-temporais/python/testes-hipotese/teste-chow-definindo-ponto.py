import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.stats import f

np.random.seed(42)
x = np.linspace(1, 50, 50)

split_idx = 30 # Ponto de divisão (breakpoint)
# cria dados que dão um salto no índice 30
dados = np.where(x <= split_idx, 2 * x + np.random.normal(0, 2, 50), 5 * x + np.random.normal(0, 2, 50))

print(dados)
plt.plot(dados)
plt.show()

df = pd.DataFrame({"x": x, "dados": dados})

#### faz a análise sem quebrar ---------------------------------------------
treino_base_completa = smf.ols("dados ~ x", data=df).fit()
soma_quadrado_erros = treino_base_completa.ssr # sum of residual Squares (SSR)
graus_lib_erros = treino_base_completa.df_resid
print(f"Soma dos quadrados dos erros: {soma_quadrado_erros:.2f}. Graus de liberdade dos residuos: {graus_lib_erros}")
# SSR: 39614.70, Graus de lib: 48

#### faz a análise quebrando, faz uma analise pra cada pedaço ---------------------------------------------
df1 = df.iloc[:split_idx]
df2 = df.iloc[split_idx:]

treino1 = smf.ols("dados ~ x", data=df1).fit()
treino2 = smf.ols("dados ~ x", data=df2).fit()

soma_quadrado_erros1 = treino1.ssr
soma_quadrado_erros2 = treino2.ssr
soma_graus_lib_grupos = treino1.df_resid + treino2.df_resid

print("GRUPO 1 -------------")
print(f"Soma dos quadrados dos erros: {soma_quadrado_erros1:.2f}. Graus de liberdade: {treino1.df_resid}")
print("GRUPO 2 -------------")
print(f"Soma dos quadrados dos erros: {soma_quadrado_erros2:.2f}. Graus de liberdade: {treino2.df_resid}\n")
print(f"Soma dos 2 graus de liberdade: {soma_graus_lib_grupos}")
# SSR grupo 1: 110.83, Graus de lib: 28
# SSR grupo 2: 77.6, Graus de lib: 18
# Soma dos 2 gras de lib: 46
#### percebe-se que os erros dos resíduos tá absurdamente maior no original, 
#### pois ñ existe regressão linear que encaixe bem com a quebra dos dados. 
#### Analisando as partes em separado suas regressões parecem mais plausiveis

#### Cálculo da Estatística F de Chow ---------------------------------------------
k = treino_base_completa.df_model + 1  # Número de parâmetros (incluindo intercepto)
numerator = (soma_quadrado_erros - (soma_quadrado_erros1 + soma_quadrado_erros2)) / k
denominator = (soma_quadrado_erros1 + soma_quadrado_erros2) / soma_graus_lib_grupos
chow_stat = numerator / denominator

p_value = 1 - f.cdf(chow_stat, k, soma_graus_lib_grupos)

print(f"Estatística F: {chow_stat:.4f}, P-valor: {p_value:.4f}")
if(p_value < 0.05):
  print("Rejeito H0, há quebra estrutural")
else:
  print("Rejeito H0, NÃO há quebra estrutural")
