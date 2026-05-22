# MÍNIMOS QUADRADOS

Usa a correlação como base, pois calcula a correlação entre as vars independentes com a dependentes e das vars independentes com elas mesmas (variância). Ou seja, calcula a variância de todas as vars independentes e delas com a dependente.

## PARA REGRESSÃO LINEAR SIMPLES (1 VAR INDEPENDENTE)

Para a equação y = ax + b, temos de definir A (coeficiente angular) e B (coeficiente linear).

$$A = r * \frac{desvio_y}{desvio_x}$$

Aonde r é o coeficiente de correlação.

$$B = media_y - A * media_x$$

Para calcular o coeficiente linear temos de calcular o angular.

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

## MÍNIMOS QUADRADOS PONDERADOS

## MÍNIMOS QUADRADOS ROBUSTOS

## PARA REGRESSÃO LINEAR MÚLTIPLA (VÁRIAS VARS INDEPENDENTES)

