from scipy.stats import binomtest

# Parâmetros: k = sucessos, n = total de tentativas, p = probabilidade esperada
k = 14  # número de sucessos observados
n = 20  # tamanho total da amostra
p = 0.6 # probabilidade esperada na hipótese nula

# Executando o teste binomial
resultado = binomtest(k, n, p=p, alternative='greater') # (H1: p > 0.6)

print(f"P-valor: {resultado.pvalue:.4f}")

if resultado.pvalue < 0.05:
    print("Rejeito (H0). A proporção de sucessos é significativamente maior que 0.6.")
else:
  print("Não rejeito H0. Não há evidências suficientes para afirmar que a proporção de sucessos é maior que 0.6.")

print("--------------- Segundo teste ---------------")
k = 17
n = 20
p = 0.6

resultado = binomtest(k, n, p=p, alternative='greater')
print(f"P-valor: {resultado.pvalue:.4f}")

if resultado.pvalue < 0.05:
    print("Rejeito (H0). A proporção de sucessos é significativamente maior que 0.6.")
else:
  print("Não rejeito H0. Não há evidências suficientes para afirmar que a proporção de sucessos é maior que 0.6.")
