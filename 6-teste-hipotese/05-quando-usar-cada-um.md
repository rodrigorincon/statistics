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
- Wilcoxon
- Mann-Whitney
- Kruskal-Wallis
- Dunn

- McNemar
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
- Comparar medianas/dispersão:
	- 2 amostras dependentes (antes/depois): **Wilcoxon**
	- 2 amostras independentes: **Mann-Whitney**
	- 3 ou mais: **Kruskal-Wallis**
- Comparar variâncias: **Levene**
- Comparar vars categórias (ex: antes e depois): **McNemar**
- Relação entre vars categóricas: 
	- Amostras grandes: **Qui-Quadrado** 
	- Amostras pequenas ou não cumpre as premissas: **Fisher**
- Correlação entre vars (independente do tipo): **Correlação**
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
	- Não paramétrico: **Dunn**