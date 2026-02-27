# O que é Probabilidade
- Área da matemática que estuda a aleatoriedade (estudo das chances de algo acontecer)
- Difere da estatística pois busca entender aelatoriedade (e a estatística não envolve aleatoriedade)
- Não é nada intuitivo
- Tenta prever o futuro. Chance de algo vir a acontecer
- Geralmente se tem a população toda

`Aleatório = cada resultado individualmente são incertos, mas tem um padrão por trás`

- Uma probabilidade é sempre entre 0 e 1 incluindo os mesmos (0 <= prob <= 1)
- A soma de todas as probabilidades tem de ser = 1
- Costumamos apresentar a probabilidade de algo acontecer como `P(X=x)`
	- X maiúsculo é o objeto estudado (variável aleatória)
	- x minúsculo é o valor que ele tem (o que aconteceu)


# Conceitos Básicos 

## ESPAÇO AMOSTRAL
- Todos os resultados possíveis da variável
	- Ex: espaço amostral dum dado = {1,2,3,4,5,6}
	- Ex2: espaço amostral duma moeda = {cara, coroa}
- Define os valores que o `x minúsculo` pode ter


## EVENTO
- Subconjunto do espaço amostral
- Resultados possíveis dada uma restrição/condição
	- Ex: jogou um dado e deu par = {2,4,6}
	- Ex2: jogou um dado e deu menor que 3 = {1,2}
	- Ex3: jogou o dado e caiu 6 = {6} -> um evento pode ser 1 único valor
	- Ex4: fazer uma prova. Espaço amostral: {passar, não passar}. Evento: se aprovado: {passar}

Evento é o que queremos calcular. É o nosso `x minúsculo`

## MUTUAMENTE EXCLUSIVO
- 2 eventos que **não possuem** nenhum valor em comum
- 2 eventos são **independentes** entre si

## EVENTO/VARIÁVEL INDEPENDENTE
- Dois eventos A e B são independentes quando um **não afeta** a chance do outro acontecer
	- Ex: A = vestir a meia da sorte. B = meu time ganhar
- **Independentes = mutuamente exclusivos**

A e B são independentes SE `P(A|B) = P(A) ou P(B|A) = P(B)` (basta 1 deles ser igual)
- Será melhor explicado na sessão "condicional"

## VARIÁVEL ALEATÓRIA
- Uma variável **quantitativa** cujo valor depende de algo aleatório (ex: jogar um dado)
- Pode ser discreto ou contínuo
- Espaço amostral define o conjunto de valores que pode ter
- É o `X maiúsculo`


Quando é **discreto**, o espaço amostral é sempre **finito** 
Quando é **contínuo**, o espaço amostral é sempre **infinito**
- Ex: numero de caras em 3 lançamentos de moedas (espaço amostral é 0,1,2 e 3)
- Ex2: números reais (espaço amostral de -infinito a infinito)

Uma var aleatória tem uma função `P(X=valor)` que diz a probabilidade daquele evento X praquele valor
- Forma complicada de dizer que tem uma probabilidade de algo acontecer. 
- Não existe uma fórmula geral pra todas as vars aleatórias, o contexto ou um conjunto de medições vai te fazer definir a probabilidade (tentar aproximar para alguma distribuição conhecida)

Para uma var aleatória **contínua**, como tem **infinitos** valores, a chance de cair um nº específico **tende a zero**
- Ex: qual a pobrabilidade de uma pessoa pesar exatamente 70,567438290193845738229294145 kg?
- P(X=x) = 0 -> probabilidade de X (peso da pessoa) ser x (70,567438290193845738229294145)

Portanto `P(X<= x) = P(X < x)` (o igual pode ser desconsiderado do cálculo)
