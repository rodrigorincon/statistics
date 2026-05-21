# COMO FAZER REGRESSÃO

## MÉTODOS DE CALCULAR

Existem 1 método principal e alguns mais específicos para casos especiais. Todos com a mesma base: coeficiente de correlação. O método principal, as vezes até confundido com a própria regressão linear é os **mínimos quadrados**. Ele é usado em todos os exemplos de regressão linear sem distinção de onde termina a regressão em si e começa os mínimos quadrados. Os métodos mais comuns são:

- Minimos quadrados (OLS)
  - Principal
- Mínimos quadrados ponderados (WLS)
  - Variação do original aonde cada ponto tem um peso
  - Dá peso a outliers, diminuindo sua influência no cálculo
  - Ótimo quando tem heteroscedasticidade (variância nos erros)
- Gradiente descendente 
  - Usado quando tem muitos dados e muitas variáveis
  - Ideal para big data e treinamento em tempo real
  - Variações:
    - Em Lote (Batch)
    - Estocástico (SGD) 
    - Em Mini-Lotes
- Regularização
  - Usado quando as variáveis independentes são muito correlacionadas entre si 
  - Evita overfitting
  - Variações:
    - Ridge (L2)
    - Lasso (L1)
    - Elastic Net (combinação dos 2)

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

O teste de hipótese em cima da regressão (linear e polinomial) testa de A (que multiplica x) é significativamente diferente de 0. Pois se A=0 então x é cortado da equação e não afeta Y de nenhum modo. Ele **faz mais sentido em regressão múltipla ou um polinomial**.

$H0: todos os A = 0$, sem relação entre X e Y 

Portanto H0 diz que X **não é significativo** para prever Y.

$H1: pelo menos um A \ne 0$, com relação entre pelo menos 1 X e Y

Portanto H1 diz que X (ou o modelo de regressão como um todo no caso da Anova) é significativo para prever Y.

Portanto, queremos um **p-valor > alfa** para rejeitar H0 e validar o modelo. Usamos H0 como uma negação pois nossas opções são rejeitá-lo ou inconclusivo (não rejeitá-lo). Não rejeitar não prova o modelo, portanto não responde nossa pergunta.

Os testes usados para validar é o teste T e a **Anova/teste F**. O teste T é usado na regressão simples para ver se $A \ne 0$ e a Anova na múltipla para ver se ao menos algum X afeta Y (se algum $A_i é \ne 0$). Caso a Anova encontre relação é rodado o teste T para cada X para encontrar quais são relacionados (**teste T é o post hoc da Anova**).

A diferença para regressão polinomial é que ele mede os A que muliplicam $x^2$ em diante.

### INTERVALO DE PREDIÇÃO

Essa nova técnica de inferência nos diz o intervalo de valores que Y pode ter para um determinado valor de X. Ele é como um intervalo de confiança para cada valor de X, pois nos diz o intervalo que Y pode estar com um nível de confiança.

Ex: em 95% das vezes Y vai estar nessa faixa para esse valor de X.

`O intervalo de confiança dá o intervalo para o coeficiente A, o intervalo de predição dá o intervalo para Y dado X = alguma coisa.`

Importante: Cada X terá um intervalo diferente, pois se X mudou o intervalo vai mudar junto. Porém o tamanho desse intervalo deve ser o mesmo (o intervalo não vai formar um cone, crescendo ou diminuindo).

O intervalo de predição só é preciso em caso de homocedasticidade.