# TESTE BINOMIAL

Usado quando temos uma **var categórica com 2 categorias** (binária). Comparamos a **proporção da amostra com um valor definido**. É usado no teste de McNemar para valores pequenos.

Segue a distribuição Bernoulli: A probabilidade de uma das categorias é p e da outra 1-p. Mesmo que a variável original seja numérica e contínua,nós trabalharemos com uma categórica binária (Ex: quero saber quantas pessoas tem mais de 1,90 de altura. Altura é numérica, mas meu dado é categórico: tem ou não tem). 

Eu **não comparo 2 amostras**, só tenho 1 amostra e comparo com um valor definido.

## PREMISSAS

- Os dados devem ser independentes
- A variável só deve ter 2 categorias
- Amostra pequena

## HIPÓTESES

$H0: p = c$, onde c é o valor definido (entre 0 e 1). Lembrando que o sinal de comparação varia com o tipo de cauda que tô testando.

Também podemos escrever como

$H0: s \le s_{\alpha}$, onde s é a quantidade de sucessos na minha amostra e $s_{\alpha}$ é a quantidade de sucessos que dão a probabilidade alfa.

## COMO CALCULAR

$$pValor = \sum_{i=0}^s \binom{n}{i} p^i (1-p)^{n-i} = P(s \le x | p = c)$$

Caso H0 tenha o símbolo $\ge$ (teste unicaudal a esquerda). 

Se o símbolo for $\le$ (unicaudal a direita) então é

$$pValor = \sum_{i=s}^n \binom{n}{i} p^i (1-p)^{n-i} = P(s \ge x | p = c)$$

Se o teste for bicaudal calcula a cauda menor (o menor entre s ou n-s) e multiplica por 2.

Repare que o símbolo usado em H0 é inverso do usado no cálculo do p-valor, pois para o cálculo do p-valor costumamos usar o comparador de H1, que é quem queremos que seja verdade.

Aonde

- n é o tamanho da amostra
- p é a probabilidade da categoria que quero testar (sucesso)
- s é a quantidade encontrada na amostra da categoria que quero testar (quantidade de sucessos)

Com isso p-valor é a probabilidade caso Ho seja verdadeiro, pois está usando a probabilidade p que é a igualdade na hipótese. Repare que por partir do pressuposto que Ho é verdadeiro, se sua amostra cai dentro da cauda (região crítica) da equação eu confirmo Ho, caso contrário contradigo Ho (rejeito).  

Repare que $\binom{n}{s} p^s (1-p)^{n-s}$ é a probabilidade de encontrar exatamente s sucessos em n tentativas. O equivalente a $P(s = x | p = c)$. Mas não queremos a probabilidade só desse ponto, mas todas as probabilidade até esse ponto (o símbolo na nossa probabilidade condicional é $\le$). Por isso o somatório, para somar a probabilidade de 0 sucessos, 1 sucesso até S.

No caso de querermos saber a chance de ser maior temos de fazer o complemento, a soma de todas as probabilidade de encontrarmos valores maiores que S, por isso o somatório começa em S e vai até N.

## EXEMPLO

Quero verificar se o número de pessoas favoráveis a uma lei é maior que 60% com alfa = 5%. 

$H0: p \le 0.6$ e $H1: p > 0.6$

**1. Perguntei para 20 pessoas e tive 14 opiniões favoráveis.**

N=20, p=0.6, s=14. 14 é 70% da amostra, porém isso é estatisticamente significativo?

$pValor = \binom{20}{14} 0.6^14 (0.4)^6 = 0.124$

Isso significa que a chance de eu encontrar exatamente 14 sucessos em 20 é 0.124, porém a probabilidade de encontrar de 14 a 20 seria 0.25. Ou seja, temos 25% de H0 ser verdadeiro. Portanto p-valor > alfa, então **não rejeito H0**. Esse valor não é estatisticamente significativo.

Como meu alfa é 5%, o valor de s para dar 0.05 é pouco maior que 15. Só passaria se o valor fosse maior que 15 então.

**2. Perguntei para 20 pessoas e tive 17 opiniões favoráveis.**

N=20, p=0.6, s=17. 14 é 85% da amostra, porém isso é estatisticamente significativo?

$pValor = \sum_{i=17}^{20} \binom{20}{i} 0.6^i (0.4)^{20-i} = P(x=17 | p=0.6) + P(x=18 | p=0.6) + P(x=19 | p=0.6) + P(x=20 | p=0.6) = 0.016$

Isso significa que a chance de eu encontrar 17 ou mais sucessos em 20 é 0.016. Ou seja, temos 1.6% de H0 ser verdadeiro. Portanto p-valor < alfa, então **rejeito H0**. Esse valor é estatisticamente significativo.

