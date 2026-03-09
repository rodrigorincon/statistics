# TESTE Z

- Serve para **testar proporções**
- Compara a proporção tanto com um valor específico quanto com outra proporção
- Serve apenas para **comparar até 2 proporções**
	- Acima disso precisa ser o Qui-Quadrado

# PREMISSAS

- A amostra deve seguir uma distribuição normal 
	- n * p > 10 e n * (1-p) > 10
- Os dados devem ser binários (binomial)
- Os dados devem ser independentes
- **Variância da população precisa ser conhecido**

---

**OBSERVAÇÃO**

- Caso os dados não sejam normais, posso tentar transforma-los para base logaritma
- Assim as discrepâncias são amenizadas e os dados ficam mais agrupados (menor amplitude)
- Porém preciso testar a normalidade nos dados transformados para ver se agora eles são normais
- A partir daí, tudo deve ser transformado igual (as outras amostras, os valores de comparação...)

# Teste para 1 proporção

- Compara a propoção da amostra com um valor específico
- proporcaoAmostra é representado por p
- valorComparacao é representado por p0

$$z = \frac{proporcaoAmostra - valorComparacao}{ \sqrt{ \frac{valorComparacao(1-valorComparacao)}{n}} }$$

É a mesma equação do teste T para 1 média, trocando a variância pelo p(1-p). p é a proporção com a qual queremos comparar.

**O p-valor será o valor de alfa na tabela z.** 

- O z calculado acima é o valor no meio da tabela
- Temos de fazer o caminho inverso para, a partir do valor final, chegar no valor z0 (nas laterais da tabela).
- Para bicaudal, p-valor será o resultado final * 2

### Exemplo

**1. Uma loja quer avaliar se a taxa de devolução de produtos é maior que 5%. Coletaram uma amostra de 500 pedidos e viram que 30 deles foram devolvidos. Alfa de 5%.**

p = proporcaoAmostra = 30/500 = 0,06

valorComparacao = 5% = 0,05

PREMISSAS:

Cada dado coletado é uma var binária (devolve ou não devolve).

n * p > 10 -> 500 * 0,06 = 30 > 10

n * (1-p) > 10 -> 500 * (1-0,06) = 500 * 0,94 = 470 > 10

HIPÓTESES

Ho: proporção de devoluções é menor ou igual que 5% -> p $\le$ 0,05

Ha: proporção de devoluções é maior que 5% -> p > 0,05

$z = \frac{0,06 - 0,05}{ \sqrt{ \frac{0,05(1-0,05)}{500}} } = 1,03$

p-valor = P(Z > 1,03) = 1 - P(Z < 1,03) = 1 - 0,8485 = 0,1515

p-valor > alfa, logo `não rejeitamos Ho`.

# Teste para 2 proporções

- **Usado em testes A/B**
- Além das 2 proporções usamos também a proporção total (médias das 2 proporções)
- É equivalente ao teste de independência do Qui-Quadrado

$$z = \frac{propA - propB}{\sqrt{ propTotal(1-propTotal)(\frac{1}{nA} + \frac{1}{nB}) }}$$

**O p-valor será o valor de alfa na tabela z.** 

- O z calculado acima é o valor no meio da tabela
- Temos de fazer o caminho inverso para, a partir do valor final, chegar no valor z0 (nas laterais da tabela).
- Para bicaudal, p-valor será o resultado final * 2

É a mesma equação para 1 proporção, porém dividindo a média das proporções pelo tamanho de cada amostra ao invés de dividir a única proporção que temos pelo tamanho da única amostra.

Repare que não há variância na fórmula, pois por se tratar de proporção, a variância não é relevante.

### Exemplo

**1. Uma loja deseja comparar qual layout gerou mais conversões. O alfa é 0,05. Os dados foram os seguintes:**

Layout A: 2mil visitantes, 180 conversões. pA=0,09

Layout B: 2200 visitantes, 250 conversões. pB=0,1136

Ho: pA = pB 

Ha: pA $\ne$ pB

pTotal = $\frac{180+250}{2000+2200} = 0,1024$

$z = \frac{pA - pB}{\sqrt{ pTotal(1-pTotal)(\frac{1}{nA} + \frac{1}{nB}) }} = \frac{0,09 - 0,1136}{\sqrt{ 0,1024(1-0,1024)(\frac{1}{2000} + \frac{1}{2200}) }} = -2,52$

P(Z < -2,52) = P(Z > 2,52) = 1 - P(Z < 2,52)

O teste é bicaudal. Na tabela Z bicaudal P(Z < 2,52) = 0,9941

p-valor = 2 * P(Z < -2,52) = 2 * (1 - 0,9941) = 0,0118
