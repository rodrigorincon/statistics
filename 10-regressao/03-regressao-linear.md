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

## DIFERENÇA ENTRE POPULAÇÃO E AMOSTRA

Equação para a população:

$$y = ax + b + erro$$

Equação para a amostra:

$$ŷ = ax + b$$

Quando falamos de população precisamos considerar o erro. Na amostra não precisa pois o y já é uma estimativa (ŷ significa y estimado).

## 