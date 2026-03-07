# P-VALOR

- É a **probabilidade de encontrarmos um resultado dado que Ho é verdadeiro**.
- p-valor = P(Ho).
- Como queremos provar Ha e P(Ha) = 1 - P(Ho), **quanto menor p-valor melhor**
	- Especificamente tem de ser menor que alfa (como explicado mais abaixo).

### Descrição formal

É a probabilidade de observar os resultados atuais (ou mais extremos) se Ho é verdadeiro

- Com mais extremos queremos dizer algo menor/maior, na direção que confirma Ho
- **P-valor é a chance para todos os valores que provam Ho**.
	- Lembrando que Ho representa o cenário atual

Posso descrever p-valor como:

- P(dados serem iguais ou mais extremos que os que fazem Ho ser verdade | Ho)
- Probabilidade dos dados dizerem algo **dado que** Ho é verdadeiro
- Como assume que Ho é verdadeiro, p-valor é sempre uma prob condicional

### Sobre o cálculo

- A fórmula de calcular o p-valor varia com cada teste
- Cada teste serve para um contexto diferente. É preciso conhecer os testes e entender bem o seu contexto
- O cálculo precisa considerar o tipo de cauda (unicaudal a esquerda, direita ou bicaudal)
	- O tipo de cauda influencia na forma do cálculo
- Alfa não é usado no cálculo do p-valor, só na tomada de decisão final
- O valor de p-value não é a probabilidade de alguma hipótese ser verdadeira

---

**Exemplo**: 

Queremos provar que uma moeda é viciada. É considerada viciada se 30% ou menos derem o mesmo resultado.

Ho = prob de dar cara <= 30%, logo p-valor = P(cara) <= 0,3

Significado da frase `"É a probabilidade de observar os resultados atuais (ou mais extremos)"`

- Resultados atuais = P(cara) = 0,3
	- A moeda dar exatamente o que se espera de uma moeda viciada (30%)
- Resultados mais extremos = P(cara) < 0,3
	- A moeda dar valores ainda piores do que se espera de uma moeda viciada (20%, 10%...)

# TOMADA DE DECISÃO

- Se **p-valor < alfa** = Rejeite Ho (**H1 é verdadeiro**)
- Se **p-valor >= alfa** = Não Rejeite Ho (**inconclusivo**)

### Significado

- p-valor é a probabilidade de todos os valores que provam Ho (probabilidade de Ho acontecer)
- Alfa é a nossa taxa de erro aceitável

Logo podemos descrever a regra `p-valor < alfa = Rejeite Ho` como:

- **A probabilidade de Ho acontecer tá dentro da nossa margem de erro**

E podemos descrever a regra `p-valor > alfa = Não Rejeite Ho` como:

- **Não sabemos se essa amostra representa a população ou se foi um caso isolado porque nossa taxa de erro é muito grande**
- O resultado é muito provável de ter ocorrido ao acaso, mesmo que Ho seja verdade. Portanto não há evidências suficientes para rejeitar Ho.

Não podemos afimar que Ho é verdade porque testamos P(dados | Ho), não P(Ho | dados).

---

### Exemplo:

Uma pizzaria diz que seu tempo de entrega é, em média, menor que 30 minutos. Analisamos 30 entregas, com média 32 minutos e desvio padrão de 8 minutos.

**1. Quais as hipóteses, seus significados e cauda?**

- H1: media > 30
- Ho: media <= 30
- Significados:
	- Rejeitar Ho: O tempo médio de entrega é maior que 30 minutos. Vou boicotar.
	- Não Rejeitar Ho: Não tenho evidências para concluir que o tempo médio de entrega é maior que 30 minutos.
- Teste unicaudal a direita.

OBS: não posso falar que o tempo médio é menor que 30 como explicado no arquivo 2.

**2. Escolhi uma alfa de 5%. O que isso significa?**

Significa que tenho 5% de chances de boicotar a pizzaria injustamente.

**3. Qual meu p-valor usando o teste t?**

Cálculo do teste t:

$t = \frac{mediaAmostra - valorComparacao}{ \frac{desvioAmostra}{\sqrt{n}} }$

Portanto

$t = \frac{32 - 30}{ \frac{8}{\sqrt{30}} } = 1,37$

- Procuramos na tabela T com grau de significância 29 (n-1) qual alfa dá o valor calculado de t.
- Vemos que na linha de gl=29 o valor 1,37 está entre os alfas 0,1 e 0,05 (mais próximo de 0,1)
- Então p-valor é pouco menor que 0,1
- Para um valor exato, só usando software
- Usando software, chegamos a **p-valor=0,09**

**4. Qual a conclusão final?**

Como p-valor > alfa, então então **não devemos rejeitar Ho**

Portanto,a resposta final é "Não tenho evidências para concluir que o tempo médio de entrega é maior que 30 minutos".
