# TESTE DE KRUSKAL WALLIS

Serve para comparar 3 ou mais medianas e ver se são todas iguais.

É a versão da Anova de 1 via para dados não paramétricos (categóricos ou que não seguem a distribuição normal). Caso os dados não cumpram as premissas para a Anova (resíduos normais, passar no teste de Levene e não ter muito outliers) deve-se usar esse. Dados categóricos também se encaixam bem nele.

Ele é **muito baseado na mediana** ao invés da média. Por usar a mediana outliers não afetam o cálculo e distrbuições não normais também não são problemas.

Serve para a **Anova de 1 via** (comparar várias variáveis com 1 categoria só).

Importante saber que o **nº de dados em cada amostra não precisa ser o mesmo**.

## PREMISSAS

- Os dados devem ser independentes
- Variável deve ser numérica ou ordinal (1º, 2º, 3º...)

## HIPÓTESES

### Para 1 Amostra

H0: medianaA = medianaB = medianaC

H1: Pelo menos 1 mediana é diferente

Para saber qual amostra que difere tem de fazer o **teste de Dunn (post hoc)**.

## COMO CALCULAR

Ele é muito parecido com o Mann-Whitney, mudando só na forma de calcular o valor final. Mas o processo de ordenar e rankear todas as amostras juntas e depois somar os rankings de cada grupo se mantém igual.

### Passo 1: junte as amostras e ordene os dados 

Coloque todas as amostras numa lista só e os ordene do menor ao maior (independente de qual amostra cada um veio).

### Passo 2: rankeie as posições

Faça um ranking para cada valor de acordo com sua posição, com o menor sendo o 1, o segundo menor 2 e assim por diante. Em caso de empate todos os valores empatados devem ter a média das posições.

Exemplo: se o 3º, 4º e 5º são iguais o ranking dos 3 serão 4 (média de 3, 4 e 5).

### Passo 3: Some os rankings de cada amostra

Some o valor dos rankings de cada amostra separadamente. Aqui se separa as amostras novamente e soma as posições de cada grupo. Chamamos R1, R2... Rn a soma dos rankings de cada amostra.

### Passo 4: Define H calculado

A equação básica de H é

$$H = \frac{12}{N(N+1)} (\sum{ \frac{R_i^2}{n_i} }) - 3(N+1)$$

Aonde

- N é o total de todas as amostras (somando todos os grupos)
- $R_i$ é a soma dos rankings da amostra i
- $n_i$ é o tamanho da amostra i

Essa divisão da soma dos rankings de cada grupo pelo tamanho do grupo que garante que podemos comparar grupos de tamanhos diferentes.

Caso haja algum empate é preciso fazer uma pequena correção no cálculo de H, com a seguinte equação:

correcao = $1 - \frac{ \sum{t_i^3 - t_i} }{N^3 - N}$

Aonde t é a quantidade de valores empatados que teve. O somatório é para caso haja vários empates. 

Exemplo: 2 valores 123 e 4 valores 140. O somatório repetirá 2 vezes, a primeira com t=2 e a segunda com t=4.

Por fim o H corrigido será

$H_c = \frac{H}{correcao}$

### Passo 5: Tabela Qui-Quadrado

O valor de H segue a distribuição Qui-Quadrado, sendo então usada sua tabela. H é o qui-quadrado calculado e deve ser comparado com o qui-quadrado tabelado (chamado de H tabelado para manter a mesma nomunclatura).

A tabela qui-quadrado usa o alfa e os graus de liberdade para encontrar o valor. Os **graus de liberdade serão o nº de grupos - 1**. Assim encontramos o H tabelado olhando na linha graus de liberdade (Nº grupos - 1) e coluna alfa.

Lembrando que H, seja calculado ou tabelado, são valores qui-quadrado relacionados a tabela.

`Se H calculado > X tabelado, rejeito H0`.

### Extra: Encontrar p-valor

Caso queira definir o p-valor, basta procurar na mesma linha dos graus de liberdade pelo seu valor calculado. O valor da coluna será seu p-valor. Caso ele seja menor que alfa, rejeita-se H0.

## EXEMPLO

Uma escola quer saber há variância entre as notas de acordo com a etnia, com 5% de alfa.

| | | | | | | | |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|Blacks | 1246 | 1148 | 1300 | 1404 | 1396 | 1450 | |
|Hispanics | 1267 | 1228 | 1450 | 1351 | 1280 | | |
|Whites | 1581 | 1649 | 9811 | 8771 | 629 | 1800 | 1423 |
|Asians | 1623 | 1550 | 1936 | 1800 | 1750 | | |

Ordenando e rankeando ficou assim

| Etnia | Nota | Ranking |
| :--   | :--  | :--     |
| White | 981  | 1       |
| Black | 1148 | 2       |
| Hisp  | 1228 | 3       |
| Black | 1246 | 4       |
| Hisp  | 1267 | 5       |
| Hisp  | 1280 | 6       |
| Black | 1300 | 7       |
| Hisp  | 1351 | 8       |
| Black | 1396 | 9       |
| Black | 1404 | 10      |
| White | 1423 | 11      |
| Black | 1450 | 12,5    |
| Hisp  | 1450 | 12,5    |
| Asian | 1550 | 14      |
| White | 1581 | 15      |
| Asian | 1623 | 16      |
| White | 1629 | 17      |
| White | 1649 | 18      |
| Asian | 1750 | 19      |
| White | 1800 | 20,5    |
| Asian | 1800 | 20,5    |
| White | 1877 | 22      |
| Asian | 1936 | 23      |

Repare que tivemos 2 repetições, uma no valor 1450, em que tivemos 2 valores iguais nas posições 12 e 13. Assim damos o valor 12,5 para os 2. Na outra repetição, 2 valores nas posições 20 e 21, os 2 com média 20,5. Repare que mesmo sendo de amostras diferentes fizemos a média, pois a amostra original é indiferente.

Os valores de cada grupo são

- Black: n = 6 e R = 44,5
- White: n = 7 e R = 104,5
- Hispanic: n = 5 e R = 34,5
- Asian: n = 5 e R = 92,5

Com N total = 23

A partir disso calculamos H

$H = \frac{12}{23(23+1)} (\frac{44,5^2}{6} + \frac{104,5^2}{7} + \frac{34,5^2}{5} + \frac{92,5^2}{5}) - 3(23+1) = 11.4647$

Porém tivemos repetições, então temos de corrigir H. Tivemos 2 repetições com 2 valores em cada.

correcao = $1 - \frac{2^3 - 2 + 2^3 - 2}{23^3 - 23} = 0.999$

$H = \frac{11.4647}{0.999} = 11.4762$

Temos 4 grupos, logo nossos graus de liberdade são 3. Olhando na tabela qui-quadrado alfa=0,05 e gl=3 encontramos H tabelado = 7,815. 

Como T calculado (11,4762) > T tabelado (7,815) então rejeito H0.

Caso queira saber p-valor, olho na mesma linha da tabela e procuro pelo valor mais próximo de 11,4762. No caso Encontro 11,345 para alfa = 0,01. Logo o p-valor será um pouco menor que 0,01