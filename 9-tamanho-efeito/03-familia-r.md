# R de Cohen

Mede o grau de correlação entre 2 amostras. É uma variação da correlação de Pearson (R e Pearson).

$$R = \frac{Z}{ \sqrt{N} }$$

Aonde

- Z é o valor de z calculado, do teste Z
- N é a soma do tamanho de todas as amostras

Extendendo a equação fica:

$R = \frac{propA - propB}{\sqrt{ propTotal(1-propTotal)(\frac{1}{nA} + \frac{1}{nB})(nA + nB) }}$

Aonde

- propTotal é a média das proporções das 2 amostras.

## Interpretação

Como uma variação da correlação normal, **pode variar de -1 a +1**, informando apenas quão correlacionado está. **Não informa a porcentagem de correlação**, isso é o R² que diz. Normalmente é considerado:

- Irrisório: até 0,1 
- Pequeno: absoluto entre 0,1 até 0,3
- Médio: absoluto entre 0,3 e 0,5
- Grande: absoluto acima de 0,5

## Usado para

- Teste Z
- Mann-Whitney
- Wilcoxon

### Exemplo

1. Foi feito um teste Z para comparar 2 grupos. O teste deu um Z = -4,242.

GrupoA: N=341, média=19,66, desvio=5,48.

GrupoB: N=249, média=17,45, desvio=6,12. 

Tota de pessoas = 590

$R = \frac{-4,242}{\sqrt{590}} = -0,17$

O valor é negativo porque a média do grupo B é menor. Como a diferença das médias é 2 e os desvios de ambos são grandes (significativamente maiores que a diferença das médias) o valor baixo para o tamanho do efeito faz sentido. O teste pode ser significativo, mas a diferença é muito pouca, pois ainda fica dentro dos desvios padrão.

# Coeficiente phi

Mede o grau de correlação entre 2 variáveis categóricas, tanto nominais quanto ordinais. As variáveis podem ter apenas **2 categorias cada uma, formando assim uma tabela 2x2**. Ele é calculado a partir da distribuição qui-quadrado de independência (usa independência pois queremos saber quão relacionados são).

$$\phi = \sqrt{ \frac{Q}{n} }$$

Aonde

- Q é o valor da distribuição qui-quadrado
- n é o tamanho total da amostra somando todas as variáveis e categorias

## Interpretação

**Pode variar de 0 a 1, informando a porcentagem de correlação**. Normalmente é considerado:

- Irrisório: até 0,1
- Pequeno: entre 0,1 e 0,2
- Médio: entre 0,2 e 0,6
- Grande: acima de 0,6

# V de Kramer

Ele é a generalização do Coeficiente phi para qualquer quantidade de categorias nas variáveis. Mede o grau de correlação entre 2 variáveis categóricas, tanto nominais quanto ordinais. As variáveis podem ter quantas categorias quiser. Ele é calculado a partir da distribuição qui-quadrado de independência (usa independência pois queremos saber quão relacionados são).

$$V = \sqrt{ \frac{Q}{n * min(linhas - 1, colunas - 1)} }$$

Aonde

- Q é o valor da distribuição qui-quadrado
- n é o tamanho total da amostra somando todas as variáveis e categorias
- min é o menor valor entre linhas - 1 e colunas - 1
  - É o menor k-1 das variáveis envolvidas

Perceba que a única mudança é o mínimo no denominador. Isso porque no coeficiente phi, por trabalhar apenas com tabelas 2x2, seu valor é sempre 1.

## Interpretação

**Pode variar de 0 a 1, informando a porcentagem de correlação**. Para interpretar o valor precisamos dos graus de liberdade do qui-quadrado. A sugestão, na falta de uma interpretação oficial dada pela área de atuação, é dada pela tabela abaixo:

|GL  | Irrisório | Pequeno         | Médio           | Grande     |
|:-- | :--       | :--             | :--             | :--        |
| 1  | < 0,1     | 0,1 > X < 0,3   | 0,3 > X < 0,5   | $\ge$ 0,5  |
| 2  | < 0,07    | 0,07 > X < 0,21 | 0,21 > X < 0,35 | $\ge$ 0,35 |
| 3  | < 0,06    | 0,06 > X < 0,17 | 0,17 > X < 0,29 | $\ge$ 0,29 |
| 4  | < 0,05    | 0,05 > X < 0,15 | 0,15 > X < 0,25 | $\ge$ 0,25 |
| 5  | < 0,05    | 0,05 > X < 0,13 | 0,13 > X < 0,22 | $\ge$ 0,22 |

# ETA-QUADRADO

Mede quantos porcento da variância é definido pelas variáveis independentes. Por medir mudança na variância é muito usado na Anova. Pode ser entendido como uma variação do coeficiente de determinação R².

$$\eta = \frac{SS_{efeito}}{SS_{total}}$$

Aonde

- $SS_{efeito}$ é a soma dos quadrados entre as médias (QME, o numerador do valor F)
- $SS_{total}$ é a soma dos quadrados de tudo (todos os grupos, erros e interações entre os grupos)

Com isso estamos dividindo a variância do efeito por toda variância, pois a soma dos erros é a variância sem a divisão pelo N. Por dividir a soma dos efeios pelo todo temos uma porcentagem, já que o todo inclui o grupo.

## Interpretação

**Pode variar de 0 a 1, informando a porcentagem de correlação**. Normalmente é considerado:

- Irrisório: até 0,01
- Pequeno: entre 0,01 e 0,06
- Médio: entre 0,06 e 0,09
- Médio-grande: entre 0,09 e 0,14
- Grande: acima de 0,14

### Exemplo

Queremos saber se o sexo e a intensidade dos exercícios influenciam a perda de peso. Chamamos 30 homens e 30 mulheres e colocamos 10 de cada fazendo exercícios leves, 10 moderados e 10 pesados. Ao final a soma dos quadrados de todos os gêneros deu 15,8 e a soma dos exercícios deu 505,6 e o quadrado dos resíduos deu 89,2. Assim o total deu 610,6.

O eta quadrado pro sexo é 15,8 / 610,6 =  0,026. O eta quadrado pra intensidade do exercício é 505,6 / 610,6 =  0,828. Logo o sexo pouco influencia na perda de peso, mas sim a intensidade do exercício.
