from scipy.stats import spearmanr

precos = [265, 225, 160, 325, 430, 515, 180, 423]
dias = [136, 125, 120, 140, 145, 150, 122, 145]

# calculating manually the ranks

rank_prices = [4, 3, 1, 5, 7, 8, 2, 6]
rank_dias = [4, 3, 1, 5, 6.5, 7, 2, 6.5]
n = len(precos)

total_differences = sum([ (rank_prices[i] - rank_dias[i])**2 for i in range(n)])
spearman = 1 - 6*total_differences/(n*(n**2 - 1))
print(f"Valor da correlação de Spearman: {spearman:.4f}")

## calculating using scipy

corr, p_value = spearmanr(precos, dias)
print("-------------")
print(f"Valor da correlação de Spearman: {corr:.4f}")
print(f"P-valor de Spearman: {p_value}")

# checking if changing the order the result is the same
corr, p_value = spearmanr(dias, precos)
print("-------------")
print(f"Valor da correlação de Spearman: {corr:.4f}")
print(f"P-valor de Spearman: {p_value}")