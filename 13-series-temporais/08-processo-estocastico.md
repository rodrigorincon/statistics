# PROCESSO GERADOR

Uma série temporal pode ser produzida a partir de um processo gerador. 

Um processo gerador é um mecanismo que cria valores ao longo do tempo. Todo processo gerador cria um valor a partir de alguma função ou algoritmo. A criação de números um após o outro cria uma série temporal, visto que existe uma ordem no tempo (um mais antigo que vem logo antes de um mais novo). 

Perceba que como um processo gerador pode ser qualquer coisa, **não há necessidade do valor anterior afetar o próximo**.

# PROCESSOS ESTOCÁSTICOS

O processo estacástico é um tipo de processo gerador, aonde os valores são definidos aleatoriamente dentro de uma faixa definida. 

```
Ex: uma série de valores aleatórios entre 0 e 1.

Ex2: uma série de valores aleatórios entre 5 e 8. 
```

Um processo estocástico descreve as mudanças em um sistema aonde as mudanças são aleatórias ou incertas ao longo do tempo. Em vez de seguir um único caminho previsível (determinístico), ele admite múltiplos resultados possíveis, mapeados através de probabilidades. Portanto para não ficar 100% aleatório definimos uma probabilidade para os valores (ou uma distribuição) para tentar prever para que lado os próximos valores vão ir.

Em resumo: processos estocásticos são **sistemas que mudam ao longo do tempo com um grau de aleatoriedade ou incerteza**.

Por ter essa aleatoriedade ele é perfeito para construir modelos de previsão, pois na sua própria natureza considera uma flutuação aleatória presente ao tentar prever valores futuros. Como todo modelo possui um erro envolvido, um processo estocástico já traz esse erro embutido naturalmente.

`Um processo gerador (estocástico ou não) gera uma série temporal, pois a cada loop ele gera um valor aleatório dentro de uma faixa definida.`

É **muito usado em IA e machine learning** quando queremos prever valores **naturalmente imprevisíveis** ou quando queremos que a **resposta final varie a cada uso**. Nesse último cado adicionamos uma pitada de impresibilidade, assim os valores nunca serão iguais mesmo que a base de treinamento seja.

## Imprevisibilidade

Essa imprevisibilidade é necessária quando se quer modelar comportamentos naturalmente variáveis, como comportamento humano, clima ou sociedade. 

```
Ex: mesmo fazendo o mesmo percurso pro trabalho todo dia a velocidade que boto no carro, o tempo de chegada e o local exato que troco de faixa nunca serão exatamente os mesmos. Há uma aleatoriedade no comportamento. Adicionar uma pequena flutuação aleatória torna o comportamento do modelo mais parecido e menos determinístico, que age sempre igual.
```

Essa aleatoriedade pode ser definida por uma probabilidade, dando maior chance para certos valores/comportamentos.

```
Ex: É mais provável eu andar na velocidade da via que há 20km/h.
```

Essa adição de imprevisibilidade não é só para tornar mais parecido com o mundo real, mas também dá liberdade ao modelo para encontrar novos caminhos e sair de platôs (como no gradiente descendente estocástico) e assim encontrar novas soluções. Ou seja, **um toque de aleatoriedade além de permitir saídas variadas (mas guiadas para um lado mais provável) também pode otimizar um algoritmo**.

## EXEMPLOS

- LLMs
- Modelos de séries temporais
- Métodos de Monte Carlo
- Simulações de risco
- Simulações climáticas
- Cadeias de Markov
- Aprendizado por reforço
  - Jogos, robótica e carros autônomos

## CONCEITOS BÁSICOS

Descrevendo com outras palavras, um processo estocástico é uma lista de valores aleatórios indexados por um índice/parâmetro (no caso, o tempo).

**1. Espaço de estados**

É a faixa de valores que os dados podem assumir (de 0 a 1, de 5 a 8, -infinito a +infinito...)

**2. Conjunto de índices**

É o parâmetro que ordena o processo (tempo). Mas devemos descrever a unidade de tempo (ex: minutos, horas, dias...). O parâmetro pode ainda ser algo mais ligado ao contexto, como um evento que dispara uma ação aleatória.

Exemplos:

- Rodadas de um jogo
- Recebimento de um sinal, requisição, corrente ou bit
- Disparo de um trigger
- Encontrar um cenário pré-estabelecido que exige um novo cálulo, ação ou mudança

Ou seja, pode ser qualquer coisa que **aconteça com frequência que dispare uma ação ou mudança do sistema**. Essa coisa **não precisa acontecer sempre no mesmo intervalo de tempo**.

## TIPOS DE PROCESSOS

O proceso estocástico pode ser classificado de acordo com como os valores antigos afetam os futuros.

### Martingale

A maior probabilidade para o próximo valor é o valor atual. Isso significa que o **valor esperado é igual ao valor atual**. A tendência é constante (uma linha reta, não sobe nem desce). 

**Isso só é possível quando a chance de acerto é de 50%.**

```
Ex: cara ou coroa. Você começa com 10 reais e aposta 1 real em cada lance. Como a chance de ganhar ou perder são iguais, a expectativa é que daqui N lances você ainda tenha 10 reais.
```

#### Estratégia de apostas Martingale

Você começa apostando 1 real, se perder dobra a aposta (2). Se perder de novo dobra novamente (4) e assim por diante. Quando ganhar recuperará todo o valor gasto + o valor da aposta inicial. Porém além de exigir um caixa gigantesco por crescer exponencialmente, se a chance de perda for levemente maio que 50% a chance de perder tudo é enorme, o que torna essa estratégia de altíssimo risco e **não recomendada**.

### Não usar em sistemas de soma zero!

```
Ex: comecei apostando 10. Gastei ao total 10. 

Errei.

Apostei 20. Gastei ao total 30.

Errei.

Apostei 40. Gastei ao total 70.

Acertei. Ganhei 80, o mesmo que gastei (70) + a aposta inicial (10)
```

#### Quando usar

- Jogos ou sistemas "justos", com 50% de chance de ganhar ou perder
- Movimento Browniano Padrão
  - Movimento de partículas
- Preço de ativos financeiros
- Preço de Ações Eficientes (Teoria do Mercado)

### Passeio Aleatório

Uma sucessão de passos em direções aleatórias. O próximo valor pode ser qualquer um, mudando de forma imprevisível. Porém isso não significa que todas as opções tem a mesma probabilidade. **Cada possibilidade pode ter probabilidades diferentes**. 

A variância tende a só crescer a cada novo valor, significando que os valores individuais são dispersos (aleatórios).

Se só houver 2 opções de caminho/mudança e as duas tiverem a mesma probabilidade, é igual a um **processo de Martingale**.

#### Quando usar

- Jogos ou sistemas com chances diferentes de 50% de chance de ganhar ou perder
- Movimento Browniano
- Comportamento humano e de sociedade
- Preço de ativos financeiros
- Preço de Ações Eficientes (Teoria do Mercado)
- Dispersão de populações

### Cadeias de Markov

O próximo valor depende apenas do valor atual, não importando o histórico anterior. Também chamado de "falta de memória". É diferente do Martingale pois o próximo valor não é igual ao atual, mas sim que apenas ele impacta e os anteriores são ignorados.

Possui um conjunto de estados que o sistema pode estar (Espaço de estados), o estado inicial (medição inicial) e uma matriz de transição que informa a probabilidade de mudar daquele estado para aquele outro. Importante ressaltar que a soma de todas probabilidades de saída de um estado devem ser 1 (pois só existem aqueles estados).

Podemos visualizar como um grafo ou máquina de estados, mas para calcular consideramos uma matriz.

#### Quando usar

- Meteorologia
- Prever próxima palavra
- Jogos por turno
- Tempo de espera de servidores, bancos e filas
- Page Rank
- Mapeamento genético

### Processo de Poisson

O próximo valor é medido a partir da distribuição de poisson. Usado quando o tempo entre cada dado é sempre o mesmo e o dado é uma contagem de acontecimentos nesse período e esses acontecimentos são aleatórios. 

