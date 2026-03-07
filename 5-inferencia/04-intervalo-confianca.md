# MARGEM DE ERRO

- É a faixa aonde o valor medido pode estar
- O valor real está dentro duma faixa que varia em volta do valor da amostra
- Calculado a partir do erro padrão

Margem de erro da média:

$margemErroMedia =  t * ErroPadrao(media)$

Margem de erro da proporção:

$margemErroProp =  z * ErroPadrao(prop)$

Aonde $z = \frac{x - media}{desvio}$ e t = valor na tabela t-score

- Porém não usaremos essa equação de Z. Ao invés disso usaremos a tabela z-score
- A partir do nivel de confiança, fazemos o caminho contrário do habitual para chegar no valor de z
	- Usamos o nível de confiança para saber o valor do meio da tabela e a partir dele encontrar os valores dos cantos, que compõem o valor final
- **Z é o da equação, não o valor encontrado no meio da tabela**
- Ou seja z é quantos desvios padrões você está distante da média
	- Em outras palavras, margem de erro é **distanciaDesvio * erroPadrão**
- O intervalo para outras medidas exigem técnicas mais avançadas (como simulações ou bootstrap) não abordadas aqui

---

### T-score na margem da média

**No caso da média, usa a tabela T-score ao invés da Z-score, mas o processo é o mesmo.**

- O T-score diminui a imprecisão trazida ao usar o desvio da amostra ao invés da população
	- Como T-score é sempre menor que o Z-score, minimiza a incerteza do erro padrão (representada pelo desvio da amostra)
	- T-score se ajusta ao tamanho da amostra (por ter N-1 como um dos params) e com isso é mais precisa para amostras pequenas (N<30)
- Para N grande, a tabela T se aproxima da Z, ficando a mesma coisa

---

### O Que afeta a Margem de Erro

- Tamanho da amostra (N) 
	- Quanto maior, menor a margem
- Nível de confiança (z ou t)
	- Quanto maior, maior a margem

Logo, **queremos uma amostra grande e um nível de confiança pequeno.**

---

### Restrições

**Só posso usar esse método caso a distribuição amostral for normal**
- N > 30 para média
- np E n(1-p) > 5 ou 10 (a depender do contexto) para proporções
	- Quanto mais rigoroso, maior

---

### Exemplos

**1. Quero 95% de confiança na minha pesquisa. Quanto deve ser meu z?**

**1.1 Usando a tabela unicaudal**

- Como a tabela unicaudal só considera 1 lado, tenho dividir por 2 = 95/2 = 47,5%
- Caço na tabela z unicaudal aonde tem o resultado 0,475
- O mais próximo que achei foi 0,475
- O valor de Z para essa posição é 1,96

**1.2 Usando a tabela bicaudal**

- alfa = 1 - 0,95 = 0,05
- Como esse valor representa as 2 caudas, divido por 2 = 0,025
- pego o complementar (área coberta) = 1 - 0,025 = 0,975
- Caço na tabela z bicaudal aonde tem o resultado 0,975
- O mais próximo que achei foi 0,975
- O valor de Z para essa posição é 1,96

**2. Quero 75% de confiança na minha pesquisa. Quanto deve ser meu z?**

**2.1 Usando a tabela unicaudal**

- Como a tabela unicaudal só considera 1 lado, tenho dividir por 2 = 75/2 = 37,5%
- Caço na tabela z unicaudal aonde tem o resultado 0,375
- O mais próximo que achei foi 0,3749
- O valor de Z para essa posição é 1,15

**2.2 Usando a tabela bicaudal**

- alfa = 1 - 0,75 = 0,25
- Como esse valor representa as 2 caudas, divido por 2 = 0,125
- pego o complementar (área coberta) = 1 - 0,125 = 0,875
- Caço na tabela z bicaudal aonde tem o resultado 0,875
- O mais próximo que achei foi 0,8749
- O valor de Z para essa posição é 1,15

**3. Quero 30% de confiança na minha pesquisa. Quanto deve ser meu z?**

**3.1 Usando a tabela unicaudal**

- Como a tabela unicaudal só considera 1 lado, tenho dividir por 2 = 30/2 = 15%
- Caço na tabela z unicaudal aonde tem o resultado 0,15
- O mais próximo que achei foi 0,1517
- O valor de Z para essa posição é 0,39

**3.2 Usando a tabela bicaudal**

- alfa = 1 - 0,3 = 0,7
- Como esse valor representa as 2 caudas, divido por 2 = 0,35
- pego o complementar (área coberta) = 1 - 0,35 = 0,65
- Caço na tabela z bicaudal aonde tem o resultado 0,65
- O mais próximo que achei foi 0,6517
- O valor de Z para essa posição é 0,39

# INTERVALO DE CONFIANÇA

- É a união do valor medido com a margem de erro
- $valor \pm margemErro = valor \pm z * erroPadrao$

---

### Exemplo

**1. Antes de iniciar uma ação nova, um banco gostaria de saber a proporção de clientes que aceitariam a oferta. Eles enviaram a oferta para mil pessoas e 140 aceitaram. Qual o intervalo de confiança que vão aceitar a oferta com 95% de precisão?**

prop = 140/1000 = 0,14

z (dado 95% de confiança) = 1,96

Intervalo = $prop \pm z * \frac{prop * (1-prop)}{n} = 0,14 \pm 1,96 * \frac{0,14 * (1-0,14)}{1000} = 0,14 \pm 0,0215012$ = entre 0,1185 e 0,1615

**2. O banco pesquisou o saldo bancário desses 140 que aceitaram para ver se valeria a pena. A média era 1990,50 com desvio padrão de 2833,33. Qual o intervalo de confiança do saldo bancário deles, com 95% de confiança?**

- media=1990,50  desvioAmostra=2833,33 N=140
- Como quer ver o intervalo da média, usar a tabela T
- alfa = 1 - confiança = 1 - 0,95 = 0,05
- Procurar na tabela T o valor pra grau=139 e alfa=0,025 (na unicaudal) ou alfa=0,05 (na bicaudal)
- T = 1,977

intervalo = $media \pm t * \frac{desvioAmostra}{\sqrt{n}} = 1990,50 \pm 473,41$ = entre 1.517 e 2.464


# NÍVEL DE CONFIANÇA

- É o grau de certeza que o seu valor está dentro da margem de erro
- Com a amostra, não temos certeza do valor real (da população)
	- Mas temos X% de certeza que está numa certa faixa
- Se repetir o teste mais vezes (pegar mais amostras), em X% delas a média estará nesta faixa
- Normalmente é usado os níveis de 90%, 95% e 99%
	- Em diferentes contextos os níveis comuns podem mudar
	- Não tem como definir 100% de certeza de nada
- **Quanto maior o nível de confiança:**
	- Maior a amostra
	- Mais caro e difícil 
	- **maior a margem de erro**

---

### Relação confiança e margem de erro

Se a margem de erro é maior, eu tenho mais certeza que meu valor está lá dentro.

```
Ex: Tenho 99,99% de certeza que vou acordar entre 1 da manhã e 23:59

- O nível de confiança é alto justamente porque a margem é alta
- É difícil errar quando sua margem é gigantesca
```

Quem define o grau de confiança na margem é o z/t. Ele vem das tabelas (o nível de confiança é um dos parâmetros em ambos).

- No Z, o nível de confiança é o valor tanto na linha como na coluna
- No T, é o complementar do alfa

**Em resumo, precisamos escolher entre confiança e precisão.**

---

### Alfa

O **oposto** do nível de confiança é o **alfa**, a % de erro aceita na estimativa.

$$alfa = 1 - confianca$$

---

### Z-score

- Nível de confiança vem da tabela z-score.
	- É o **valor encontrado no meio da tabela**
- É o total da área coberta da curva normal
- **Só posso usar esse método caso a distribuição amostral for normal**

Assim como a faxia coberta pelo desvio padrão da normal também vem do z-score, então dizer que tenho 95% de confiança significa que 95% da área da curva normal está coberta. O que significa que cobri até X desvios padrões que dão esse valor.

**Exemplo:**
- 2 desvio padrões é 0,9544, logo 2 desvios padrões cobertos dá 95,44% de nível de confiança
- 95% de confiança é ligeiramente abaixo de 2 desvios padrões, dando 1,96 desvios padrões

---

### Forma correta de se referir

Sendo bem puritano, **é errado dizer** `"A probabilidade que a média esteja nessa faixa é de 95%"`. Isso porque a média populacional é fixa e a frase dá a entender que ela varia de acordo com a amostra

**É correto dizer** `"Tenho 95% de confiança que a média está nessa faixa"`. Apesar de parecer a mesma coisa, assim deixa claro que a média é fixa.

**É correto dizer** `"Se repetirmos o teste diversas vezes, em 95% das vezes a média estará nessa faixa"` (estaremos corretos 95% das vezes).
