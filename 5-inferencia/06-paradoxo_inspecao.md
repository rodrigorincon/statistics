# Paradoxo da Inspeção

É um paradoxo que ocorre quando a **forma como amostramos** ou observamos um sistema **altera a probabilidade percebida** dos eventos, fazendo com que a **média observada seja maior do que a média real** da população.

Acontece principalmente quando observamos um processo em um ponto aleatório no tempo ou no espaço.

## Exemplos do paradoxo

### Espera no ponto de ônibus

- Se os ônibus passam a cada 10 minutos, a intuição diz que você esperará 5 minutos.
   - 3 ônibus passam a cada 20 minutos: um no minuto 0, outro no minuto 10 e outro no 20.
- Na prática, a espera costuma ser **maior que 5 minutos**.
- **Por quê?** Os atrasos criam intervalos irregulares.
   - Ex: um ônibus passa no minuto 0, outro no minuto 5 e outro no 20. Os mesmos 3 ônibus em 20 minutos.
   - Esses atrasos criam intervalos de 5 minutos e de 15 minutos, gerando esperas médias de 2,5 e 7,5 minutos. 
   - É muito mais provável você chegar durante a janela de 15 minutos do que na de 5 minutos.
- A média ponderada (quantidade de pessoas em cada grupo vezes tempo esperado do grupo) joga a média para mais próxima do valor com mais pessoas, **distorcendo para mais perto dos maiores valores**.
> - Essa puxada se deve por mais pessoas caírem no grupo que espera em média 7,5 minutos simplesmente por que a faixa de tempo é maior.

Como as pessoas chegam aleatoriamente na parada de ônibus e de forma independente do horário do ônibus o grupo 1 (que espera 15 minutos em média) é 3x maior que o grupo 2 (que espera 5 minutos em média) simplesmente porque tem 3x mais tempo para receber pessoas (e elas chegam de forma uniforme no tempo). Como o grupo é 3x maior ele puxa a média pro seu lado.

media ponderada = $\frac{3x * 7,5 + x * 2,5}{4x}$ = 6,25 minutos.

> Isso significa que as pessoas esperam em média 6,25 minutos. Maior que a média simples de 5. Isso vem por conta de atraso mas pode vir por qualquer fenômeno que cause um grupo maior que o outro.

### Tamanho das turmas na faculdade
- Uma faculdade tem 2 turmas, uma com 10 alunos e outra com 30.
- A faculdade diz: "O tamanho médio das turmas é de 20 alunos".
- O estudante reclama: "Minhas salas estão sempre cheias, com média de 30 alunos!".
- **Quem está mentindo?** Nenhum dos dois.
   - **Perspectiva da faculdade:** Média simples por turma (soma dos alunos por sala dividida pelo total de salas).
   - **Perspectiva do aluno:** Média ponderada. Salas maiores contêm mais alunos, logo mais pessoas "experimentam" estar em salas cheias.

> Aqui o ponto de vista muda o valor. É muito mais provável o aluno novo cair na turma cheia porque ela recebe mais gente. Logo a maioria dos alunos caem na turma cheia e sentem que as turmas são lotadas.

### Amigos nas redes sociais
- Em média, seus amigos têm mais amigos no Facebook/Instagram do que você (Paradoxo da Amizade).
- **Por quê?** Pessoas com muitos amigos aparecem em mais conexões do que pessoas com poucos amigos. Assim 1 pessoa muito sociável se repete diversas vezes gerando a impressão.

### Opinião política enviesada por redes sociais

- Um político A tem seus posts enviados a mil eleitores enquanto o político B tem seus posts enviados a 100.
- Como muito mais gente recebe propaganda de A, mais gente é mais convencida a votar nele simplesmente por quase não ver conteúdo do outro.
- Ao fazer uma pesquisa de intenção de voto o grupo que vota em A será maior que a média simples (50%) por uma distribuição desigual de propaganda.

## A Ideia Intuitiva

O paradoxo todo surge por conta do **viés da média ponerada** de puxar a média para o lado com mais dados. Ela arrasta a média para mais perto do grupo com mais números. Em casos reais os **grupos mais numerosos tendem a ser mais selecionados em amostras** enquanto grupos menores mal aparecem ou nem são selecionados, fazendo a média da amostra ser maior que a média da população (que desconhecemos). Isso nos leva a crer que assumir a média da amostra como a média da população é um erro se não levar outros pontos em consideração (proporção entre grupos, erro padrão, intervalo de confiança...). A **amostragem estratificada existe para resolver esse problema**.

### Pensando em tempo e entrada uniformes

- Intervalos **mais longos** ocupam mais tempo no calendário/linha do tempo.
- Por ocuparem mais tempo, a chance de você cair dentro de um intervalo longo é **maior** do que a de cair em um intervalo curto.
- Logo, sua amostra fica **enviesada para os intervalos maiores**.

### Pensando em grupos de tamanhos diferentes

- Grupos com tamanhos maiores (como as salas da faculdade) recebem mais pessoas que as pequenas.
- Uma nova pessoa tem mais chance de cair no grupo maior simplesmente porque ele recebe mais pessoas.
- Mais pessoas terão a experiência do grupo grande apenas por ele ser mais numeroso.

## O Teorema da Inspeção

Seja X a variável aleatória que representa o tamanho de um intervalo (ou duração) original, com média $E[X] = \mu$.

Quando inspecionamos o sistema em um instante aleatório, a variável observada Y (o tamanho do intervalo que "capturamos") não tem a mesma distribuição de X.

### 1. Ponderação pela Duração
A probabilidade de observar um intervalo de tamanho x é proporcional ao próprio tamanho x:

$$f_Y(x) = \frac{x \cdot f_X(x)}{E[X]}$$

Onde:
- $f_X(x)$ é a densidade original do intervalo.
- $f_Y(x)$ é a densidade do intervalo observado.
- $E[X]$ garante que a soma das probabilidades continue sendo $1$.

### 2. O Valor Esperado Observado
Calculando a média do intervalo observado $E[Y]$:

$$E[Y] = \sum x \cdot f_Y(x) = \sum x \cdot \left( \frac{x \cdot f_X(x)}{E[X]} \right) = \frac{E[X^2]}{E[X]}$$

Usando a fórmula da variância $\operatorname{Var}(X) = E[X^2] - (E[X])^2$:

$$E[X^2] = (E[X])^2 + \operatorname{Var}(X)$$

Substituindo na equação de $E[Y]$:

$$E[Y] = \frac{(E[X])^2 + \operatorname{Var}(X)}{E[X]} = E[X] + \frac{\operatorname{Var}(X)}{E[X]}$$

Ou seja, a média real E[Y] é a média simples E[X] + uma distorção causada pela ponderação ($\frac{\text{Var}(X)}{E[X]}$).

## Conclusões Fundamentais

1. **A média observada é sempre maior ou igual à média real:**
   $$E[Y] \ge E[X]$$
2. **O papel da Variância:**
   - Se a variância for zero (Var(X) = 0, ou seja, todos os intervalos são perfeitamente regulares), $E[Y] = E[X]$.
   - Quanto **mais desregular/variado** for o processo (maior Var(X)), **maior será o viés** da inspeção.

## Quando Ficar Atento ao Paradoxo

- **Análise de Dados / Data Science:** Ao coletar logs ou eventos por amostragem temporal aleatória.
- **Engenharia de Tráfego / Redes:** Ao medir tempo de resposta de pacotes de dados.
- **Pesquisas de Satisfação:** Entrevistar usuários em momentos aleatórios tende a **capturar clientes que passam mais tempo utilizando o serviço**.
- **Saúde Pública:** Pacientes infectados por doenças crônicas (longa duração) têm maior probabilidade de serem detectados em triagens aleatórias do que aqueles com doenças agudas (curta duração).

## Como Evitar o Viés da Inspeção

- **Amostragem Probabilística Correta:** Usar amostragem estratificada ou por conglomerado.
- **Ajuste Matemático:** Ponderar os dados coletados multiplicando os resultados pelo inverso do seu peso de seleção ($\frac{1}{x}$).