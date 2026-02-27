# TIPOS DE MÉDIAS

## MÉDIA ARITIMETICA

- Soma de todos os valores dividido pela quantidade
- Sempre será menor que o maior valor (xi)

$$media = \frac{\sum_{i=1}^n x_i}{N}$$

## MÉDIA PONDERADA

- Soma dos valores vezes seu respectivo peso dividido pela soma dos pesos
- Sempre será menor que o maior valor (maior x)

$$media = \frac{\sum_{i=1}^n x_i * p_i}{\sum_{i=1}^n p_i}$$

Em outras palavras...

$$\frac{x1*p1 + x2*p2 + x3*p3 ...}{p1+p2+p3...}$$

## MÉDIA GEOMÉTRICA

- Raiz enésima da multiplicação de todos os valores
- **Possui um cálculo de variância exclusivo**

$$media = \sqrt[N]{\prod_{i=1}^N{x_i}}$$

Em outras palavras...

$$\sqrt[N]{x1 * x2 * x3...}$$

- **Não é sensível a outliers** (a ÚNICA)
- Usar quandos os nºs parecem saltar exponencialmente
- Bom pra calcular taxas de crescimento, juros compostos ou encontrar tendências quando há aumentos sucessivos seguindo padrão geométrico (ex: pandemia)
- **Não** pode ser usada para valores 0 ou negativo

## MÉDIA HARMÔNICA

- O total sobre a soma dos inversos
- **É sensível a outliers**
- **Possui um cálculo de variância exclusivo**

$$media = \frac{n}{\sum_{i=1}^n\frac{1}{x_i}}$$

Em outras palavras...

$$\frac{n}{ \frac{1}{x1} + \frac{1}{x2} + \frac{1}{x3}...}$$

## MÉDIA QUADRÁTICA

- A raiz quadrada da média aritimetica (onde os valores são elevados ao quadrado)
- **É sensível a outliers**

$$media = \sqrt{\frac{\sum_{i=1}^n{x_i^2}}{n}}$$

# Quando usar cada um

### Média Aritimética
- Quando os dados forem **simétricos** ou estiverem **mais concentrados no centro**
- Quando os dados forem **uniformes**
	- Ex: média da idade de uma cidade, média das notas do enem

### Média Ponderada
- Nos mesmos casos da aritimética e quando alguns dados forem **mais importantes** que outros

### Média Geométrica
- Quando os nºs parecem saltar exponencialmente
	- Ex: média de casos de uma epidemia, média da população no último śeculo

### Média Harmônica
- Quando temos os valores vem de grandezas inversamente proporcionais 
	- Ex: velocidade e tempo, preço e lucro, densidade e volume, tempo de trabalho e eficiencia
	- Ex: média da razão preço/lucro de um produto ao longo do ano, média de taxa de entrega de tickets / tempo trabalhado

### Média Quadrática
- Quando tem valores positivos e negativos e o que importa é o valor absoluto
- Para calcular desvio padrão e erro quadrático em IA
- Para calcular quando envolve eletricidade ou ruído
	- Ex: média da qualidade sonora ao mapear o som numa casa de show, média do quanto uma ação varia

# Relação entre as médias

- Se todos os valores forem iguais, todas as médias serão iguais tbm
- Quando os valores são diferentes **sempre** a quadrática é a maior e a harmonica a menor

$mediaQuad >= médiaArit >= mediaGeom >= mediaHarm$

Ex1: dados: 6, 6 e 6
$mediaQuad = \sqrt{ \frac{6^2 + 6^2+ 6^2}3 } = \sqrt{\frac{3*36}{3}} = \sqrt36 = 6$

$mediaArit = \frac{6+6+6}{3} = \frac{18}{3} = 6$

$mediaGeom =  \sqrt[3]{6*6*6} = \sqrt[3]{6^3} = 6$

$mediaHarm = \frac{3}{ \frac{1}{6} + \frac{1}{6} +\frac{1}{6} } = \frac{3}{\frac{3}{6}} = 3 * \frac{6}{3} = 6$

Ex2: dados: 6, 8 e 12
$mediaQuad = \sqrt{ \frac{6^2 + 8^2+ 12^2}3 } = \sqrt{\frac{244}{3}} = \sqrt{81,333} = 9$

$mediaArit = \frac{6+8+12}{3} = \frac{26}{3} = 8,66$

$mediaGeom =  \sqrt[3]{6*8*12} = \sqrt[3]{576} = 8,3$

$mediaHarm = \frac{3}{ \frac{1}{6} + \frac{1}{8} +\frac{1}{12} } = \frac{3}{\frac{(4+3+2)}{24}} = \frac{3}{\frac{9}{24}} = 3 * \frac{24}{9} = 8$

# Cálculo das Variâncias 

## Geométrica
- Variância é o mesmo cálculo, porém usando os logs dos valores e a média dos logs
- Aqui a média dos logs é a média aritimética

$$variancia = \frac{\sum_{i=1}^n {(log(x_i) - mediaDosLogs)^2 }}{n}$$

**Lembrando**: **população** divide por N e **amostra** divide por N-1

Ex: 6, 8 e 12
$mediaDosLogs = \frac{log(6) + log(8) + log(12)}{3} = 0,92$
$variancia = \frac{(log(6)-0,92)^2 + (log(8)-0,92)^2 + (log(12)-0,92)^2}{3} = 0,01$

## Harmônica
- Variância é o mesmo cálculo, porém usando os inversos dos valores e o inverso da media harmonica

MH = média harmonica
$$variancia = \frac{\sum_{i=1}^n{ (\frac{1}{x_i} - \frac{1}{MH})^2 }}{n}$$

**Lembrando**: **população** divide por N e **amostra** divide por N-1

Ex: 6, 8 e 12
$MH = \frac{3}{ \frac{1}{6} + \frac{1}{8} + \frac{1}{12} } = 8$
$variancia = \frac{ ( \frac{1}{6} - \frac{1}{8})^2 + (\frac{1}{8} - \frac{1}{8})^2 + (\frac{1}{12} - \frac{1}{8})^2 }{3} = 0,0012$

## Quadrática
- É igual a variância normal
