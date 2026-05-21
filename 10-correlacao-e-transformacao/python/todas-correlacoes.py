import scipy.stats as stats

precos = [265, 225, 160, 325, 430, 515, 180, 423]
dias = [136, 125, 120, 140, 145, 150, 122, 145]

corr, p_value = stats.pearsonr(precos, dias)
print("-------------")
print(f"Valor da correlação de Pearson: {corr:.4f}")
print(f"P-valor de Pearson: {p_value}")

corr, p_value = stats.spearmanr(precos, dias)
print("-------------")
print(f"Valor da correlação de Spearman: {corr:.4f}")
print(f"P-valor de Spearman: {p_value}")

corr, p_value = stats.kendalltau(precos, dias)
print("----------")
print(f"Correlação de Kendall: {corr:.4f}")
print(f"P-value: {p_value:.4f}")

### CADA MÉTODO RETORNA UM VALOR DIFERENTE, MOSTRANDO QUE DEVE SABER ESCOLHER O METODO CERTO
### APESAR DE TODOS TEREM DADOS VALORES PRÓXIMOS E P-VALORES QUE REJEITAM H0