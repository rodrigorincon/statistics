# RIDGE e LASSO

Os dois são técnicas de regularização da regressão, ou seja, são alterações na fórmula da regressão para **evitar overfitting**. A regressão Lasso também é chamado de L1. A regressão Ridge é chamada de L2. Ambos as técnicas servem tanto para regressão linear como para logística. 

Muito usados em machine learning. Eles evitam o overfitting ao **tratar a multicolineariedade**, sendo opções robustas para esse cenário.Ambos tratam isso **adicionando uma penalidade** (também chamada fator de regularização).

### O QUE MUDA

Primeiro calcula-se a regressão normalmente, encontrando os coeficientes colinearizados. Para descolinearizar a regressão é refeita usando os coeficientes calculados como parte do cálculo de penalidade.

A única coisa que muda nos 2 métodos é a forma de calcular a penalidade. Todo o resto é idêntico. Em Ridge o cálculo da penalidade é:

$$S_{yy} = \sum{(y_i - ŷ_i)^2} + \lambda \sum{A_i^2}$$

Em Lasso o cálculo é:

$$S_{yy} = \sum{(y_i - ŷ_i)^2} + \lambda \sum{|A_i|}$$

Aonde 

- $A_i$ são os coeficientes antigos calculados do método tradicional
- Lambda é uma constante pré-definida para controlar o quanto quer penalizar variáveis correlacionadas.

`Sim, a única coisa que muda é que uma eleva os coeficientes ao quadrado e outra tira o módulo.` Mas isso muda muita coisa.

Repare que ao juntar todos os coeficientes colinearizados e colocar-los de volta na equação faz com que os novos coeficientes sejam mais balanceados, pois no processo de cálculo leva em conta a variância dos coeficientes antigos.

Por fim, substitua $S_{yy}$ no cálculo original da regressão por essa versão.

`Importante: repare que todos os coeficientes são afetados, inclusive os que não são correlacionados com ninguém.`

### EFEITO DO LAMBDA

Lambda existe para controlar o efeito da penalidade. Quanto maior lambda mais os coeficiente finais diminuem (na equação dos mínimos quadrados $S_{yy}$ está no denominador). Para um lambda infinito todos os coficientes se aproximam de zero e a reta fica horizontal (só sobra a constante).

Não existe uma faixa de quanto é alto ou baixo para lambda, depende muito da magnitude dos seus dados.

### QUANDO USAR

Quando tiver

- Muitas variáveis
- multicolinearidade
- Seleciona as variáveis mais importantes (Lasso apenas)

### PASSO A PASSO

- Calcule a regressão normal
- Escolha um lambda para controlar o efeito da penalidade (quanto maior lambda, maior a penalidade)
- Pegue os coeficientes e recalcule $S_{yy}$ (dispersão dos erros)
- Refaça a regressão usando essa nova dispersão no lugar da original

### EFEITO RIDGE

**O resultado é coeficiente menores**. Com isso as variáveis tem efeito menor na regressão. Porém em nenhum hipótese um coeficiente chega a zero. Essa é a grande diferença entre Ridge e Lasso, pois Lasso iguala alguns coeficientes a zero, removendo-os da equação. **Ridge encolhe a influência dos dados, Lasso remove os menos influentes**.

No Rdige, quanto maior lambda mais os coeficientes serão reduzidos e menos efeito terão.

### EFEITO LASSO

**O resultado é zerar diversos coeficientes**. Com isso as variáveis com coeficientes zeradas são removidas da regressão. Essa é a grande diferença entre Ridge e Lasso. **Ridge encolhe a influência dos dados, Lasso remove os menos influentes**.

No Lasso, quanto maior lambda mais coeficientes serão reduzidas a zero e com isso mais variáveis são eliminadas.

# ELASTIC NET

Elastic Net junta os 2, fazendo as duas penalidades. Ele tem um parâmetro extra alfa, que diz quantos porcento de cada um deve ser usado. Podemos fazer que a penalidade seja 60% Ridge e 40% Lasso ou qualquer outra combinação ou até 100% uma delas.

$$S_{yy} = \sum{(y_i - ŷ_i)^2} + \lambda [ \frac{1 - \alpha}{2} \sum{A_i^2} + \alpha \sum{|A_i|}]$$