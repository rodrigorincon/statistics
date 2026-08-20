import ruptures as rpt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import f

# Exemplo de dados com quebra no meio (nos pontos 50, 120, 150)
parte1 = np.random.normal(0, 1, 50)
parte2 = np.random.normal(8, 1, 70)
parte3 = np.random.normal(4, 1, 30)
parte4 = np.random.normal(13, 1, 50)
dados = np.concatenate([parte1, parte2, parte3, parte4])
size_data = len(dados)

x = np.linspace(1, size_data, size_data)
df = pd.DataFrame({"x": x, "dados": dados})

#### acha o ponto de ruptura -------------------------------------------------------------
alg = rpt.Pelt(model="rbf").fit(dados)
rupturas_idx = alg.predict(pen=10)

# Caso o algoritmo retorne o ultimo ponto do array como ruptura, remova-o
if(rupturas_idx[-1] == len(dados)):
  rupturas_idx.pop()

#### Treino com base completa -------------------------------------------------------------
treino_base_completa = smf.ols("dados ~ x", data=df).fit()
soma_residuos_completo = treino_base_completa.ssr # sum of residual Squares (SSR)

#### divide os dados onde tem ruptura ---------------------------------------------
lista_dados = []
idx = 0
while(idx < len(rupturas_idx)):
  if(idx == 0):
    pedaco = df.iloc[:rupturas_idx[idx]]
  elif(idx == len(rupturas_idx) - 1):
    pedaco = df.iloc[rupturas_idx[idx]:]
  else:
    pedaco = df.iloc[rupturas_idx[idx-1]:rupturas_idx[idx]]
  idx += 1
  lista_dados.append(pedaco)

#### treino de cada parte dividida ---------------------------------------------
pedacos_stats = pd.DataFrame({'soma_resid': [], 'graus_lib': []})
i = 0
while(i < len(lista_dados)):
  pedaco = lista_dados[i]
  treino = smf.ols("dados ~ x", data=pedaco).fit()
  soma_residuo = treino.ssr
  graus_lib = treino.df_resid
  pedacos_stats.loc[ len(pedacos_stats) ] = [soma_residuo, graus_lib]
  i += 1


soma_todos_graus_lib = pedacos_stats.graus_lib.sum()

#### calcula o teste chow  ---------------------------------------------
k = treino_base_completa.df_model + 1  # Número de parâmetros (incluindo intercepto)

numerator = (soma_residuos_completo - pedacos_stats.soma_resid.sum() ) / k
denominator = pedacos_stats.soma_resid.sum() / soma_todos_graus_lib
chow_stat = numerator / denominator

p_value = 1 - f.cdf(chow_stat, k, soma_todos_graus_lib)

print("Pontos de corte: ", rupturas_idx)
print(f"Estatística F: {chow_stat:.4f}, P-valor: {p_value:.4f}")
if(p_value < 0.05):
  print("Rejeito H0, há quebra estrutural")
else:
  print("Rejeito H0, NÃO há quebra estrutural")
