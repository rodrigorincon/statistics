# PROBABILIDADE CONDICIONAL
- Dado que algo **já aconteceu** ou **já sei de algo relevante**, qual a probabilidade do outro evento acontecer

```
P(A|B) = probabilidade de A acontecer dado que B já aconteceu
```
$$P(A|B) = P(A∩B)/P(B)$$ 
Explicação:
- P(A∩B) é porque ambos precisam acontecer, por isso a intercessão
- Divide por P(B) pois como B já aconteceu, eu diluo sua probabilidade do total
- Como toda prob é menor que 1, ao `dividir eu aumento` as chances de P(A∩B) acontecer
	- Tudo que já aconteceu é dividido para aumentar as chances, mas sem nunca chegar em 1
- Outra forma de entender é: P(A∩B) é o espaço amostral original e P(B) **diminui** esse espaço amostral 

---

**Não pode** trocar a ordem dos eventos, as expressões não são iguais!
$P(A|B) \neq P(B|A)$

---

Se os eventos A e B forem **independentes** (um não tiver nenhuma relação com o outro), então 
$$P(A|B) = P(A)$$ $$P(B|A) = P(B)$$

Do mesmo modo, A e B **são independentes se** 
$P(A|B) = P(A)$ ou $P(B|A) = P(B)$ 
**Basta 1 deles ser igual**

### Exemplos
**Ex1: Jogue um dado. Os eventos "4" e "caiu par" são independentes?**
A = "caiu 4" B = "caiu par"
$P(A|B) = P(4|par) = \frac{1}{3}$ se caiu par então as possibilidades são 2, 4 e 6
$P(A) = P(4) = \frac{1}{6}$
$P(B|A) = P(par|4) = 1$ como a única possibilidade é 4, obviamente par aconteceu
$P(B) = P(par) = \frac{1}{2}$

$P(A|B) \neq P(A)  => \frac{1}{3} \neq \frac{1}{6}$
$P(B|A) \neq P(B)  => 1 \neq \frac{1}{2}$
Portanto os eventos são **dependentes**

**Ex2: Tire uma carta. os eventos "tirar um rei" e "ser de copas" são independentes?**
A = "tirar um rei" B = "tirar uma carta de copas"
$P(A|B) = P(rei|copas) = 1/13$ tem 1 rei entre as 13 cartas de copas
$P(A) = P(rei) = 1/13$ no baralho todo essa é a proporção de reis
Sim, tirar um rei e tirar uma carta de copas são **independentes**

**Ex3: Tire uma carta. Os eventos "tirar um rei" e "tirar um J, Q ou K" são independentes?**
A = "tirar um rei" B = "tirar um J, Q ou K"
$P(A|B) = P(rei|JQK) = 1/3$ rei é uma das 3 opções
$P(A) = P(rei) = 1/13$
$P(B|A) = P(JQK | rei) = 1$ K é o rei
$P(B) = P(JQK) = 3/13$

$P(A|B) \neq P(A)  => \frac{1}{3} \neq \frac{1}{13}$
$P(B|A) \neq P(B)  => 1 \neq \frac{3}{13}$
Portanto os eventos são **dependentes**

**Ex4: total é `{1,2,3,4,5,6}`. A = `{1,2,3}` e B = `{2,3,4}`. A e B são dependentes?**
P(A|B) = P(`{1,2,3}` | `{2,3,4}`) = probabilidade de sair 1, 2 ou 3 dado que saiu ou 2, ou 3 ou 4 
$P(A|B) = \frac{2}{3}$

Repare que ao definir que B aconteceu, o espaço amostral diminui de `{1,2,3,4,5,6}` para `{2,3,4}`

P(B|A) = P(`{2,3,4}` | `{1,2,3}`) = probabilidade de sair 2, 3 ou 4 dado que saiu ou 1, 2 ou 3
$P(B|A) = \frac{2}{3}$

$P(A|B) \neq P(A)  => \frac{2}{3} \neq \frac{1}{2}$
$P(B|A) \neq P(B)  => \frac{2}{3} \neq \frac{1}{2}$

Portanto os eventos são **dependentes** 
`Pois ao dizer que saiu algum numero de B o espaço amostral é reduzido`

## Usando condicional para descobrir a probabilidade sem condições
Com a prob condicional conseguimos calcular P(A) a partir de outro evento
$$P(A) = P(A|B)*P(B) + P(B|\sim{B})*P(\sim{B})$$

- A chance de A acontecer é a média ponderada das probs de A acontecer dado B e B acontecer dado B não ter acontecido
	- Os pesos são as probs das condicionais
- Prob de A é a média entre a chance dele acontecer dado B + a chance dele acontecer caso B não ocorra, usando as probs de B acontecer ou não como peso

---

**Ex: probabilidade de estar grávida sabendo que fez um exame e deu positivo**
A = grávida B = teste positivo  ~B = teste negativo

$P(gravida) = P(gravida|testePositivo) * P(testePositivoAcertar) + P(gravida|testeNegativo) * P(testeNegativoErrar)$

$P(gravida) = P(gravida|testePositivo) * taxaAcertoTeste + P(gravida|testeNegativo) * taxaErroTeste$

**A equação considera falsos positivos e falsos negativos**

**Ex2: probabilidade de eu jogar bola depende se vai chover ou não. Se não chover é quase certo que eu vá, mas se chover só vou se me pilharem muito**

Ou seja: `eu muito provavelmente vou caso tenha sol e talvez caso tenha chuva`.

Suponhamos:
P(futebol | sol) = 0,95 e P(futebol | chuva) = 0,1 
- 10% de chance de me convencerem a jogar na chuva e 95% de chance de eu ir em caso de sol

Olhei a previsão do tempo e tá: P(sol) = 0,9. Portanto P(chuva) = 0,1

$P(futebol) = P(futebol | sol) * P(sol) + P(futebol | chuva) * P(chuva)$
$P(futebol) = 0,95*0,9 + 0,1*0,1 = 0,865$


## DICA PRA USAR A EQUAÇÃO CORRETA
- Se faça as perguntas:
	- O que exatamente estamos medindo? 
	- O que veio antes (causa)? O que veio depois (efeito)?

Ex: caso OJ Simpson. Ele batia na esposa e ela foi encontrada morta espancada. O que calcular?
**A)** Qual a chance de uma mulher ter sido morta pelo marido dado que ele a batia? **(correta)**
B) Qual a chance de uma mulher ser morta pelo marido que a bate?
