=========================== DISTRIBUIÇÃO POISSON
mede o nº de sucessos (ou falhas) em um período de tempo ou espaço
é preciso ter uma média de sucessos por tempo/espaço definida E FIXA 
!!se a média mudar caso o perído de tempo/espaço mude ñ serve
!!os eventos DEVE ser INDEPENDENTES. Ou seja, um evento acontecer num periodo de tempo/espaço ñ deve afetar a quantidade em outro período

ex: nº carros que passam numa ponte entre 9h e 10h
ex2: nº defeitos em um carro (carro é o espaço)
ex3: nº terremotos em uma região

P(X=x) = e^(-media) * media^x / x! = media^x/(e^media * x!)

P(X=x) =   media^x
	 ____________
   	 e^media * x!

OBS: a média PRECISA ser no mesmo período/espaço que se quer medir

e^(-media) -> faz a chance dum evento cair exponencialmente conforme se distancia da média
media^x -> chance de x eventos ocorrerem dado a média
x! -> divide a chance de acontecer (media^x) pela quantidade de maneiras que o evento pode ocorrer. Garante que a ordem dos eventos não importe

!!A MÉDIA, ESPERANÇA E VARIÂNCIA SÃO IGUAIS em algo que segue uma distribuição de poisson
é derivada da distribuição binomial.

Para médias baixas, O GRÁFICO TEM UM FORMATO ASSIMÉTRICO PRA ESQUERDA com pico na média e na média-1
ele cai mais rápido pra esquerda e é mais suave pra direita
Conforme a média cresce o gráfico vai se aproximando duma normal (media > 30 pode usar a normal)

quando x = media, o valor da prob é diferente pra cada x e vai só diminuindo conforme eles aumentam
ex: x=media=2 P(X)=0,27  x=media=3 P(X)=0,224 x=media=4 P(X)=0,195
isso ocorre pq o gráfico tá ficando cada vez menos assimétrico e distribuindo seu pico entre os demais valores

Quando tenha Probabilidade condicional com maior ou menor eu subtraio os valores
P(X>a | X>b) = P(X>a-b)
ex: P(X>10 | x>4) = P(X>6) -> probabilidade de algo acontecer 10x dado que já aconteceram 4

-------- exercícios 
1: a média de vezes que um cliente vai na sua loja é 3x na semana. Qual a probabilidade de um cliente ir 5x?
média = 3, x = 5

P(X=5) = e^-3 * 3^5 / 5! = 0,1008

2: a média de vezes que um cliente vai na sua loja é 3x na semana. Qual a probabilidade de um cliente ir exatamente 3x?
media = 3, x = 3

P(X=3) = e^-3 * 3^3 / 3! = 0,22

3: a média de vezes que um cliente vai na sua loja é 8x na semana. Qual a probabilidade de um cliente ir exatamente 8x?
media = 8, x = 8

P(X=3) = e^-8 * 8^8 / 8! = 0,1396

OBS: mesmo a média e o x sendo iguais nos exercícios 2 e 3, os resultados são diferentes

4: a média de vezes que um cliente vai na sua loja é 3x por dia. Qual a probabilidade de um cliente ir 24x na semana?
média_dia = 3
media_semana = 21
x = 24
PRECISA ARRUMAR A MEDIA

P(X=24) = e^-21 * 21^24 / 24! = 0,066

5: a média de vezes que um cliente vai na sua loja é 3x na semana. Qual a probabilidade de um cliente ir mais de 6x?
media = 3, x = 6

P(X>6) = 1 - P(X=0) - P(X=1) - P(X=2) - P(X=3) - P(X=4) - P(X=5)
P(X>6) = 1 - 0,049787 - 0,149361 - 0,22404 - 0,22404 - 0,16803 - 0,1008188 = 0,0839
