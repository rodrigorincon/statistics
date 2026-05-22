import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

qtt_vendas = [61781, 65435, 71924, 83322, 63124, 70469, 68196, 60715, 59867, 57472, 56062, 54450, 54177, 51120, 53068, 54876, 64129, 
74369, 71731, 69471, 66879, 55948, 57962, 66263, 67922, 59662, 63050, 72730, 64574, 64149, 59183, 51964, 52616, 54014, 60574, 64058, 
64509, 60551, 53407, 50121, 48961, 50610, 50290, 48318, 43978, 51794, 51585, 47968, 50424, 48856, 52859, 46774, 50128, 60984, 55817, 
62798, 60838, 58590, 50782, 51596, 55281, 56620, 46169, 53472, 46947, 43809, 43332, 41703, 39762, 35416, 29987, 26582, 38516, 47191, 
50068, 49858, 46547, 35539, 34370, 35788, 33091, 32266, 34301, 37605, 33064, 35484, 37246, 31493, 35509, 43702, 44604, 40973, 41946, 
43015, 39814, 47725, 33835, 39021, 30233, 28855, 151498, 116579, 75886, 61498]

preco = [1.000, 0.976, 0.944, 0.927, 0.988, 0.969, 0.984, 1.012, 1.018, 1.036, 1.043, 1.059, 1.072, 1.073, 1.045, 1.046, 0.991, 0.955, 
0.953, 0.958, 0.983, 1.029, 1.034, 0.991, 1.039, 1.031, 0.981, 0.967, 0.970, 0.985, 1.025, 1.051, 1.065, 1.060, 1.023, 0.989, 0.988, 
1.002, 1.062, 1.064, 1.101, 1.109, 1.113, 1.111, 1.106, 1.105, 1.109, 1.106, 1.102, 1.102, 1.088, 1.141, 1.096, 1.024, 1.027, 1.011, 
1.023, 1.052, 1.072, 1.053, 1.057, 1.034, 1.088, 1.118, 1.114, 1.140, 1.178, 1.212, 1.223, 1.293, 1.313, 1.320, 1.222, 1.118, 1.114, 
1.102, 1.107, 1.253, 1.262, 1.265, 1.260, 1.268, 1.278, 1.274, 1.287, 1.324, 1.336, 1.320, 1.258, 1.144, 1.162, 1.180, 1.160, 1.207, 
1.210, 1.222, 1.264, 1.309, 1.329, 1.317, 0.696, 0.799, 0.915, 1.009]

#### REGPLOT FAZ O GRAFICO DE DISPERSÃO JÁ COM A REGRESSÃO LINEAR E INTERVALO DE CONFIANÇA. ÓTIMO QUANDO SÓ QUER VISUALIZAR
# sns.regplot(x=preco, y=qtt_vendas, line_kws={'color':'red'})
# plt.xlabel('Preço Médio')
# plt.ylabel('Volume de Vendas')
# plt.title('Relação entre Volume de Vendas e Preço Médio')
# plt.show() # maioria dos dados fora da reta e do intervalo de confiança. Visivelmente os dados não são lineares


### Regressão linear nos dados não-lineares para pegar os resíduos
x = sm.add_constant(preco) # Adicionar intercepto
y = qtt_vendas
regressao = sm.OLS(y, x).fit()
residuos = regressao.resid

### Regressão Linear com log-log
x_log = sm.add_constant(np.log(preco)) #Adicionar intercepto
y_log = np.log(qtt_vendas)
regressao_log = sm.OLS(y_log, x_log).fit()
residuos_log = regressao_log.resid

# Histograma para verificar a distribuição dos dados
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 8))
axs[0][0].hist(qtt_vendas, bins=20, alpha=0.7)
axs[0][0].set(title="Vendas Original", xlabel="Vendas", ylabel="Frequência")
axs[0][1].hist(preco, bins=20, alpha=0.7)
axs[0][1].set(title="Preço Original", xlabel="Preço Médio", ylabel="Frequência")
axs[1][0].hist(y_log, bins=20, alpha=0.7)
axs[1][0].set(title="Vendas Log-Log", xlabel="Vendas", ylabel="Frequência")
axs[1][1].hist(np.log(preco), bins=20, alpha=0.7)
axs[1][1].set(title="Preço Log-Log", xlabel="Preço médio", ylabel="Frequência")
plt.tight_layout()
plt.show() 
# ANALISE DO ORIGINAL
# até 70k vendas por semana é comum, acima disso foram raras as vezes. 
# A maior parte do tempo o preço esteve entre 0.95 e 1.15
# também foi visto que ambas as variáveis possuem uma distribuição assimétrica com cauda à direita,
# oq pode indicar a necessidade de transformação para melhorar a linearidade e homocedasticidade dos resíduos na regressão linear.
# também parece ter outliers com valores muito acima nas vendas e 1 isolado no preço pra baixo
# ANALISE LOG-LOG
# Vendas deu uma distribuída melhor, mas talvez ainda tenha outliers para cima
# Preço não houve muitas mudanças

# Boxplot para verificar a distribuição dos dados
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 8))
axs[0][0].boxplot(qtt_vendas)
axs[0][0].set(title='Vendas Original')
axs[0][1].boxplot(preco)
axs[0][1].set(title='Preço Original')
axs[1][0].boxplot(y_log)
axs[1][0].set(title='Vendas Log-Log')
axs[1][1].boxplot(np.log(preco))
axs[1][1].set(title='Preço Log-Log')
plt.tight_layout()
plt.show() 
# ANALISE DO ORIGINAL
# Boxplot de vendas parece até normal, oq o histograma mostrou que não é. Os outliers vistos nos histogramas aqui são confirmados
# ANALISE LOG-LOG
# A dispersão nas vendas aumentou (conforme visto no histograma), porém no preço diminuiu e gerou um novo outlier

# Scatterplot para verificar a relação entre as variáveis
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))
axs[0].scatter(x=preco, y=qtt_vendas)
axs[0].set(title='Valores Originais', xlabel='Preço Médio', ylabel='Volume de Vendas')
axs[1].scatter(x=np.log(preco), y=y_log)
axs[1].set(title='Valores Log-Log', xlabel='Preço Médio', ylabel='Volume de Vendas')
plt.show() 
# ANALISE DO ORIGINAL
# pontos parecem formar uma curva que vai diminuindo 
# ANALISE LOG-LOG
# pontos parecem mais retos, embora ainda não seja perfeito, já está bem melhor que o anterior

## validação dos residuos do original: checando homocedasticidade do original e transformado
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))
axs[0].scatter(x=preco, y=residuos)
axs[0].set(title='Resíduos Originais', xlabel='Preço Médio', ylabel='Resíduos', )
axs[0].axhline(y=0, color='red', linestyle='--')
axs[1].scatter(x=np.log(preco), y=residuos_log)
axs[1].set(title='Resíduos Log-Log', xlabel='Preço Médio', ylabel='Resíduos')
axs[1].axhline(y=0, color='red', linestyle='--')
plt.show() 
# ANALISE DO ORIGINAL
# resíduos nada homogeneos, residuos formando um U, premissa negada. Tem de fazer transformacao
# ANALISE LOG-LOG
# dados bem mais homogeneos, embora ainda não perfeito. Talvez um cone se formando a partir do ponto -0.1

## Calculando novo valor
novo_valor = 1.02
novo_valor_log = np.log(novo_valor)

novo_X = sm.add_constant([novo_valor_log], has_constant='add')
novo_Y_log = regressao_log.predict(novo_X)[0]
novo_y = np.exp(novo_Y_log)

print(f"Previsão para um preço médio de {novo_valor}:")
print(f"Volume previsto: {novo_y:.2f}")
#