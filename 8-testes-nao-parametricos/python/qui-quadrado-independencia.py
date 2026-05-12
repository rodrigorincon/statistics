import numpy as np
from scipy.stats import chi2_contingency

def calc_rejeitos(observados, esperados):
  print("\n---------- Calculando Rejeitos Padronizados...")
  total = np.sum( np.array(observados) )
  residuos = []
  for i in range(len(observados)):
    residuos.append([])
    totalLinha = sum(observados[i])
    for j in range(len(observados[0])):
      O = observados[i][j]
      E = esperados[i][j]
      totalColuna = sum([observados[k][j] for k in range(len(observados))])
      residuo = (O - E)/( np.sqrt(E) * np.sqrt(1 - totalLinha/total) * np.sqrt(1 - totalColuna/total) )
      residuos[i].append(residuo)
  print("Rejeitos Padronizados:", residuos)
  print("------------ Quais que estão fortemente associados (outliers, acima de 1,96)")
  for i in range(len(observados)):
    for j in range(len(observados[0])):
      if abs(residuos[i][j]) > 1.96:
        print(f"Linha {i} e Coluna {j}")

# Exemplo: Teste de Independência
data = [[10, 18, 15], [20, 40, 20]] # Valores Observados
chi2, p, dof, expected = chi2_contingency(data)
print(f"Graus de liberdade: {dof}") 
print(f"Valores esperados: {expected}") 
print(f"Valor do X²: {chi2}")

print(f"p-valor: {p}")
if p < 0.05:
    print("Variáveis dependentes (rejeita H0)")
    calc_rejeitos(data, expected)
else:
    print("Variáveis independentes (não rejeita H0)")


# Exemplo2
print("----------------")
data = [[10, 11, 17], [6, 30, 9]] # Valores Observados
chi2, p, dof, expected = chi2_contingency(data)
print(f"Graus de liberdade: {dof}") 
print(f"Valores esperados: {expected}") 
print(f"Valor do X²: {chi2}")

print(f"p-valor: {p}")
if p < 0.05:
    print("Variáveis dependentes (rejeita H0)")
    calc_rejeitos(data, expected)
else:
    print("Variáveis independentes (não rejeita H0)")
