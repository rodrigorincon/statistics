# TAMANHO DA AMOSTRA

- O ideal seria cada tipo de amostragem ter sua fórmula, mas isso não acontece
- Então usamos a equação da amostragem aleatória simples
- Usamos a equação da **margem de erro da proporção**
- Há um tamanho máximo também, aonde aumentar além disso não agrega valor aos resultados

### Como calcular

- Primeiro passo é definir o nível de confiança e a margem de erro que quero
	- Chamando z de intervalo = IC
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

Equação da margem de err da proporção:

$margemErro = z * \sqrt{ \frac{p * (1-p)}{n} }$

Chamando margemErro de ME, z de IC e p = 0,5

$ME = IC * \sqrt{ \frac{0,5 * (1-0,5)}{n} } = IC * \sqrt{ \frac{0,25)}{n} }$

Passando ME e IC para o mesmo lado e retirando a raiz

$(\frac{ME}{IC})^2 = \frac{0,25}{n}$

Subindo N pro denominador

$(\frac{IC}{ME})^2 = \frac{n}{0,25}$

Passa 0,25 pro outro lado

$n = 0,25 * (\frac{IC}{ME})^2 = \frac{1}{4} * (\frac{IC}{ME})^2 = (\frac{1}{2})^2 * (\frac{IC}{ME})^2$

Juntando as frações

$n = (\frac{IC}{2ME})^2$

---

**Ex: Para uma população de 2mil pessoas, com uma confiança de 95% e 5% de margem de erro, qual o tamanho da amostra?**

IC=1,96 (valor de z para 0,95) ME=0,05 N=2000

$n = (\frac{1,96}{2 * 0,05})^2 = (\frac{1,96}{0,1})^2 = 19.6^2 = 384.16$

$nFinal = \frac{2000 * 384.16}{2000 + 384.16} = \frac{768320}{2384,16} = 322$

## OBSERVAÇÃO

Chega um momento que a população é tão grande que a última parte é desnecessária, pois é tão grande que pro cálculo é como se fosse infinito.

Por volta de 100 e 200 mil a amostra cresce muito pouco.

## TAMANHO MÁXIMO

