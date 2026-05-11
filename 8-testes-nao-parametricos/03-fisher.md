# TESTE DE FISHER

É uma versão **mais precisa** do teste Qui-Quadrado, porém só funciona em **amostras pequenas** e com 2 categorias. Por só servir em testes muito pequenos não é amplamente usado, pois tem limitações grandes. Porém sua alta precisão o torna muito bom quando temos poucos dados e poucas categorias, pois cada pequena variação causa grande diferença na resposta.

Como é **usado para comparar independência entre 2 vars**, cada uma com 2 categorias, forma uma tabela 2x2. Isso significa que a variável só pode ter 2 valores (sim/não, a favor/contra, venceu/perdeu), tornando isso uma **distribuição binomial**.

Ele é **mais conservador**, então é mais difícil de rejeitar H0 (os valores precisam ser muito discrepantes para rejeitar).

## QUANDO USAR

- Usado quando **não cumpre as premissas** do Qui-Quadrado
- Quando algum valor esperado for menor que 5
- Quando a amostra é pequena (< 20, mas esse número varia muito na bibliografia)
- Geralmente usado quando só tem 2 categorias (tabelas 2x2)

## HIPÓTESES

H0: Variáveis independentes (Não há associação entre elas).
- P(Categoria1 da Var1) = P(Categoria2 da Var1)

H1: Variáveis dependentes (Há associação significativa entre elas).
- Ao menos 1 categoria da var1 tem probabilidade diferentes

## EQUAÇÃO

Por se tratar de uma dsitribuição binomial, usa muito fatorial. Você pode entender da seguinte forma: dado N amostras, qual a chance de p sucessos (caírem numa determinada categoria)?

$$p = \frac{ \binom{totalLinha}{x} \binom{totalColuna}{totalLinha - x } }{ \binom{total}{totalLinha} }$$

Aonde

- x: é o valor na combinação que queremos analisar

Em outras palavras, está calculando a probabilidade dessas 2 categorias ter x pessoas dado que a categoria Linha tem tanto, a categoria Coluna tem outro tanto e o total de tudo é N.

Ou seja, podemos escrever como uma probabilidade condiciona, pois o valor da combinação depende dos totais das linhas e colunas.

$p_{ij} = P(O_{ij} = x | linha_i, linha_j, coluna_i, coluna_j )$

Podemos reescrever a equação dessa maneira

$$p(O_1 = x) = \frac{ linha1! * linha2! * coluna1! * coluna2! }{ x! * O_2! * O_3! * O_4! * n!}$$

Aonde $O_i$ são os valores das outras combinações.

O valor de uma posição depende dos valores nas outras posições.

OBS: essa equação parte do pressuposto que a probabilidade de linha1,coluna1 e linha2,coluna1 são as mesmas (a combinação das categorias da var 2 são as mesmas na var 1). Ou seja, **essa equação parte do pressuposto que as vars são independentes**, por isso H0 é que elas sejam independentes ($P_0 = P_1$). Encontrar valores muito diferentes do esperado significa que o pressuposto foi quebrado.

## TABELA

A tabela é a soma de todas as probabilidades iguais ou maiores (mais extremas) que ela. Então calculo a probabilidade para todas as combinações (dado que o totas das linhas e colunsa não mudam) e somo todas que forem igual ou maior que o valor que encontrei para a combinação que quero verificar.

**Caso a probabilidade da minha combinação seja maior que alfa, rejeito H0**. Ou seja, se P calculado > P tabelado, rejeito H0.

## EXEMPLO

Quero saber se a opinião sobre aborto é igual entre homens e mulheres. Uma das minhas vars é gênero (homem e mulher) e a outra é a opinião (a favor ou contra). Fiz a pesquisa tive essa tabela de valores observador.

|      | Homem | Mulher | Total |
| :--: | :--:  | :--:   | :-:   |
|Favor |  2    |  2     |   4   |
|Contra|  1    |  5     |   6   |
|Total |  3    |  7     |  10   |

Podemos resumir a tabela toda a homens a favor = 2 e mulheres a favor = 1 num total de 10. A pergunta que fica é qual a chance de encontrar essa combinação de homens e mulheres a favor em 10 pessoas? A partir disso determinar se essa diferença é significativa.

P(homem a favor = 0 | 3 votos a favor em 10, com 4 homens e 6 mulheres) = $\frac{ \binom{4}{0} \binom{6}{3} }{\binom{10}{3}} = 0,1667$

Isso é a combinação de em 4 homens 0 votarem a favor vezes a combinação de 6 mulheres 3 votaram a favor num total de 10 pessoas 3 votarem a favor.

P(homem a favor = 1 | 3 votos a favor em 10, com 4 homens e 6 mulheres) = $\frac{ \binom{4}{1} \binom{6}{2} }{\binom{10}{3}} = 0,5$

P(homem a favor = 2 | 3 votos a favor em 10, com 4 homens e 6 mulheres) = $\frac{ \binom{4}{2} \binom{6}{1} }{\binom{10}{3}} = 0,3$

P(homem a favor = 3 | 3 votos a favor em 10, com 4 homens e 6 mulheres) = $\frac{ \binom{4}{3} \binom{6}{0} }{\binom{10}{3}} = 0,033$

A soma desses valores para ter P(X>k) são nosso p tabelado.

|  k   | P(x=k) | P(x>k) |
| :--: | :--:   | :--:   |
|3     | 0,033  |  0,033 |
|2     | 0,3    |  0,333 |
|1     | 0,5    |  0,833 |
|0     | 0,1667 |  1     |


Com isso sei que a chance de encontrar essa combinação é de 30% e de encontrar valores iguais ou mais extremos ( P(x>k) ) é de 33,3%. 

Com um alfa de 5%, vejo que 0,33 > 0,05, portanto rejeito H0.