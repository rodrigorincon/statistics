# FUNÇÃO SIGMOIDE

A função sigmoide transforma as entradas X (que variam de -infinito a +infinito) para uma saída entre 0 e 1. Assim podemos medir a probabilidade de cada categoria de Y. 

Isso é possível fazendo o log da chance (probabilidade da categoria dividido por todo o resto). Com isso chegamos na equação para encontrar as probabilidades de cada categoria.

$$p(y_i) = \frac{1}{1 + e^{-y_i}}$$

Aonde $y_i$ é uma categoria da variável Y e representa uma regressão linear das vars X.

Ou seja, `para fazer a regressão logística preciso antes fazer a linear`.

Isso torna importante compreender alguns conceitos mais a fundo.

## RAZÃO DA CHANCE

Podemos reescrever essa mesma equação de forma linear (eliminando os expoentes e divisões) para facilitar nossa vida da seguinte forma:

$$log(p) = ln(\frac{p}{1-p}) = A_0 + A_1X_1 ... + A_nX_n$$

Por isso vemos tanto a frase que deve ter uma relação linear entre as variáveis independentes X e o log da razão de chances de Y. **É exatamente isso que está escrito nessa equação.**

A prova disso foi dada no arquivo anterior quando explico a diferença entre probabilidade e chance, mas aqui passarei pelos pontos principais.

- A probabilidade é encontrada pela razão das chances, pois a chance é a forma de transformar variáveis que variam ao infinito em respostas de 0 a 1.
- A razão das chances é a divisão da probabilidade do evento pelo probabilidade dele não acontecer
- Usar o log na probabilidade remove as divisões e exponenciais, transformando tudo numa equação linear

Com isso concluímos porque as vars X precisam ter essa relação linear com o log da razão das chances, pois é a única forma de conseguirmos validar que essa equação é possível. **Podemos validar isso vendo se os pontos seguem o formato de signmoide e pelo teste Box-Tidwell**.

Em resumo, `essa frase complicada só está dizendo que os dados precisam seguir o formato sigmóide para a regressão ser válida`.

## COEFICIENTES

**Aviso**: Ciência de dados e IA não busca interpretar os coeficientes, pois para eles não importa esses dados, apenas a probabilidade final (ser capaz de fazer previsões).

---

Os coeficientes não são tão claramente interpretáveis, pois eles influenciam de forma exponencial a probabilidade. A interpretação é que, a cada $C$ unidades alteradas na var $X_i$ a **chance** (não a probabilidade) é alterada em $(e^{C * A_i} - 1)$%. Esse valor é chamado de **razão de chance (odd ratio)** e pode ser encontrado nas ferramentas.

$$alteracao(C) = (e^{C * A_i} - 1)\%$$

A escala da variável é crucial para definir o tamanho do coeficiente. Se a escala é curta (os valores ficam todos num espaço curto, como de 0 a 3) o coeficiente é muito grande. Isso acontece porque uma mudança de 1 unidade representa uma mudança de patamar e é um crescimento muito mais expressivo. 

Por outro lado uma variável que pode variar de 0 a 100 terá um coeficiente pequeno. Aumentar o valor em 1 não significa uma mudança considerável no valor como no exemplo anterior. Isso se reflete no valor do coeficiente.

Repare que para a regressão saber a amplitude que seus valores podem ter eles tem de estar presentes na amostra. **Se sua amostra é enviesada e só tem valores numa pequena faixa a regressão achará que essa é a faixa possível inteira**.

## MÁXIMA VEROSSIMILHANÇA

A regressão linear usada dentro da logística não usa os mínimos quadrados para descobrir os coeficientes. Ao invés disso ele usa o **gradiente descendente**. O algoritmo iterativo do gradiente descendente definirá os coeficientes $A_i$ que melhor se encaixam nos dados, porém o algoritmo precisa de uma função de custo que calcula o quão longe os dados reais estão dos estimados.

Essa função de custo (que nos mínimos quadrados é a variância dos erros) aqui é a máxima verossimilhança. Como o gradiente descendente busca descer as montanhas (reduzir a diferença entre o medido e o real) ele acaba tornando os dados medidos mais próximos dos reais, o que também significa deixar os dados medidos mais verossímeis.

A verossimilhança é justamente medir quão bem os dados descrevem uma curva (ou quão bem eles se encaixam em uma distribuição). A máxima verossimilhança então é a combinação de dados que descreve perfeitamente uma distribuição. Por isso reduzir o erro leva à máxima verossimilhança, pois os dados reais e medidos ficam os mais próximos possíveis (ŷ descreve a distribuição real o melhor possível).

### CÁLCULO DA MÁXIMA VEROSSIMILHANÇA

#### Passo 1: probabilidade de cada dado ser classificado corretamente

A probabilidade de cada ponto ter sido classificada corretamente é de:

$P(ŷ_i = y_i) = p_i^{y_i} * (1 - p_i)^{1 - y_i}$

Repare que a equação acima é para uma regressão binária, aonde $y_i$ só pode ser 0 ou 1. Portanto o comportamento é igual a distribuição de Bernoulli, aonde ou $p_i$ ou $1 - p_i$ será elevado a 0 e o outro elevado a 1. 

Com isso a probabilidade de cada dado será ou a probabilidade dele mesmo (caso o dado esteja do lado certo) ou seu complemento (caso esteja do lado errado).

**Ex: um dado x1 foi classificado como falha (0) e com os parâmetros usados deu que ele é um sucesso (1) a resposta da probabilidade será $1 - p_1$.**

#### Passo 2: verossimilhança

O cálculo da verossimilhança será melhor explicado no próximo arquivo, mas adiantando ele é a multiplicação da probabilidade de cada dado ter sido classificado corretamente.

$L(\theta | dados) = \prod_{i=1}^n {P(ŷ_i = y_i)}$

Como temos muitas multiplicações, para otimizarmos processamento calculamos o log da verossimilhança para transformar multiplicação em soma. O motivo desse log não é por conta de prova matemática de algum conceito estatístico, é só para ganho de desempenho.

Trocar multiplicação por soma também evita underflow (números decimais extremamente próximos de zero que o computador não consegue armazenar).

#### Passo 3: log-verossimilhança

Com isso podemos simplificar toda a equação da máxima verossimilhança na equação abaixo.

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * ln(p_i) + (1 - y_i) * ln(1 - p_i) }$

Multiplicando o lado direito temos

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * ln(p_i) + ln(1 - p_i) - y_i * ln(1 - p_i) }$

Juntando o que tem $y_i$ fica

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (ln(p_i) - ln(1 - p_i)) + ln(1 - p_i) }$

Resolvendo a subtração de logs

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (ln(\frac{p_i}{1 - p_i})) + ln(1 - p_i) }$

#### Passo 4: logit

Como sabemos que o logit é o log de p/(1-p) e que ele é igual a equação da reta, podemos substituir na nossa equação.

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (logit(p_i)) + ln(1 - p_i) }$

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (a_0 + \sum{a_ix_i}) + ln(1 - p_i) }$

Trocando $p_i$ pelo valor medido na regressão $ŷ_i$

$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (a_0 + \sum{a_ix_i}) + ln(1 - ŷ) }$

#### Fórmula Final

Você pode encontrar a fórmula da máxima entropia nas 2 seguintes formas:

$$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * (a_0 + \sum{a_ix_i}) + ln(1 - ŷ) }$$

Ou

$$ln(L(\theta | dados)) = \sum_{i=1}^n {y_i * ln(ŷ_i) + (1 - y_i) * ln(1 - ŷ_i) }$$

### MÁXIMA VEROSSIMILHANÇA NA REGRESSÃO LOGÍSTICA

Como dito, a verossimilhança é nossa função de custo. Porém ela não vem sozinha, para usá-la precisamos fazer a média de todo esse somatório. O somatório é nossas entradas, então podemos dizer que nossa função de custo é a média da regressão logística das entradas.

$$fnCusto = \frac{ln(L(\theta | dados))}{n}$$

Aonde

- n é o tamanho da amostra (quantidade de entradas)