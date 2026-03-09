import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import shapiro

# a call center receipt these calls per day. I wan to check after a chatbot solution, if the calls is less than 20.
# Ho: media >= 20 (what is tested by the method)
# Ha: media < 20
ligacoes = [10,11,11,12,12,12,13,13,13,14,14,14,15,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
media_to_compare = 20
alfa = 0.05

# step 1, check if the sample is normal
shapiro_stat, shapiro_p_valor = shapiro(ligacoes)
if shapiro_p_valor < alfa:
	print("A amostra NÃO é normal, tentarei usar convertendo os dados para base logaritima")
	
	# step 1.1, try to save test T converting the data to log base
	ln_ligacoes = np.log(ligacoes) # this is ln, not log in 10 base
	shapiro_stat, shapiro_p_valor = shapiro(ln_ligacoes)
	if shapiro_p_valor < alfa:
		print("Mesmo convertendo pra base log a amostra segue NÃO normal, não posso usar teste T")
		sys.exit([0])
	else:
		print("Funcionou, seguir com o teste na base log")
		# convert all data to log base
		ligacoes = ln_ligacoes
		# as we're using log data, the compared value need to be in the same range
		# the values are not 17, 19..., are 2, 3... Compare then with 20 will fail, but log(20) = 3, that is in the same magnitude
		media_to_compare = np.log(media_to_compare)


# step 2, do the test
t_stat, p_valor = ttest_1samp(ligacoes, media_to_compare) # test Ho, P(T < t). By default, alternative='two-sided'

print(f'Valor na tabela t e valor no eixo x: {t_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')

if p_valor < alfa:
	print("a media é < 20, o chatbot serviu para diminuir o numero de chamadas")
else:
	print("a media é >= 20, o chatbot NÃO serviu para diminuir o numero de chamadas")