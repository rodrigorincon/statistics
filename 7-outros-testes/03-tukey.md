# TESTE DE TUKEY

Testa pares de grupos e informa se há diferença significativa entre eles. É usado após a Anova quando há diferença entre os grupos para encontrar quais grupos diferem entre si. Para tanto ele testa todos os grupos entre si.

Ele é considerado bom pois mantém a taxa de erro tipo I (falso positivo) controlada, mesmo quando se realizam múltiplas comparações. Ele é mais conservador do que outros testes post-hoc, como o teste de Bonferroni, o que significa que é menos propenso a detectar diferenças significativas quando elas não existem.

## PREMISSAS

- Dados devem seguir distribuição normal
- Variância homogênea entre os grupos (passar no teste de Levene)
- Os dados devem ser independentes
- Todos os grupos devem ter o mesmo tamanho

## COMO CALCULAR

Ele repete o 1º e 3º passos da Anova, pois precisa da variância dentro dos grupos (média dos erros).

### Passo 1: médias de cada grupo e total

- Calcular as médias e as variâncias de cada grupo
- Calcular a média total (juntando todos os grupos)

### Passo 2: calcular a variância dentro dos grupos

- Calcula o quanto cada grupo varia internamente (variância)
- Soma as variâncias de cada grupo, dando peso a cada um (o peso é o tamanho do grupo)
- Por ser a variância sem explicação é o nosso **erro ou resíduo**

$QMD = \frac{ \sum_{i=1}^k {(n_i-1)vari_i} }{N-k}$

Aonde

- k é o nº de grupos
- n é a quantidade de amostras em cada grupo (tamanho do grupo)
- $vari_i$ é a variância do grupo
- N é o tamanho da amostra total, somando todos os grupos

### Passo 3: Calcula o erro padrão entre os grupos

$erro = \sqrt{\frac{QMD}{n}}$

Aonde
- QMD é o erro/resíduo
- n é a quantidade de amostras em cada grupo (supondo que são iguais)

O erro reresenta variação esperada entre as médias dos grupos. A variação interna (erro) dá uma margem de confiança do quanto os grupos podem variar.

#### Tratando grupos de tamanhos diferentes

No passo anterior vimos que os tamanhos tem de ser iguais. Caso não seja n = média harmônica dos tamanhos dos grupos.

Usa-se média harmônica pois, com uma amostra total fixa, ao aumentar um grupo o outro precisa diminuir.

### Passo 4: calcular Q calculado

$$q = \frac{|media1 - media2|}{ erro }$$

Q = diferença entre os grupos dividido pelo erro, trazendo essa difrença pro contexto geral de todos os grupos. Teremos um Q para cada par. **Esse passo é repetido para cada par de grupos**.

### Passo 5: encontrar Q tabelado

O teste usa a distribuição Q (uma variação da T) para medir a como os dados se distribuem. Ela tem uma tabela que para ser lida precisa dos graus de liberdade do erro (N-k) e do número de grupos.

Pega-se a tabela referente ao alfa desejado (igual o teste F) e usa os graus de liberdade na linha e o nº de grupos na coluna. **Temos apenas 1 Q tabelado para todos os Q calculado**.

- Como temos 2 variáveis independentes (graus de liberdade e nº de grupos), não podemos ter 1 única tabela para todos os alfas
- A tabela fornece um valor genérico, pois usa apenas o nº de grupos e tamanho da amostra para achar Q. Não usa os dados reais
  - Os dados são usados no Q calculado que será comparado
- O tamanho da amostra e de grupos dão o ponto limite em que se cai na área alfa

### Passo 6: comparar os Q

Se **Q calculado > Q tabelado, a diferença é significativa (rejeita Ho)**. Deve-se fazer essa análise para cada par de grupos.

## O QUE É A TABELA Q

A tabela Q é uma variação da tabela T. Antigamente se usava a tabela T ao final da Anova, porém ela aumentava o erro tipo 1 por acumular os erros de cada comparação. Foi quando Tukey propôs uma alteração que eliminasse esse acúmulo.

O valor q nada mais é que a amplitude da amostra dividido pelo desvio padrão.

$q = \frac{amplitude}{desvio} = \frac{valorMaior - valorMenor}{ \sqrt{variancia} }$

No cálculo de Tukey só foi adaptado para trocar a amplitude pela média de 2 grupos ao invés do maior - menor (por isso precisa deixar absoluto). A divisão por N no denominador vem pelo Tukey não dividir exatamente pela variância, mas pelo erro padrão.

## Exemplo

Um agrônomo deseja comparar o rendimento de 3 formas de cultivar o milho (A, B e C). Ele fez 4 testes de cada forma, sob as mesmas condições de solo, irrigação e manejo. Após a colheita, o objetivo é verificar se há diferença significativa na produtividade média (em sacas por hectare) entre os métodos.

- Grupo A: 140, 135, 142, 138 (média 138,75)
- Grupo B: 125, 130, 127, 128 (média 127,5)
- Grupo C: 145, 150, 148, 149 (média 148)

Alfa = 5%. Todos as formas tiveram 4 testes (n=4). QMD = 4,5. Graus de liberdade = 12-3=9

$erro = \frac{4,5}{4} = 1,125$

Q tabelado (com alfa = 0,05, 3 grupos e 9 graus de liberdade) = 3,77

$A-B: \frac{|138,75 - 127,5|}{1,125} = \frac{11,25}{1,125} = 10$

$A-C: \frac{|138,75 - 148|}{1,125} = \frac{9,25}{1,125} = 8,22$

$B-C: \frac{|127,5 - 148|}{1,125} = \frac{20,5}{1,125} = 18,22$

Todos são maiores que o Q tabelado (3,77), logo todos são diferentes entre si.

# TESTE DE BONFERRONI

A única mudança está em como controla o erro tipo 1. Ele é **ainda mais rigoroso**, porém **só funciona bem com poucos grupos**.

**Só é usado quando precisa de um rigor extremo para falsos positivos.**

## COMO FUNCIONA

Enquanto Tukey mantem o alfa igual para todos os testes, Bonferroni **divide alfa pelo nº de comparações** e usa o resultado como o alfa para buscar na tabela. 

Isso diminui muito a chance de falsos positivos, mas aumenta o risco de não detectar diferenças reais (erro tipo II).

Por isso ele deve ser usado com poucos grupos, o nº de comparações cresce muito rápido, tornando o alfa minúsculo (e por consequência, o p-valor também) e quase impossível de dar um resultado significante.

$$alfa = \frac{alfa}{combinacoes}$$

$$combinacoes = \frac{k(k-1)}{2}$$

Ex: com 10 grupos temos 45 comparações, então dividimos o alfa (valor tabelado) por 45. Só então comparamos com o valor calculado.

## TABELA

Bonferroni usa a **tabela T**, diferente do Tukey. Para buscar na tabela T ele usa o novo alfa (após dividir pelo nº comparações) e os graus de liberdade do erro (N-k).

Para calcular o T usa o T para 2 médias independentes com variâncias próximas.

## Exemplo

Usaremos o mesmo exemplo do Tukey. Relembrando:

- Grupo A: 140, 135, 142, 138 (média 138,75, var=8,92)
- Grupo B: 125, 130, 127, 128 (média 127,5, var=4,33)
- Grupo C: 145, 150, 148, 149 (média 148, var=4,67)

Alfa Inicial = 5%. N=12, k=3, n=4. QMD = 4,5. 

Graus de liberdade = N - k = 12 - 3 = 9

**Calculando a parte nova**

combinacoes = $\frac{3(2)}{2} = 3$

$alfa = \frac{0,05}{3} = 0,017$

T tabelado (com alfa = 0,017 e 9 graus de liberdade) $\approx$ 2.4

$A-B: t = \frac{138,75 - 127,5}{ \sqrt{ \frac{8,92}{4} + \frac{4,33}{4} } } = \frac{11,25}{\sqrt{3,31}} = 6,18$

$A-C: t = \frac{148 - 138,75}{\sqrt{ \frac{8,92}{4} + \frac{4,67}{4} }} = \frac{9,25}{\sqrt{ 3.4 }} = 5,02$

$B-C: t = \frac{148 - 127,5}{\sqrt{ \frac{4,67}{4} + \frac{4,33}{4} }} = \frac{20,5}{\sqrt{2,25}} = 13,67$

Todos são maiores que o Q tabelado (2,4), logo todos são diferentes entre si.
