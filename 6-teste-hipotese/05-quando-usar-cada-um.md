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
- Teste do Sinal
- Friedman
- McNemar
- Binomial
- Poisson
- exponencial

# QUANDO USAR

1. Comparar valores:

- Média:
	- até 2: **Teste T**
	- 3 ou mais: **Anova**
- Proporção:
	- 1 com valor determinado e se for categórica binária: **Binomial**
	- até 2: **Teste Z**
	- 3 ou mais: **Qui-Quadrado**
	- 2 dependentes (antes/depois): **McNemar**
- Mediana/dispersão:
	- 2 dependentes (antes/depois): **Wilcoxon**
	- 2 independentes: **Mann-Whitney**
	- 3 ou mais dependentes (mesma coisa agiu em todas as categorias): **Friedman**
	- 3 ou mais independentes: **Kruskal-Wallis**
- Variâncias: **Levene**
- Vars Ordinais: 
	- Dependentes (antes/depois): **Teste do sinal** 

2. Relação entre grupos:

- Se uma afeta o valor da outra: **Correlação**
- Se são independentes: 
	- Amostras grandes: **Qui-Quadrado** 
	- Amostras pequenas ou não cumpre as premissas: **Fisher**

3. Checar se uma amostra segue uma distribuição

- Distribuição normal
	- Amostra pequena: **Shapiro-Wilk**
	- Amostras grandes: **Kolmogorov-Smirnov**
	- Dados categóricos: 
		- Amostras grandes: **Qui-Quadrado** 
		- Amostras pequenas ou não cumpre as premissas: **Fisher**
- Outra distribuição: 
	- Dados numéricos: **Kolmogorov-Smirnov** 
	- Dados categóricos:
		- Amostras grandes: **Qui-Quadrado** 
		- Amostras pequenas ou não cumpre as premissas: **Fisher**

4. Encontrar amostra que se difere das outras

- Poucos grupos: **Bonferroni**
- Muitos grupos: **HSD de Tukey**
- Grupos não tem variâncias homogêneas: **Games-Howell**
- Não paramétrico: **Dunn**

5. Acontecimentos por tempo

- Frequência no período tá dentro do esperado: **Poisson**
- Tempo entre os acontecimentos tá dentro do esperado: **Exponencial**