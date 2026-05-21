# O QUE É REGRESSÃO

- Fórmulas e técnicas para prever o valor de uma variável a partir da outra (ou outras)
- Elas precisam ser **correlacionadas**
- Usa a correlação entre elas pra prever isso
- Posso usar regressão com N variáveis, mas torna mais complexo a compreensão e saber o quanto cada uma influencia
- As variáveis precisam ser quantitativas (numéricas). Não funciona com categóricas
- Tenta criar uma equação que seja a mais próxima possível das medidas reais
  - Regressão linear descreve a correlação através de uma equação linear
  - Regressão logística classifica dados através da função sigmoide (logística)

`Regressão trata de prever o comportamento futuro a partir de correlação (dados passados)`

Importante que a regressão mede **tendência**, os valores reais podem não seguir perfeitamente a equação. Toda regressão tem uma margem de erro média. Por ser um erro médio, ainda posso ter outliers que saem muito longe da reta e ultrapassam essa margem.

## DIFERENÇA ENTRE CORRELAÇÃO E REGRESSÃO

- Correlação analisa os dados passados
- Regressão tenta prever o futuro (criando uma equação que melhor represente os dados)
- Correlação é a base para regressão
- Regressão é uma versão mais avançada e poderosa da correlação

## O QUE REGRESSÃO MEDE A MAIS

Além de **tudo que a correlação mede** (se são relacionadas, direção e força), a regressão também mede: 

- Quanto uma var muda se aumentarmos/diminuirmos outra
- Prever/estimar o valor final da variável para cada valor da outra
- Quais vars formam o melhor modelo (quais descrevem melhor o comportamento de Y)

### PONTOS DE ATENÇÃO

- A regressão não indica relação causa x efeito (correlação não é causalidade)
- A regressão não ajuda a encontrar variáveis ocultas 
 - As vezes há outras vars influenciando além das usadas ou mesmo uma que define o comportamento das suas

## NOMENCLATURA

- Var Independente (ou explicativa)
  - São o que causa mudança na var estudada
  - Podem ser várias
  - É o nosso X da equação
- Var Dependente (ou resposta)
  - É influenciada pelas demais variáveis
  - Só temos 1
  - É o nosso Y da equação

## PARA QUE SERVE

- Modelos de previsão
- Modelos de classificação
  - ex: uma compra é uma fraude dado o histórico desse cliente?
- Entender a relação entre variáveis

## TIPOS DE REGRESSÃO

1. **Regressão Linear Simples**

$y = a*x + b$

- Cria uma equação linear com apenas 1 var independente
- Só tem 1 único X

2. **Regressão Linear Múltipla**

$y = a_1*x_1 + a_2*x_2 ... + a_n*x_n + b$

- Cria uma equação linear com 2 ou mais vars independentes
- Simples com vários X
 
3. **Regressão Polinomial**

$y = a_1*x + a_2*x^2 + a_3*x^3 ... + a_n*x^n + b$

- Cria uma equação exponencial
- Tenta descobrir o coeficiente de cada expoente e quantos expoentes tem (se acaba no elevado a 3 ou no elevado a 10)
- Não envolve raiz quadrada, elevado a números fracionados ou negativoss
- Pode ter diversas variáveis independentes (X)
- É preciso ter uma amostra com no mínimo N dados (o máximo de expoentes que consegue definir é o tamanho da amostra)
- Fácil de causar overfitting quando tem alto grau (elevado a 3 ou mais)
- Árvores e decisão e Redes Neurais são mais eficientes que a regressão polinomial. Se a relação é muito complexa que precisa de vários polinômios, essas soluções de IA são mais precisas

Quando tem vários Xs a equação fica

$y = a_1*x_1 + a_2*x_2 + a_3*x_1^2 + a_4*x_2^2 ... + a_{2n-1}*x_1^n + a_{2n}*x_2^n + b$

4. **Regressão Logística**

$y = \frac{1}{1+ e^{-(a_1*x + a_2*x + a_3*x... + a_n*x + b)} }$

- Usada para **classificação**
- Pode ser usado com **variáveis categóricas**
- Resposta é uma probabilidade de um evento ocorrer dado as variáveis independentes
- Usa uma equação linear para calcular uma pontuação e então aplica a função sigmoide (ou logística) para transformar esse resultado em uma probabilidade
- Apesar do nome, essa regressão **não usa log e não tem relação com polinômios**

## COEFICIENTES

Uma regressão costuma ter um formato:

$y = b + \sum_{i=1}^n a_i*x^i$

Aonde

- X é a variável (ou variáveis) independente
- Y é a variável dependente
- A são os pesos de cada expoente. O quanto cada expoente influencia no valor final de y
  - Na linear (y = ax + b) A é o coeficiente angular (grau de inclinação da reta)
  - Como na linear só temos 1 peso (a do expoente 1), ele tem o nome especial, pois sua influência é muito mais nítida e decisiva
- B é o coeficiente linear (onde a reta corta o eixo Y ou o valor de Y quando x=0)

### DIFERENÇA ENTRE POPULAÇÃO E AMOSTRA

Equação para a população:

$y = b + \sum_{i=1}^n a_i*x^i + erro$

Ex: y = ax + b + erro

---

Equação para a amostra:

$ŷ = b + \sum_{i=1}^n a_i*x^i$

Ex: ŷ = ax + b

---

Quando falamos de população precisamos considerar o erro. Na amostra não precisa pois o y já é uma estimativa (ŷ significa y estimado).

## ERRO

`Erro (ou resíduo) é a diferença entre o valor real e o valor da reta/estimado (valor da regressão). Ele mede a distância de cada ponto verdadeiro da reta.`

Já que a regressão define a melhor reta que descreve os pontos, a que melhor se aproxima, ela não é perfeita. Impossível passar em cima de todos os pontos sendo uma reta. Assim, alguns pontos podem passar exatamente em cima da reta, mas a maioria vai passar próximo. A distância do ponto (dado real usado para criar a reta) da reta para o mesmo X é o erro ou resíduo.

**O objetivo da regressão é definir a reta com menor erro médio possível**. Ou seja, a **dispersão dos pontos em volta da reta** tem de ser a mínima possível. Isso significa ter a menor variância dos resíduos/erros.

e = real - previsto = y - ŷ

## INFERÊNCIA COM REGRESSÃO

Como estudamos, a inferência tem 2 técnicas, o intervalo de confiança e o teste de hipótese. Ambas funcionam como uma forma de testar se a correlação entre as variáveis é realmente significativa, mas medem coisas diferentes da correlação em si. Enquanto a correlação nos diz a força entre as variáveis, a inferência nos dá **uma faixa para essa relação e testa se essa relação é estatisticamente relevante**.

### INTERVALO DE CONFIANÇA

O intervalo nos diz quais os possíveis valores que o coeficiente A (que multiplica x) está. Também podemos medir se X é realmente significativo em Y ou não (se podemos desconsiderar a correlação entre eles). Para isso verificamos se o intervalo é todo positivo ou todo negativo. Caso seja então o valor de X é significativo na definição do valor de Y.

Isso acontece pois, caso haja um 0 dentro desse intervalo (uma ponta do intervalo seja negativa e a outra positiva) então há a chance de multiplicarmos X por 0, portanto não haver relação nenhuma entre eles.

### TESTE DE HIPÓTESE

O teste de hipótese em cima da regressão testa de A (que multiplica x) é significativamente diferente de 0. Pois se A=0 então x é cortado da equação e não afeta Y de nenhum modo. Ele **faz mais sentido em regressão múltipla ou um polinomial**.

Com regressão múltipla testamos (??)

Com regressão polinomial testamos (??)


### INTERVALO DE PREDIÇÃO

Essa nova técnica de inferência nos diz o intervalo de valores que Y pode ter para um determinado valor de X. Ele é como um intervalo de confiança para cada valor de X, pois nos diz o intervalo que Y pode estar com um nível de confiança.

Ex: em 95% das vezes Y vai estar nessa faixa para esse valor de X.

`O intervalo de confiança dá o intervalo para o coeficiente A, o intervalo de predição dá o intervalo para Y dado X = alguma coisa.`

Importante: Cada X terá um intervalo diferente, pois se X mudou o intervalo vai mudar junto. Porém o tamanho desse intervalo deve ser o mesmo (o intervalo não vai formar um cone, crescendo ou diminuindo). (???)

O intervalo de predição só é preciso em caso de homocedasticidade.