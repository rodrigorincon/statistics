import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from scipy.stats import levene
from scipy.stats import shapiro

# teste T para vars independente com variância próxima
print("VARS INDEPENDENTE COM VARIANCIA PROXIMA")
sample1 = [8.88, 9.12, 9.00, 9.08, 9.01, 8.85, 9.06, 8.99]
sample2 = [8.88, 8.95, 9.15, 9.58, 8.36, 9.18, 8.67]

# checando se as amostras são normais para poder aplicar teste T
_, p_valor1 = shapiro(sample1)
_, p_valor2 = shapiro(sample2)
if p_valor1 >= 0.05 and p_valor2 >= 0.05:
	print("amostras normais")
else:
	print("alguma amostra NÃO segue a normal, NÃO PODE APLICAR TESTE T")
	sys.exit([0])

# checando se as variancias sao proximas o suficiente
_, p_valor = levene(sample1, sample2)
if p_valor < 0.05:
	print("as variancias são proximas o suficiente")
else:
	print("as variancias NÃO são proximas o suficiente")

# executando o teste
t_stat, p_valor  = ttest_ind(sample1, sample2) # por default a variancia é próxima. P(T < t)
print(f'Estatística t: {t_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')


print("--------------------------------")
# teste T para vars independente com variância distante
print("VARS INDEPENDENTE COM VARIANCIA DISTANTE")
sample1 = [6,15,19,26,2,16,31,14,15,16]
sample2 = [-3,15,28,18,32,31,15,12,10,15]

# checando se as amostras são normais para poder aplicar teste T
_, p_valor1 = shapiro(sample1)
_, p_valor2 = shapiro(sample2)
if p_valor1 >= 0.05 and p_valor2 >= 0.05:
	print("amostras normais")
else:
	print("alguma amostra NÃO segue a normal, NÃO PODE APLICAR TESTE T")
	sys.exit([0])

# checando se as variancias sao proximas o suficiente
_, p_valor = levene(sample1, sample2)
if p_valor < 0.05:
	print("as variancias são proximas o suficiente")
else:
	print("as variancias NÃO são proximas o suficiente")

# executando o teste
t_stat, p_valor  = ttest_ind(sample1, sample2, equal_var=False) # P(T < t)
print(f'Estatística t: {t_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')


print("--------------------------------")
# teste T para vars dependentes
print("VARS DEPENDENTES")
antes = [395,404,401,405,396,410,410,406,398,400,392,395,399,395,386,399,394,390,399,393,392,407,405,395,396,402,405,410,415,392,415,404,395,392,402,404,411,395,401,406]
depois = [378,392,395,398,387,402,387,395,391,377,386,397,393,401,387,387,394,384,390,407,388,394,394,386,386,384,404,391,392,388,392,387,395,390,396,391,393,383,397,400]

# checando se as amostras são normais para poder aplicar teste T
_, p_valor1 = shapiro(antes)
_, p_valor2 = shapiro(depois)
if p_valor1 >= 0.05 and p_valor2 >= 0.05:
	print("amostras normais")
else:
	print("alguma amostra NÃO segue a normal, NÃO PODE APLICAR TESTE T")
	sys.exit([0])

# executando o teste
t_stat, p_valor = ttest_rel(antes, depois) # P(T < t)
print(f'Estatística t: {t_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')
