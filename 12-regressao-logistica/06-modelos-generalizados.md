# MODELO LINEAR GENERALIZADO (GLM)

É uma generalização da regressão linear, fornecendo um algoritmo flexível para qualquer tipo de regressão. Ele tem 3 partes principais que podem ser customizáveis, permitindo usá-lo tanto para regressões lineares como logísticas binárias, multinomiais, gama e até poisson.

Importante ressaltar que toda regressão linear é uma regressão generalizada e o mesmo vale para a logística. Mas nem toda regressão generalizada é uma delas (pode ser gama ou poisson ou tantas outras).

# COMPONENTES

Toda regressão tem 3 componentes principais:

- Componente aleatório
  - Diz qual a distribuição de probabilidade do Y (normal, binomial, poisson...)
- Componente sistemático
  - Equação linear dos X ($a_0X_0 + a_1X_1 + ... + a_nX_n$)
- Função de ligação
  - Especifica como X e Y se relacionam
  - Como o valor esperado de Y se relaciona à equação linear dos X
  - Ex: identidade, ln, logit, inverso...

### Exemplo: Regressão Linear

1*ŷ = $a_0 + a_1X_1 + a_2X_2 + ... + a_nX_n = \sum{a_iX_i}$

Aonde:

- $\sum{a_iX_i}$ é o componente sistemático
- ^ no y (valor esperado) é o componente aleatório (no caso distribuição normal)
- 1 é a função de ligação (no caso, a função identidade)

A regressão linear tem como componente aleatório a distribuição normal pois tem como premissa os erros seguirem uma distribuição normal. Como ŷ é o valor previsto, espera-se que ele tenha um erro embutido e esse erro deve ter uma distribuição normal. Portanto implicitamente essa fórmula esconde um pressuposto de distribuição normal.

Como não fazemos nenhuma transformação no valor para ele se encaixar em Y, a função de ligação é a função identidade (sem alterações).

No R a regressão linear pode ser feita das 2 formas que dão exatamente o mesmo resultado:

```r
reg <- lm(y ~ x1 + x2, data = dados) # função da regresão linear comum

reg <- glm(y ~ x1 + x2, data = dados, family= gaussian(link = 'identity')) # função do modelo generalizado especificando a família (distribuição de Y) e a o tipo de link (função de ligação)
```

### Exemplo: Regressão Logística

$ln(\frac{p}{1-p}) = $a_0 + a_1X_1 + a_2X_2 + ... + a_nX_n = \sum{a_iX_i}$

Aonde:

- $\sum{a_iX_i}$ é o componente sistemático
- $p$ é o componente aleatório (no caso distribuição binomial)
- $ln(\frac{p}{1-p})$ é a função de ligação (no caso, a função logit)

P é a probabilidade de Y ser ou não de uma categoria. Como ele só pode assumir 2 valores (sim/não, passou/reprovou...) a distribuição de P é binomial. Novamente Y esconde uma distribuição implicitamente.

O logit é a tranformação que fazemos para os valores se encaixarem em Y, por isso ele é a nossa função de ligação.

Podemos entender a regressão logística como uma transformação de Y através da divisão das chances e o log para fazê-lo se adaptar a 2 valores binários. Isso é o que define a função de ligação.

O exemplo de como fazer a regressão logística no R mostra como um modelo generalizado funciona:

```r
reg <- glm(y ~ x1 + x2, data = dados, family= binomia(link = 'logit')) # família = distribuição de Y (no caso, binomial pois só pode ter 2 categorias). link = função de ligação (no caso, logit)
```

## Componente sistemático

É a soma de todos os X com seus pesos. A definição de como encontrar esses pesos varia (mínimos quadrados, gradiente descendente, gradiente estocástico, Ridge...), mas ao final sempre deve ter um somatório das variáveis independentes com seus pesos.

## Componente aleatório

É a distribuição de Y. Ela não é visível na equação, mas saber qual a distribuição dos seus dados e/ou de seus resíduos é essencial para conseguir fazer uma regressão confiável. Apesar de não estar lá diretamente, sempre terá uma variável dependente presente que pressupõe uma distribuição (ŷ que é um valor previsto ou p que é uma probabilidade).

Por isso é importante estudar seus dados e entender seu contexto, para escolher a regressão correta para seus dados e o que quer fazer com eles.

## Função de ligação

É uma função que faz seu cálculo se encaixar nos Ys observados na amostra. Ele faz uma transformação nos seus dados calculados para que eles tomem a forma do Y. **É essa função que dá a forma da sua equação de regressão**.

Os tipos mais comuns são:

- Identidade: não faz nada, deixa a reta como está (como na regressão linear)
- Ln: faz o log da equação
- Inverso: 1/equação
- Logit: log da razão das chances

# TABELA DE GLMs

Abaixo são mostrados alguns modelos para ajudar a escolher o mais apropriado para seu caso. Importante saber que esses não são todos. Existem muito mais, mas estes são um bom início.

|Modelo                   | Distribuição| Função Ligação | Tipo Y                     | Exemplo                  |
|:--                      | :--         | :--            | :--                        | :--                      |
|Reg linear               | Normal      | Identidade     | Contínua                   | Prever valores numéricos |
|GLM com Distribuição Gama| Gama        | Ln ou Inverso  | Contínua > 0               | Prever valores numéricos > 0, quando os dados são assimétricos |
|Reg logistica            | Binomial    | Logit          | Categ Binário              | Sim/Não, Passou/Reprovou |
|Reg logistica multinomial| Binomial    | Logit          | Categ > 2 grupos           | regiões, cidades, votação|
|Reg logistica ordinal    | Binomial    | Logit          | Categ ordinal              | likert                   |
|Reg Poisson              | Poisson     | Ln             | Discreto, media = variância| Nº de casos numa região ou período|
|Reg Poisson c\ offset    | Poisson     | Ln             | Taxa, media = variância    | Porcentagem de casos numa região ou período|
||||||

Para dados (Y) discretos com media $\ne$ variância (quando a premissa de Poisson não é cumprida), temos 2 opções de regressão que podem ser usadas. Elas servem tanto como substitutos do Poisson como o Poisson com offset.

- Regressão Quasi-Poisson: quando a diferença não é tão grande
  - Usa a distribuição Poisson
  - Função de ligação ln
- Regressão Binomial negativa: quando a diferença é muito grande
  - Usa a distribuição Binomial Negativa
  - Função de ligação ln
