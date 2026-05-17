import numpy as np
import statsmodels.api as sm

### Exemplo de teste de sinal (binomial) para comparar dois conjuntos de dados relacionados

print("-------- EXEMPLO 1: REMEDIOS PARA DOR --------")
antigos = np.array([4, 3, 5, 2, 1, 2, 1, 3, 6, 8])
novos = np.array([3, 3, 3, 1, 1, 3, 2, 2, 2, 5])

diferenca = novos - antigos
positivos = np.sum(diferenca > 0) # diferenca > 0 cria um array booleano, e np.sum conta quantos são True
n = np.sum(diferenca != 0) # conta quantos elementos da diferença são diferentes de zero

# teste de sinal (binomial)
p_valor = sm.stats.binom_test(positivos, n, alternative='two-sided')
print(f"Número de diferenças positivas: {positivos}")
print(f"P-Valor: {p_valor:.4f}")

print("-------- EXEMPLO 2: SABORES DE PIZZA --------")
antigos = np.array([3, 3, 2, 4, 2, 1, 3, 1, 2, 4, 3, 4, 1, 3, 5, 3, 1, 4, 3, 2])
novos = np.array([4, 2, 5, 4, 5, 3, 2, 2, 4, 5, 4, 5, 2, 3, 3, 4, 5, 2, 4, 5])

diferenca = antigos - novos
positivos = np.sum(diferenca > 0) # diferenca > 0 cria um array booleano, e np.sum conta quantos são True
n = np.sum(diferenca != 0) # conta quantos elementos da diferença são diferentes de zero

# teste de sinal (binomial)
p_valor = sm.stats.binom_test(positivos, n, alternative='smaller')
print(f"Número de diferenças positivas: {positivos}")
print(f"P-Valor: {p_valor:.4f}")