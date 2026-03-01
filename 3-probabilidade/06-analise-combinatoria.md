# Análise Combinatória

Ela faz a análise das possibilidades e das combinações possíveis entre um grupo de dados. É muito usada na probabilidade e faz parte de diversas equações de distribuição. Além das distribuições também é usado para resolver problemas mais simples como o paradoxo do aniversário ou "qual a chance de dar 2 coroas em 3 jogadas?". Tem 3 tipos de contas que se pode fazerr: arranjos, combinações e permutações.

## Arranjo

Forma de agrupamento de um `subconjunto` de dados de um conjunto maior. **A ordem importa**! Calcula quantas maneiras diferentes podemos selecionar `e ordenar` P dados de um conjunto N.

Como a ordem importa, se eu tenho que selecionar 2 objetos, {A, B} $\ne$ {B, A}.

**Quantas formas diferentes tenho de agrupar E ORDENAR p desses dados?**.

$$A(n,p) = \frac{n!}{(n-p)!}$$

Lembrando que n > p. N = todo o conjunto e P = nº de vezes que vai pegar um dado.

---

Ex: Quantas senhas de 2 letras distintas podemos formar com as letras A, B, C?

{A.B} {A,C} {B,A} {C,A} {B,C} {C,B} = 6

$A(3,2) = \frac{3!}{(3-2)!} = \frac{6}{1} = 6$

### Arrajo com Repetição

O mesmo elemento pode aparecer em mais de uma posição. Ex: Pegar bolinhas coloridas duma caixa, porém devolve pra dentro da caixa antes de pegar uma nova.

$$Ar(p,n) = n^p$$

---

Ex: Quantas senhas de 2 letras distintas podemos formar com as letras A, B, C, podendo repetir?

{A.B} {A,C} {B,A} {C,A} {B,C} {C,B} {A,A} {B,B} {C,C} = 9

$Ar(3,2) = 3^2 = 9$

## Permutação

Forma de agrupamento de um `conjunto` de dados (nada de subconjunto).

Mesma coisa do arranjo, porém com todos os dados do conjunto. Como usa todos os dados e não um subconjunto, só tem N. Aqui **a ordem importa**!

**Quantas formas diferentes tenho de agrupar todos esses dados?**.

$$P(n) = n!$$

É igual a equação do arranjo, porém como o subconjunto P é todo o conjunto N principal, o denominador fica 1.

$P(3,3) = \frac{n!}{(n-p)!} = \frac{3!}{(3-3)!} = \frac{3!}{(0!} = \frac{3!}{1}$

## Combinação

Forma de agrupamento de um `subconjunto` de dados de um conjunto maior. **A ordem NÃO importa**! Calcula quantas maneiras diferentes podemos selecionar P dados de um conjunto N.

Como a ordem **NÃO** importa, se eu tenho que selecionar 2 objetos, {A, B} = {B, A}.

**Quantas formas diferentes tenho de agrupar p desses dados?**.

$$C(n,p) = \frac{n!}{p!*(n-p)!}$$

Lembrando que n > p. N = todo o conjunto e P = nº de vezes que vai pegar um dado.

### Explicação da equação

Como a ordem não importa, temos de diminuir a quantidade de opções em relação ao arranjo (arranjo > combinação). Pois onde antes tinha vários resultados, agora só tem um.

{ABC} no arranjo pode ser {ABC}, {ACB}, {CAB}, {CBA}.

{ABC} na combinação é só {ABC} mesmo.

Para diminuir dividimos por `p!`, assim só ficamos com os maiores valores de n acima de p. Um exemplo diso pode ser visto no paradoxo do aniversário.

---

Ex: De um grupo de 5 pessoas, 3 serão escolhidas para compor o juri. Quantas formações diferentes temos?

{ABC} {ABD} {ABE} {ACD} {ACE} {ADE} {BCD} {BCE} {BDE} {CDE} = 10

$C{5,3} = \frac{5!}{3!*(5-3)!} = \frac{5*4*3!}{3!*(2)!} = \frac{5*4}{2} = 5*2 = 10$
