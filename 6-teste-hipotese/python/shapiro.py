from scipy.stats import shapiro

def check_shapiro(data, alfa):
	# Ho: normal (p_value >= 0.05)
	# Ha: not normal (p_value < 0.05)
	stat, p_valor = shapiro(data)

	print(f'Estatística do teste: {stat:.4f}')
	print(f'p-valor: {p_valor:.4f}')

	if p_valor < alfa:
		print("A amostra NÃO é normal")
	else:
		print("A amostra é normal")


# test if the sample is normal
sample1 = [15,21,19,17,23,16,18,17,23,18,16,14,10,18,21,15,21,19,17,15,22,16,14,18,15,20,18,21,17,20]
alfa = 0.05
check_shapiro(sample1, alfa)

print("---------------")
sample2 = [10,11,11,12,12,12,13,13,13,14,14,14,15,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
check_shapiro(sample2, alfa)