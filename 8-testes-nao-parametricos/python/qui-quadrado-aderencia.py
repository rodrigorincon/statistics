import numpy as np
import scipy.stats as stats

def calc_rejeitos(observados, esperados):
  print("\n---------- Calculando Rejeitos Padronizados...")
  total = np.sum(observados)
  residuos = (observados - esperados)/np.sqrt(esperados)
  print("Rejeitos Padronizados:", residuos)
  print("------------ Quais que estão fortemente associados (outliers, acima de 1,96)")
  for i in range(len(observados)):
    if abs(residuos[i]) > 1.96:
      print(f"Linha {i}, Valor Observado: {observados[i]}, Valor Esperado: {esperados[i]}")


# TESTE: Checar se um dado é justo. Jogamos o dado 60x
# Compara com a distribuição uniforme

# Frequências observadas (quantas vezes cada face saiu)
observados = np.array([17, 5, 14, 6, 6, 12])

# Frequências esperadas (se o dado fosse perfeitamente justo, 
# esperaríamos 10 vezes para cada uma das 6 faces: 60/6 = 10)
esperados = np.array([10, 10, 10, 10, 10, 10])

# Realizar o teste qui-quadrado
chi2, p_valor = stats.chisquare(f_obs=observados, f_exp=esperados)

print(f"Valor do X²: {chi2}")
print(f"Graus de Liberdade: ", len(observados) - 1)
print(f"p-valor: {p_valor}")

# Interpretação
if p_valor < 0.05:
  print("Não segue a distribuição esperada (rejeita H0)")
  calc_rejeitos(observados, esperados)
else:
  print("Segue a distribuição esperada (não rejeita H0)")
