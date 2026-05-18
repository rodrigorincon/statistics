# TESTE DE POISSON

Testa se **x ou mais eventos acontecerem num período t é estatisticamente esperado**. Como a distribuição de Poisson mede o número de acontecimentos em um período de tempo, seu teste diz se essa quantidade de eventos é normal ou não, comparado com o alfa.

**Só serve para fazer contagem de valor inteiros**.

## PREMISSAS

- Os dados devem ser independentes
- A média deve ser próxima da variância
- A taxa média de ocorrência é constante durante o período

## HIPÓTESES

$H0: x = media$, ou seja, o nº de eventos medidos é estatisticamente igual a média esperada

$H0: x \ne media$, ou seja, o nº de eventos medidos é estatisticamente diferente da média esperada

Para tanto devemos definir uma média de eventos esperados e um intervalo de tempo.

## COMO CALCULAR

Usamos a distribuição de Poisson

$P(X=x) = \frac{e^{-media} * media^x}{x!}$

Aonde

- x é o nº de eventos da amostra
- média é a taxa média esperada em H0

Porém queremos calcular a probabilidade de todos os eventos iguais ou mais extremos que nossa média esperada. Para isso calculamos todas as probabilidades que não entram na região crítica e tiramos o complemento.

$$P(X > x) = 1 - \sum_{i=0}^x \frac{e^{-media} * media^i}{i!}$$

**A probabilidade já é nosso p-valor**.

## EXEMPLO

1. Normalmente em um dia temos só 3 requisição ao servidor que passa dos 10 segundos. Está dentro do eperado termos 5 requisições que passem dos 10 segundos em um dia? Meu alfa é 5%.

H0: x $\ge$ media, a diferença é significativamente maior que o esperado

H1: x < media, a diferença é significativamente maior que o esperado

media = 3, x = 5

p-valor = $1 - \sum_{i=0}^5 \frac{e^{-3} * 3^i}{i!} = 1 - \frac{e^{-3} * 3^0}{0!} - \frac{e^{-3} * 3^1}{1!} - \frac{e^{-3} * 3^2}{2!} - \frac{e^{-3} * 3^3}{3!} - \frac{e^{-3} * 3^4}{4!} - \frac{e^{-3} * 3^5}{5!} = 0.084$

Como p-valor > alfa, então não rejeito Ho, está dentro do esperado.

---

2. E se tivermos 7 requisições que passem dos 10 segundos?

media = 3, x = 7

p-valor = $1 - \sum_{i=0}^5 \frac{e^{-3} * 3^i}{i!} = 0.012$

Como p-valor < alfa, então rejeito Ho, não está mais dentro do esperado.

---

3. Qual meu valor crítico? Ou seja, para qual valor p-valor = alfa?

P(X > x) = alfa

Olhando na tabela Poisson na coluna média (lambda) = 3, procuramos o valor 0.95 (complemento do alfa) e encontramos que ele está entre as linhas x=5 e x6. Isso significa que 5 ainda não rejeita, mas 6 rejeita. Logo o menor valor de x que extrapola nosso valor esperado é 6.

# TESTE EXPONENCIAL

Testa se o **tempo médio entre os dados da amostra está dentro do esperado**. Como a distribuição exponencial calcula o tempo entre 2 eventos, o teste verifica se os dados da amostra tem um tempo médio dentro do esperado. Ela usa a tabela qui-quadrado.

## PREMISSAS

- Os dados devem ser independentes
- Os eventos que geram os dados devem ser independentes
- Os dados devem vir da mesma distribuição exponencial (com mesmos parâmetros)

## HIPÓTESES

H0: taxaEsperada = taxaCalculada

A taxaEsperada é o valo com que queremos comparar e a taxa calculada vem da equação do teste. Chamaremos taxaCalculada de taxa e taxa esperada de $taxa_0$.

## COMO CALCULAR

Cada dado da amostra deve ser o tempo entre 2 eventos. A equação é

$$taxa = 2 * taxa_0 * \sum_{i=1}^n x_i$$

Aonde

- O resultado é nossa taxa calculada
- $x_i$ é cada dado da amostra
- $taxa_0$ é a taxa esperada usada em H0

Ou seja, é o dobro da soma dos dados * taxa esperada.

Compare com o valor da tabela qui-quadrado para **grau de liberdade = 2n**. O valor da tabela será nossa taxa tabelada.

### Checando Hipótese via valor calculado

Para teste unicaudal:

Se taxaCalculada > taxa tabelada, rejeito H0.

Para teste bicaudal:

Uso metade do alfa na busca da tabela e rejeito H0 se taxaCalculada < taxa tabelada (usando alfa/2) ou taxaCalculada > taxa tabelada (usando -alfa/2).

### Checando Hipótese via p-valor

Para encontrar nosso p-valor usamos a tabela Qui-quadrado, buscando o valor da taxa calculada na linha do nosso grau de liberdade. O valor daquela coluna será nosso p-valor.

## EXEMPLO

Um elevador costuma quebrar a cada 100 horas de uso. Quero testar se um novo modelo tem taxa média menor, ou seja, se o tempo médio entre as quebras diminuiu. Meu alfa é 5%.

n = 30 elevadores testados

Tempo para os 30 quebrarem 1 vez = 2500 horas

$taxa_0$ = 1 falha a cada 100 horas = 1/100 = 0.01 falhas por hora

$q = 2 * 0.01 * 2500 = 50$

grau liberdade = 2*30 = 60

Olhando na tabela para gl=60 e alfa=0,05 encontro o valor 79,082. Como taxa calculada (50) < taxa tabelada (79,082) então não rejeito H0.

Calculando o p-valor, Procuro na tabela na linha 60 o valor 50. Ele é um pouco menor que 0,5, portanto maior que alfa, então não rejeito H0.