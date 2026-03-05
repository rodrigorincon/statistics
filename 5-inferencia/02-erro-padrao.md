# Distribuição Amostral

- É a média das médias
- Cada amostra tem uma média diferente, a distribuição amostral diz **como a média pode variar entre as amostras**
- Podemos tanto definir uma distribuição gráfica (ex: normal) como calcular valores específicos
- Por ser a média das médias, dependendo do contexto pode ser a média final

Ex: nota que as pessoas deram para um filme após saírem da sessão.

| | Sessão 1 | Sessão 2 | Sessão 3 | Sessão 4 |
| ---: | ---: | ---: | ---: | ---: |
| | 6 | 10 | 8 | 5 |
| | 5 | 6 | 8 | 6 |
| | 5 | 7 | 6 | 2 |
| | 4 | 6 | 5 | 4 |
| | 3 | 5 | 5 | 5 |
| média | 4,6 | 6,8 | 6,4 | 4,4 |

**Média final = distribuição amostral = 5,5**

`Nos diz como uma medida muda entre as amostras e nos ajuda a compreender o quanto uma amostra é confiável.`

Sua principal medida é o erro padrão.

# Erro Padrão

- É o desvio padrão da distribuição amostral
- Diz a **precisão da média** e da inferência de uma amostra
	- Diz também o quanto a **média** de diferentes amostras podem variar entre si
- Ocupa uma função parecida que o **desvio padrão** ocupa na população
	- Isso não significa que o desvio não tem valor na amostra, os 2 medem coisas diferentes
	- Desvio = dispersão dentro daquela amostra
	- Erro padrão = precisão da média amostral
- Está ligado ao grau de confiança/precisão que eu busco

`Se eu quero alta precisão, vou buscar uma amostra cujo erro padrão seja baixo, pois sei que os valores dessa amostra estão próximos do real.`

$$EP(media) = \frac{desvio}{\sqrt{n}}$$

- O desvio usado na conta é o **desvio da amostra** (calculado com n-1)
- N é o tamanho da **amostra**
- Erro padrão é sempre menor que o desvio
- **Um valor baixo indica que a média da amostra está próxima da média real**

`Caso o desvio real (da população) seja alto, e por consequência o da amostra também, com um N grande meu erro padrão cai e com isso sei que, mesmo calculando um desvio alto, sei que estou próximo do valor real.`

**Importante: erro padrão não é margem de erro!** Ele é usado para calcular a margem!

---

### Erro padrão e probabilidade

Quando estou calculando probabilidades de amostras (de um grupo, não de um indivíduo), eu troco o desvio pelo erro padrão.

- No cálculo do Z para procurar na tabela, troca desvio pelo erro.
- A probabilidade sempre **cai muito**
- A prob de um grupo fugir da média é maior que a de um indivíduo
	- Todos do grupo precisam coincidentemente tá perto da média ou compensar um único que saia muito

Lembrando que essa troca é **só para amostra** e só quando quer medir a **probabilidade da média de um grupo**! Se for medir para 1 indivíduo usa o cálculo normal.

---

Ex: Uma garrafa de cerveja costuma ter em médoa 330ml com desvio padrão de 4ml. A variação é normal.

**1. Qual a chance de 1 garrafa aleatória ter menos de 325ml?**

media = 330  desvio = 4

$P(X < 325) = 0,1056$ calculado da curva normal usando o desvio padrão

**2. Qual a chance de um engradado aleatório de 6 garrafas ter em média menos de 325ml?**

Em outras palavras, média do engradado ser menor que 325.

media = 330  

$erroPadrao = \frac{desvio}{\sqrt{n}} = \frac{4}{\sqrt{6}} = 1,63$

$P(X < 325) = 0,0011$ calculado da curva normal usando o erro padrão no lugar do desvio

**3. Qual a chance de um engradado aleatório de 12 garrafas ter em média menos de 325ml?**

media = 330  

$erroPadrao = \frac{desvio}{\sqrt{n}} = \frac{4}{\sqrt{12}} = 1,15$

$P(X < 325) = 0,00001$ como aumentou N, a chance de ainda mais garrafas coincidirem perto da média diminui ainda mais

---

### Erro padrão da Proporção

Se queremos medir a proporção (porcentagem) de algo na população, consideramos que a proporção da amostra é igual a da população com o erro padrão abaixo.

$erroParao(p) = \sqrt{ \frac{ p * (1-p) }{n} }$

p = **proporção da amostra**

- Diz a precisão (grau de confiança) da proporção
- Diz também o quanto a **proporção** de diferentes amostras podem variar entre si
- Quanto menor, mais próximo a proporção medida está da real
- O erro é maior se a proporção está próxima de 50% e menor se próxima de 1 ou 0

A distribuição amostral da proporção tende a ser normal, assim como a média (teorema do limite central).

A distribuição amostral da proporção é normal se
- A população é normal **ou**
- O tamanho da amostra é suficientemente grande
	- np > 5 **E** n(1-p) > 5
	- Caso queira ser mais conservador, considerar 10
- **A equação só é válida e só pode ser usada nesse caso, pois ela é derivada do desvio padrão da normal.**

**Lembrando: erro padrão não é margem de erro!** Ele é usado para calcular a margem!

---

**Ex: numa feira foram entrevistadas 2mil pessoas sobre o que as leva até lá e 30% falou que era frutas e verduras. Qual o erro padrão dessa porcentagem?**

p=0,3 n=2000

Tanto $np$ como $n(1-p)$ são maiores que 5, então a distribuição dessa proporção em diversas amostras será normal.

$erroProporcao = \sqrt{ \frac{ 0,3 * (1-0,3) }{2000} } = 0,0102$

# Teorema Central do Limite

- Quando o tamanho da amostra (N) aumenta, a distribuição amostral das médias (média das médias) aproxima-se de uma curva normal
- Se vc fizer uma distribuição das médias de várias amostras vai ter uma dist normal **independente** da forma da distribuição original
	- Porém a amostra precisa ter N >= 30
- Se a população tiver distribuição normal, a dist amostral também terá mesmo que N < 30
- Ou seja, uma distribuição amostral **será normal** se a **população for normal OU tamanho da amostra > 30**!
- Serve para distribuições discretas e contínuas

O mesmo vale para a proporção. A distribuição de uma proporção também tende a ser normal quando N cresce, porém as regras de quando será normal são levemente diferentes (explicado no seu tópico).

- Isso é útil pois te **permite usar as equações da dist normal para sua amostra e calcular o erro padrão.**
- Sem poder considerar a distribuição normal não consigo calcular o erro padrão (tanto da média como da proporção) pois seus cálculos derivam da variância da dist normal

`Você não precisa tirar várias amostras pra fazer uso do teorema. Basta 1 única amostra grande.`

Por isso é melhor uma amostra maior do que muitas amostras!

- Amostras maiores permitem:
	- Poder usar o teorema do limite central e assumir uma distribuição normal
	- Erro padrão baixo
		- Por conta da equação do erro dividir por N
	- Inferências mais precisas
- Enquanto mais amostras permitem (melhor somente em casos muito específicos):
	- Estudar a variabilidade da estimativa
	- Fazer simulação de Monte Carlo
