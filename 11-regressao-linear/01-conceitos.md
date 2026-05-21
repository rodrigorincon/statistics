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
