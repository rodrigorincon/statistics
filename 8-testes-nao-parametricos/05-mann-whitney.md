# TESTE DE MANN-Whitney

Muito semelhante ao teste de Wilcoxon, calcula se tem **diferenças entre as medianas de 2 amostras independentes**. Assim como seus conceitos são próximos, seus cálculos também são. Ele também se baseia em rankings, mas ao invés de rankear as diferenças entre cada par, as amostras são combinadas em uma única amostra e então rakeadas.

Ele não tem versão para 1 amostra, apenas para 2 amostras independentes. Ele é o equivalente não paramétrico do **teste T para 2 médias independentes**. Ele é **baseado na mediana** ao invés da média. Por usar a mediana outliers não afetam o cálculo e distrbuições não normais também não são problemas.

## PREMISSAS

- Amostras independentes
- Os dados devem ser independentes
- Variável deve ser numérica ou ordinal (1º, 2º, 3º...)

## HIPÓTESES

$H0: medianaA = medianaB$ (não há diferença significativa)

$H1: medianaA \ne medianaB$ (há diferença significativa)

OBS: o teste que verifica se são **iguais é o bicaudal**. Caso queira verificar igualdade entre as medianas tem de usar a tabela bicaudal. Caso queira verificar se uma mediana é maior ou menor que a outra fazemos um teste unicaudal a direita ou esquerda.

$H0: medianaA \le medianaB$ e $H1: medianaA > medianaB$ tabela unicaudal a direita (cauda segue o símbolo de H1)

$H0: medianaA \ge medianaB$ e $H1: medianaA < medianaB$ tabela unicaudal a esquerda (cauda segue o símbolo de H1)

## COMO CALCULAR

### Passo 1: junte as amostras e ordene os dados 

Coloque as 2 amostras numa lista só e os ordene do menor ao maior (independente de qual amostra cada um veio).

### Passo 2: rankeie as posições

Faça um ranking para cada valor de acordo com sua posição, com o menor sendo o 1, o segundo menor 2 e assim por diante. Em caso de empate todos os valores empatados devem ter a média das posições.

Exemplo: se o 3º, 4º e 5º são iguais o ranking dos 3 serão 4 (média de 3, 4 e 5).

### Passo 3: Some os rankings de cada amostra

Ao invés de somar as diferenças positivas e negativas como em Wilcoxon, aqui somamos os rankings de cada amostra separadamente. Chamamos R1 e R2 a soma dos rankings de cada amostra.

### Passo 4: Define U calculado

Calculo U para cada amostra.

$$U_i = n1 * n2 + \frac{n_i(n_i+1)}{2} - R_i$$

Aonde

- n1 e n2 são os tamanhos das 2 amostras
- $R_i$ é a soma dos rankings da amostra

Ou seja, o U da amostra é a multiplicação do tamanho das amostras vezes um cálculo usando o tamanho da sua amostra menos a soma dos seus rankings. É a subtração que vai nos dizer qual amostra tem a mediana maior.

U calculado (final) é o menor entre os U amostrais.

$$U = min(U1, U2)$$

### Passo 5: Tabela

O teste usa a tabela de Mann-Whitney, que usa os valores de alfa, U1 e U2 para encontrar o valor de U tabelado. Para cada alfa existe uma tabela diferente, aonde U1 define a linha e U2 a coluna a ser observada.

Se **U calculado $\le$ U tabelado rejeita-se H0**.

As tabelas de Mann-Whitney só vão até o valor de 20, pois acima desse valor ela fica muito próxima a tabela Z. Para N (soma das 2 amostras) > 20, use a tabela Z. Para tanto precisamos converter U em z.

$z = \frac{U - \frac{n1 * n2}{2} }{ \sqrt{ \frac{n1 * n2 * (n1 + n2 + 1)}{12}} }$

Nesse caso z dará seu p-valor direto, que deve ser comparado com seu alfa.
