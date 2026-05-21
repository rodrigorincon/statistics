from scipy.stats import kendalltau

# Exemplo 1, com correlação negativa
x = [41, 39, 19, 36, 36]
y = [8, 5, 10, 6, 8]

# Calcula correlacao de  Kendall
corr, p_value = kendalltau(x, y)

print(f"Correlação de Kendall: {corr:.4f}")
print(f"P-value: {p_value:.4f}")

# Exemplo 2, com correlação positiva
x = [7.1, 7.1, 7.2, 8.3, 9.4, 10.5, 11.4]
y = [2.8, 2.9, 2.8, 2.6, 3.5, 4.6, 5.0]

corr, p_value = kendalltau(x, y)

print("----------")
print(f"Correlação de Kendall: {corr:.4f}")
print(f"P-value: {p_value:.4f}")