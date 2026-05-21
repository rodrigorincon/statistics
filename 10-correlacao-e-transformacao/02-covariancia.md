# COVARIÂNCIA

- É outra medida de como 2 variáveis se comportam em relação uma a outra
- Informa apenas a direção entre as variáveis (se são proporcionais)
- Como ela `varia de -infinito a +infinito` não conseguimos medir a força/influência entre as variáveis
- Por conta disso ela é muito menos usada
- Comparar vars AxB é a mesma coisa de comparar BxA. O resultado é o mesmo independente da ordem
- Não diz quem influencia quem, se A influencia B ou o contrário

Positivo as duas vars crescem junto, negativo são inversamente propocionais e 0 não possuem relação. Porém **como vai até o infinito não sabemos se um valor é alto ou não** (ex: 300 indica uma relação forte ou fraca?).

- Ela é **fortemente afetada pela unidade de medida** (o valor pode ser 15 ou 150 a depender da unidade usada). 
- Por isso que o valor em si não é significativo, só seu sinal. 
- Por isso **não podemos comparar 2 covariâncias**, o que não ocorre com a correlação.

OBS: Ela só é importante em assuntos muito específicos, então só compensa estudar caso o projeto lhe exija.

Podemos definir covariância como a **soma das variâncias de X e Y multiplicados** e representá-lo como $vari_{xy}$.

## EQUAÇÃO

Pode ser calculada de 2 maneiras. Os dois dão o mesmo resultado

### 1: Média do produto das variâncias

Multiplico cada ponto com o ponto médio. Não é a distância, distância seria se somasse os eixos x e y.

$vari_i = (x_i - media_x) * (y_i - media_y)$ 

Tiro a média de todos as variâncias.

$$covariancia = \frac{ \sum_{i=1}^n variancia_i }{n-1}$$

Divida por N em caso de população e N-1 em caso de amostra.

### 2: Diferença entre a média do produto e o produto das médias

Tiro a média de todos os pontos, multiplicando seu x e y.

$mediaPontos = \frac{ \sum{i=1}^n x_i * y_i }{n-1}$

Divida por N em caso de população e N-1 em caso de amostra.

Subtraio disso a média de cada eixo.

$$covariancia = mediaPontos - media_x * media_y$$
