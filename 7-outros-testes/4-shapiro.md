# TESTE SHAPIRO-WILK

É um teste que **verifica se os dados tem distribuição normal ou próxima o suficiente**. O teste é compara a distribuição dos dados com a normal teórica. 

H0: os dados seguem a normal.

H1: os dados não são normais.

Logo, p-valor $\leq$ alfa = dados não normais, p-valor > alfa = dados normais. **Queremos encontrar um p-valor maior que alfa**.

## PREMISSAS

- Os dados devem ser independentes
- Os dados devem ser contínuos (não funciona com dados discretos)
- Melhor com amostras pequenas (n < 50)
  - Mas ainda funciona bem com amostras grandes
  - Não usar acima de 5000

## COMO FUNCIONA

O teste dá uma probabilidade W que vai de 0 a 1, onde 1 é uma normal perfeita.

### Passo 1: Ordenar os valores

Deve-se ordenar os dados da amostra, do menor ao maior

$x_1 < x_2 < x_3 ... < x_n$

### Passo 2: Soma dos quadrados

Calcula a variância, porém sem a divisão.

$SS = \sum_{i=1}^n (x_i - media)^2$

### Passo 3: Soma ponderada

Subtrai o último do primeiro, penultimo do segundo... e multiplica por um peso.

$b = \sum_{i=1}^{\frac{n}{2}} a_i(x_{n-i+1} - x_i)$

Caso N seja ímpar, o somatório vai até $\frac{n+1}{2}$

O peso $A_i$ é o coeficiente de Shapiro-Wilk, tabelado. Eles representam **como uma distribuição normal deve se comportar**, pois são gerados a partir das médias, variâncias e covariâncias de uma distribuição normal de tamanho N-i+1. Porém não precisamos calcular variância e covariância da distribuição normal diversas vezes, isso nos é dado pela tabela de Shapiro-Wilk.

Quanto menor i, maior A, isso significa que os primeiros pesos (i pequeno) são maiores que os últimos. Logo, as maiores amplitudes (último - primeiro) tem peso maior que as amplitudes menores (subtração dos 2 do meio), o que dá **mais peso para as caudas e menos para valores centrais**. O fato da amplitude nos valores centrais já ser muito pequena e enorme nos primeiros exarceba ainda mais essa diferença, multiplicando números grandes nos primeiros loops e nos últimos multiplicando 2 números próximos de 0.

Com isso B representa quão bem nossos dados se encaixam numa normal.

### Passo 4: Estatística W calculada

$$W = \frac{b^2}{SS}$$

Dividimos o encaixe do nossos dados na normal pela dispersão dos dados. Isso nos dá o resultado final do quão bem o encaixe ficou. Como a dispersão usada é a variância (que eleva ao quadrado), elevamos B também para ficar na mesma magnitude.

**W é o tamanho do efeito** do teste. Não precisamos fazer mais cálculos para encontrá-lo. Ele também costuma ser retornado pelo python.

### Passo 5: Determinar p-valor

Usamos a tabela do p-valor de Shapiro-Wilk para procurar o valor tabelado. Shapiro-Wilk tem 2 tabelas, uma para os coeficientes A e outra para determinar o p-valor.

Para encontrar o p-valor procuramos na linha do nosso tamanho da amostra (N) o valor do W calculado. O p-valor dessa coluna será o nosso p-valor. Caso Não tenha o valor de W calculado na tabela, fazemos a interpolação dos valores mais próximos.

$$p-valor = \frac{(W-y_0)(x_1 - x_0)}{y_1-y_0} + x_0$$

Aonde Y são os valores no meio da tabela entre nosso W calculado e X são os p-valores das colunas. W é nosso W calculado.

### Passo 6: Interpretação

Se p-valor > alfa, então os dados são normais. Repare que só usamos nosso alfa agora, **não usamos alfa na busca na tabela**.

## Exemplo

A seguinte amostra é normal? Amostra = [1.906, 2.103, 1.522, 2.618, 1.427, 2.225, 1.697, 3.154, 1.985, 1.996, 1.71]

N=11, SS = 2.5060

Para calcular B, temos que pegar a amplitude dos extremos daquele loop e pegar os coeficientes. Como N=11, teremos 6 coeficientes. Pegamos os coeficientes da coluna N=11. $A_1$ será a 1ª linha e assim por diante. $A_i$ sendo sempre a i-ésima linha.

Como N=11 só tem 5 linhas, o último coeficiente é sempre 0 (o que só acontece em N ímpar), pois como multiplica o dado subtraído dele mesmo será ignorado de todo modo (dado do meio no somatório acaba não tendo par, sendo tanto o número maior como o menor). Em outras palavras, quando N é ímpar essa volta do somatório é 0*0.

Loop 1: A1 = 0.5601. Amplitude 1.7270

Loop 2: A2 = 0.3315. Amplitude 1.0960

Loop 3: A3 = 0.2260. Amplitude 0.5280

Loop 4: A4 = 0.1429. Amplitude 0.3930

Loop 5: A5 = 0.0695. Amplitude 0.0900

Loop 6: A6 = 0. Amplitude 0

Com isso achamos b = 1.5124 e W: 0.9127

Procuramos na tabela do p-valor na linha N=11 qual coluna tem o valor W. Como não achamos fazemos a interpolação dos valores mais próximos.

Valores próximos: p-valor=0.05 com W=0.850 e p-valor=0.1 com W=0.876. Usamos os p-valores como X e os W como Y na interpolação.

$p-valor = \frac{(0.9127 - 0.850)(0.1 - 0.05)}{0.876 - 0.850} + 0.1 = 0.3294$

Ou seja, os dados são normais.

# TESTE Kolmogorov-Smirnov

É um teste **não paramétrico** que compara se 2 amostras seguem a mesma distribuição ou se uma 1 **amostra segue alguma distribuição específica, podendo escolher qual distribuição quer testar**.

Executamos o teste com os dados juntamente com uma amostra perfeitamente encaixada na sua distribuição. Assim sabemos se os dados seguem aquela distribuição. Assim também podemos mudar qual distribuição queremos verificar facilmente, só trocando a amostra controle. 

Seguindo a mesma lógica podemos comparar 2 grupos de dados independentes e ver se eles tem a mesma distribuição (embora não saberemos qual).

Definição: **Compara os dados com uma amostra da distribuição que queremos testar**.

## HIPÓTESES

H0: Os dados seguem a distribuição especificada.

H1: Os dados não seguem a distribuição especificada.

Queremos encontrar um p-valor menor que alfa, confirmando que segue a distribuição.

## QUANDO USAR

- Quando quer testar os dados para várias distribuições
- Quando quer testar os dados para distribuições diferentes da normal
- Quando quer testar a normalidade e a quantidade de dados são muito grandes (N>5000)
  - Superior ao Shapiro para muitos dados

## PREMISSAS

- A amostra da distribuição está correta e representa todo seu formato
- Os dados devem ser contínuos (não funciona com dados discretos)
- Quando compara 2 dados para ver se tem a mesma distribuição, os dados precisam ser independentes

#### LIMITAÇÕES

O teste não detecta bem diferenças nas caudas da distribuição. Se a única diferença for o peso das caudas ele pode não detectar.

## COMO FUNCIONA

https://pt.wikipedia.org/wiki/Teste_Kolmogorov-Smirnov
https://www.uel.br/projetos/experimental/pages/arquivos/Kolmogorov-Smirnov.html
https://pellisistemas.com/teste-de-kolmogorov-smirnov-ks/?srsltid=AfmBOoo6Zzda8pvLBy9Kau0VZgOn5eO6X4wxt5frFzfDVdzuUuvHg9vU
https://support.minitab.com/pt-br/minitab/help-and-how-to/statistics/basic-statistics/how-to/normality-test/methods-and-formulas/methods-and-formulas/

## EXEMPLO