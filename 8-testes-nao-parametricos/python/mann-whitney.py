from scipy.stats import mannwhitneyu


financas = [46, 47, 50, 52, 52, 52, 54, 55, 61, 62]
computacao = [58, 59, 60, 64, 65, 66, 67, 68, 69, 70]

stat, p_valor = mannwhitneyu(financas, computacao) #2 amostras independentes
print(f"U: {stat}")
print(f"p-valor: {p_valor:.4f}")