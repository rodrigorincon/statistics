# TESTE DE FRIEDMAN

É a versão não paramétrica do teste **Anova de 1 via pareada** (dados dependentes). Fazemos quando **N coisas interagem com 3 ou mais categorias/amostras/variáveis**. O caso mais comum é comparar um antes, durante e depois.

Geralmente para esse teste temos uma tabela como a de baixo:

| Pessoa | Categoria 1 | Categoria 2 | Categoria 3 |
| :--:   | :--:        | :--:        | :--:        |
| A      |   1         |    2        | 3           |
| B      |   4         |    5        | 6           |
| C      |   7         |    8        | 9           |

### Exemplos

- Comparar a dispersão das notas de alunos em vários testes
- Comparar avaliação de vários sommeliers em vários vinhos
- Comparar o tempo de resposta de diferentes microsserviços ou funções do código

## PREMISSAS

- Os dados devem ser independentes
- Variável deve ser numérica ou ordinal (1º, 2º, 3º...)
- As categorias devem estar relacionados

## COMO CALCULA

### Passo 1: ordena e rankeia as categorias por linha

Ao invés de rankear todos os eventos da categoria, rankeamos as categorias para cada linha. Isso significa que vamos rankear para cada pessoa/evento quais categorias tiveram maior valor. A mesma categoria pode ter valores iguais, pois cada linha (pessoa/evento) são independentes.

Em caso de empate, rankeamos as posições com a média das posições empatadas (ex: se o 2º e 3º estão empatados, ambos recebem o ranking 2.5, média entre 2 e 3).

### Passo 2: soma os ranks de cada categoria

Somamos as posições/rankings de cada categoria (coluna). Enquanto no passo anterior o foco eram nas linhas, agora o foco é nas colunas. Com isso temos o **valor de cada categoria para essa amostra de dados**.

$R_i = \sum_{j=1}^n {rank_j}$

Aonde

- $R_i$ é a soma dos rankings para a categoria i
- n é a quantidade de dados de cada amostra (quantidade de linhas)
- $rank_j$ são os rankings nessa categoria

### Passo 3: calculo F

$$F = (\frac{12}{nk(k+1)} \sum_{i=1}^k {R_i^2}) - 3n(k+1)$$

Aonde

- n é a quantidade de dados de cada amostra (quantidade de linhas)
- k é a quantidade de categorias (colunas)
- R são as somas dos rankings de cada categoria

Caso haja empates é preciso fazer uma pequena alteração na equação para corrigi-lo. Nesse caso deve-se usar a versão abaixo.

$C_f = \frac{nk(k+1)^2}{4}$

$F = \frac{ n(k-1) ( \sum_{i=1}^k { \frac{R_ i^2}{n}} - C_f ) }{ \sum_{j=1}^n r_{ij}^2 - C_f }$

Aonde $r_{ij}$ é cada ranking existente.

Essa equação serve tanto para dados com ou sem empates, podendo ser usada em todos os casos.

O denominador é a soma de todos os rankings de todas as categorias. Não posso somar as somas de cata categoria ($R_i$) porque tenho de elevar cada ranking ao quadrado para só então somar.

OBS: No somatório do numerador apenas a parte $\frac{R_i^2}{n}$ está dentro dele e no somatório do denominador apenas o $r_{ij}^2$. Em suma, $C_f$ sempre está fora do somatório.

### Passo 4: Tabela Qui-Quadrado

O valor de F segue a distribuição Qui-Quadrado, sendo então usada sua tabela. F é o qui-quadrado calculado e deve ser comparado com o qui-quadrado tabelado (chamado de F tabelado para manter a mesma nomunclatura).

Se meu H0 é uma igualdade, uso a bicaudal, se H1 for > uso a unicaudal a direita e se H1 for < uso a unicaudal a esquerda.

A tabela Qui-Quadrado precisa do grau de liberdade e do alfa. O grau de liberdade será o número de categorias - 1 (k-1).

Se F calculado > F tabelado, então rejeito H0. Lembrando que a comparação muda de acordo com o sinal em H1.

### Extra, calcular p-valor

Para encontrar o p-valor, procuramos na tabela qui-quadrado nosso F calculado na linha do nosso grau de liberdade. O valor de alfa para essa linha será nosso p-valor.

Caso p-valor < alfa, rejeito H0.

## TAMANHO DO EFEITO

É calculado através da **correlação de Kendall**.