# TESTE DE WILCOXON

É a versão do teste T para dados não paramétricos (categóricos ou que não seguem a distribuição normal). Caso os dados não cumpram as premissas para o teste T (normal, vars numéricas contínuas, passar no teste de Levene e ter muito outliers) deve-se usar esse. Dados categóricos também se encaixam bem nele.

Ele é **muito baseado na mediana** ao invés da média. Por usar a mediana outliers não afetam o cálculo e distrbuições não normais também não são problemas.

Serve para o **teste T para 1 média** (compara mediana com um valor específico) e para **2 médias dependentes** (antes e depois). Para 2 médias independentes é usado o teste de Mann-Whitney.

Usa a `mediana das diferenças` entre as amostras, não a mediana das amostras.

## PREMISSAS

- Amostras dependentes (representam os mesmos dados antes e depois de algum evento)
- Os dados devem ser independentes
- Variável deve ser numérica ou ordinal (1º, 2º, 3º...)

## HIPÓTESES

### Para 1 Amostra

$H0: mediana \le valorComparacao$

Ou simplemente H0 = a amostra é estatísticamente menor ou igual ao valor de comparação.

$H1: mediana > valorComparacao$

### Para 2 Amostras

$H0: medianaA = medianaB$ (não há diferença significativa)

Ou simplesmente H0 = A diferença entre os pares segue uma distribuição simétrica em torno de zero.

$H1: medianaA \ne medianaB$ (há diferença significativa)

OBS: o teste que verifica se são **iguais é o bicaudal**. Caso queira verificar igualdade entre as medianas tem de usar a tabela bicaudal. Caso queira verificar se uma mediana é maior ou menor que a outra fazemos um teste unicaudal a direita ou esquerda.

$H0: medianaA \le medianaB$ e $H1: medianaA > medianaB$ tabela unicaudal a direita (cauda segue o símbolo de H1)

$H0: medianaA \ge medianaB$ e $H1: medianaA < medianaB$ tabela unicaudal a esquerda (cauda segue o símbolo de H1)

## COMO CALCULAR

O processo é idêntico para 1 ou 2 amostras, a única diferença é que com 1 amostra eu comparo com um valor específico e com 2 amostras eu comparo o valor de uma com da outra.

#### Passo 1: calcular diferença entre os dados

`Esse é o único passo que muda entre 1 ou 2 amostras.` 

Para 1 amostra calcula a diferença entre cada dado e o valor de comparação.

$dif_i = amostra_i - valorComparacao$

Para 2 amostras calcula a diferença entre um dado de cada amostra.

$dif_i = amostra1_i - amostra2_i$

Os demais passos são todos iguais. 

#### Passo 2: remover diferenças = 0

Se dif = 0 deve-se removê-lo da sua lista de diferenças. Só nos importa dados diferentes do nosso valor de comparação ou que tenham mudado do antes/depois (no caso de 2 amostras). Como vou tirar a mediana das diferenças, as diferenças 0 vão distorcer meu resultado.

#### Passo 3: salve os valores absolutos de cada diferença

$abs_i = |dif_i|$

O que importa é a distância entre o dado e o valor comparativo, não importando se é para baixo ou para cima.

#### Passo 4: ordenar e rankeie as diferenças absolutas do menor ao maior

Além de ordenar, deve-se dar um valor a cada diferença de acordo com sua posição. 1 para o primeiro, 2 para o segundo e assim por diante. Em caso de empate (2 valores iguais em seguida), o ranking dado deve ser a média das posições.

Ex: o terceiro e quarto possuem o mesmo valor, então o ranking de ambos será 3,5 (média entre 3 e 4). O próximo após eles será o ranking 5.

Observe que aqui se ordena de acordo com os **valores absolutos**, não as diferenças reais. Esse é o **único local aonde o valor absoluto será usado**.

#### Passo 5: soma os rankings das diferenças positivas e negativas

Separe as diferenças positivas e negativas (ignorando o absoluto) e some seus rankings. Chamamos a soma dos rankings positivos de W+ e a soma dos rankings negativos de W-.

$W+ = \sum_{i=1}^{n_t} { ranking_i, dif_i > 0 }$ considera só os rankings das diferenças positivas.

$W- = \sum_{i=1}^{n_t} { ranking_i, dif_i < 0 }$ considera só os rankings das diferenças negativas.

Aonde

- $n_t$ é o tamanho da amostra cuja diferença deu diferente de 0 (apenas os valores que foram rankeados)
- ranking é o valor do ranking (definido considerando o absoluto)
- dif é o valor da diferença (sem o absoluto)

#### Passo 6: define W calculado

W calculado é o menor valor dentre os 2 W calculados.

$$W = min(W+, W-)$$

#### Passo 7: tabela Wilcoxon

Usa-se a tabela Wilcoxon, usando o alfa escolhido e o $N_t$ (tamanho da amostra removido os com a diferença = 0). Você pode entender N como sendo a soma dos tamanho de W+ e W- (tamanho da amostra de fato usada no teste).

Se **W calculado < W tabelado eu rejeito Ho**.

#### Extra: Calcular p-valor

A comparação entre W calculado e tabelado já nos dar a resposta do teste, mas caso queira calcular o p-valor podemos fazer via **tabela Z**. Para tanta calculamos o valor de z.

$$z = \frac{(W+) - \frac{n_t (n_t + 1) }{4} }{ \sqrt{ \frac{n_t(n_t+1)(2n_t+1)}{24} } }$$

Aonde

- W+ é a soma dos rankings com diferença positiva
- $n_t$ é o tamanho da amostra cuja diferença deu diferente de 0 (apenas os valores que foram rankeados)

Devemos comparar o valor de Z com a **tabela bicaudal de Z**. Se `|Z calculado| > |Z tabelado| eu rejeito Ho`. Repare que só importa os valores absolutos para poder comparar ambas as caudas.

OBS: enquanto W calculado tem de ser menor que o tabelado, Z tem de ser maior para rejeitarmos. **Os comparadores são invertidos para cada forma de comparar**.

Caso haja empates nos rankings o cálculo de Z muda um pouco. Em caso de empates z é

$z = \frac{(W+) - \frac{n_t (n_t + 1) }{4} }{ \sqrt{ \frac{n_t(n_t+1)(2n_t+1)}{24} - \sum{\frac{t^3 - t}{48}} } }$

Aonde t é a quantidade de valores empatados que teve. O somatório é para caso haja vários empates. 

Exemplo: 2 valores 123 e 4 valores 140. O somatório repetirá 2 vezes, a primeira com t=2 e a segunda com t=4.

## EXEMPLO

Dado a lista x = [-7.34, 18.33, 33.35, 59.45, 8.09, 43.79, 34.3, 36.13, -56.02, 76.45], compare o teste com valor de comparação 5 com alfa de 5%.

| x     | dif (x-5) | abs(dif) | rank | ranks positivos | ranks negativos |
| :--   |  :--      |   :--    |  :-- |  :--            |  :--            |
| -7.34 |  -12.34   |   12.34  |  2   |   -             |       2         |
| 18.33 |  13.33    |   13.33  |  3   |   3             |       -         |
| 33.35 |  28.35    |   28.35  |  4   |   4             |       -         |
| 59.45 |  54.45    |   54.45  |  8   |   8             |       -         |
| 8.09  |  3.09     |   3.09   |  1   |   1             |       -         |
| 43.79 |  38.79    |   38.79  |  7   |   7             |       -         |
| 34.3  |  29.3     |   29.3   |  5   |   5             |       -         |
| 36.13 |  31.13    |   31.13  |  6   |   6             |       -         |
|-56.02 |  -61.02   |   61.02  |  9   |   -             |       9         |
| 76.45 |   71.46   |   71.46  |  10  |   10            |       -         |

W+ = 3+4+8+1+7+5+6+10 = 44

W- = 2+9 = 11

W calc = min(11, 44) = 11

$N_t = 10$

Para alfa = 0,05 e N = 10 (8 positivos e 2 negativas), olhamos na tabela na coluna 0,05 e linha 10. Encontramos o valor W tabelado = 8.

Como W calculado (11) > W tabelado (8) então não rejeito H0. A mediana da amostra é maior que 5.

O cálculo do p-valor será

$z = \frac{44 - \frac{10 (10 + 1) }{4} }{ \sqrt{ \frac{10(10+1)(2*10+1)}{24} } } = \frac{16,5}{ \sqrt{96,25} } = 1.68$

Procurando o valor na tabela bicaudal para z = 1,68 (linha 1,6 e coluna 0,08) encontramos p-valor = 0,9535. Como p-valor > alfa, não rejeito H0.