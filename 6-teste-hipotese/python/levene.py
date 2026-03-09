import numpy as np
from scipy.stats import levene

# checa se as variancias são próximas o suficiente para serem consideradas iguais
def check_levene(data1, data2):
	# checando se as variancias sao proximas o suficiente
	stat, p_valor = levene(data1, data2)

	print(f'Estatística do teste de proximidade da variancia: {stat:.4f}')
	print(f'p-valor do teste de proximidade da variancia: {p_valor:.4f}')
	if p_valor < 0.05:
		print("as variancias são proximas o suficiente")
	else:
		print("as variancias NÃO são proximas o suficiente")


# Ex 1: variancias muito distantes
sample1 = [1,2,2,5,5,5,7,8,9,11] # vari = 3.11
sample2 = [1,2,4,5,5,6,7,7,9,10] # vari = 2.69
print("Amostra 1: media", np.mean(sample1), "variancia ", round(np.var(sample1),2))
print("Amostra 2: media", np.mean(sample2), "variancia ", round(np.var(sample2),2))

check_levene(sample1, sample2)

print("----------------------")

# Ex 2: variancias proximas o suficiente
sample1 = [8.88, 9.12, 9.00, 9.08, 9.01, 8.85, 9.06, 8.99] # vari = 0.01
sample2 = [8.88, 8.95, 9.15, 9.58, 8.36, 9.18, 8.67] # vari = 0.13
print("Amostra 1: media", round(np.mean(sample1),4), "variancia ", round(np.var(sample1),2))
print("Amostra 2: media", round(np.mean(sample2),4), "variancia ", round(np.var(sample2),2))

check_levene(sample1, sample2)
