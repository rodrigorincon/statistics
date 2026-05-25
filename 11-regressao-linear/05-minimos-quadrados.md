# MÍNIMOS QUADRADOS

Usa a correlação como base, pois calcula a correlação entre as vars independentes com a dependentes e das vars independentes com elas mesmas (variância). Ou seja, calcula a variância de todas as vars independentes e delas com a dependente.

## TERMOS COMUNS

Alguns trechos do cálculo recebem nomes para limpar a equação e facilitar o entendimento. A maioria deles está dentro da fórmula da correlação.

$S_{xx} = \sum{ (x_i - media_x)^2 }$ mede a variância de alguma var X (porém sem a divisão por N-1). Também chamado de soma dos quadrados de X.

$S_{yy} = \sum{ (y_i - media_y)^2 }$ mede a variância da var dependente Y (porém sem a divisão por N-1). Também chamado de soma dos quadrados de Y.

$S_{xy} = \sum{ (x_i - media_y)(y_i - media_y) }$ mede a variância entre as vars X e Y. Mede a dispersão dos pontos no gráfico. Também chamado de soma dos quadrados de X e Y.

## VARIAÇÕES

Existem deviersas variações desse algoritmo para quando não cumpre as premissas de normalidade ou homocedasticidade ou para muitas variáveis.

- Mínimos quadrados ordinais (OLS)
  - Padrão
- Mínimos quadrados ponderados (WLS)
  - Cada ponto tem um peso
  - Outliers tem peso próximo de 0, diminuindo sua influência no cálculo
  - Usado quando tem **heteroscedasticidade** (variância nos erros)
  - Uso ideal: quando **conhecemos previamente as incertezas** dos dados
  - Ex: medições feitas com instrumentos de diferentes precisões ou bases de dados com características diferentes, onde a incerteza de cada medição é previamente conhecida
- Mínimos quadrados Robustas (RLS)
  - Semelhante ao ponderado, porém dá os pesos dos pontos de forma iterativa
  - Iterativo: recalcula a reta toda vez que encontra um ponto muito discrepante
  - Usado quando tem outliers muito fora da curva
  - Usado quando não cumpre as premissas (**erros não normais ou heteroscedasticidade**)
  - Uso ideal: quando **não conhecemos previamente as incertezas** dos dados
  - Ex: dados possuem erros de medição, de digitação ou outros que distorçam gravemente
- Mínimos quadrados generalizados (GLS)
  - Usa uma matriz de covariância no lugar dos pesos
  - Generalização do ponderado, trocando pesos por uma matriz das covariâncias
  - Usado quando há **multicolinearidade ou heterocedasticidade** (variáveis X correlacionadas)
- Mínimos quadrados não lineares (NLS)
  - Quando os dados são **polinomiais**
  - Usa métodos numéricos iterativos (outros algoritmos) para convergir ao menor erro
  - Não será analisado aqui por fugir do escopo
- Mínimos quadrados parciais (PLS)
  - Quando tenho **mais variáveis do que dados** ou tenho **multicolinearidade**
  - Todos os outros exigem que a amostra seja maior que o número de variáveis, esse não
  - Reduz as vars, eliminando as correlacionadas, até ter um número aceitável

Importante: **não confundir o peso do ponto com o coeficiente A**. O peso multiplica o ponto, o coeficiente multiplica a variável X como um todo (e é definida considerando os pesos dos pontos).

## MÍNIMOS QUADRADOS ORDINAIS (OLS)

Para a equação y = ax + b, temos de definir A (coeficiente angular) e B (coeficiente linear).

$$A = r * \frac{desvio_y}{desvio_x}$$

Aonde r é o coeficiente de correlação.

$$B = media_y - A * media_x$$

Para calcular o coeficiente linear temos de calcular o angular.

Usando os termos comuns, podemos reescrever a fórmula de A como:

$A = r * \frac{ \sqrt{N * S_{yy}} }{ \sqrt{N * S_{yy}} } = r * \frac{ \sqrt{N} \sqrt{S_{yy}} }{ \sqrt{N} \sqrt{S_{yy}} } = r * \frac{ \sqrt{S_{yy}} }{ \sqrt{S_{yy}} }$

Como $r = \frac{ S_{xy} }{ \sqrt{ S_{xx} * S_{yy} }}$ podemos juntar tudo:

$A = \frac{ S_{xy} }{ \sqrt{S_{xx}} * \sqrt{S_{yy}} }$

### PROVA

A equação real de A é 

$A = \frac{n\sum{x_i y_i} - \sum{x_i} * \sum{y_i}}{n\sum{(x_i^2)} - (\sum{x_i})^2}$

A equação da covariância é

$cov = \sum{(x_i - media_x)(y_i - media_y)}$, multiplicando fica

$cov = \sum{ x_i y_i - x_i*media_y - y_i*media_x + media_x*media_y }$, separamos em somatórios diferentes

$cov = \sum{x_i y_i} - \sum{x_i*media_y} - \sum{y_i*media_x} + media_x*media_y$, trocando as médias por suas fórmulas fica

$cov = \sum{x_i y_i} - \sum{x_i * \frac{\sum{y_i}}{n}} - \sum{y_i * \frac{\sum{x_i}}{n}} + \frac{\sum{x_i}}{n}*\frac{\sum{y_i}}{n}$, simplificando

$cov = \sum{x_i y_i} - \frac{\sum{x_i y_i}}{n} - \frac{\sum{y_i x_i}}{n} + \frac{\sum{x_i}}{n}*\frac{\sum{y_i}}{n}$, multiplicando tudo por N fica

$N*cov = n\sum{x_i y_i} - \sum{x_i y_i} - \sum{y_i x_i} + \sum{x_i} * \sum{y_i}$, a multiplicação de 2 somatórios é igual ao somatório das multiplicações, então

$N*cov = n\sum{x_i y_i} - 2\sum{x_i y_i} + \sum{x_i y_i} = n\sum{x_i y_i} - \sum{x_i y_i}$, voltado ao formato anteior,

$N*cov = n\sum{x_i y_i} - \sum{x_i} \sum{y_i}$

Portanto o numerador é N*cov.

A correlação de Pearson é

$r = \frac{cov}{desvio_x *desvio_y} = \frac{cov}{\sqrt{\frac{\sum{(x_i-media_x)^2}}{N}} * \sqrt{\frac{\sum{(y_i-media_y)^2}}{N}}}$, unindo as 2 raízes fica

$r = \frac{cov}{ \sqrt{ \frac{\sum{(x_i-media_x)^2 * (y_i-media_y)^2}}{N^2} } } = \frac{cov}{ \frac{\sqrt{\sum{(x_i-media_x)^2 * (y_i-media_y)^2}}}{N} } = \frac{N*cov}{\sqrt{\sum{(x_i-media_x)^2 * (y_i-media_y)^2}}}$

Repare que a correlação de Pearson tem o mesmo numerador que A. Falta provar que o denominador da correlação é próximo do denominador de A. Para isso vamos fazer o caminho inverso, indo do final ao início

$A = r * \frac{desvio_y}{desvio_x} = \frac{N*cov}{ \sqrt{\sum{(x-media_x)^2}} * \sqrt{\sum{(y-media_y)^2}}} * \frac{\sqrt{ \frac{\sum{(y-media_y)^2}}{N} }}{ \sqrt{ \frac{\sum{(x-media_x)^2}}{N} } }$

Retiramos N de dentro da raíz e juntamos as frações

$A = \frac{ N*cov*\frac{ \sqrt{\sum{(y-media_y)^2}} }{\sqrt{N}} }{ \sqrt{\sum{(x-media_x)^2}} * \sqrt{\sum{(y-media_y)^2}} * \frac{ \sqrt{ \sum{(x-media_x)^2} } }{ \sqrt{N} } } = \frac{ \frac{N*cov*\sqrt{\sum{(y-media_y)^2}}}{\sqrt{N}} }{ \frac{ \sqrt{\sum{(x-media_x)^2}}*\sqrt{\sum{(y-media_y)^2}}*\sqrt{\sum{(x-media_x)^2}} }{\sqrt{N}} }$

Cortamos os $\sqrt{N}$ fica

$A = \frac{N*cov*\sqrt{\sum{(y-media_y)^2}}}{\sqrt{\sum{(x-media_x)^2}}*\sqrt{\sum{(y-media_y)^2}}*\sqrt{\sum{(x-media_x)^2}}}$

Dá pra cortar a raiz do somatório de Y que é igual em cima e embaixo e no denominador temos duas raízes do somatório de X iguais, podendo elevar elas ao quadrado. Como elevaremos a raiz do somatório ao quadrado, ficará só o somatório.

$A = \frac{N*cov}{ \sum{(x-media_x)^2} } = \frac{N*cov}{ \sum{(x^2 - 2*x*media_x + media_x^2)} } = \frac{N*cov}{\sum{x^2} - 2*\sum{x*media_x} + media_x^2}$

Trocando média pela sua equação (somatório de x dividido por N):

$A = \frac{N*cov}{\sum{x^2} - 2\sum{x\frac{\sum{x}}{N} + (\frac{\sum{x}}{N} })^2} = \frac{N*cov}{ \sum{x^2} - \frac{2}{N}\sum{x\sum{x}} + \frac{(\sum{x})^2}{N^2} } = \frac{N*cov}{ \sum{x^2} - \frac{2}{N}(\sum{x})^2 + \frac{(\sum{x})^2}{N^2} }$

Multiplicando tudo no denominador por N temos

$A = \frac{N*cov}{N\sum{x^2} - 2(\sum{x})^2 + (\sum{x})^2} = \frac{N*cov}{N\sum{x^2} - (\sum{x})^2}$

Exatamente igual a equação encontrada na internet para A. Com isso provamos que A nada mais é que a correlação multiplicado pela divisão dos desvios de Y por X.

## MÍNIMOS QUADRADOS PONDERADOS (WLS)

A diferença nos ponderados é que cada ponto tem um peso, em que pontos com maior variância recebem peso menor. Quanto mais longe o ponto está da média, menor seu peso e menos ele influencia.

$S_{yy} = \sum{ w_i(y_i - media_y)^2 }$

Aonde

- w é o peso daquele ponto

O cálculo do ponto é feito a partir da matriz de covariância. O peso em si é o inverso do desvio padrão daquele ponto. Porém calcular o desvio padrão de um ponto que pega.

$w_i = \frac{1}{desvio_i}$

O desvio do ponto é calculado pela covariância na regressão simples e pela matriz de covariância na regressão múltipla.

$desvio_i = \sqrt{MC}$

Aonde MC é a matriz de covariância.

$MC = \begin{bmatrix} 
vari(x_1) & cov(x_1,x_2) & ... & cov(x_1,x_n) \\
cov(x_2,x_1) & vari(x_2) & ... & cov(x_2,x_n) \\
... & ... & ... & ... \\
cov(x_n,x_1) & cov(x_n,x_2) & ... & vari(x_n) \\
\end{bmatrix}$

Na matriz de covariância cada linha é a covariância de $x_1$ com todas as outras variáveis independentes, na linha 2 o mesmo com $x_2$ e assim por diante. A diagonal é a variância daquela variável. Importante lembrar que a **variância nada mais é que a covariância da variável por ela mesma**. Ou seja, todas as posições são covariâncias da variável daquela linha pela variável daquela coluna.

$vari(x) = \sum{(x_i - media_x)(x_i - media_x)}$

$cov(x, y) = \sum{(x_i - media_x)(y_i - media_y)}$

## MÍNIMOS QUADRADOS ROBUSTOS (RLS)

Aqui os pesos são definidos após fazer o mínimo quadrado ordinário. Usa-se o método padrão inicialmente e depois calcula os pesos através de uma função de perda (quanto maior o erro, maior a perda e menor o peso). Então é feito o mínimo quadrado ponderado usando os pesos calculados pela função de perda e recalcula os pesos para ver se houve uma melhora significativa.

Caso não haja uma melhora significativa, a função de perda é calculada novamente e recalculado os pesos. Esse ciclo é repetido até que os novos pesos e os antigos parem de mudar (encontre um platô).

Esse ciclo de recálculo dos pesos é o que faz o método ser iterativo, ficando em um loop até encontrar um platô ou estourar um limite predefinido de loops. Os pesos começam todos com 1 e vão sendo recalculados com base nos erros e enquanto os pesos antigos e novos continuarem mudando significativamente, o loop continua.

As funções de perda mais comuns são a função de Huber e a Bisquare de Tukey.

## MÍNIMOS QUADRADOS GENERALIZADOS (GLS)

Aqui, ao invés de calcularmos os pesos através dos erros, usamos uma matriz de covariância. Como a matriz de covariância usa o erro (distância do ponto à reta) acaba sendo parecido, mas o peso não é o inverso da raiz da matriz como no ponderado, mas a própria matriz de covariância. 

O cálculo para regressão múltipla é dado por:

$A_i = (XX^TC^T)^{-1} * X^TC^{-1}Y$

Aonde

- X é a matriz com todos os valores de todas as varáveis (adicionado a coluna 1 do intercepto)
- $X^T$ é a matriz transposta
- C é a matriz de covariância
- Y é a matriz dos valores Y

## ORDINAIS (BASE) COM REGRESSÃO MÚLTIPLA

### De onde vem as matrizes

Lembrando que a equação para 1 variável é

$y = A_0 + A_1X + erro$

Quando se tem mais de 1 variável precisamos calcular A1, A2, A3... $A_k$. Como temos K variáveis (e coeficientes a serem descobertos) e N medidas em cada variável teremos k equações semelhante a debaixo:

$Y_1 = A_0 + A_1X_{1,1} + A_2X_{2,1} ... + A_nX{n,1} + erro_1 = A_0 + \sum{A_iX_{1,i}} + erro_1$

Aonde o somatório soma todos os dados da variável $X_1$. 

Repare que **para encontrar cada Y eu preciso usar todos os coeficientes**. Isso também acontece na versão simples, aonde $y_1 = a_0 + a_1x$. Por ser o único y que tínhamos essa relação não era tão óbvia.

Essa equação não define o coeficiente, mas define como Y (que nós conhecemos) é definido por eles. Como temos k variáveis dessa, podemos organizar todas em uma única matriz.

$\begin{bmatrix} 
y_1 \\
y_2 \\
y_3 \\
... \\
y_k
\end{bmatrix} = \begin{bmatrix}
1 & x_{1,1} & x_{2,1} & ... & x_{n,1} \\
1 & x_{1,2} & x_{2,2} & ... & x_{n,2} \\
1 & x_{1,3} & x_{2,3} & ... & x_{n,3} \\
... & ... & ... & ... & ... \\
1 & x_{1,k} & x_{2,k} & ... & x_{k,k}
\end{bmatrix} * \begin{bmatrix}
A_0 \\
A_1 \\
A_2 \\
... \\
A_k
\end{bmatrix} + \begin{bmatrix}
erro_0 \\
erro_1 \\
erro_2 \\
... \\
erro_k \\
\end{bmatrix}
$

A matriz acima pode ser resumida na equação abaixo

$$Y = X * A + E$$

Aonde

- Y é a lista de todos os valores de y
- X é a matriz com todos os dados de todos os X
- A são os coeficientes que queremos definir (a1, a2, a3...)
- E são os nossos erros (resíduos)

O motivo da primeira coluna da matriz ser toda 1 é porque ela multiplica o coeficiente linear (A0). Como esse coeficiente não tem relação com nenhuma variável (e a matriz é a lista de todos os dados de todas as variáveis) então colocamos 1 para ela ficar sempre sozinha na equação.

A matriz é só uma forma mais organizada de resumir o sistema linear que temos, de k equações com k variáveis. Poderíamos fazer também no seguinte formato:

$Y_1 = A_0 + A_1X_{1,1} + A_2X_{2,1} ... + A_nX{n,1} + erro_1$

$Y_2 = A_0 + A_1X_{1,2} + A_2X_{2,2} ... + A_nX{n,2} + erro_2$

$Y_k = A_0 + A_1X_{1,k} + A_2X_{2,k} ... + A_nX{n,k} + erro_k$

Lembrando que as únicas variáveis que não sabemos os valores os os coeficientes A.

### Conceito dos mínimos quadrados

Em todas as vertentes dos mínimos quadrados o que buscamos é encontrar os coeficientes aonde o quadrado dos erros é o menor possível (por isso o nome). Em todas suas versões queremos elevar cada erro ao quadrado (variância) e somar todos eles.

Lembrando que isso nada mais é que a variância sem a divisão pelos graus de liberdade, pois o erro é a diferença entre o valor real e a média (ou valor esperado pela regressão). **A soma dos quadrados sempre pode ser entendido como a variância ou a dispersão dos dados**, seja a dispersão em volta da média ou em volta do valor esperado (reta da regressão).

Pensando nisso podemos isolar os k erros, elevar ao quadrado e somá-los conforme mostra abaixo.

$\sum{erro^2} = \sum_{i=1}^k {(Y_i - A_0 - \sum_{j=1}^n {A_j X_{i,j}})^2}$

É aqui que a versão matriz mostra seu valor, pois podemos trocar os somatórios pela matriz, pois a multiplicação de matrizes já é um somatório. Isolando o erro temos

$E = Y - X * A$

Elevando ao quadrado fica

$E * E^T = (Y - X * A) * (Y - X * A)^T$

Lembrando que em matrizes para elevar algo ao quadrado precisamos multiplicar a matriz pela sua versão transversal. Assim $E^2$ vira $E * E^T$. O mesmo vale para o outro lado da equação.

Fazendo a multiplicação fica

$E * E^T = YY^T - 2X^TYA + XX^TAA^T$


### Derivada para encontrar o mínimo

Até então temos a soma dos quadrados dos erros, mas não encontramos o valor mínimo deles. Falta o mínimo do mínimos quadrados. **Para encontrar o menor valor fazemos a derivada e igualamos a 0**. Como queremos encontrar os coeficientes A derivamos em relação a eles.

$\frac{\partial{E}}{\partial{A}} = -2X^TY + 2XX^TA = 0$

Isolando A temos

$$A = (XX^T)^{-1} * YX^T$$

Com essa equação conseguimos calcular todos os coeficientes da regressão.
