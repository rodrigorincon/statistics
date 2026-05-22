import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats

preco = [840000, 822000, 713000, 689000, 685000, 645000, 625000, 620000, 587500, 585000, 583000, 569000, 546000, 540000, 537000, 
516000, 511000, 510000, 495000, 463000, 457000, 451000, 435000, 431700, 414000, 401500, 399000, 380000, 380000, 375900, 372000, 367500,
356500, 330000, 330000, 307500]

m2 = [257, 232, 222, 204, 252, 234, 253, 226, 195, 180, 206, 303, 166, 138, 270, 181, 162, 160, 157, 159, 153, 156, 139, 176, 109, 107, 
128, 124, 118, 211, 93, 118, 132, 126, 136, 78]

df = pd.DataFrame({'preco': preco, 'm2': m2})

######################################################
# Descrevendo os dados. Vemos que a média e mediana são próximas, o que indica uma distribuição relativamente simétrica. 
# O desvio padrão é alto em ambos, indicando que os preços e as áreas variam bastante.
resume = df.describe()
for coluna in df:
  q1 = resume[coluna]['25%']
  q3 = resume[coluna]['75%']
  iqr = q3 - q1
  limite_inferior = q1 - 1.5 * iqr
  limite_superior = q3 + 1.5 * iqr
  num_outliers = len(df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)])
  print(f'-------{coluna} -------') 
  print(f'Média: {round(resume[coluna]['mean'])}, Mediana: {round(resume[coluna]['50%'])}, Desvio Padrão: {round(resume[coluna]['std'])}')
  print(f'Mínimo: {round(resume[coluna]['min'])}, Máximo: {round(resume[coluna]['max'])}, Q1: {round(q1)}, Q3: {round(q3)}')
  print(f'Limite Inferior: {round(limite_inferior)}, Limite Superior: {round(limite_superior)}')
  print(f'Número de Outliers: {num_outliers}')

######################################################
# Visualizando os dados com boxplots para identificar possíveis outliers e tamanho da variação. 
# Ambos mostram uma variação significativa, especialmente no preço, mas sem outliers.
sns.boxplot(y=df['preco'])
plt.title('Boxplot dos Preços')
plt.ylabel('Preço (R$)')
plt.show()

sns.boxplot(y=df['m2'])
plt.title('Boxplot do M²')
plt.ylabel('Área (m²)')
plt.show()

######################################################
# Visualizando a relação entre preço e área com um gráfico de dispersão. 
# Vemos uma tendência positiva, mostrando que imóveis maiores tendem a ser mais caros
# Vemos que parece ter uma relação linear
sns.scatterplot(x=df['m2'], y=df['preco'])
plt.title('Dispersão entre M² e Preço')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.show()

######################################################
# Correlação entre preço e área
# A correlação = 0.78, indicando uma forte relação positiva entre área e preço.
# O coeficiente de determinação = 0.6, indicando que 60% da variação nos preços pode ser explicada pela área
print('-------Correlação -------')
correlacao = df['preco'].corr(df['m2'])
print(f'Correlação entre Preço e M²: {round(correlacao, 2)}')
print(f'Coeficiente de Determinação (R²): {round(correlacao**2, 4)}')

######################################################
# Regressão linear
# P-valor para o coeficiente da área é muito baixo, indicando que a relação é estatisticamente significativa.
X = sm.add_constant(df['m2']) # Adicionar intercepto (A0 da equação y = A0 + A1*x)
# Por algum motivo, o statsmodels não adiciona o intercepto automaticamente, então precisamos fazer isso manualmente.

y = df['preco']
regressao = sm.OLS(y, X).fit() # OLS = Ordinary Least Squares (Mínimos Quadrados Ordinários). 
# Se usar outra fórumula, como RLM (Robust Linear Model), é outro método e retornará outro resultado.

print('-------Regressão Linear -------')
print(regressao.summary())
# Y = 1925.13x + 172,700
# O teste T de ambos os coeficientes tem p-valores muito baixos, indicando que ambos são estatisticamente significativos.
# A0 = 172,700 +- 99300 e A1 = 1925.13 +- 544,3 com 95% de confiança
# tipo de covariancia = nonrobust (não é robusta a heterocedasticidade. Se os resíduos ñ tiverem variância constante, o modelo dá respostas erradas)
# olharei para o AIC e ignorarei BIC, pois estou querendo fazer previsões e preciso de certa flexibilidade. 
# AIC = 923.2 (para comparar com outros modelos, quanto menor melhor)
# p-valor de Jarque-Bera = 0.659, resíduos seguem a normal (Prob(JB))
# Skewness = -0.134, resíduos têm uma leve assimetria, concentrados um tiquinho a mais pra direita, mas ainda próximo da normal
# Kurtosis = 3.696, resíduos próximo da normal (kurtosis = 3)


######################################################
# plot dos resiuduos
residuos = regressao.resid

sns.histplot(residuos, kde=True)
plt.xlabel('Resíduos')
plt.ylabel('Frequência')
plt.title('Histograma dos Resíduos')
plt.show()
# parece mostrar uma leve assimetria a direita, melhor ver pelo grafico de dispersao

sns.scatterplot(x=df['m2'], y=residuos)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Area do Imovel')
plt.ylabel('Resíduos')
plt.title('Relação entre Area e Resíduos')
plt.show()
# resíduos formam um cone, variância dos resíduos aumenta com o aumento da área

sm.qqplot(residuos, line='45', fit=True)
plt.xlabel('Quantiles da Distribuição Amostral dos Resíduos')
plt.ylabel('Quantiles da Distribuição Normal')
plt.title('Gráfico QQ Plot dos Resíduos')
plt.show()
# resíduos não seguem a normal

######################################################
# transformando os dados para tentar corrigir a heterocedasticidade e a não normalidade dos resíduos
print('\n\n-------Regressão Linear com Transformação -------')
X = sm.add_constant(df['m2']) # Adicionar intercepto
y = df['preco']/df['m2']
regressao2 = sm.OLS(y, X).fit()
print(regressao2.summary())
# AIC = 542.3 (menor, então assim fica melhor)
# p-valor de Jarque-Bera = 0.879, resíduos seguem a normal (Prob(JB))
# Skewness = -0.17, valores muito próximos da normal e do valor anterior
# Kurtosis = 2.762, valores muito próximos da normal e do valor anterior

######################################################
# plot dos resiuduos transformados

residuos2 = regressao2.resid
sns.scatterplot(x=df['m2'], y=residuos2)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Area do Imovel')
plt.ylabel('Resíduos')
plt.title('Relação entre Area do Imovel e Resíduos')
plt.show()

sm.qqplot(residuos2, line='45', fit=True)
plt.xlabel('Quantiles da Distribuição Amostral dos Resíduos')
plt.ylabel('Quantiles da Distribuição Normal')
plt.title('Gráfico QQ Plot dos Resíduos')
plt.show()

######################################################
# PREVER O VALOR PARA UM IMÓVEL DE 200 M²
area_nova = 200
X_novo = sm.add_constant([area_nova], has_constant='add') # Adicionar intercepto
previsao = regressao2.predict(X_novo)

preco_previsto = previsao[0] * area_nova # desfaço a transformação, pois o valor prevista era o preço por m² e quero responder o preço total do imóvel

print(f'\n\n-------Previsão para Imóvel de {area_nova} m² -------')
print(f'Preço previsto: R$ {round(preco_previsto, 2)}')