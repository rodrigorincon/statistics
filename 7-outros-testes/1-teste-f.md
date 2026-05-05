# TESTE F

É um teste que usa a distribuição F para comparar 2 variâncias e responder se elas são similares o suficiente pra serem consideradas iguais ou não. Ela nos responde se a dispersão entre 2 grupos (amostras, grupos distintos dentro da mesma amostra, antes/depois...) é parecida ou não.

O foco não é ver se as médias se parecem, mas se a dispersão (variância) é parecida. Isso ajuda a definir se 2 grupos podem ser comparados ou se as médias são comparáveis.

Ho costuma ser que as variâncias são iguais/similares. $H0: var1 = var2$.

## Passos

1. Calcular o tamanho e as variâncias dos grupos
2. Definir meu alfa (valor crítico)
3. Calcular o F tabelado
4. Calcular o F a partir das variâncias
5. Comparar os Fs

## Calcular F tabelado

Igual a distribuição F, define-se o alfa e  pega os graus de liberdade dos grupos. Geralmente o grau de liberdade é o tamanho do grupo - 1 (N-1), podendo ter pequenas mudanças dependendo do teste específico (Anova de 2 vias com interação faz pequenos ajustes). Com o alfa e os graus de liberdade, você usa a tabela de distribuição F.

O numerador (coluna) é o maior grau de liberdade (grupo maior) e o denominador (linha) é o menor grau de liberdade (grupo menor). O valor que você encontra na tabela é o F tabelado.

Reforçando: **o numerador é o grupo com maior grau de liberdade**.

O **F tabelado é o nosso limite aceitável**, até onde podemos ir sem quebrar a hipótese nula. Como ele é o valor de X aonde começa a área de alfa (por isso só usa o tamanho das amostras, não os dados), dele em diante estamos na área que rejeita H0.

## Calcular F a partir das variâncias

Após calcular as variâncias dos grupos, você pega a maior variância e divide pela menor variância. O resultado é o F calculado. Importante que a **maior variância deve ser o numerador**!

O **F calculado é o nosso F real**, representa nossos dados.

## Comparação dos Fs

Como F calculado é nosso F real e F tabelado é o nosso limite, queremos ver se o calculado ultrapassa o segundo (se ultrapassamos o limite aceitável).

O H0 costuma ser variancia1 = variancia2, porém H1 pode mudar (>, < ou $\neq$ ). Então usamos H1 para comparar os Fs. **Usamos a mesma comparação de H1 para comparar os Fs**.

Se $H1: var1 > var2$ então F calculado > F tabelado, rejeito H0.

Se $H1: var1 < var2$ então F calculado < F tabelado, rejeito H0.

Se $H1: var1 \neq var2$ então F calculado > F tabelado ou F calculado < F tabelado, rejeito H0.

# QUANDO USAR

- Teste Anova
- Regressões

# PREMISSAS

- os dados precisam seguir distribuição normal

# Comparação com teste de Levene

O teste de Levene funciona para qualquer tipo de dado, não precisando ser normal, porém se for normal o F é mais poderoso. Levene também permite comparar diversos grupos enquanto F só permite comparar 2.

Portanto **só compensa usar o teste F caso tenha certeza dos dados serem normais**. Para mais dados ou não normalidade é melhor usar Levene.