# COEFICIENTE DE DETERMINAÇÃO

Mede o **quanto a variância de uma var é definida por outra variável**. Com ela medimos a força do coeficiente (seu valor absoluto) e damos a porcentagem do quanto as variáveis se interferem.

Apesar de parecer que o coeficiente já dá uma porcentagem de quanto as vars são relacionadas por ir de 0 a 1, seu valor é distorcido, não representando uma porcentagem fielmente. Assim, o coeficiente de determinação é calculado em cima do coeficiente de correlação para dar **quantos % da variância é definida (igual) nas 2 vars**. 

`Um valor alto significa que elas variam mais próximo. Por isso também é chamado de variância compartilhada`.

## COMO USAR

Quanto maior o coeficiente de determinação, mais devemos dar importância para a correlação. Uma determinação muito baixa significa que não vale tentar entender o porquê dessa correlação, já que a relação é tão fraca e influencia tão pouco uma na outra.

OBS: quanto maior a correlação, maior o coeficiente de determinação. Porém o coeficiente de determinação é sempre menor que a correlação (exceto pra r=0 e r=1).

Também é importante ter noção que ela tem um gráfico exponencial. Isso significa que, ao comparar 2 correlações, quanto maior o valor dessas correlações maior a diferença entre as determinações.

Exemplo: uma correlação de 0,1 e outra de 0,2 tem 0,1 de diferença e suas determinações tem 3% de diferença. Uma correlação 0,8 e outra de 0,9 tem os mesmos o,1 de diferença, porém suas determinações tem 17% de diferença.

Isso significa que **para correlações altas, cada pequena mudança faz toda diferença na determinação**. `Um pequeno crescimento na correlação melhora muito seu modelo` (se os valores já forem altos), porém **se as correlações forem baixas essa pequena mudança é irrisória**. Por isso que para valores baixos nem merece gastar tempo analisando e tentando entender.

### Ele é o equivalente ao TAMANHO DO EFEITO na inferência estatística.
	
## QUANDO USAR

- Avaliar o ajuste de um modelo de regressão, se os dados se encaixam num modelo testado.
- Ver quão relevante é a correlação

No fundo, os 2 são a mesma coisa.

## EQUAÇÃO

O coeficiente de determinação é representado como R², pois ele é o coeficiente de correlação ao quadrado.

$$coefDet = coefCorr^2 = r^2$$