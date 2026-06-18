# MÉDIA MÓVEL

Média que muda ao longo do tempo, representando a **média dos valores em uma janela de tempo**. É o tipo de média usado em **séries temporais**.

Ela é útil para **identificar tendências em dados contínuos** que variam ao longo do tempo e **reduzir o ruído**. O fato de variar com o tempo faz com que sempre haja novos dados entrando e saindo, havendo descarte de dados antigos (que já estão muito distante e não influenciam no comportamento atual) e adição de dados recentes. Assim, **definir a janela de tempo significa definir por quanto tempo um dado é influente**. O normal é fazer várias janelas de tempo para uma análise completa. O tamanho da janela também depende do contexto e objetivo.

Ela não serve para descobrir o que causa a mudança no valor, só como ele varia ao longo do tempo e identificar tendências.

A unidade de tempo da janela é chamada de `período`.

### EXEMPLOS

- Ações (leitura de gráfico)
- Criptomoedas
- Epidemias (como visto na Covid)
- Economia
- Meteorologia

## OBJETIVOS

- Identificar tendências em dados contínuos
  - Faz isso analisando o sinal e a magnitude da média
- Reduzir ruído
  - Faz isso definindo a melhor janela de tempo

## TAMANHO DA JANELA

O tamanho varia de acordo com o contexto e objetivo. Entender seu contexto ajuda a encontrar o tempo mínimo que faz sentido para a análise e reduzir o ruído. 

Ex: é comum a pessoa não ir ao médico no final de semana, deixando para ir na segunda. Se considerar diário vai parecer que todo mundo fica doente segunda e saudável sábado, quando na verdade já estavam doente. Pegar uma janela de 7 dias corrige a subnotificação.

Ex2: o valor de uma ação é muito afetado por notícias, mas a notícia afeta por poucos dias e logo o preço volta ao normal. Fazer janelas diárias ou de horas te deixa sensível a essas flutuações aleatórias. Usar uma janela semanal corrige essa flutuação.

Ex3: é normal seus gastos serem maiores perto de quando recebe o salário. Aniversários e shows também podem causar picos momentâneos de gastos. Fazer uma janela mensal corrige essa distorsão.

Também é comum usar mais de uma janela de tempo para compreender melhor seus dados. Ter uma janela curta e uma longa pode mostrar a tendência de curto e longo prazo (tanto para ações como para doenças). Perceba que 2 janelas com medidas diferentes podem ser a mesma coisa (média móvel semanal e de 7 dias são a mesma coisa).

`Geralmente a literatura informará as janelas de tempo usadas no seu contexto`.

**Janelas maiores tendem a mudar mais devagar**, formando curvas mais suaves. Isso porque carrega o peso de dados antigos que puxam para o lado oposto da tendência atual. **Janelas menores podem oscilar bruscamente**.

**Janelas maiores representam tendências de longo prazo**. Janelas menores de curto prazo.

## DEFININDO VALOR DE CADA PERÍODO

Imaginando que o valor varia a cada minuto, fazer uma janela de X minutos é fácil, pois os valores tão dados. Mas como faremos a janela em horas ou dias?

A resposta depende do contexto. No mercado financeiro (ações e criptomoedas) o valor do período é o **valor do fechamento** dele (valor que ele tinha quando encerrou o período). Na área da saúde o valor do período é a **soma ou média do período**.

---

**Exemplo 1: uma ação teve seus valores 10, 11, 10, 12, 9, 9, 8 ao longo da semana. Ao fazer uma janela de tempo semanal, qual o valor a ser usado para representar essa semana?**

Usa o último valor, no caso: 8.

**Exemplo 2: uma cidade teve a seguinte quantidade de novos casos de Covid por dia: 12, 13, 11, 14, 10, 10, 9. Ao fazer uma janela de tempo semanal, qual o valor a ser usado para representar o nº de novos casos dessa semana?**

Usa a soma de todos os novos casos de Covid, pois é ela quem diz quantas pessoas pegaram a doença na semana. No caso: 79.

**Exemplo 3: uma cidade tinha a seguinte porcentagem de leitos de UTI ocupados por dia: 12, 13, 11, 14, 10, 10, 9. Ao fazer uma janela de tempo semanal, qual o valor a ser usado para representar essa semana?**

Usa a média de todos os dias, pois temos gente entrando e saindo da uti. No caso: 11,28

---

#### RESUMO

- Finanças: último valor da escala definida (último valor da hora ou do dia)
- Saúde: soma ou média dos valores daquela escala
  - Soma quando os valores só se acumulam (óbitos, novos casos)
  - Média quando o valor pode aumentar e diminuir

## MÉDIA MÓVEL ARITIMÉTICA (MMA)

Também chamada de média móvel simples. É a média aritimética dos períodos inclusos na janela.

### Quando usar

- Ver as médias reais dos períodos
- Analisar `períodos mais longos`
- Reduzir ruídos de períodos outliers

`É a melhor para cenários ligados a saúde ou análises financeiras de longo prazo`.

---

Exemplo: Valores de cada dia: 7, 8, 8, 7, 6, 8, 9. Janela de 7 dias. 

media = $\frac{7 + 8 + 8 + 7 + 6 + 8 + 9}{7} = 7,57$

No oitavo dia o valor é de 11. O 1º valor (mais antigo) sai da janela e o novo valor entra. A média muda para:

media = $\frac{8 + 8 + 7 + 6 + 8 + 9 + 11}{7} = 8,14$

No nono dia o valor é de 1. O valor mais antigo sai da janela e o novo valor entra. A média muda para:

media = $\frac{8 + 7 + 6 + 8 + 9 + 11 + 1}{7} = 7,14$

## MÉDIA MÓVEL EXPONENCIAL (MME)

Também conhecida como EMA. Dá mais importância para os dados mais recentes e diminui a influência dos dados antigos, no final da janela. Para isso usa uma fórmula que diminui o peso dos valores mais antigos. **Nos dá um valor mais próximo do valor atual por ser mais sensível a mudanças bruscas**.

`Focada nas mudanças recentes`.

### Quando usar

- Encontrar tendências mais rapidamente
- Analisar `períodos mais curtos`
- Quando quer que a linha da média fique mais colada dos valores reais

É amplamente usada em day e swing trade por responder rápido as mudanças do mercado. Por mudar mais rápido informa antecipadamente pontos de inflexão e cruzamento com preços e outras médias.

`É a melhor para cenários ligados a finanças`.

### Equação

O cálculo é iterativo, pois é preciso repetir a mesma equação para o dia anterior.

$$MME_{hoje} = \frac{2(valor_{hoje} - MME_{ontem})}{n+1}  + MME_{ontem}$$

Aonde

- n é o tamanho da janela (nº de períodos)

Ou podemos escrever como:

$$MME_i = \frac{2(x_i - MME_{i-1})}{n+1}  + MME_{i-1}$$

Para calcular a média mais antiga da janela, que não tem anterior, usa-se a média simples.

---

Exemplo: Uma janela de 4 períodos, com a sequência de valores 3, 6, 4, 5, 8, 7, 8.

Os dias que usaremos na janela são os 4 últimos (5, 8, 7 e 8).

Calcula a média móvel simples do dia 1 com uma janela de 4 períodos. Para isso precisa usar 3 valores fora da janela final que queremos. 

$MME_1 = MMS_1 = \frac{3 + 6 + 4 + 5}{4} = 4,5$

$MME_2 = \frac{2(8 - MME_1)}{4+1} + MME_1 = \frac{2(8 - 4,5)}{5}  + 4,5  = \frac{2(3,5)}{5} + 4,5 = \frac{7}{5} + 4,5 = 1,4 + 4,5 = 5,9$

$MME_3 = \frac{2(7 - MME_2)}{4+1} + MME_2 = \frac{2(7 - 5,9)}{5}  + 5,9  = \frac{2(1,1)}{5} + 5,9 = \frac{2,2}{5} + 5,9 = 0,44 + 5,9 = 6,34$

$MME_4 = \frac{2(8 - MME_3)}{4+1} + MME_3 = \frac{2(8 - 6,34)}{5} + 6,34 = \frac{2(1,66)}{5} + 6,34 = \frac{3,32}{5} + 6,34 = 0,664 + 6,34 = 7,004$

---

### Explicação da equação

Podemos chamar $\frac{2}{n+1}$ de k, nosso multiplicador. A equação então fica

$MME_i = (x_i - MME_{i-1})k  + MME_{i-1}$

Analisando o multiplicador vemos que quando a janela é unitária (n=1) k=1. Assim a média final fica valor atual - média anterior + média anterior = valor atual. Portanto a média exponencial é o próprio valor, pois não há nenhum outro valor na janela para alterá-lo. Quanto maior a janela, menor k, portanto menos o valor anterior vai afetar no cálculo.

Ex: imagine k muito pequeno como no caso $(10 - 4)0,01 + 4 = 6*0,01 + 4 = 4,06$. O multiplicador pequeno fez com que a mudança no valor da média fosse mínimo. Assim com janelas grandes a mudança é mais suave de um passo para o outro.

A ideia de fazer **(X - média)k + média** é para que todo o lado esquerdo vire só um passo, o quanto vou mudar a partir do ponto que estou agora (último valor da média). Isso faz que ela forme uma linha contínua suave, que não fica quebrando toda hora. K se torna o tamanho do passo. Por fim somamos o passo à posição atual para termos a posição futura.