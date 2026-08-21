# AUTORREGRESSÃO

Autorregressão significa que um valor atual é relacionado aos seus valores passados, portanto podemos **prever valores futuros com base em seus próprios valores passados**. Ao usar um modelo que tem autorregressão assume-se que o dado atual **depende diretamente** dos dados anteriores. Ele também é chamado de AR.

A decisão mais importante em modelos AR é o tamanho da janela de pesquisa (quantos dados anteriores serão avaliados). Esse valor é chamado de p, portanto um modelo de autorregressão também é chamado de modelo AR(p). **O valor p é o tamanho da janela**, quantos valores antigos ele usa para prever o atual. Se ele depender só do último valor (p=1), então ele é chamado de ordem 1. Se depender dos 2 últimos de order 2 e assim por diante.

No AR `os valores devem depender UNICAMENTE dos valores imediatamente anteriores`, ou seja, **não pode ter sazonalidade nem tendência**. Por esse motivo ele é `perfeito para dados estacionários`. Portanto para usar autorregressão a primeira coisa a se fazer é um teste de hipótese ADF e/ou KPSS.

Modelos de autorregressão podem ser usados em dados sequenciais, mesmo que não haja nada relacionado a tempo. Pode ser usado, por exemplo, para calcular a probabilidade da próxima palavra dado as últimas palavras do texto. O tempo pode ser trocado por qualquer tipo de dado sequencial: texto, pixels de uma imagem, frames de um vídeo, localização em dados espaciais... Por essa razão é muito usado em IA generativa e em PLN (processamento de linguagem natural). Nesses casos, a rede neural usa a saída como uma das entradas para o próximo loop.

## COMO CALCULAR

A autorregressão, como o nome diz, é uma regressão, mais especificamente uma regressão linear múltipla. Ele tenta descobrir os pesos (coeficientes) para cada um dos p valores anteriores.

$$X_t = C + A_{t-1}X_{t-1} + A_{t-2}X_{t-2} + ... + A_{t-p}X_{t-p} + e_t$$

Ou simplesmente

$$X_t = C + e_t + \sum_{i=t-p}^{t-1} A_i X_i$$

Aonde:

- C é o intercepto
- $e_t$ é o erro aleatório (ruído) para essa variável
  - Cada variável tem seu próprio ruído
- p é o tamanho da janela
- $X_i$ é um dado anterior dentro da nossa janela de tamanho p
- $A_i$ é o peso de um dado anterior, que iremos calcular

O algoritmo usado dentro da regressão pode ser tanto mínimos quadrados (OLS) como máxima verossimilhança (MLE). Você pode rodar com os 2 métodos, cada um com diferentes tamanhos de janela e escolher o com a melhor métrica (menor AIC ou BIC).

## TAMANHO DA JANELA

O tamanho da janela (P), também chamado de defasagem ou lag, é o ponto crucial da autorregressão. Uma **janela pequena não nos permite descobrir o quanto é realmente influência real e o quanto é só aleatoriedade** (ruído). Esse problema nos faz querer evitar uma amostra muito pequena e buscar janelas maiores.

Porém **janelas muito grandes** torna o modelo **excessivamente complexo e demorado de calcular**, além de podermos estar adicionando complexidade desnecessária ao modelo. Além do crescimento exponencial de complexidade e processamento, também **perdemos padrões locais (de curto prazo)**, pois ao analisar janelas longas esse efeito temporário parece só ruído. Assim um fenômeno real e importante (e talvez até cíclico) é descartado como ruído por ser efêmero.

Além de esconder efeitos de curto prazo, janelas grandes suavizam as curvas, eliminando picos curtos. Isso pode ser bom por manter só o que é perene, mas também descarta padrões temporários verdadeiros (e possivelmente corriqueiros) que podem ser úteis. Aí ao tentar prever o próximo valor esses **efeitos de curto prazo descartados podem gerar uma previsão muito errada**.

Por isso é importante entender seu objetivo. O que você quer com esse modelo? É saber o valor exato do próximo ponto ou a tendência de longo prazo?

### AUTO CORRELAÇÃO

O tamanho ideal da janela pode ser encontrado através da autocorrelação. Ao medir a correlação entre o ponto atual e um ponto passado podemos definir o quanto ele é relevante para definir seu valor. Assim fazemos um ponto de corte aonde só fica dentro da janela pontos que tenha correlação forte com o ponto atual. 

Ao definirmos essa janela P com dados já conhecidos, mantemos a mesma janela para os dados futuros a serem previstos. 

A função de autocorrelação é chamada de ACF e queremos encontrar picos em seu gráfico. Quanto maior o ACF, maior o pico desse ponto no gráfico e maior será sua relevância.

## QUANDO EXISTE TENDÊNCIA

Como dito anteriormente, a **autorregressão funciona bem quando não há tendência**. Quando existe uma tendência a autorregressão sozinha não funciona, sendo preciso soluções que levem mais coisas em consideração. É aí que entra modelos como ARMA, ARIMA, VARIMA E SARIMA. Eles unem a autorregresão com médias móveis para analisar dados mais complexos.

- ARMA: funciona apenas com dados estácionários (média e variância fixas no tempo)
- ARIMA: transforma dados não estacionários em estacionários, então aplica o ARMA
- VARIMA: variação do ARIMA para dados multivariados (ARIMA Vetorial)
- SARIMA: variação do ARIMA para dados com forte sazonalidade