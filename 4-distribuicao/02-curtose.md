# CONCEITO: MOMENTO ESTATÍSTICO

- Números que descrevem aspectos da distribuição

1º momento: média 
$\frac{\sum_{i=1}^n{x_i}}{n} = \frac{\sum_{i=1}^n{(x_i-0)^1}}{n}$

2º momento: variância 
$\frac{\sum_{i=1}^n{(x_i-media)^2}}{n}$

3º momento: referente a assimetria (mas não exatamente ela)
$\frac{\sum_{i=1}^n{(x_i-media)^3}}{n}$

4º momento: referente a curtose (mas não exatamente ela) 
$\frac{\sum_{i=1}^n{(x_i-media)^4}}{n}$

- Elevar os desvios a 4 garante que todos sejam par, assim um menor que a média não vai anular um maior, todos vão se somar pra calcular quão longe da média estão
- Elevar os desvios a 4 faz com que outliers crescam exponencialmente. Enquanto nºs proximos da média vão crescer muito pouco, outliers vão explodir ao elevar a 4
- Isso faz com que se tiver outliers, o 4º momento será imenso

# CÁLCULO DA ASSIMETRIA

- Nível de assimetria também é chamado de skewness
- Nos diz o quão simétrico é uma distribuição e para que lado ele é assimétrico
	- Simétrico = 0
	- Assimetria a direita > 0 (valores concentrados a esquerda)
		- Média > Moda
	- Assimetria a esquerda < 0 (valores concentrados a direita)
		- Média < Moda
- Quanto maior o valor, mais assimétrico é

$$skewness = \frac{3ºMomento}{desvio^3} = \frac{ \frac{\sum_{i=1}^n{(x_i-media)^3}}{n} }{desvio^3}$$

# CONCEITO: CURTOSE

- Grau de achatamento da distribuição/gráfico
- Ou seja, quão concentrados ao redor da média estão os dados
- Em outras palavras, mede quão pesadas são as caudas
- Caudas pesadas/altas, mais outliers (valores longe da média)

$$curtose = \frac{4ºMomento}{desvio^4} = \frac{ \frac{\sum_{i=1}^n{(x_i-media)^4}}{n} }{desvio^4}$$

curtose < 0  mais espaçado (mais espalhado) 

curtose = 0  curva normal

curtose > 0  mais pontudo (mais concentrado) e presença de outliers
![](images/curtose.png)

- Quanto maior a curtose, mais rápido os valores caem e mais os valores tão próximos da média
- Existem outros métodos de calcular (Pearson, aonde a normal é = 3)

---

- Quanto menor, mais achatado no eixo y e mais esparço (desvio padrão alto)
	- Pelo desvio ser alto, os valores são mais esparços e mais difícil de um valor ser considerado outlier
- Quanto maior, mais fino, mais outliers e mais concentrado perto da média (desvio padrão baixo)
	- Quanto maior o desvio padrão, menor a curtose 

**Serve para ver se os dados são muito agrupados/concentrados e se tem outliers (mas não identifica quais ou quantos)**

**É uma boa análise preliminar**
