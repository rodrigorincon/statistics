# Sobre o Centro

- Diz qual valor médio da amostra/população
- Distribuição diz como os demais valores se concentram/espalham ao redor desse centro.
- É a primeira informação que buscaremos sobre uma amostra/população

Para escolher o centro: 
- É preciso olhar seus dados pra ver qual reflete melhor
- É uma boa ideia medir os 3 (média, mediana e esperança) e suas dispersões (variância e desvio padrão) e comparar com o gráfico pra ver o que faz sentido
- Também é preciso conhecer **muito bem o contexto** dos dados pra encontrar vieses ou algo que possa causar distorções 
	- Ex: comparar a nota de 2 restaurantes, um com poucas avaliações e outro com muitas
- Existem testes de hipótese que ajudam a verificar qual das distribuições melhor encaixa nos dados, o que ajuda a escolher a média tbm
- Percebe-se que definir a melhor média é feito depois de tirar mil dados e análises, mesmo que ela também seja a 1ª coisa a se medir

**Escolher o centro errado é uma forma fácil de mentir com dados.**

# TIPOS DE CENTRO

1: MÉDIA
- Existem vários tipos (aritimética, geométrica, harmônica...) cada uma útil pra um contexto específico
- Quase sempre usado a aritimética
- Cada média é descrita na sessão médias

2: MEDIANA
- Ordena os valores e pega o do meio (caso tenham valores pares, tira a média dos 2 valores do meio)
- Metade dos valores estão acima dele e metade estão abaixo
- Não é sensível a outlier
- Usar quandos os dados forem **assimétricos** ou tiver **muitos outliers**

3: ESPERANÇA
- Valor esperado caso um experimento seja repetido infinitas vezes
- **`esperança = valor esperado = média`**
- **É sensível a outliers**

Média ponderada de todos possíveis resultados vezes sua respectiva probabilidade

$$E(x) = \sum_{x=1}^n x_i p(x_i) $$

Se for uma distribuição contínua
$$E(x) =\int_{-\infty}^{\infty} xf(x) \,dx$$

	Onde f(x) é a equação da distribuição

- Ela não precisa ser um dos valores existentes nos dados ou parte dos conjuntos dos valores possíveis (como no exemplo abaixo)
- Nas distribuições se ela tiver uma média predefinida esse será sua esperança

Ex1: esperança de um dado
	
$1*\frac{1}{6} + 2*\frac{1}{6} + 3*\frac{1}{6} + 4*\frac{1}{6} + 5*\frac{1}{6} + 6*\frac{1}{6} = 3,5$

Propriedades:
```
E(c) = c
E(X + c) = E(X) + c
E(aX) = a * E(X)
E(X + Y) = E(X) + E(Y)
E(XY) = E(X) * E(Y) se X e Y forem INDEPENDENTES
```

4: MODA
- Valor que mais se repete na população/amostra
- Pode ter várias modas (caso 2 ou mais valores estejam empatados em 1º)
- **NÃO substitui** as demais
