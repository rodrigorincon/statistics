# TESTE DO SINAL

Teste não paramétrico usado para testar dados ordinais (que podem ser numerados em sequência). Ele é usado quando não é possível quantificar a distância entre as categorias/posições (ex: qual a diferença entre bom e muito bom) ou quando a categoria é subjetiva (o que uma pessoa dá nota bom outra dá nota ótimo).

Exemplos:

- Posições (1º, 2º, 3º...)
- Ranking
- Pontuação (1 a 5 estrelas, de 0 a 10...)
- Categorias que podem ser ordenadas (ruim/bom/ótimo..., discordo totalmente/discoro em parte/concordo, menos de 5k, entre 5k e 10k, acima de 10k...)

## OBJETIVO

Medir se uma `amostra tem categorias significativamente maior que outra`. Por isso as **categorias tem de ser ordenáveis** (essa é "maior" que aquela). 

Feita para quando **não há definição exata do quanto uma categoria é "maior" que outra** (ex: "concordo totalmente" é quão maior que "concordo em partes") e para quando as **categorias são subjetivas** (ex: o que para um é bom, para outro é ótimo).

### Em Resumo

Usar quando: 

- Analisar o **antes e depois** dos mesmos usuários
- **Métrica principal é ordinal e não é possível calcular média e desvio padrão**

### Exemplos

- Um novo remédio para dor é mais eficiente?
- A nova receita de pizza é mais gostosa?
- O novo layout é mais intuitivo?

## PREMISSAS

- Dados ordenáveis
- Amostras pareadas (antes e depois)
- Os pares devem ser independentes

## HIPÓTESES

Ho: antes = depois (não houve mudança significativa)

Posso colocar no Ho ainda $\le$ ou $\ge$ a depender do que estou avaliando.

H1: antes $\ne$ depois ou antes < depois ou antes > depois (houve mudança significativa para tal lado)

---

Também é comum compararmos com uma **proporção p**, que é nossa **proporção esperada**, que acreditamos ser o que vai acontecer e fazemos o teste para confirmar.

Ho: C tabelado = p

Posso colocar no Ho ainda $\le$ ou $\ge$ a depender do que estou avaliando.

H1: C tabelado $\ne$ p

## COMO CALCULAR

### Passo 1: subtraia cada par e salve o sinal

$sinal_i = sinal(antes_i - depois_i)$ ou $sinal_i = sinal(x_i - y_i)$

O importante aqui não é o valor, apenas se foi positivo, negativo ou 0.

### Passo 2: elimine os zeros

Os pares que deu 0 (mesmo resultado antes e depois) são descartados, pois não houve diferença. Por fim seguiremos com um novo N (tamanho da amostra) sem os zeros.

$N_t = N - N_{zeros}$

### Passo 3: conte a quantidade de positivos e negativos

Isso nos dará **quantas pessoas deram votos maiores e quantos deram votos menores**. No fundo é só isso que o teste mede.

Guardo os valores de $N_{pos}$ e $N_{neg}$.

$N_pos = \sum{ 1, sinal_i > 0 }$ e $N_neg = \sum{ 1, sinal_i < 0 }$

### Passo 4: Cálculo de C

$$C = min(N_pos, N_min)$$

Esse será nosso C calculado que será usado para encontrar C tabelado.

### Passo 5: Tabela Binomial

Como só temos 2 possibilidades (valores positivos ou valores negativos) usamos a distribuição binomial e sua tabela para definir o C tabelado. A tabela binomial usa N (no caso, $N_t$), nosso C calculado e o p que é a proporção de positivos que esperamos.

A tablea binomial tem diversas tabelas, uma para cada N. Usamos a tabela do N do nosso $N_t$ e verificamos a linha do nosso C e a coluna do nosso p. O valor encontrado é nosso p_valor.

**Se C calculado < alfa, rejeito Ho**.

Caso a comparação de H0 seja =, usamos a bicaudal. Caso H1 seja >, usamos caudal a unicaudal a direita. Caso H1 seja <, usamos caudal a unicaudal a esquerda. Caso só possua a bicaudal e queira calcular a unicaudal, multiplique seu alfa por 2.

### Extra: Calculando resultado sem a tabela

Outra forma de responder sua hipótese sem usar a tabela e sem calcular o p-valor é comparando nossa proporção escolhida p com a proporção encontrada p+.

$$p+ = \frac{N_{pos}}{N_t}$$

Isso nos dá a proporção de votos que aumentaram. Com isso podemos comparar com o p que definimos como meta na hipótese e, **caso p+ cumpra H0, não a rejeitaremos**.

**Caso H0 seja uma igualdade** (H0: p = valor) então nosso **p+ deve ser dobrado**, pois se trata de um teste bicaudal.

## EXEMPLO

**1. Foi testado um novo remédio para dor de cabeça, aonde 10 pessoas tomaram o remédio antigo e o novo e para cada um deram uma nota de 1 a 5 de quanto melhorou. Queremos saber se o novo remédio é diferente do antigo com alfa = 5%.**

Se queremos saber se é diferente então nosso p é 0,5 (metade preferiu o antigo, metade o novo). Qualquer coisa diferente disso indica que houve preferência por um dos dois.

Ho: C tabelado = 0,5 H1: C tabelado $\ne$ 0,5

As notas dos pacientes foram:

| Antigo | Novo | Dif  | Sinal |
| :--:   | :--: | :--: | :--:  |
| 4      | 3    | -1   |  -    |
| 3      | 3    | 0    |       |
| 5      | 3    | -2   |  -    |
| 2      | 1    | -1   |  -    |
| 1      | 1    |  0   |       |
| 2      | 3    |  1   |  +    |
| 1      | 2    |  1   |  +    |
| 3      | 2    | -1   |  -    |
| 6      | 2    | -4   |  -    |
| 8      | 5    | -3   |  -    |

N original = 10, $N_t$ = 8, $N_{pos} = 2$, $N_{neg} = 6$

C = min(2,6) = 2. Olhamos na tabela unicaudal 8, linha 2 e coluna 0,5. Achamos o valor 0,1094. Porém a comparação feita é d eigualdade, portanto bicaudal. Portando dobramos o p-valor encontrado, assim p-valor = 0,2188.

Como C calculado (0,1094) é > que alfa (0,05), não rejeito H0.

Calculando p+

$p+ = \frac{2}{8} = 0,25$. Como estamos comparando igualdade, temos de dobrar p+ (teste bicaudal). Com isso p+ = 0,5 portanto igual ao nosso p estipulado em H0 (H0 -> p = 0,5). Com isso H0 é cumprido e não rejeitado.

---

**2. Uma pizzaria quer testar uma receita de massa nova. Chamou 20 pessoas para comer a massa antiga e a nova e dar pontos de 1 a 5. Queremos saber se a receita nova é preferida que a antiga com alfa 5%.**

Se queremos saber se é melhor então nosso p é 0,5 (mais da metade preferiu o novo).

Ho: C tabelado $\ge$ 0,5 H1: C tabelado < 0,5

As notas das pessoas foram:

|Cliente | Antigo | Novo | Dif  | Sinal | Cliente | Antigo | Novo | Dif  | Sinal | 
| :--:   | :--:   | :--: | :--: | :--:  | :--:    | :--:   | :--: | :--: | :--:  |
| 1      | 3      | 4    | -1   |  -    |   11    |  3     |  4    | -1  | -     |
| 2      | 3      | 2    | 1    |  +    |   12    |  4     |  5    | -1  | -     |
| 3      | 2      | 5    | -3   |  -    |   13    |  1     |  2    | -1  | -     |
| 4      | 4      | 4    | 0    |       |   14    |  3     |  3    | 0   |       |
| 5      | 2      | 5    |  -3  | -     |   15    |  5     |  3    | 2   | +     |
| 6      | 1      | 3    |  -2  |  -    |   16    |  3     |  4    | -1  | -     |
| 7      | 3      | 2    |  1   |  +    |   17    |  1     |  5    |  -4 | -     |
| 8      | 1      | 2    | -1   |  -    |   18    |  4     |  2    |   2 | +     |
| 9      | 2      | 4    | -2   |  -    |   19    |  3     |  4    | -1  | -     |
| 10     | 4      | 5    | -1   |  -    |   20    |  2     |  5    | -3  | -     |
 
N original = 20, $N_t$ = 18, $N_{pos} = 4$, $N_{neg} = 14$

C = min(4,14) = 4. Olhamos na tabela 18, linha 4 e coluna 0,5. Achamos o valor 0,0117.

Como C calculado (0,0117) é < que alfa (0,05), rejeito H0.

Calculando p+

$p+ = \frac{4}{18} = 0,222$. Como H0 é p $\ge$ 0,5 a hipótese não foi cumprida, portanto rejeitada.

## TAMANHO DO EFEITO

É calculado através do **R de Cohen**.