# TESTES DE CORRELAÇÃO

- Usam o coeficiente de correlação (qualquer um deles) para fazer um teste
- Verifica se existe uma **relação significativa entre 2 variáveis**
- O tipo de variável define o tipo de correlação usado

## HIPÓTESES

$H0: r = 0$ (correlação inexistente)

$H1: r \ne 0$ (existe correlação significativa)

## QUAL CORRELAÇÃO USAR

- 2 variáveis paramétricas com poucos outliers: Pearson
- 2 variáveis não paramétricas (categóricas): Spearman
- 2 variáveis não paramétricas com amostra pequena: Kendall
- 1 variável paramétrica e outra não paramétrica com apenas 2 categorias: Bisserial

OBS: as variáveis paramétricas devem seguir a distribuição normal.

## EQUAÇÃO

$$t = \frac{ r \sqrt{n-2} }{ \sqrt{1 - r^2} }$$

Aonde

- r é o coeficiente de correlação (qualquer um dos tipos escolhidos)
- n é o tamanho da amostra

O resultado será seu t calculado e deve ser comparado com o t tabelado usando a **tabela T com n-2 graus de liberdade**. Se **T calculado > T tabelado, rejeita-se H0**.

Em suma, o teste de correlação é uma variação do teste T.

### TESTES NÃO PARAMÉTRICOS

Mesmo quando se faz um teste de correlação não paramétrico (Spearman, Kendall, Bisserial) usa-se o teste T. O teste não muda independente de ser paramétrico ou não nem com o tipo de correlação usada.