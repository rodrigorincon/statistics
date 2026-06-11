# MEDIANA DE MOOD

Teste não paramétrico para verificar se 2 ou mais medianas são iguais ou não. É a **versão da Anova de 1 via** para dados não paramétricos (categóricos ou que não seguem a distribuição normal). Caso os dados não cumpram as premissas para a Anova (resíduos normais, passar no teste de Levene e não ter muito outliers) deve-se usar esse. Dados categóricos também se encaixam bem nele.

Ele é **muito baseado na mediana** ao invés da média. Por usar a mediana outliers não afetam o cálculo e distrbuições não normais também não são problemas.

## PREMISSAS

- Os dados devem ser independentes
- Variável deve ser numérica ou ordinal (1º, 2º, 3º...)

## HIPÓTESES

H0: as medianas de todos os grupos são iguais

H1: Pelo menos 1 mediana é diferente das demais

Para saber qual amostra que difere tem de fazer o **teste de Dunn (post hoc)**.

## COMO CALCULAR

### Passo 1: mediana global

Calcula a mediana global, considerando todos os valores de todos os grupos.

### Passo 2: classificação

Em cada grupo, conta-se quantos dados são maiores que a mediana global. Menores ou iguais são colocados juntos em outro grupo. Ao final teremos uma tabela de contigência 2xK como a abaixo

|              | Categoria 1 | Categoria 2 | Categoria 3 |
|:--           | :--         | :--         | :--         |
| > mediana    | 10          |  3          |  12         |
| $\le$ mediana| 21          |  9          |  4          |

### Passo 3: Qui-Quadrado

Usa o teste Qui-Quadrado para ver se a proporção de observações acima e abaixo da mediana difere significativamente entre os grupos.

## SEMELHANÇA COM KRUSKAL-WALLIS

Ele e Kurskal-Wallis são opções para a Anova de 1 via e ambos são baseados em medianas, bons para dados ordinais e categóricos e usam Dunn como post-hoc. **Eles servem para os mesmos casos**.

Porém o **funcionamento interno é totalmente diferente**. Kurskal-Wallis usa ranks e avalia a diferença na distribuição geral. Mood usa só a mediana geral e vê quantos estão acima e abaixo. **Mood é muito mais simples, porém tem menor poder esatpistico (maior erro tipo II)**.

`Kruskal-Wallis deve ser sua primeira opção`. Use Mood somente se você tiver **escalas com limites bem definidos com muitos valores acumulados neles**.

## TAMANHO DO EFEITO

É calculado comparando as medianas de cada grupo. Quanto maior a diferença entre as medianas dos grupos, maior o efeito medido.