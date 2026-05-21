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

## GRAUS DE LIBERDADE

Os graus de liberdade numa regressão linear é **n - k - 1**, onde k é o número de variáveis independentes (X). Isso porque você está tentando definir n coeficientes (os valores que multiplicam x1, x2, x3...), logo temos k coeficientes, portanto k-1 graus de liberdade.

OBS: o intercepto (a0), coeficiente constante que não multiplica nada, é ignorado.

Ex: Na regressão linear simples (1 X e 1 Y) os graus de liberdade são n-2.

## INFERÊNCIA

A seguir mostro como calcular os intervalos de confiança e predição para a regressão linear simples.

### INTERVALO DE CONFIANÇA

???

### INTERVALO DE PREDIÇÃO

???

