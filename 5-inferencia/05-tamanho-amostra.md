# TAMANHO DA AMOSTRA

- O ideal seria cada tipo de amostragem ter sua fórmula, mas isso não acontece
- Então usamos a equação da amostragem aleatória simples
- Usamos a equação da **margem de erro da proporção**
- Há um tamanho máximo também, aonde aumentar além disso não agrega valor aos resultados

## Cálculo pela margem de erro

- Primeiro passo é definir o **nível de confiança e a margem de erro** que quero
	- Através do nível de confiança encontramos o intervalo de confiança
		- Usamos as tabelas ou a equação da distribuição relacionada
		- Chamando a de intervalo = IC
	- Chamando margem de erro = ME
- Definimos a maior proporção possível (p = 0,5)
	- Caso você tenha uma ideia da proporção de algum dos objetos estudados, troque p pela proporção que se tem
	- O uso duma proporção já conhecida é quando já foi feita uma pesquisa anterior ou se tem algum conhecimento empírico sobre os dados (**pode incluir viés**)
	- Usar p = 0,5 é bom quando não se conhece a variabilidade ou se quer um resultado mais conservador

$$n = (\frac{IC}{2ME})^2$$

- Caso o tamanho da população seja conhecida ou pequena, adiciona um último passo

$$nFinal = \frac{N * n}{N+n}$$

Onde n é a resposta do cálculo anterior e N é o tamanho da população.

### Prova

Equação da margem de erro da proporção:

$margemErro = z * \sqrt{ \frac{p * (1-p)}{n} }$

Chamando margemErro de ME, z de IC e p = 0,5

$ME = IC * \sqrt{ \frac{0,5 * (1-0,5)}{n} } = IC * \sqrt{ \frac{0,25}{n} }$

Passando ME e IC para o mesmo lado e retirando a raiz

$(\frac{ME}{IC})^2 = \frac{0,25}{n}$

Subindo N pro denominador

$(\frac{IC}{ME})^2 = \frac{n}{0,25}$

Passa 0,25 pro outro lado

$n = 0,25 * (\frac{IC}{ME})^2 = \frac{1}{4} * (\frac{IC}{ME})^2 = (\frac{1}{2})^2 * (\frac{IC}{ME})^2$

Juntando as frações

$n = (\frac{IC}{2ME})^2$

### Exemplos

**1: Para uma população de 2mil pessoas, com uma confiança de 95% e 5% de margem de erro, qual o tamanho da amostra?**

IC=1,96 (valor de z para 0,95) ME=0,05 N=2000

$n = (\frac{1,96}{2 * 0,05})^2 = (\frac{1,96}{0,1})^2 = 19.6^2 = 384.16$

$nFinal = \frac{2000 * 384.16}{2000 + 384.16} = \frac{768320}{2384,16} = 322$

---

**2: Qual a quantidade de pessoas que devo entrevistar para uma pesquisa eleitoral com 95% de confiança e 2% de margem de erro?**

IC=1,96 (valor de z para 0,95) ME=0,02

$n = (\frac{1,96}{2 * 0,02})^2 = (\frac{1,96}{0,04})^2 = 49^2 = 2401$

## TAMANHO NÃO MUDA CONFORME A POPULAÇÃO

Perceba pelo exemplo anterior que a quantidade de pessoas entrevistadas não muda se a população cresce. Isso acontece porque a `precisão estatística depende da variância` dos dados, e não da quantidade total de indivíduos. Por isso a única variável que afeta é o desvio padrão (que está implícito no z-score do intervalo de confiança). 

Para uma população normalmente distribuída o desvio padrão é bem conhecido, por isso é mais importante conhecer a distribuição da população (ou estimá-la através dum teste de hipótese ou likelihood) do que o tamanho dela. O teorema do limite central também é crucial aqui para podermos definir que o desvio da amostra representa o desvio da população.

## TAMANHO MÁXIMO

Chega um momento que aumentar a amostra não aumenta tanto a resposta da pesquisa, atingindo um **ponto de saturação**. A partir desse limite, a margem de erro não diminui significativamente e adicionar novos dados apenas gera custos ou tempo desperdiçado sem aumentar a precisão.

A margem de erro cai drasticamente no início (passar de 50 para 100 pessoas muda muito o resultado). Mas a curva começa a tender para uma margem de erro mínima e aumentar além disso não traz efeitos significativos. Passar de 1500 para 3000 pessoas exige o dobro de esforço, mas melhora a margem de erro em frações mínimas. `Esse limite é o tamanho da amostra calculado pela equação acima`.

Quando falamos de **pesquisa qualitativa** (com **poucas pessoas ou de resposta aberta ou escolher dentre as opções**) o cálculo pode não fazer tanto sentido, devendo ter um consenso de quando parar. Nesse caso faz-se a pesquisa com o número possível de dados e anota os resultados. Depois continua buscando por novos dados/entrevistados. `Deve-se parar quando uma nova leva de dados/entrevistados não traz nenhuma nova resposta ou mudança significativa nas proporções das respostas`. Caso queira ser mais conservador por seguir a regra de 2 coletas seguidas sem alteração nos resultados.