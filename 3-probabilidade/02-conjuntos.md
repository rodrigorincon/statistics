
# CONJUNTOS
- Funções básicas para calcular probabilidade

## UNIÃO (U)
- Significa **ou**
- Soma as probabilidades dos eventos e subtrai a interseção (pra não contar 2x esses valores)

$$P(A U B) = P(A) + P(B) - P(A ∩ B)$$

Ex: total é `{1,2,3,4,5,6}`. A = `{1,2,3}` (metade) B = `{2,3,4}` (metade)
- A união não pode ser 1 mesmo cada um sendo metade, pois tem valores em comum
- A U B = `{1,2,3,4}` = 4/6 (não repete a interseção)
- Se não subtrair a interseção ficaria `{1,2,3,2,3,4}`
$P(A U B) = 1/2 + 1/2 - 2/6 = 4/6$

## INTERCESSÃO (∩)
- Significa **E**
- Pega só o que é igual nos 2
- Multiplica as probabilidades dos eventos
- **Há duas equações, uma quando as vars são independentes e outra quando não**

**PARA VARS INDEPENDENTES**
$$P(A ∩ B) = P(A) * P (B)$$ 

Ex: Jogamos um dado e uma moeda. A = dado é B = moeda. A = `{1,2,3,4,5,6}` e B = `{cara,coroa}`. Qual a chance de sair um 2 e cara?
$P(A=2) = \frac{1}{6}$
$P(B=cara) = \frac{1}{2}$
$P(A ∩ B) = \frac{1}{6} * \frac{1}{2} = \frac{1}{12}$ 

**PARA VARS DEPENDENTES**
$$P(A ∩ B) = P(A|B) * P(B) = P(B|A) * P(A)$$
Essa equação vem da equação da probabilidade condicional, passando o divisor pro outro lado.

Ex: total é `{1,2,3,4,5,6}`. A = `{1,2,3}` (metade) B = `{2,3,4}` (metade)
A ∩ B = `{2,3}` = 1/3  (**valor correto**)
$P(A ∩ B) = P(A) * P(B) = \frac{1}{2} * \frac{1}{2} = \frac{1}{4}$ 
Deu diferente porque `não são independentes/mutuamente exclusivos`

Forma certa de resolver esse:
P(A|B) = P(`{1,2,3}` | `{2,3,4}`) = **qual a probabilidade de ter saído 1, 2 ou 3 dado que saiu 2, 3 ou 4** 
P(A|B) = 2/3 (2 dos 3 números presentes em B existem em A)
$P(A ∩ B) = P(A|B) * P(B)$
$P(A ∩ B) = \frac{2}{3} * \frac{1}{2} = \frac{2}{6} = \frac{1}{3}$ (agora o cálculo deu certo!)

## COMPLEMENTO (~)
- Significa **NOT**
- Tudo que está fora do subconjunto do evento (tudo exceto o evento)
- Igual a 1 - evento

$$P(\sim{A}) = 1 - P(A)$$

## DIFERENÇA (\\)
- Significa **MAS**
- Pertencem a um conjunto, mas não pertencem a outro
- Subtrai a intercessão do evento

**PARA VARS DEPENDENTES**
$$P(A \backslash B) = P(A) - P(A ∩ B)$$

**PARA VARS INDEPENDENTES**
$$P(A \backslash B) = P(A)$$
Visto que, por serem independentes, A ∩ B = `{}` (vazio, sem interseção).

# Exercícios

### 1: ao jogar 3 moedas, qual a chance de nenhum dar coroa?

Espaço Amostral:
- cara, cara, cara (cumpre)
- cara, cara, coroa
- cara, coroa, cara
- cara, coroa, coroa
- coroa, cara, cara
- coroa, cara, coroa
- coroa, coroa, cara
- coroa, coroa, coroa
**8 possibilidades**

Evento: nenhuma coroa
olhando o espaço amostral, só 1 caso cumpre
Resposta: 1/8

Por equação:
nenhuma coroa = 3 caras 
Evento = 3 caras
P(cara) = 1/2
$P(3 caras) = cara * cara * cara = 1/2*1/2*1/2 = 1/8$

### 2: um banco pergunta para 200 clientes qual tipo de conta deles. 70 possuem conta corrente, 120 poupança, 50 ambas e 60 nenhuma. Qual a probabilidade de alguém aleatório desse grupo:

Espaço amostral: `{ter conta corrente, ter conta poupança, ter ambas, não ter nenhuma}`
P(cc) = $\frac{70}{200}$
P(poup) = $\frac{120}{200}$
P(ambos) = $\frac{50}{200}$
P(nenhum) = $\frac{60}{200}$

#### 2.1 ter conta corrente?
$P(cc) = \frac{70}{200}$

#### 2.2 não ter conta corrente?
$P(~cc) = 1 - P(cc) = 1 - \frac{70}{200} = \frac{130}{200}$

#### 2.3 ter conta corrente E poupança?
$P(ambos) = \frac{50}{200}$ 
OBS: não posso usar a equação P(cc ∩ poup) = P(cc) * P(poup) pois são variáveis dependentes

#### 2.4 ter conta corrente OU poupança?
$P(cc U poup) = P(cc) + P(poup) - P(cc ∩ poup) = \frac{70}{200} + \frac{120}{200} - \frac{50}{200} = \frac{190}{200} - \frac{50}{200} = \frac{140}{200}$

#### 2.5 ter ambas as contas ou nenhuma?
$P(ambos U nenhum) = P(ambos) + P(nenhum) - P(ambos ∩ nenhum) = \frac{50}{200} + \frac{60}{200} - 0 = \frac{110}{200}$

#### 2.6 ter conta corrente mas não ter poupança?
Conta corrente SEM itersessão com poupança
$P(cc) - P(cc ∩ poup) = \frac{70}{200} - \frac{50}{200} = \frac{20}{200}$

OBS: a gente NÃO pode transformar P(cc ∩ poup) em P(cc) * P(poup) pq as vars são dependentes (se a conta for uma coisa, ela não pode ser outra)
