# 6 SIGMA

`Ferramenta de análise de dados feita para avaliar se mudanças em um processo trouxe ou não melhorias`. Serve para mensurar mudanças em processos, sendo muito útil para gestores.

Ele é todo feito em cima de testes de hipóteses, então a chave do 6 sigma é saber definir hipóteses nula e alternativa e **saber exatamente o que você quer medir e testar**. Definir os objetivos e forma de coletar os dados para formas nossas amostras é parte do trabalho do gestor ao implantar o 6 Sigmas. Executar os testes de hipótese acaba sendo a parte mais fácil.

## TESTES

Os testes usados no 6 sigma são:

- Teste T
- Anova
- Levene
- Mediana de Mood
- Qui-Quadrado
- Regressão linear
- Correlação
- Regressão Logística

A tabela abaixo mostra quais testes usar a depender dos seus dados:

|  Tipo de dados      |Saída **contínua e normal**  |Saída **contínua e não normal**|Saída **discreta** |
|:--                  | :--                         | :--                           | :--               |
|Entrada **contínua** |regressão linear / correlação|regressão linear / correlação  |regressão logística|
|Entrada **discreta** |Teste T / Anova / Levene     |Mediana de Mood / Levene       | Qui-Quadrado      |


Também podemos listar qual teste usar e acordo com a necessidade:

- Comparar 2 médias entre si ou com valor fixo: Teste T
- Comparar 3 ou mais médias entre si: Anova
- Comparar 2 ou mais variâncias entre si: Levene 
- Comparar 2 ou mais medianas entre si: Medianas de Mood
- Ver como um fator muda o valor do outro: Regressão linear
- Ver como um fator muda o tipo do outro: Regressão logística
- Comparar a quantidade de 2 ou mais grupos: Qui-Quadrado
- Ver se existe relação entre 2 fatores categóricos: Qui-Quadrado

Apesar de não ser usado para o objetivo final, o teste de **Shapiro-Wilk** também é muito usados para testar as premissas dos testes usados.

### EXEMPLOS

- Ver se há diferença no número de falhas entre o turno da manhã e da noite: Qui-Quadrado
- Ver se o tipo de técnica usada aumenta o número de falhas: Teste T ou Anova
- Quais intervenções produzem melhores resultados: Anova

## HIPÓTESES

| Teste              | H0                                              | H1                                 |
| :--                | :--                                             | :--                                |
| Shapiro            | Dados são normais                               | Dados não normais                  |
| Teste-T (bicaudal) | $\mu_1 = \mu_2$                                 | $\mu_1 \ne \mu_2$                  |
| Teste-T (unicaudal)| $\mu_1 \le \mu_2$                               | $\mu_1 > \mu_2$                    |
| Anova              | $\mu_1 = \mu_2 = \mu_3 ... = \mu_n$             | Ao menos 1 é diferente             |
| Qui-Quadrado       | Q = 0                                           | Q $\ne$ 0                          |
| Levene             | $\sigma_1 = \sigma_2 = \sigma_3 ... = \sigma_n$ | Ao menos 1 é diferente             |
| Mediana de Mood    | mediana1 = mediana2 = ... = medianaN            | Ao menos 1 é diferente             |

## TAMANHO DO EFEITO

O tamanho do efeito de cada teste é:

- Teste T: D de Cohen
- Anova: eta-quadrado
- Levene: eta-quadrado
- Mediana de Mood: Comparação das medianas
- Qui-Quadrado: V de Cramér
- Regressão linear: coeficiente de determinação R²
- Regressão Logística: pseudo R² (McFadden)