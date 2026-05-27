# REGRESSÃO LOGÍSTICA

É totalmente diferente da regressão linear. E também não tem nada a ver com regressão em formato de log.

Ela modela a **probabilidade de algo acontecer**, enquanto a linear mede o valor exato. Essa diferença acontece porque a **variável dependente (Y) é categórica**. Então não há como definir um valor exato para cada categoria da variável, o que se pode fazer é definir o quanto um grupo é mais comum que outro e definir a chance de uma medição cair em algum deles.

- Regressão linear: modelos de previsão
- Regressão logísitca: modelos de classificação

Tem dois tipos: Binária (apenas 2 categorias) e múltipla (3 ou mais categorias). Porém **as categorias precisam ser odernáveis/rankeáveis**. Elas tem de ter alguma ordem (de 1 a 5 estrelas, de discorto totalmente a concordo totalmente...) para criar faixas de valores que representam cada uma. Variáveis categóricas não ordinais (como regiões do país, bairros, etnias...) não podem ser usadas na regressão logística.

Ela também é chamada de modelo logit e de classificador de máxima entropia.

## RELAÇÃO ENTRE AS VARIÁVEIS X E Y

A regressão logística parte do pressuposto de uma relação linear entre as variáveis independentes X e o log da razão de chances de Y. Ou seja, o **log da chance de Y deve ser descrito por uma equação linear de X**. Isso é muito diferente de dizer que X e Y devem ser lineares ou que log de Y é linear com X, pois o que tem que ser linear não é Y ou log de Y, mas o log de sua chance.

O log da razão das probabilidades (conhecido como função logit) é a base da regressão logística. Esse conceito molda a função sigmoide (usada na regressão logística), definindo seu comportamento. Ou seja, é a definição da sigmoide que é o coração dessa regressão.

Mas em poucas palavras isso significa dizer que `Y deve se distribuir no formato da sigmoide (forma de S)`.

## PREMISSAS

- Independência dos dados
- Var dependente **Y categórica ordinal**
- Linearidade das variáveis X com o log das chances de Y
  - Y deve ter formato de sigmoide
- Ausência de multicolinearidade
- **Não ter outliers**
- Y deve ser binária ou ordinal
- Amostra grande

### NÃO PRECISA SEGUIR ESSAS REGAS

Por outro lado a regressão não precisa seguir as seguintes regras:

- Seguir a distribuição normal
- Não precisa ter homocedasticidade (variância igual dos erros)

Ou seja, não precisa testar os resíduos.

## QUANDO USAR

- Modelos de classificação
- Var dependente Y é categórica
- Quando houver relação linear entre as variáveis independentes e o log da chance da dependente 
  - Y deve ter formato de sigmoide

## QUANDO NÃO USAR

- Quando houver risco de, por puro acaso, pegar 2x o mesmo dado para análise (independência dos dados)
- Quando os dados forem pareados (antes/depois) (independência dos dados)
- Encontrar forte correlação entre as variáveis independentes (multicolinearidade)
- Não conseguir fazer uma regressão linear entre os dados e o log da probabilidade de Y
- Categorias de Y não puderem ser ordenadas/rankeadas

## TAMANHO MÍNIMO DA AMOSTRA

Para a regressão logística ser precisa é preciso um número grande de amostras. A regra geral é pelo menos 10 amostras na cateogria menos frequente para cada X. Ou seja, a equação para a o tamanho mínimo é:

$n = \frac{10k}{p_m}$

Aonde

- k é o número de variáveis independentes X
- $p_m$ é a probabilidade da categoria menos provável

## FUNÇÃO USADA

As funções que vão definir o valor não podem ir de -infinito a +infinito como na linear, elas tem de ficar restritas de 0 a 1. Logo uma reta não serve. Os coeficientes dessas funções não tem uma interpretação tão óbvia como na linear, como sendo coeficiente linear ou angular, mas deve ser entendido como pesos para uma avaliação.

A equação naturai da regressão logística é a sigmoide, pois mesmo que as variáveis X tendo valores de -infinito a +infinito o resultado de Y ficará entre 0 e 1 e com X=0 Y=0,5. Além disso ele tem uma subida suave, formando um S.

$$p = \frac{1}{1 + e^{-y}}$$

Aonde

- p é a probabilidade de y acontecer
- y é a regressão linear com os valores de X ($A_0 + A_1X_1 + A_2X_2 ...$)

## RAZÃO DAS CHANCES

É dito que **X deve ser linear com o log da razão das chances de Y**, mas o que isso significa? 

Como não podemos modelar probabilidades diretamente usando uma função linear (porque as probabilidades são limitadas entre 0 e 1), em vez disso trabalhamos com a chance. Aqui é importante dizer a diferença entre probabilidade e chance.

### O QUE É CHANCE

- Probabilidade: possibilidade de um evento ocorrer entre todos os resultados possíveis
  - Quase uma análise combinatória das opções com pesos para as mais prováveis
- Chance: compara a possibilidade de um evento ocorrer com a possibilidade de ele não ocorrer
  - É a comparação de uma probabilidade com seu complemento

Resumindo: `Chance nos diz quantas vezes mais provável é esse evento acontecer do que ele não acontecer`.

$chance(x) = \frac{p(x)}{1 - p(x)}$

Chance também é chamada de odd.

```
Ex: Tenho 2 maçãs, 1 pera e 5 laranjas. A probabilidade de eu pegar uma laranja é 5/8 = 0,625. A chance de eu pegar uma laranja é 5/3 = 1,667. Ou seja, eu tenho 1,667 vezes mais chances de pegar uma laranja do que pegar alguma outra fruta.
```

A chance pode variar de 0 ao infinito, com valores > 1 significando maior possibilidade e < 1 significando menor chance e 1 significa chances iguais. Nosso centro então é o número 1.

Porém a distribuição é muito assimétrica a direita (pico a esquerda). Algo 2x mais ou menos provável é 2 e 0.5, algo 4x mais ou menos provável é 4 e 0.25, os dados ficam muito concentrados entre 0 e 1 muito dispersos acima de 1. Algo 4x menos provável está muito mais perto de 1 (0,75 de distância) do que 4x mais provável (3 de distância).

### PROVA DA SIGMOIDE

Para consertar a assimetria tiramos o ln da chance, que transforma o resultado de -infinito a +infinito e espaçando igualmente as chances do centro 1. Como essa equção vai de -infinito a +infinito conseguimos usá-la para representar funções lineares com ela.

$ln(chance(x)) = ln(\frac{p(x)}{1 - p(x)}) = y$ aonde y é uma equação linear.

Elevando os 2 lados a "e" temos:

$chance(x) = \frac{p(x)}{1 - p(x)} = e^y$

Isolando a probabilidade temos que a probabilidade é

$$p(x) = \frac{e^y}{1 + e^y}$$

### RAZÃO DA CHANCE E AS VARIÁVEIS

A razão nos ajuda a interpretar os coeficientes que a regressão nos dá como resposta. Para a função $y = a_0 + a_1x$ temos a chance

$odd(x) = e^{a_0 + a_1x}$

Ao aumentarmos x em 1 unidade fica

$odd(x + 1) = e^{a_0 + a_1(x + 1)} = e^{a_0 + a_1x + a_1} = e^{a_0 + a_1x} * e^{a_1}$

Isso significa que ao aumentar 1 unidade em $X_i$, a chance é multiplicada por $e^{A_i}$. Esse multiplicador é a razão de chance. 

#### Se $A_i$ > 1 a chance aumenta, se < 1 a chance diminui e se = 1 então X não afeta o valor de Y.

## DEFINIÇÃO DE VALORES

Como Y varia entre 0 e 1, uma categoria deve representar o valor 1 e outra o valor 0. O ponto de corte costuma ser 0.5, assim sempre que um valor dá acima de 0.5 é jogado na categoria 1 e abaixo na categoria 0. Isso faz que, mesmo a função do cálculo sendo a sigmóide, ela se comporte como uma função degrau.

Quando tiver mais categorias são criadas faixas de valores para cada um. Isso transforma a sigmoide em uma escada.

A escolha de qual categoria será 1 é crucial para a interpretação. Eu vou sempre medir a probabilidade da variável Y ser 1, portanto o valor final calculado corresponde a categoria 1. Portanto defina como 1 a categoria que você quer testar ou considera mais importante (para o binário, quando é múltiplo é a categoria maior).