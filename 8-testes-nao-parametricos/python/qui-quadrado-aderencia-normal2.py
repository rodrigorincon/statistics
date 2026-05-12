import numpy as np
import scipy.stats as stats
import sys

def calc_rejeitos(observados, esperados):
  print("\n---------- Calculando Rejeitos Padronizados...")
  total = np.sum( np.array(observados) )
  residuos = []
  for i in range(len(observados)):
    residuo = (observados[i] - esperados[i])/np.sqrt(esperados[i])
    residuos.append(residuo)
  print("Rejeitos Padronizados:", residuos)
  print("------------ Quais que estão fortemente associados (outliers, acima de 1,96)")
  for i in range(len(observados)):
    if abs(residuos[i]) > 1.96:
      print(f"Posição {i}, esperado {esperados[i]}, observado {observados[i]}")


def calc_prob_intervalo(min, max, media, desvio_padrao):
  prob_values = stats.norm.cdf([min, max], media, desvio_padrao) # calcula P(x < min) e P(x < max)
  return prob_values[1] - prob_values[0] # prob da faixa = P(x < max) - P(x < min)

# TESTE: Checar se a distribuição de notas do ENEM segue uma distribuição normal
# exemplo com dados não normais
# Compara com a distribuição normal
media = 500
desvio_padrao = 100
tamanho_amostra = 600

notas = np.round(np.random.uniform(low=0, high=1000, size=tamanho_amostra))

# Passo 1: definir intervalos (faixas de valores)
# Passo 2: valores observados = contagem de valores em cada faixa
#   Ao fazer isso tornamos os dados categóricos
# Passo 3: calcular a probabilidade de cada faixa (usando a distribuição que queremos comparar)
# Passo 4: valores esperados = prob da faixa * tamanho amostra (prob de encontrar um valor naquela faixa * num tentativas)
# Passo 5: checa as premissas (todos os grupos esperados devem ser 5 ou mais)

# 1: Definir intervalos (divide as observações em k grupos) 
grupo_menos300 = [nota for nota in notas if nota < 300]
grupo_entre_300_500 = [nota for nota in notas if nota >= 300 and nota < 500]
grupo_entre_500_700 = [nota for nota in notas if nota >= 500 and nota < 700]
grupo_mais700 = [nota for nota in notas if nota >= 700]

# O nº de grupos define seus graus de liberdade
num_grupos = 4
num_params_normal = 2
graus_liberdade = num_grupos - 1 - num_params_normal # 2

# 2: calcular valores observados em cada categoria (intervalo)
valores_observados = [ len(grupo_menos300), len(grupo_entre_300_500), len(grupo_entre_500_700), len(grupo_mais700)]

# 3: Probabilidade de cada intervalo
prob_menos300 = calc_prob_intervalo(0, 300, media, desvio_padrao)
prob_entre_300_500 = calc_prob_intervalo(300, 500, media, desvio_padrao)
prob_entre_500_700 = calc_prob_intervalo(500, 700, media, desvio_padrao)
prob_mais700 = calc_prob_intervalo(700, 1000, media, desvio_padrao)

# 4: valores esperados
esperado_menos300 = round(prob_menos300 * tamanho_amostra)
esperado_entre_300_500 = round(prob_entre_300_500 * tamanho_amostra)
esperado_entre_500_700 = round(prob_entre_500_700 * tamanho_amostra)
esperado_mais700 = round(prob_mais700 * tamanho_amostra)

valores_esperados = [esperado_menos300, esperado_entre_300_500, esperado_entre_500_700, esperado_mais700]

# Imprimindo O e E
print(f"De 0 até 300: nº observado {valores_observados[0]}, nº esperado: {valores_esperados[0]}")
print(f"De 300 até 500: nº observado {valores_observados[1]}, nº esperado: {valores_esperados[1]}")
print(f"De 500 até 700: nº observado {valores_observados[2]}, nº esperado: {valores_esperados[2]}")
print(f"Acima de 700: nº observado {valores_observados[3]}, nº esperado: {valores_esperados[3]}")
print("--------")
print(f"Total observados: {sum(valores_observados)} Total esperados: {sum(valores_esperados)}")

# 5: checa se tem algum grupo com menos que 5
if(np.any(np.array(valores_esperados) < 5)):
  print("------- Algum valor é menor que 5, não pode executar o teste")
  sys.exit()

chi2, p_valor = stats.chisquare(f_obs=valores_observados, f_exp=valores_esperados, ddof=graus_liberdade)

print(f"Valor do X²: {chi2}")
print(f"Graus de Liberdade: ", graus_liberdade)
print(f"p-valor: {p_valor}")

# Interpretação
if p_valor < 0.05:
  print("Não segue a distribuição esperada (rejeita H0)")
  calc_rejeitos(valores_observados, valores_esperados)
else:
  print("Segue a distribuição esperada (não rejeita H0)")
 