# MEDIDAS DE ADEQUAÇÃO

Além dos testes de hipótese das premissas (que veem se os dados cumprem os requisitos do algoritmo) e do teste dos coeficientes (que testa se as variáveis afetam o resultado final de fato) podemos testar o **quão bem a reta se ajusta aos dados**. Usada tanto para validar a regressão como para **comparar diferentes regressões**.

Importante perceber que uma reta bem ajustada aos dados **pode ser sinal de overfitting**! 

## DESVIO PADRÃO DOS ERROS

Mede o quanto os erros variam em torno da reta. Ou seja, mede a **dispersão dos pontos em relação a reta**.

Varia de 0 a infinito, aonde 0 acontece apenas se todos os pontos estão exatamente em cima da reta. Ou seja, **quanto menor melhor**. Por ir até o infinito o número em si não é muito informativo, servindo para **comparar regressões** e ver qual tem o menor erro.

$$desvio_e = \sqrt{ \frac{ \sum{(y_i - ŷ_i)^2} }{N-k-1} }$$

Aonde

- k é a quantidade de variáveis independentes (X)
- $ŷ_i$ é o valor da reta para aquela posição

Ou seja, $y_i - ŷ_i$ é o erro, a diferença entre o ponto e a reta. Com isso podemos ver que a conta é idêntica ao do desvio padrão normal, porém usando os graus de liberdade da regressão.

## COEFICIENTE DE DETERMINAÇÃO

Mede o **quanto a variância de uma var é definida por outra variável**. Em termos práticos ele informa **quantos % da variância é definida por outra var**.

Como só analisa um par de variáveis, analisamos a var dependente (Y) com a reta da regressão (ŷ). Ou seja, comparo Y com os valores que a regressão dá para os mesmos Xs.

Ele é o coeficiente de correlação ao quadrado. Varia de 0 a 1, sendo 1 significando 100% de correlação. Logo, **quanto maior melhor**.

`Um valor alto significa que elas variam mais próximo. Por isso também é chamado de variância compartilhada`.

$$coefDet = r^2$$

Aonde r é calculado a partir de ŷ. Ao invés de fazermos y - média na soma dos quadrados nós fazemos y - ŷ.

## COEFICIENTE DE DETERMINAÇÃO AJUSTADO

O coeficiente de determinação ele tem uma falha que é que quanto mais variáveis X eu uso maior o resultado, independente se ela melhora minha reta ou torna os dados mais corretos. Ou seja, posso adicionar variáveis ruins, que não ajuda a prever o valor de Y, ou repetir a mesma variável ou colocar variáveis muito correlacionadas entre si, que não agregam, e meu coeficiente irá aumentar mesmo assim.

Também retorna de 0 a 1, sendo 1 significando 100% de correlação. Logo, **quanto maior melhor**. O valor ajustado será sempre menor que o coefiente tradicional.

`Ótimo para comparar regressões com quantidade de Xs diferentes`.

$$coefDetAjust = 1 - [ \frac{(1 - r^2)(n - 1)}{n-k-1} ]$$

Aonde

- $r^2$ é o coefiente de determinação tradicional
- n é o tamanho da amostra
- k é o número de variáveis usada

Repare que o denominador é o nosso grau de liberdade.

## AIC e BIC

Ambos os métodos calculam o quanto a regressão se ajusta aos dados a partir de um equilíbrio entre precisão e complexidade. Ambos penalizam regressões que tentam ser muito complexos (usam variáveis demais). Assim eles buscam informar se sua regressão não está desnecessariamente complexa e daria para enxugar algumas variáveis.

Ambos não possuem um valor mínimo ou máximo fixo, portanto o valor sozinho não diz nada, mas comparando com outra regressão consegue dizer qual é melhor. **Quanto menor melhor**.

Ambos penalizam regressões que usam muitas variáveis, dando pontos menores (melhores) para regressões que usam menos variáveis. Assim a equação de ambos **equilibra a quantidade de variáveis (K) com a precisão deles (L)**.

A ideia é tanto **evitar overfitting** quanto comparar regressões. Mas diferente das outras medidas, essa não diz qual é melhor propriamente, mas qual é mais simples sem perder qualidade. O que também é ser melhor, mas não propriamente dá resultados mais precisos, e sim **qual dá a mesma precisão com menos complexidade**.

Os dois usam a verossimilhança (L), uma técnica que calcula o parâmetro da distribuição a partir dos dados partindo do pressuposto que os dados seguem a distribuição que quer descobrir os dados.

#### Verossimilhança

Enquanto diversas técnicas descobrem uma probabilidade dada a distribuição dos dados, a verossimilhança faz o caminho oposto. Supondo que os dados seguem uma certa distribuição, ela calcula qual parâmetro dessa distribuição para os dados se encaixarem nele.

Ex: eu tenho os dados 12, 15 e 18 e digo que eles seguem uma distribuição normal. A verossimilhança vai tentar adivinhar qual a média e desvio padrão (os parâmetros dessa distribuição) dessa curva normal.

A máxima verossimilhança busca encontrar o valor máximo dessa curva (no exemplo da normal, seria a média).

Para simplificar o método costuma-se usar a log-verossimilhança (tirar o log de todo o cálculo), pois assim multiplicações viram somas. Em seguida derivar a função resultante e igualá-la a 0 para encontar seu ápice (o ponto que a derivada é 0 é o ápice da curva).

#### Cálculo do AIC e BIC

$$AIC = -2ln(L) + 2k$$

$$BIC = -2ln(L) + k*ln(n)$$

Aonde

- L é a verossimilhança da regresão para a normal (quão bem os dados se ajustam ao modelo a partir da normal)
  - Representa a precisão da regressão
- k é o número de variáveis
  - Representa a complexidade da regressão
- n é o tamanho da amostra

Dos dois, **BIC penaliza ainda mais regressões comlpexas.**

Use AIC quando quiser:

- Fazer previsões
- Aceitar modelo mais flexível (menos precisão)
- Usar séries temporais
- Usar mínimos quadrado generalizados

Use BIC quando quiser:

- Encontrar a resposta mais próxima do correto
- Descobrir fórmula matemática
- Maior rigidez/precisão (porém aumenta chances de erro tipo II)
- Estudos Bayesianos
