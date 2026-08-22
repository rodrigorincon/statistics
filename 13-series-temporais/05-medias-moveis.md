# MÉDIA MÓVEL

Média que muda ao longo do tempo, representando a **média dos valores em uma janela de tempo**. É o tipo de média usado em **séries temporais**.

Ela é útil para **identificar tendências em dados contínuos** que variam ao longo do tempo e **reduzir o ruído**. O fato de variar com o tempo faz com que sempre haja novos dados entrando e saindo, havendo descarte de dados antigos (que já estão muito distante e não influenciam no comportamento atual) e adição de dados recentes. Assim, **definir a janela de tempo significa definir por quanto tempo um dado é influente**. O normal é fazer várias janelas de tempo para uma análise completa. O tamanho da janela também depende do contexto e objetivo.

Ela não serve para descobrir o que causa a mudança no valor, só como ele varia ao longo do tempo e identificar tendências.

A unidade de tempo da janela é chamada de `período`.

## MÉDIAS MÓVEIS PARA PREVISÃO

Médias móveis é a média dos dados dentro da janela de observação (os últimos N dados). Podemos usar essas médias para prever os próximos valores quando temos autocorrelação (os valores passados influenciam os futuros) e são estacionários (valores variam ao redor de uma média e essa média muda junto com a tendência). É um método simples de previsão e que serve de base para modelos mais complexos (como ARIMA).

A média móvel trabalha a bem com tendências, e portanto a sazonalidade acaba atrapalhando. A série pode ter sazonalidade, pois podemos resolver esse problema aumentando a janela para caber todo o ciclo sazonal. EX: 12 meses para uma sazonalidade anual. Para tanto é preciso conhecer o ciclo da sazonalidade de antemão.

É amplamente usado no mercado financeiro para prever valor de ações e análise gráfica de ativos, sendo usado diaraimente para previsões nesse setor.

## PREMISSAS

As premissas são as mesmas do primeiro documento: os dados tem de ser igualmente espaçados e tem de estar ordenados. Os dados tem de ser autocorrelatos (os anteriores afetam os futuros), do contrário não faz sentido usar série temporal. Os dados não podem ter rupturas (pois isso zoaria sua média) e devem ser estacionários.

## TAMANHO DA JANELA

O tamanho varia de acordo com o contexto e objetivo. Entender seu contexto ajuda a encontrar o tempo mínimo que faz sentido para a análise e reduzir o ruído. 

Ex: é comum a pessoa não ir ao médico no final de semana, deixando para ir na segunda. Se considerar diário vai parecer que todo mundo fica doente segunda e saudável sábado, quando na verdade já estavam doente. Pegar uma janela de 7 dias corrige a subnotificação.

Ex2: o valor de uma ação é muito afetado por notícias, mas a notícia afeta por poucos dias e logo o preço volta ao normal. Fazer janelas diárias ou de horas te deixa sensível a essas flutuações aleatórias. Usar uma janela semanal corrige essa flutuação.

Ex3: é normal seus gastos serem maiores perto de quando recebe o salário. Aniversários e shows também podem causar picos momentâneos de gastos. Fazer uma janela mensal corrige essa distorsão.

Também é comum usar mais de uma janela de tempo para compreender melhor seus dados. Ter uma janela curta e uma longa pode mostrar a tendência de curto e longo prazo (tanto para ações como para doenças). Perceba que 2 janelas com medidas diferentes podem ser a mesma coisa (média móvel semanal e de 7 dias são a mesma coisa).

`Geralmente a literatura informará as janelas de tempo usadas no seu contexto`.

**Janelas maiores tendem a mudar mais devagar**, formando curvas mais suaves. Isso porque carrega o peso de dados antigos que puxam para o lado oposto da tendência atual. **Janelas menores podem oscilar bruscamente**.

**Janelas maiores representam tendências de longo prazo**. Janelas menores de curto prazo.

## MÉDIA MÓVEL SIMPLES (MMS ou MMA)

É a média aritimética dos k últimos dados. Funciona bem quando nao há tendência clara nem sazonalidade. A sazonalidade e uma tendência que muda rápido pode causar erros, pois a média pode não prever uma mudança de percurso de última hora. Pode ser usada em cenários de sazonalidade se o número de períodos usados for igual ao tempo para o padrão sazonal se repetir (como 12 dados mensais para captar a sazonalidade anual).

É conhecido pela sua sigla em português MMS e pela sigla em inglês MMA.

$$V_t = \frac{ \sum_{i=t-k}^{t-1} V_i }{k}$$

Que pode ser reescrito como:

$V_t = \frac{ V_{t-1} + V_{t-2} + ... + V_{t-k} }{k}$

Aonde:

- $V_t$ é o valor do momento atual (t)
- $V_{t-1}$ é o valor do momento anterior
- k é o tamanho da janela

Para prever vários valores consecutivos, usa-se os valores previstos até o momento desejado. Isso significa que teremos muito erro acumulado, pois a cada previsão teremos um erro e, ao usar esse valor previsto como base para prever o seguinte, esses erros se somam. Toda previsão a longo prazo tem esse problema, quanto mais distante do agora mais impreciso fica.

---

#### Exemplo

Dados = [120, 124, 122, 123]. Com uma janela = 4, Preveja os 5ºs e 6ºs valores.

k = 4

$V_5 = \frac{120 + 124 + 122 + 123}{4} = 122,25$

$V_6 = \frac{124 + 122 + 123 + 122,25}{4} = 122,8125$

## MÉDIA MÓVEL EXPONENCIAL (EMA)

A média móvel exponencial é uma média móvel ponderada aonde os pesos caem exponencialmente. Assim os dados mais próximos tem valores muito maiores que os do meio da janela. Ela te salva de ter de inventar pesos para cada valor, dando um peso automaticamente através de sua fórmula. É conhecido pela sua sigla em inglês EMA. Ela também sofre quando há sazonalidade.

Você só tem 1 parâmetro para definir, o fator de sauvização (k). O fator de suavização define quão rápido ou devagar os pesos caem. Geralmente k = 2/(n+1). Com essa fórmula k é sempre entre 0 e 1 (alcançando o valor máximo 1 quando n=2).

A EMA responde mais rapidamente as mudanças devido a dar peso maior para os últimos dados e menos para dados mais antigos. Assim ela reflete melhor o cenário atual, porém se a mudança recente for por conta de ruído ela sofre mais também.

$$EMA_{t} = V_{t-1} * k + EMA_{t-1} * (1-k)$$

Aonde:

- t é a posição do valor que queremos prever
- $EMA_t$ é o valor que que queremos prever. O mesmo que $V_t$ (que não existe ainda)
- k é o fator de suavização
- $EMA_{t-1}$ é o cálculo da EMA para o valor anterior

Importante ressaltar que somente $EMA_t$ e $V_t$ são iguais. $EMA_{t-1}$ e $V_{t-1}$ são valores muito diferentes. Isso ocorre porque os valores de t-1 pra trás já existem e o valor de t não, logo a EMA de t (sua previsão) será considerada seu próprio valor. $EMA_{t-1}$ é só uma representação de todos os valores anterioes já com seus pesos.

Com isso vemos que a EMA é recursiva, parando quando acaba a janela. O valor da EMA do primeiro valor da janela (o mais antigo) é apenas o próprio valor, sem multiplicar por K nem nada, por isso começamos pelo primeiro valor e vamos avançando rumo o presente. Podemos reescrever como:

$$EMA_{amanha} = V_{hoje} * k + EMA_{hoje} * (1-k)$$

E o critério de parada

$EMA_{1º} = V_{1º}$

### Outros tipos de suavização exponencial

A EMA usa a suavização como k = 2/(n+1), porém existem outras fórmulas de suavização exponencial. Uma dela é a de holt-winters e há mais outras. Tudo que elas fazem é mudar a fórmula de k, mas a equação da EMA se mantém a mesma.

---

#### Exemplo

Dados = [150, 70, 65]. Queremos prever o 4º valor. A janela é de 3.

k = 2/(n+1) = 2/(3+1) = 2/4 = 0.5

$EMA_1 = V_1 = 150$

$EMA_2 = V_2 * k + EMA_1 * (1 - k) = 70 * 0.5 + 150 * 0.5 = 110$

$EMA_3 = V_3 * k + EMA_2 * (1 - k) = 65 * 0.5 + 110 * 0.5 = 87.5$

**Logo a previsão para o 4º valor é 87,5.**

## QUANDO USAR CADA UMA

### Média SIMPLES

- Quando quero ver as médias reais dos períodos
- Quando quero reduzir ruídos
- Analisar `períodos mais longos`

`É a melhor para cenários ligados a saúde ou análises financeiras de longo prazo`. Na COVID os casos eram medidos todos com média simples.

### Média EXPONENCIAL

- Encontrar tendências mais rapidamente
- Quando quer que a linha da média fique mais colada dos valores reais
- Analisar `períodos mais curtos`

É amplamente usada em day e swing trade por responder rápido as mudanças do mercado. Por mudar mais rápido informa antecipadamente pontos de inflexão e cruzamento com preços e outras médias.

`É a melhor para cenários ligados a finanças`.

# MÉTRICAS

Para saber quão preciso é nosso modelo temos de comparar os dados previstos com os reais. Para tanto é usado diversas métricas diferentes. Abaixo cada uma é explicada como calcular, como e quando usar. Eles também servem para comparar 2 modelos e decidir qual o melhor (Ou o mesmo modelo com janelas diferentes).

## 1. Erro médio absoluto (MAE)

Mede `o quanto sua previsão erra`. É o mais simples de todos, mas ainda é muito valioso. Tira a média aritimética de todos os erros, ignorando os sinais (faz o absoluto deles, por isso o nome).

$$MAE = \frac{\sum |e_i| }{n}$$

Aonde

- $e_i$ é o erro de cada medida
- n é o total de previsões feitas

**A resposta dele é que, em média, sua previsão erra X unidades**. A desvantagem dele é que ele trata todos os erros igualmente, portanto **é muito sensível a outliers**. Quando se tem erros muito grandes e quer uma métrica menos sensível, usa-se o RMSE.

### USO

- Quando não tem outliers
- Todos os erros tem a mesma importância
- Quer comparar modelos com dados na mesma unidade
- Definir a melhor janela (lag)

## 2. Erro médio ao quadrado (MSE)

Mede `o quanto meus erros tem outliers`. É o MAE, mas ao invés de tirar o sinal, eleva ao quadrado. Isso faz com que seus valores sejam muito maiores que seus dados e não seja tão compreensível seu valor. Ainda assim, quanto menor, melhor. Ele explicita ainda mais os erros muito maiores que os demais, **tornando outliers mais visíveis**. Podemos considerar como a **variância dos erros**.

$$MSE = \frac{ \sum e_i^2 }{n}$$

### USO

- Visualizar outliers nos erros
- Quando tem outliers (mas ainda é preferível RMSE)

## 3. Raíz do erro médio ao quadrado (RMSE)

Mede `o quanto sua previsão erra TRATANDO OUTLIERS`. É a raíz do MSE. Se diferencia do MAE por trocar absoluto pelo quadrado, mas tira a raíz para voltar a um valor próximo ao dos dados e usando a mesma unidade deles. Podemos considerar como o **desvio padrão dos erros**. Quanto menor, melhor.

$$RMSE = \sqrt{\frac{ \sum e_i^2 }{n}}$$

A resposta dele é que, **em média, sua previsão erra X unidades com maior influência de erros grandes**. 

É sempre bom comparar o MAE e o RMSE para ver se tém outliers. **Caso MAE e RMSE sejam parecidos então os erros não tem outliers**. E ao comparar 2 modelos, se um tem o RMSE maior que o do outro significa que ele tem mais outliers nos erros. Dê preferência para modelos com RMSE menor.

### USO

- Quando tem outliers
- Quer comparar modelos com dados na mesma unidade
- Definir a melhor janela (lag)

### Exemplo

Ao comparar 2 modelos foi calculado o MAE e o RMSE de ambos.

- Modelo 1: MAE 5, RMSE 5,5
- Modelo 2: MAE 5, RMSE 9

Isso significa que apesar do erro médio ser o mesmo, o modelo 2 tem erros muito maiores. O modelo 1 é melhor.

## 4. Erro médio absoluto em porcentagem (MAPE)

Mede `em quantos porcento erramos`. Semelhante ao MAE, mas dá a porcentagem do erro ao invés de quantas unidades. Complementa a avaliação do MAE e do RMSE.

$$MAPE = \frac{\sum{ |\frac{e_i}{valorReal_i}| }}{n} $$

Aonde:

- n é o número de previsões
- Dividimos cada erro pelo valor real daquela previsão

A resposta dele é que o **erro médio é de aproximadamente X% do valor observado**.

### Observação

Muito cuidado com valores reais iguais ou próximos a zero, pois isso pode quebrar o código (divisão por 0 ou explodir o valor para o infinito).

### USO

- Quando os valores não forem próximos de 0
- Quando quero saber a porcentagem do erro
- Complementar a escolha da melhor janela (lag)

## 5. Erro padrão residual (EPR)

Seu cálculo é similar ao do desvio padrão: o erro é a subtração do esperado do real. Soma-se o quadrado dos erros, divide por K-1 e tira a raíz de tudo. A divisão é por N-k por ser os graus de liberdade.

$$erp = \sqrt{ \frac{ \sum{e^2} }{n-k} }$$

Aonde:

- e é o erro da previsão (previsto - real)
- n é o número de dados total
- k é o tamano da janela

Essa métrica nos dá `o quão disperso são nossos erros`. Quanto menor essa métrica, melhor. Ela só mede a dispersão dos erros/resíduos, por isso **NÃO É USADA EM PREVISÕES DE SÉRIES TEMPORAIS**, mas em outras áreas.

Ela é muito semelhante ao RMSE ($\sqrt{ \frac{\sum{e^2}}{n} }$), onde a única diferença é que o EPR divide pelos graus de liberdade e o RMSE divide por N simplesmente. Porém cada um tem usos diferentes.

### USO 

**regressões lineares e inferência estatística** para medir a dispersão dos erros/resíduos.

### Exemplo

Dados = [120, 124, 122, 123]. Com uma janela = 4, Foi previsto os 5º e 6º valores como 122,25 e 122,8125. Porém os valores reais foram 125 e 128. Calcule o erro residual.

k = janela = 4

$e_5 = 122,25 - 125 = -2,75$

$e_6 = 122,8125 - 128 = -5,1875$

$epr = \sqrt{ \frac{ (-2,75)^2 + (-5,1875)^2  }{6-4} } = 4,1516$

**Resposta: Nosso erro típico é de 4,1516.**

## TESTANDO PRECISÃO DAS PREVISÕES

Podemos medir se o modelo tem grandes outliers dividindo o RMSE pelo MAE. Essa razão nos dá a dispersão dos nossos erros e sempre irá de 1 a MAE * $\sqrt{n}$. Quanto menor menos outliers tem e menos disperso são os erros.

$disp = \frac{RMSE}{MAE}$

- Até 1.2 não existe outliers e a dispersão é pequena
  - Algumas literaturas dizem até 1.25
- De 1.2 até 1.5 há dispersão moderada, mas ainda tudo tranquilo
- **Acima de 1.5 há grandes outliers e seu modelo erra gravemente os valores**

Caso encontre um valor acima de 1.5 deve refazer seu modelo e procurar outra janela de tempo.

# EXEMPLO - COVID

Na pandemia de COVID os dados eram medidos com média móvel simples. A janela tinha 7 dias para analisar o crescimento de casos e de morte. Porém devido ao período de incubação do vírus a variação de casos e morte é comparada com o número de 14 dias atrás. Então a média móvel simples dos últimos 7 dias nos dava a tendência futura e a comparação da média móvel simples de hoje com a de 14 dias atrás nos dava a variação passada (se nessas últimas 2 semanas os casos estabilizaram, aumentaram ou diminuíram). 

Na comparação com a média de 14 dias atrás é considerado que os casos estabilizaram se ficar entre -15% e 15%. Acima disso o número de casos aumentou e abaixo o número diminuiu.

- Média móvel simples de **7 dias** = tendência (análise **futura**) 
- **Comparação** da média móvel simples de **hoje** com a de **14 dias atrás** = variação dos casos (análise do **passado**)
