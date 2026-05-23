# REGRESSÃO LINEAR

- Assume que a relação entre as variáveis é linear (pode ser descrita por uma reta)
- A relação é constante (não explode como uma exponencial) ou vai diminuindo a força da relação (como um logaritmo)

A regressão linear simples vai formar uma equação de 1º grau

$y = a*x + b$

Aonde

- x é a variável (ou variáveis) independente
- y é a variável dependente
- a é o coeficiente angular (grau de inclinação da reta)
- b é o coeficiente linear (onde a reta corta o eixo Y ou o valor de Y quando x=0)

## SIGNIFICADO DOS COEFICIENTES

1. Coeficiente angular (a)

- Revela o quanto a var X influencia Y
- Quanto maior, mais forte é a influência
- Diz se a influência é proporcional ou inversa (positiva ou negativa)

2. Coeficiente linear (b)

- Também chamado de **intercepto**
- É um valor fixo
- Diz o valor de Y quando X=0 
  - Importante avaliar se faz sentido no seu cenário X ser 0 e o que isso pode significar
  - Nem todo contexto permite X=0, então alguns buscar entendê-lo não faz sentido
- Exemplos do que pode representar:
  - O custo base ou inical, que você sempre terá, independente de X
  - Seu ponto de partida, de onde os valores começam

## COMO CALCULAR

Para uma regressão simples os **Minimos quadrados** (OLS) funcionam perfeitamente. Os demais são para variáveis múltiplas.

## TESTE DE HIPÓTESE 

Para uma regressão simples o teste T é o usado. É preciso testar as premissas, então os testes de cada premissa também devem ser usados.

- Teste T (p-valor > alfa)
- Jarque-Bera (p-valor < alfa)
- Breusch-Pagan (p-valor < alfa)
- Durbin-Watson (p-valor < alfa)
  - Apenas para séries temporais

O cálculo do nosso T calculado é:

$$T = \frac{A}{ \frac{desvio_e}{ \sqrt{\sum{(x_i - media_x)^2}} } }$$

Ou seja, divide o coeficiente da angular da reta pelo desvio padrão dos erros e pela soma dos quadrados de X. É quase a divisão pelo desvio e pela variância, mas não temo a divisão por N-1 para configurar a variância. Importante ressaltar que o desvio e a soma dos quadrados são de objetos diferentes.

O cálculo do T tabelado usa n-2 graus de liberdade e nosso alfa e deve ser **bicaudal**.

## GRAUS DE LIBERDADE

Os graus de liberdade numa regressão linear é **n - k - 1**, onde k é o número de variáveis independentes (X). Isso porque você está tentando definir k coeficientes (os valores que multiplicam x1, x2, x3...), logo temos k coeficientes, portanto k-1 graus de liberdade.

OBS: o intercepto (B), coeficiente constante que não multiplica nada, é ignorado.

Ex: Na regressão linear simples (1 X e 1 Y) os graus de liberdade são n-2.

## INTERVALO DE CONFIANÇA

O intervalo de confiança é a o valor calculado $\pm$ margem de erro. A margem de erro por sua vez é o erro padrão * T (distância até o desvio padrão). T é dado pelo teste T por ser o teste que usamos (ele também define o nível de confiança da margem). O cálculo do erro padrão é feito a partir de X. 

Simplificando o cálculo do erro padrão, chegamos nas seguintes equações da margem de erro para os coeficientes.

Para o coeficiente linear (B) é:

$$ME = T(n-2, \alpha/2) * desvio_e * \sqrt{ media_x * \frac{1}{\sum{(x_i-media_x)^2} } }$$

Para o coeficiente algular (A) é:

$$ME = T(n-2, \alpha/2) * \frac{desvio_e}{\sqrt{\sum{(x_i-media_x)^2}}}$$

Aonde

- T é calculado a partir da curva T para os parâmetros informados
- $desvio_e$ é o desvio padrão dos erros

## INTERVALO DE PREDIÇÃO

$$MP = T(n-2, \alpha/2) * desvio_e * \sqrt{ 1 + \frac{1}{N} + \frac{(x - media_x)^2}{\sum{(x_i-media_x)^2}} }$$

