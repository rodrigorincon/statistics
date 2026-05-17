# TESTE MCNEMAR

Teste não paramétrico que testa se há **diferença entre as proporções em amostras dependentes**. Amostras dependentes podem ser antes/depois ou quando a mesma pessoa ou evento age em todas as categorias. 

O teste é baseado na distribuição qui-quadrado. Inclusive é uma **opção para usar no lugar do teste qui-quadrado de independência** quando as amostras não são independents.

O teste de McNemar só serve para 2 categorias/amostras, ou seja, a variável só pode assumir 2 valores. O teste de McNemar **funciona apenas com variávels binárias** (também chamadas de Bernoulli).

As categorias não podem ser ordinais/rankeáveis (senão usaria Wilcoxon) e devem ser dependentes (senão usaria qui-quadrado).

## EXEMPLOS

- Testar a sensação de dor antes e depois de um remédio com 2 grupos (controle e que tomou remédio)
- Testar se os alunos acertaram mais uma certa questão antes e depois da aula
- Testar se os clientes tão satisfeitos ou não com atendimento em 2 lojas após ele ir em ambas
- Testar se a opinião das pessoas sobre um produto mudou após uma propaganda

## PREMISSAS

- As variáveis devem ser dependentes/relacionadas (ex: antes e depois)
- As variáveis só podem ter 2 categorias (vars binárias)
- As categorias não são ordinais (não podem ser rankeadas)

## HIPOTESES

H0: p1 = p2, As proporções de sucesso são iguais entre os grupos

H1: p1 $\ne$ p2, As proporções de sucesso são diferentes entre os grupos

## COMO CALCULAR

Ele pode ser calulado de 2 formas: via qui-quadrado ou via binomial. O qui-quadrado é o principal, sendo o `binomial usado apenas quando os valores significativos pro teste são pequenos` (p2 + p3 < 25). Isso ocorre pois com valores muito pequenos há um descolamento da distribuição qui-quadrado e a curva não descreve mais tão bem os resultados, sendo preciso usar a distribuição binomial para esses valores.

### Cálculo Qui-Quadrado

Como se trata de 2 variáveis binárias e dependentes, podemos fazer uma tabela de contigência 2x2 para descrever todas as possibilidades. O teste ele verifica a diferença entre a linha X e coluna X, checando se são iguais, menores ou maiores (de acorde com a cauda do teste). Se você vai verificar a linha 1 e coluna 1 ou linha 2 e coluna 2 depende de como você coloca os dados na tabela. O exemplo abaixo ilustra isso.

| momento |           | depois    |         |           |
| :--     | :--       | :--:      |  :--    | :--       |
|         |  dor      |  presente | ausente | **total** |
| antes   |  presente |   16 (p1) |  34 (p2)| **50**    |
|         |  ausente  |   20 (p3) |  30 (p4)| 50        |
|         | **total** | **36**    |  64     | **100**   |

De um total de 100 pessoas, 50 pessoas sentiam dor antes, depois apenas 36. Queremos saber se a pocentagem de pessoas com dor diminui, então temos de comparar a linha com dor e a coluna com dor (linha 1 e coluna 1). 

Comparar esses 2 valores é a mesma coisa que comparar a diagonal p3 e p2, pois são essas 2 células que definem os valores da linha 1 coluna 1. Linha 1 é definido por p1 + p2 e a coluna 1 por p1 + p3. Como p1 é igual em ambas, só p2 e p3 que definem a diferença entre a linha e coluna, portanto, **só p2 e p3 definem o resultado do teste**.

Com isso a equação do teste fica

$$Q = \frac{(|p2 - p3| - 1)^2}{p2 + p3}$$

Essa equação já considera a correção de Yates para tabelas 2x2. **O grau de liberdade do teste de McNemar é sempre 1**.

Para encontrar o p-valor verifica-se na tabela qui-quadrado usando o valor de Q calculado e o grau de liberdade. O valor da coluna é o p-valor.

### Cálculo Binomial Exato

**Usado apenas quando p2 + p3 < 25**. Por serem vars binárias encaixam bem na probabilidade binomial com probabilidade = 0,5. A distribuição binomial terá p=0,5 e N=p2+p3.

O binomial calcula o p-valor unicaudal. Para saber o valor bicaudal multiplique o p-valor por 2.

$$pValor = \sum_{i=b}^n \binom{n}{i} 0,5^n$$