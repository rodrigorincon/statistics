# TESTES DA REGRESSÃO LOGÍSTICA

Os testes a serem feitos na regressão logística são:

- Box-Tidwell
  - testa linearidade do logit
  - Nesse p-valor tem de ser maior que alfa
- Razão de verosimilhança (Likelihood Ratio)
  - Testa se o modelo como um todo é significativo
  - Substitui o teste F e **não tem test post-hoc**
- Teste de Wald
  - Testa cada variável se é significativa
  - Substitui o teste T

## BOX-TIDWELL

Para verificar a linearidade dos resíduos, ele verifica se as variáveis independentes (X) são lineares com relação ao logit, não ao valor Y de fato. Lembrando que o logit é o log da sigmoide.

O que ele faz é testar a qual expoente cada var independente X deve ser elevada para se aproximar do logit. No processo além de verificar a linearidade ainda retorna `qual deve ser o expoente usado em cada variável para encontrar a melhor aproximação`. Para isso você precisa passar as variáveis X elevadas aos expoentes que quer testar. Você pode passar os Xs elevados a expoentes inteiros, racionais (raíz quadrada) e ao próprio X (que resulta na mesma coisa que fazer X * ln(X), que é o que é usado nesse caso).

Para validar o logit da regressão logística passamos a var X * ln(X) ao invés de X para o Box-Tidwell.

### COMO FUNCIONA

Esse teste é feito através de uma regressão linear generalizada (usando os mínimos quadrados generalizados). Após a regressão é feita o teste T no coeficiente e checado se a linearidade com o expoente testado é válido. Na prática `o teste é uma regressão linear com a variável transformada em logit via X*ln(X)`. Por fazer a regressão linear o teste T é o teste feito por debaixo dos panos.

### HIPÓTESES

H0: A relação é linear. Passou no teste

H1: A relação não é linear. Não passou no teste. Os dados devem passar por uma transformação (serem elevados pelo expoente retornado pelo teste) e testado novamente que aí deve passar.

**Ou seja, queremos um p-valor maior que alfa nesse teste!**

### OBSERVAÇÃO

- Todos os valores de todos os Xs precisam ser obrigatoriamente > 0. Ele não funciona com valores negativos ou zero por usar log
- Não existe uma função pronta para ele no python, é preciso implementá-lo manualmente.

## RAZÃO DE VEROSSIMILHANÇA

`Usa o teste qui-quadrado para testar a divisão entre as verossimilhanças.`

### HIPÓTESES

H0: O modelo representa os dados tão bem quanto uma linha reta (só o intercepto)

H1: O modelo representa os dados melhor que uma linha reta

Ou seja, H0 zera todos os pesos/coeficientes e calcula o quão bem a regressão só com intercepto representa os dados (erro médio). 

### COMO CALCULAR

Para saber se o erro médio da nossa regressão é significativa ele faz o teste **qui-quadrado**, checando se os dados esperados (reais) e observados (previstos pela regressão logística) são significativamente distintos. 

O qui-quadrado serve perfeitamente para esse caso pois ele compara valores esperados e observados (independência) e serve para dados categóricos (que é o caso de uma regressão logística e classificadores no geral).

Nesse caso específico, o Q calculado é 

$Q = (\frac{L_{H1}}{L_{H0}})^2 = 2 * ln(\frac{L_{H1}}{L_{H0}})$, que pode ser descrito como

$$Q = 2 * [ln(L_{H1}) - ln(L_{H0})]$$

Aonde $L_{H1}$ e $L_{H0}$ são a função de máxima verossimilhança com os pesos finais de cada hipótese.

## WALD

### HIPÓTESES

H0: 

H1:

### COMO CALCULAR

z = a_i / erroPadrao(a_i)

# MEDIDAS DE ADEQUAÇÃO

Além dos testes de hipótese das premissas (que veem se os dados cumprem os requisitos do algoritmo) e do teste dos coeficientes (que testa se as variáveis afetam o resultado final de fato) podemos testar o **quão bem a sigmoide se ajusta aos dados**. Usada tanto para validar a regressão como para **comparar diferentes regressões**.

Importante perceber que uma reta bem ajustada aos dados **pode ser sinal de overfitting**! 

## Log-Verossimilhança

É a base para todos os demais métodos. Ele é a função de máxima verossimilhança com os pesos finais encontrados pela regressão.

Podemos também ter a log-verossimilhança da hipótese nula, aonde consideramos somente o peso do intercepto e todos os pesos/coeficientes das vars independentes são 0.

## PSEUDO R²

É uma variação do R² da regressão linear, mas como y é categórico a gente não pode usar correlação normalmente aqui. Mas também **informa quantos porcento da variância de Y é explicada pelo modelo**.

Existem diversas variações dele (McFadden, Cox-Snell, Nagelkerke), mas o mais comum é o McFadden.

O R² de McFadden é:

$$R_{mc} = 1 - \frac{ln(L_{reg})}{ln(L_{nulo})}$$

Aonde

- L é a função de máxima verossimilhança
- $L_{reg}$ é a máxima verossimilhança com os pesos finais da nossa regressão
- $L_{nulo}$ é a máxima verossimilhança com o peso final só do intercepto (com os pesos das vars independentes = 0)

Ou seja, é 1 menos a divisão das log-verossimilhanças. Por usar a log-verossimilhança da hipótese nula, podemos usá-lo para ter ideia de quão boa é a regressão mesmo sem comparar com outras.

#### VARIAÇÕES

Como dito antes, existem diversas variações como Cox-Snell e Nagelkerke. Cada um serve para um contexto diferente, por isso `use a versão padrão do seu contexto`.

## AIC e BIC

$$AIC = -2ln(L_{reg}) + 2k$$

$$BIC = -2ln(L_{reg}) + k*ln(n)$$

Aonde

- L é a máxima verossimilhança da regresão com os pesos finais da nossa regressão
  - Representa a precisão da regressão
- k é o número de variáveis
  - Representa a complexidade da regressão
- n é o tamanho da amostra

Novamente, ambos usam a log-verossimilhança da regressão, porém não usam a da hipótese nula. Por não usarem a verossimilhança nula só servem para comparar com outra regressão.

## MATRIZ DE CONFUSÃO

ver a aula 6

## CURVA ROC