=========================== DISTRIBUIÇÃO PROBABILISTICA CONTINUA

=============== DISTRIBUIÇÃO EXPONENCIAL
calcula o tempo entre 2 eventos INDEPENDENTES
os eventos precisam ocorrer a uma TAXA CONSTANTE
	taxa = média de acontecimentos num período de tempo
a taxa é representa com que frequencia um evento acontece

parece com a poisson aplicado a var contínua, onde a média é a taxa.
Porém a poisson mede a QUANTIDADE de eventos EM UM PERIODO DE TEMPO. A exponencial mede O TEMPO entre 2 eventos

só serve para calcular o tempo entre eventos CONSECUTIVOS (ñ posso calcular o tempo entre o 1ª e 3ª evento)
só temos erro quando calculamos em cima de amotra. Como calcular esse erro será definido na inferência estatística

-------------------
para um valor ESPECÍFICO = P(X=x) = taxa*e^(-taxa*x) = taxa/e^(taxa*x)
para todos os valores abaixo de x = P(X<x) = 1 - e^(-taxa*x) = 1 - 1/e^(taxa*x) -> essa é a integral do valor específico de 0 a x
-------------------

COMPROVAÇÃO DE QUE O VALOR P(X<x) É A INTEGRAL DO VALOR ESPECIFICO
S(taxa*e^(-taxa*x) dx ) = taxa*S(e^(-taxa*x)) = taxa * (-1/taxa * e^(-taxa*x)) = -taxa/taxa * e^(-taxa*x) = -1 + e^(-taxa*x) = 1 - e^(-taxa*x)

1/e^(taxa*x) -> chance do evento acontecer acima do x
por isso que a equação é 1 - chance

MODA = 0
ESPERANÇA =  DESVIO PADRÃO = 1/taxa
VARIANCIA = 1/taxa^2

OBS: taxa é sempre positivo
x sempre >= 0

Quando tenha Probabilidade condicional com maior ou menor eu subtraio os valores
P(X>a | X>b) = P(X>a-b)
ex: P(X>10 | x>4) = P(X>6) -> probabilidade de algo acontecer 10x dado que já aconteceram 4

USO: fluxo de entrada de casos por tempo (tempo entre chamadas ao servidor, tempo de espera numa fila), tempo entre 2 ações (manutenção num produto)

Gráfico cruza o eixo Y na taxa (quando x=0 a prob=taxa) e então cai exponencialmente
O maior valor que essa distribuição tem é x=0 (valor sendo a propria taxa)
a taxa tbm é a velocidade em que ela cai, portanto quanto maior a taxa mais vertiginosa a queda
uma equação com taxa maior sempre vai passar por baixo duma com taxa menor

------------- exercicios

1: o metrô passa a cada 15 minutos. Qual a probabilidade duma pessoa esperar menos de 10 minutos?
taxa = 1/15 (passa 1 metrô a cada 15 minutos)
x = 10

P(X<10) = 1 - 1/e^(1/15*10) = 1 - 1/e^(10/15) = 0,4866

2: o metrô passa a cada 15 minutos. Qual a probabilidade duma pessoa esperar mais de 15 minutos?
taxa = 1/15 (passa 1 metrô a cada 15 minutos)
x = 15

P(X>15) = 1 - P(X<15)
P(X>15) = 1 - (1 - 1/e^(1/15*15) ) = 1 - 1 + 1/(e^(15/15)) = 0 + 1/e^1 = 1/e

3: o metrô passa a cada 15 minutos. Qual a probabilidade duma pessoa esperar entre 7 e 10 minutos?
P(X<10 e X>7) = P(X<10) - P(X<7)
P(X<10) = 1 - 1/e^(10/15) = 0,4866
P(X<7) = 1 - 1/e^(7/15) = 0,3729
P(X<10 e X>7) = 0,4866 - 0,3729 = 0,1137

4: o metrô passa a cada 15 minutos. Uma pessoa já está esperando há 3 minutos. Qual a probabilidade dela esperar pelo menos mais 7?
P(X > 7+3 | X > 3)
	| X > 3 -> probabilidade da algo DADO QUE JÁ ESPEROU 3 MINUTOS
	X > 7+3 -> como pode vir a esperar 7 ou mais minutos, tem de ser P(X > 7). O +3 é pq já esperou esse tempo.
P(X > 10 | X > 3) -> probabilidade de esperar 10 ou mais minutos dado que já esperou 3

P(X > 10 | X > 3) = P(X > 10-3) = P(X > 7)

P(X > 7) = 1 - P(X < 6) = 1 - (1 - 1/e^(1/15*6)) = 1 - 1 + 1/e^(6/15) = 1/e^(6/15) = 0,3297

=============== DISTRIBUIÇÃO NORMAL
também chamada de gaussiana ou de sino
pode ser usado com valores discretos quando ele tem valores muito próximos
quanto maior o desvio padrão, mais aberto é o gráfico da normal (mais espaçado estão os valores)
precisa pegar a média e o desvio padrão pra calcular

moda = esperança = média 
variância = soma(xi - media)^2/total -> total para população ou total-1 para amostra
pra saber se uma distribuição é normal tem que passar no teste de hipótese XXXXXXX

68,26% fica dentro do 1º desvio padrão
95,44% fica dentro do 2º desvio padrão
99,72% fica dentro do 3º desvio padrão

f(x) = e^(-1/2*[{x-media}/desvio]^2)/(desvio*raiz(2pi)) = 1/( desvio*raiz(2pi)*e^[{(x-media)/desvio}^2/2])
calcula o resultado específico para o valor x

para calcular de -inf a x ou entre x e y tem de calcular a integral
P(X<x) = 1/(desvio*raiz(2pi)) * S e^(-1/2*[{x-media}/desvio]^2)
como essa integral ñ tem solução analítica, então é preciso simplifcar a equação (padronizar) e usar de tabelas (z-score) pra calcular

----- explicando a equação
(x-media)/desvio é a alma da equação
1/(desvio*raiz(2pi)) garante que a área total da curva dê 1
-1/2 * {(x-media)/desvio}^2 controla o formato da curva. O sinal faz a curva ser virada pra baixo com pico em 0
quanto mais x se afasta de 0 maior o valor de {(x-media)/desvio}^2, e como ele tem sinal negativo, menor o valor, garantindo que o maior valor é 0
o fato da base ser o nº de euler (e) faz a função cair vertiginosamente a medida que x se afasta de 0
o desvio ajuda a segurar a queda da função, tornando a queda mais suave caso ele seja maior
-----

----- NORMAL PADRONIZADA
é uma simplificação da distribuição normal, aonde a média é convertida pra 0 e o desvio pra 1
para isso, ao invés de calcular x, calculamos z

z = (x - media)/desvio -> é a parte principal da equação da normal
	z diz quantos desvios padrões o x está acima ou abaixo da média
	valores acima da média são positivos e abaixo da média negativos
	desvio padrão = 1, 10% acima do desvio padrão é 1.1, metade do caminho entre o 1º e 2º desvio é 1,5

f(z) = e^(-1/2*z^2)/raiz(2pi)
OBS: mesmo simplificando usando z, a integral de e^(z^2) ainda ñ tem solução analítica, então precisa usar as tabelas ou softwares
não precisa usar essa fórmula, só procurar a resposta na tabela z-score

ao padrozinar os valores eliminamos diferenças de escala, permitindo a comparação entre 2 distribuições mesmo que usem escalas diferentes

quando P(z) > 3 (quando tiver + de 3 desvios padrão) é certeza de ser OUTLIER, chance de 0,27% de chance de acontecer
quando P(z) > 2 (quando tiver + de 2 desvios padrão) pode ou não ser OUTLIER, tem de analisar o seu contexto, chance de 4,55% de chance de acontecer

----- intervalo de confiança
intervalo de confiança diz quantos % de certeza eu tenho que a média POPULACIONAL está em um intervalo

intervalo = media_amostral +- Z * devio_amostral/raiz(n)
	Z vem da tabela z-score (ñ é o z da equação!)

------------- exercícios
1: O teste de QI a média é 100 e o desvio padrão 15. Qual a probabilidade:
media=100
desvio=15
a) alguem ter QI abaixo de 110
	z = x - media / desvio = 110 - 100 / 15 = 10/15 = 0,67
	P(x<110) = P(z<0,67) = 0,7486

b) alguém ter QI entre 100 e 140
	P(100 < x < 140) = P(x<140) - P(x<100)
	z = 140 - 100 / 15 = 40/15 = 2,67
	z = 100 - 100 / 15 = 0
	P(z<2,67) - P(z<0) = 0,9962 - 0,5 = 0,4962 

c) alguém ter QI acima de 80
	z = 80 - 100 / 15 = -20/15 = -1,33
	P(z > -1,33) = P(z < 1,33) -> como é simétrico a partir do 0, podemos inverter o sinal e o comparador
	P(z < 1,33) = 0,9082

2: computadores são vendidos com valores na média de 750 dolares e devio de 60 dólares. Quantos são vendidos entre 624 e 768?
	P(624 < x < 768) = P(x<768) - P(x<624)
	z = 768 - 750 / 60 = 0,3
	z = 624 - 750 / 60 = -2,1
	P(z<0,3) - P(z < -2,1) = 
	P(z<0,3) - P(z > 2,1) = 
	P(z<0,3) - (1 - P(z < 2,1) ) = 
	P(z<0,3) - 1 + P(z < 2,1) = 
	0,6179 - 1 + 0,98214 = 0,60004 = 60%

=============== DISTRIBUIÇÃO T
é uma versão da normal PADRÃO para uma amostra pequena
o gráfico é igual a normal porém mais espaçada, menor no topo e com as bordas mais elevadas
ou seja, ela é menos precisa (justamente por ter uma amostra pequena)
por ser mais "imprecisa", encaixa perfeito pra quando vc tem amostras pequenas (< 30)
conforme sua amostra cresce, ela se aproxima da normal PADRÃO (com média 0 e desvio 1)

é simétrica em forma de sino
média = moda = mediana = esperança = 0
perfeita para quando não sabe o desvio padrão da POPULAÇÃO (só tem o da amostra)
um dos params é o grau de liberdade = tamanho da amostra - 1
	grau_liberdade = N-1

variancia = grau_liberdade / (grau_liberdade - 2) = (N-1)/(N-3) -> N precisa obrigatoriamente ser > 3
	a equação mostra que quanto menor N, maior a variância e o desvio padrão
	pra N=30, variância=1,07 e desvio=1,036 (praticamente igual a normal)
	importante ver que a T nunca será idêntica a normal (valores de variância e desvio nunca chegarão a 1), mas a partir de 30 já estão tão próximos que dá pra descartar a diferença

----- equação e tabela t-score
f(x) = (1+x^2/(n-1))^(-n/2)*gama(n/2)/(gama([n-1]/2)*sqrt(pi*[n-1]))
aonde gama é a função fatorial para todos os números reais e complexos
porém a equação quase nunca é usada, ao invés disso é usado uma tabela (tabela t-score)

pra procurar na tabela precisa usar o grau_liberdade e o alfa (% presente nas bordas)
https://www.youtube.com/watch?v=q2zLIljdvo4 min 11:08
	quanto maior o alfa mais a curva é coberta e considerada no cálculo
	alfa vem da confiança (grau de certeza) que quero ter
	o alfa considera os 2 lados do gráfico, com alfa/2 pra cada lado
	então, ao buscar a prob que cubra 15% do gráfico de cada lado o alfa é 30%
	OBS: tem gráficos bi-caudal (que faz desse modo) e uni-caudal (aonde todo alfa está em um único lado) e os valores mudam de um pro outro. Atenção pra usar a tabela certa
	para calcular intervalo de confiança, sempre usar o bi-caudal (ou divida alfa por 2 e usa o uni-caudal)

----- intervalo de confiança
confiança = 1 - alfa -> quanto menor o alfa usado, mais confiança eu tenho na minha medição (pois mais area sobra no meio, garantindo que seu valor tá ali no meio)
erro = alfa (ou 1 - confiança)
intervalo de confiança (da média populacional) = media +- t*desvio/sqrt(n)
	media e desvio DA AMOSTRA
	t é o valor da tabela
	n tamanho da amostra

podemos interpretar isso como "eu tenho (1-alfa)% de certeza que a média POPULACIONAL está neste intervalo"
	t*desvio/raiz(n) diz o quanto nossa média amostral tá longe da média real
	dividir por raiz de N faz o intervalo ficar cada vez mais incerto pra valores pequenos e mais precisoa para valores grandes (pra N infinito o intervalo é a própria média amostral, pois a amostra é toda a população)
	quanto menor N, maior o intervalo
	t é quantos desvios padrões estamos da média real e multiplicando pelo desvio da amostra ajustamos para nossa medição

https://www.youtube.com/watch?v=xP6XZabCSgs exercicio que mostra como usar no caso pratico

----- dica de qual distribuição usar
SE TEM A POPULAÇÃO TODA: NORMAL
SE TEM SÓ AMOSTRAS:
	AMOTRAS PEQUENAS: T
	AMOSTRAS GRANDES: NORMAL

--------- exercicios
1: uma loja fez um pesquisa pra saber quanto dá as compras dos clientes. A pesquisa foi feita com 15 clientes, a média foi 120 reais com desvio de 42 reais. Calcule a média populacional com 95% de confiança.

alfa = 1 - confiança = 1 - 0,95 = 0,05
grau_liberdade = 15 - 1 = 14
olhando na tabela bi-caudal, t = 2,145

intervalo_confianca = media +- t*desvio/raiz(N) = 120 +- 2,145*42/raiz(15) = 96,74 e 143,26
tenho 95% de certeza que a média verdadeira está entre 96,74 e 143,26!!
