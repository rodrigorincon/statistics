# TESTES DE HIPÓTESES

Existem vários, mas aqui listarei os mais comuns:

- Teste T
- Teste Z
- Teste F / Levene (prefira usar o de Levene)
- Anova
- Qui-Quadrado / Fisher
- Shapiro-Wilk / Kolmogorov-Smirnov
- HSD de Tukey / Games-Howell / Bonferroni
- Correlação (Pearson, Spearman, Kendall, Bisserial)

- Análise de Regressão

- Wilcoxon
- McNemar
- Mann-Whitney
- Kruskal-Wallis
- Teste do Sinal

- Binomial
- Poisson

# QUANDO USAR

- Comparar média: 
	- até 2: **Teste T**
	- 3 ou mais: **Anova**
- Comparar proporção:
	- até 2: **Teste Z**
	- 3 ou mais: **Qui-Quadrado**
- Comparar variâncias: **Levene**
- Comparar vars categórias (ex: antes e depois): **McNemar**
- Relação entre vars categóricas: 
	- Amostras grandes: **Qui-Quadrado** 
	- Amostras pequenas ou não cumpre as premissas: **Fisher**
- Relação entre vars numéricas: **Correlação ou Análise de Regressão**
- Checar se uma amostra tem distribuição normal
	- Amostra pequena: **Shapiro-Wilk**
	- Amostras grandes: **Kolmogorov-Smirnov**
	- Dados categóricos: 
		- Amostras grandes: **Qui-Quadrado** 
		- Amostras pequenas ou não cumpre as premissas: **Fisher**
- Checar se uma amostra tem alguma distribuição diferente da normal: 
	- Dados numéricos: **Kolmogorov-Smirnov** 
	- Dados categóricos:
		- Amostras grandes: **Qui-Quadrado** 
		- Amostras pequenas ou não cumpre as premissas: **Fisher**
- Encontrar amostra que se difere das outras
	- Poucos grupos: **Bonferroni**
	- Muitos grupos: **HSD de Tukey**
	- Grupos não tem variâncias homogêneas: **Games-Howell**