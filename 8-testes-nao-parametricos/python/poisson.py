import scipy.stats as stats

# Taxa média de eventos (lambda)
rate = 3 

# Probabilidade de ocorrerem exatamente k = 5 eventos
k = 5
p_valor = 1 - stats.poisson.cdf(k, rate)
print(f"Probabilidade de exatos {k} eventos: {p_valor:.3f}")


# Probabilidade de ocorrerem exatamente k = 7 eventos
k = 7
p_valor = 1 - stats.poisson.cdf(k, rate)
print(f"Probabilidade de exatos {k} eventos: {p_valor:.3f}")

# Encontrar para qual k temos p-valor de 0.05
k_crtico = stats.poisson.ppf(1-0.05, rate)
print(f"Valor crítico para p-valor de 0.05: {k_crtico}")