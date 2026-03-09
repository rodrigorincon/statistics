# TESTES DE HIPÓTESES

Existem vários, mas aqui listarei os mais comuns:

- Teste T
- Teste Z
- Teste F / Levene (prefira usar o de Levene)
- Anova
- Qui-Quadrado
- Pearson
- Correlação
- Análise de Regressão
- Wilcoxon
- Spearman
- Binomial
- Poisson
- Fisher
- McNemar
- Shapiro-Wilk / Kolmogorov-Smirnov

# QUANDO USAR

- Comparar média: 
	- até 2: **Teste T**
	- 3 ou mais: **Anova**
- Comparar proporção:
	- até 2: **Teste Z**
	- 3 ou mais: **Qui-Quadrado**
- Comparar variâncias: **Levene**
- Comparar vars categórias (ex: antes e depois): **McNemar**
- Relação entre vars categóricas: **Qui-Quadrado**
- Relação entre vars numéricas: **Correlação ou Análise de Regressão**
- Checar se uma amostra tem distribuição normal
	- Amostra pequena: **Shapiro-Wilk**
	- Amostras grandes: **Kolmogorov-Smirnov**
- Checar se uma amostra tem alguma distribuição diferente da normal: **Kolmogorov-Smirnov**