# AGRUPAMENTO DE FREQUENCIAS

Podemos agrupar as frequências para facilitar a visualização e compreensão dos mesmos

Exemplo: tempo de corrida numa maratona

| Tempo | Quantidade | Freq acumulada absoluta | Freq acumulada relativa |
| ---: | :---: | :---: | :--- |
| 1:38 | 1 | 1 | 0,037|
| 1:39 | 1   |2 | 0,074 |
| 1:41 | 2   |4 | 0,148 |
| 1:42 | 2   |6 | 0,222 |
| 1:43 | 3   |9 | 0,333 |
| 1:44 | 2   |11 | 0,407 |
| 1:45 | 3   |14 | 0,518 |
| 1:46 | 5   |19 | 0,703 |
| 1:47 | 2   |21 | 0,777 |
| 1:48 | 2   |23 | 0,851 |
| 1:51 | 2   |25 | 0,926 |
| 1:52 | 1   |26 | 0,963 |
| 1:56 | 1  | 27 | 1 |
**Total corredores: 27**

Quando se tem centenas ou milhares de valores pra var (ex: o tempo pra completar a corrida) pode ser melhor agrupar pra melhor visualizar.

Existem 3 formas de agrupar: valores definidos, raiz quadrada e regra de Sturges.

**1. Valores Definidos**
- Tiro da minha cabeça ou dependendo do contexto podem existir valores ou formas que se encaixem mais
- Exemplos: 
	- Horário de acesso: agrupar de hora em hora ou em turnos (manhã, tarde e noite)
	- Mercado financeiro gosta de agrupar em nºs redondos (o a 100, 100 a 200...)
	- Idade podemos dividir por faixa-etarias do IBGE (menos de 18, 18 a 25, 25 a 34...) 
	- Idade podemos dividir segundo classificação indicativa (contexto de cinema): 0 -10, 10 a 14, 14 a 16, 16 a 18, +18)
	- **Sempre** considere o contexto pra saber como agrupar e se usar valor definido faz mais sentido que outras opções

**2. Raiz Quadrada (principal)**
- Usa a raiz quadrada do total de medidas diferentes pra definir quantos grupos terá
```[python]
x = uniq(tempos) # no exemplo, 13
num_grupos = sqrt(x) # no exemplo, 3,6 portanto 4
```
- Por fim calcula a distância entre os grupos
```[python]
amplitude = max - min  # no caso  1:56 - 1:38 = 18 min
dist = amplitude / num_grupos #  no caso 18/4 = 4,5 portanto 5
```
- As distâncias sempre serão iguais, ou seja, divide em espaços iguais
- Ex: os grupos seriam
	- De 1:38 a 1:43 (sempre descosiderando a borda superior, ñ inclui os 1:43)
	- De 1:43 a 1:48 (sempre considerando a borda inferior, inclui os 1:43)
	- De 1:48 a 1:53
	- De 1:53 a 1:58

**3. Regra de Sturges (muito usado no meio acadêmico, e só)**
- Número de grupos definido pela equação `1 + 3,3*log(x)` onde x é o nº de medidas diferentes
```[python]
x = uniq(tempos) # no exemplo, 13
num_grupos = 1 + 3,3*log(x) # no exemplo, 4,67 portanto 5
```
- Por fim calcula a distância entre os grupos
```[python]
amplitude = max - min # no caso  1:56 - 1:38 = 18 min
dist = amplitude / num_grupos # no caso 18/5 = 3,6 portanto 4
```
- As distâncias também sempre serão iguais, ou seja, divide em espaços iguais
- Ex: os grupos seriam
	- De 1:38 a 1:42 (segue a msm regra da raiz quadrada de ñ contar a borda superior)
	- De 1:42 a 1:46
	- De 1:46 a 1:52
	- De 1:52 a 1:56
	- De 1:56 em diante (como ñ inclui a borda superior tem de ter um grupo só pra ele)

**A forma de calcular as distâncias na raiz quadrada e no Sturges é igual, só o que muda é a quantidade de grupos**
