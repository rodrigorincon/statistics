# DISTRIBUIÇÃO PROBABILISTICA

- Descreve graficamente como os valores se distribuem
- Possuem uma equação que descreve com qual frequencia a probabilidade dar tal valor
- Algumas distribuições só servem para vars discretas e outras só pra continuas

# DISTRIBUIÇÕES DISCRETAS

Neste arquivo descrevemos as distribuições mais simples e menos usadas, para nas seguintes entrar nas mais complexas.

## QUANDO USAR CADA UMA

- Binomial
	- Quando tempo não é importante (em qualquer momento o resultado é o mesmo)
	- Quando temos um nº fixo de tentativas e saber a chance de uma quantidade de sucessos
- Poisson 
	- Quando contamos quantos eventos acontecem num período ou local
	- Quando está avaliando fluxo de entrada de casos por tempo (chamadas chegando num servidor, pessoas numa fila)


## DISTRIBUIÇÃO UNIFORME

- Todos os resultados tem **a mesma chance** de acontecer

$$P(X=x) = \frac{1}{n}$$
Onde n é o tamanho do espaço amostral.

Ex: jogada de um dado.

OBS: A probabilidade **não depende de x**.

No mundo real isso é raro de acontecer, mas pode ser **próximo o suficiente** da uniforme, a ponto de poder arredondar.

- Moda = todos (todos são igualmente comuns)
- Esperança = média = $\frac{max+min}{2}$
- Variância = $\frac{(max-min)^2}{12}$
- Desvio padrão = $\sqrt{variancia} = \frac{max-min}{\sqrt{12}}$

---

Ex: Jogada de dado. N = 6

$P(X=x) = \frac{1}{6}$

Chance de cair 3:

$P(X=3) = \frac{1}{6}$

- Média de um dado = $\frac{6+1}{2} = \frac{7}{2} = 3,5$ (como são valores pares, é a média dos dois do meio, 3 e 4)
- Variância = $\frac{(6-1)^2}{12} = \frac{5^2}{12} = 2,08$
- Desvio Padrão = $\frac{6-1}{\sqrt{12}} =  \frac{5}{\sqrt{12}} = 1,44$

### Exercícios

Uma loja vende de 800 a 1800 peças por dia com distribuição uniforme. Qual a probabilidade: 

**1. de vender 817 peças em um dia?**

$P(X=817) = \frac{1}{1800-800} = \frac{1}{1000}$

**2. de vender 1300 peças em um dia?**

$P(X=1300) = \frac{1}{1800-800} = \frac{1}{1000}$

**3. de vender mais que 1400 peças em um dia?**

$P(X > 1400) = \frac{1800-1400}{1800-800} = \frac{400}{1000} = \frac{4}{10} = 0,25$

**4. de vender menos que 900 peças em um dia?**

$P(X < 900) = \frac{900-800}{1800-800} = \frac{100}{1000} = \frac{1}{10} = 0,1$

**5. de vender entre 900 e 1100 peças em um dia?**

$P(900 <= X <= 1100) = \frac{1100-900}{1800-800} = \frac{800}{1000} = \frac{8}{10} = 0,8$

## DISTRIBUIÇÃO BERNOULLI

- Só tem 2 resultados possíveis (sucesso ou fracasso)
- Tem resultado **binário**
	- Ex: se selecionou um produto com defeito ou não. Uma venda feita ou não. Um cliente ser inadiplente ou não. Aluno aprovado ou reprovado.
- Por ser binário, o espaço amostral de x é {0,1}
- **Só serve para medir 1 tentativa** (ex: lançamento de 1 moeda), **não serve para N casos** (lançar n moedas)

`Não é muito usado, mas serve de base para outras distribuições (binomial e poisson). Na verdade, a Bernoulli é a equação Binomial num cenário mais simples`

$$P(X=x) = p^x * (1-p)^{1-x}$$

Lembrando que x só pode ser 0(fracasso) ou 1(sucesso)
- p é a probabilidade de sucesso e 1-p é a de fracasso	
- Se quero medir a chance de sucesso, $p^x$ é $p^1$ (mantém a prob de sucesso na conta) e a prob de fracasso $(1-p)^{1-x}$ fica $(1-p)^0$, sendo cortado fora da equação, **ficando só o lado que nos interessa** (no caso, de sucesso)

**Um dos lados da equação sempre será cortado fora e outro será mantido (ou o valor final é p ou 1-p)**

- Moda = 1 se p>0,5 e = 0 se p<0,5 e os dois se for p=0,5
	- Ou seja, moda vai ser o que tem mais chance de acontecer
- Esperança = p (probabilidade de sucesso)

---

Ex: probabilidade de dar cara em uma moeda

p = 1/2 e x = 1 (sucesso)

$P(X=1) = 0,5^1 * (1-0,5)^{1-1} = 0,5 * (0,5)^0 = 0,5 * 1 = 0,5$

Ex2: a chance de um cliente comprar um produto na sua loja no natal é de 60%. Qual a probabilidade de alguém comprar?

p = 0,6 e x = 1 (sucesso) 

$P(X=1) = 0,6^1 * (1-0,6)^{1-1} = 0,6 * (0,4)^0 = 0,6 * 1 = 0,6$

`OBS: se eu quiser medir a chance de 1 ou + caras em vários lançamentos, tenho de usar a binomial`
