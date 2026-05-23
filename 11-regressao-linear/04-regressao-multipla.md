# REGRESSÃO LINEAR MÚLTIPLA

- Assume que a relação entre as variáveis é linear (pode ser descrita por uma reta)
- A relação é constante (não explode como uma exponencial) ou vai diminuindo a força da relação (como um logaritmo)

A grande diferença dela para a simples é que tenho mais de 1 variável independente (vários Xs) influenciando Y. Ao invés de uma linha num gráfico 2d, a melhor forma de imaginar é de um plano em um hiperplano. Cada X adiciona uma dimensão (2 vars indepenentes forma um gráfico 3D, 3 vars formam um  4D...).

A equação muda para ter vários Xs (todos elevados a 1), ficando da seguinte forma:

$y = a0 + a_1*x_1 + a_2*x_2 ... + a_k*x_k$

Aonde

- x são as variáveis independentes
- y é a variável dependente
- a são os coeficientes angular (grau de inclinação da reta em cada dimensão)
- a0 é o coeficiente linear (onde a reta corta o eixo Z quando todos os x = 0)
- k é o total de variáveis independentes (X) que temos

Observe que cada **A funciona como um peso que diz o quanto aquela variável influencia Y**. Não confundir com os pesos da versão ponderada, em que cada ponto de cada X tem um peso também.

Observe também que trocamos B por A0. É apenas uma mudança de nomenclatura para que todos os coeficientes fiquem como A e a constante que não multiplica nenhuma var é a número 0. Ele continua sendo o coeficiente linear e funcionando igual como na versão simples.

### E se não sei quais variáveis afetam meu resultado?

Nesse caso posso inserir na regressão todas as vars que suspeito que afete a var Y e depois testar cada uma para confirmar sua relação (teste T).

Posso também fazer uma matriz de correlação entre as vars independentes (Xs) para eliminar as que são muito correlacionadas.

Uma opção mais pesada é calcular a regressão com todas as combinações de variáveis (Só com X1, só com X2, com X1 e X2, com X1 X2 e X3, com X1 e X3...) e comparar os desvios dos erros e o coeficiente de determinação ajustadas de cada um para ver qual é mais preciso.

## PREMISSAS

A regressão multipla traz uma premissa extra, além dos resíduos independentes, normais e homogêneos, chamado **multicolinearidade**. 

`As variáveis independentes (Xs) não podem ser correlacionadas. Ou seja, X1 não pode interferir no valor de X2.`

Caso duas vars independentes sejam fortemente correlacionadas então fica difícil dizer se o efeito que elas causam em Y se deve a ela mesma ou por causa da outra, além de que a mesma fonte de efeito pode está sendo considerada duas vezes e afetar mais o cálculo do que deveria.

Para evitar isso mudamos o método para um que funcione com multicolinearidade. Alguns métodos analisam essas colinearidades e ou descarta uma das vars ou dá um peso pequeno. As soluções costumam ser:

- Descartar uma das vars
- Combinar as duas vars em 1
- Dar pesos pequenos para uma das vars
- Técnicas de regularização (Ridge, Lasso ou Elastic Net)
- Adicionar mais dados nas vars (acreditando que a semelhança se deva a poucas amostras)

De todo modo, optar por um algoritmo forte a multicolinearidade resolve, pois ele fará uma dessas coisas acima.

Caso queira calcular a multicolinearidade manualmente, as técnicas são:

- Matriz de correlação
  - Testa pares de vars
  - Limitação: se uma var independente for descrita pela união de outras 2 ou mais (ex: X1 = X2 * X3)
  - O limiar que define alta correlação é relativo (entre 0,5 e 0,7 a depender da pessoa)
- Fator de inflação de variância (VIF)
  - Testa várias vars juntas, resolvendo a limitação da matriz
  - Só verifica correlação se a mesma for linear
  - Resultado > 5 indica correlação moderada. Resultado > 10 indica correlação forte

### FATOR DE INFLAÇÃO DE VARIÂNCIA

Mede o quanto o erro padrão aumenta quando as variáveis independentes estão correlacionadas.

$VIF_x = \frac{1}{1 - r2_{regx}}$

Aonde

- $r2_{regx}$ é o coeficiente de determinação de uma nova regressão linear aonde $X_i$ é Y e todas as demais vars independentes se mantém como X

Seu valor varia de 1 ao infinito e **quanto menor menos correlação existe**.

Para achar o valor de VIF de uma variável X temos de fazer uma nova regressão linear aonde esse X é nossa var dependente (Y) e usamos todas as outras variáveis para criar a regressão com ela. Após isso calculamos o coeficiente de determinação da regressão e a utlizamos na equação.

Isso é bastante pesado pois temos de calcular uma regressão múltipla para cada variável, além da regressão que desejamos. Assim para fazer a regressão que desejamos acabamos fazendo k+1 regressões. Essas regressões extras são todas com **mínimos quadrados ordinais**.

## COMO CALCULAR

Por padrão usa-se os **Minimos quadrados ordinais** (OLS). A versão tradicional também serve para muitas variáveis. Caso alguma das premissas sejam quebradas, deve-se usar alguma de suas variações:

- Heterocedasticidade: mínimos ponderados ou robustos (a depender do conhecimento prévio dos dados)
- Não normalidade: mínimos robustos
- Multicolinariedade: mínimos generalizados
- Muitas vars e poucos dados: mínimos parciais

## TESTE DE HIPÓTESE 

Para uma regressão múltipla o teste Anova é o usado. Como teste post-hoc é usado o teste T entre cada X e a var dependente (Y). Junto com os testes das premissas, os testes que temos são:

- Anova (p-valor < alfa)
- Teste T (p-valor < alfa)
- Jarque-Bera (p-valor > alfa)
- Breusch-Pagan (p-valor > alfa)
- Durbin-Watson (p-valor > alfa)
  - Apenas para séries temporais

Para nosso teste principal (Anova) nosso F calculado é:

$$F = \frac{S_{xy}}{ \frac{S_e}{n-k-1}  }$$ como calcular com varias vars???

Aonde

- $S_{xy}$ é a soma dos quadrados ???

$S_e$ = S_{yy} - b * S_{xy} ???

O cálculo do F tabelado usa 1, n-2, alfa como parâmetros (1 como gl do numerador e n-2 como gl do denominador) e deve ser **bicaudal**.

Para o teste post-hoc o cálculo do nosso T calculado é:

$$T = \frac{A}{ \frac{desvio_e}{ \sqrt{\sum{(x_i - media_x)^2}} } }$$

Ou seja, divide o coeficiente da angular da reta pelo desvio padrão dos erros e pela soma dos quadrados de X. É quase a divisão pelo desvio e pela variância, mas não temo a divisão por N-1 para configurar a variância. Importante ressaltar que o desvio e a soma dos quadrados são de objetos diferentes.

O cálculo do T tabelado usa n-2 graus de liberdade e nosso alfa e deve ser **bicaudal**.

## GRAUS DE LIBERDADE

Os graus de liberdade numa regressão linear é **n - k - 1**, onde k é o número de variáveis independentes (X). Isso porque você está tentando definir k coeficientes (os valores que multiplicam x1, x2, x3...), logo temos k coeficientes, portanto k-1 graus de liberdade.

OBS: o intercepto (a0), coeficiente constante que não multiplica nada, é ignorado.

Ex: Numa regressão com 3 vars independentes (k = 3) os graus de liberdade são n-4.

## INTERVALO DE CONFIANÇA

## INTERVALO DE PREDIÇÃO

# PASSO A PASSO

1. Entenda o contexto. Esses dados fazem sentido para o que quer analisar?

2. Verifique se cada X é linear ou sem nenhuma relação visível com Y

- Gráfico de dispersão
- Correlação (valor absoluto alto)
- Caso não seja, faça uma transformação e repita o passo

OBS: dados de teste também devem passar por esta etapa

3. Faça a regressão múltipla

- Método dos mínimos quadrados ordinais

4. Pegue os resíduos, os coeficientes e os valores estimados para os mesmos Xs (ŷ)

5. Valide homocedasticidade dos resíduos (não devem ter nenhuma relação visível)

- Gráfico resíduos vs valores estimados (ŷ)
- Gráfico resíduos vs cada var independente (X)
- Teste Breusch-Pagan
- Caso não passe, volte ao passo 3 com dados transformados ou usando uma variação dos mínimos quadrados

6. Valide normalidade dos resíduos

- QQ-plot dos resíduos vs valores estimados (ŷ)
- Teste de Jarque-Bera
- Caso não passe, volte ao passo 3 com dados transformados ou usando uma variação dos mínimos quadrados

7. Valide dependência interna dos erros (séries temporais)

- Gráfico de linha dos resíduos vs cada var independente (X)
- Teste de Durbin-Watson
- Caso não passe, volte ao passo 3 com dados transformados ou usando uma variação dos mínimos quadrados

8. Valide multicolinearidade

- VIF ou matriz de correlação
- Decida o que fazer com as vars correlacionadas
- Volte ao passo 3 após tratar as vars correlacionadas ou usando uma variação dos mínimos quadrados

9. Teste Anova

- Valide se a Anova passa
- Caso não passe, descarte a regressão

10. Teste T e intervalo de confiança dos coeficientes

- Valide todas as var independentes (X)
- Valide se todas os coeficientes tem intervalos de confiança que não passem pelo 0
- Caso alguma não passe, volte ao passo 3 sem ela
  - Verifique o desvio padrão dos erros, R² ajustado e AIC/BIC do antes e depois
  - Fique com a regressão que der os melhores resultados
- Caso tenha usado transformação ou alguma variação do mínimo quadrado por conta da var X não passar em algum teste e esse mesmo X nãp passou nos testes T e do intervalo, remova-o e volte ao passo 3 usando os mínimo quadrados ordinais

11. Execute a regressão com dados de teste

- Caso tenha feito transformação nos dados, faça a mesma transformação nos dados de teste
- Caso o nº de resultados fora do intervalo de confiança seja maior que o nível de confiança alfa, jogue a regressão fora
  - Troque os dados de teste e de treino e volte ao passo 3