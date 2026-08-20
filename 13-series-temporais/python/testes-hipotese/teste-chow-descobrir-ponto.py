import ruptures as rpt
import numpy as np

# Exemplo de dados com 2 quebras no meio. Tamanho dos dados = 130
# pontos de ruptura: 50 e 65
parte1 = np.random.normal(0, 1, 50)
parte2 = np.random.normal(8, 1, 15)
parte3 = np.random.normal(2, 1, 65)

dados = np.concatenate([parte1, parte2, parte3])

# Algoritmo PELT para achar o ponto de ruptura
alg = rpt.Pelt(model="rbf").fit(dados) # PELT = Pruned Exact Linear Time. Método avançado de programação dinâmica
rupturas_idx = alg.predict(pen=10)

# o algorimo retorna a ultima posição como um ponto de ruptura. Caso ele faça isso o remove
if(rupturas_idx[-1] == len(dados)):
  rupturas_idx.pop() # remove o ultimo ponto de ruptura pois ele é o fim do array

print("Ponto(s) de ruptura identificado(s):", rupturas_idx)
