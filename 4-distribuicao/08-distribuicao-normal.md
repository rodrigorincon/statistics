# DISTRIBUIÇÃO NORMAL

- Também chamada de gaussiana ou de sino
- Pode ser usado com valores discretos quando ele tem valores muito próximos
- Quanto maior o desvio padrão, mais aberto é o gráfico da normal (mais espaçado estão os valores)
- Precisa pegar a média e o desvio padrão pra calcular
- pra saber se uma distribuição é normal tem que passar no teste de hipótese XXXXXXX

## Equação

Para um valor específico.

$$f(x) = \frac{e^{-\frac{1}{2}(\frac{x-media}{desvio})^2}}{desvio\sqrt{2\pi}}$$

Para todos os valores abaixo de x ou entre x e y

$$P(X < x) = \frac{1}{desvio\sqrt{2\pi}} * \int e^{-\frac{1}{2}(\frac{x-media}{desvio})^2} \,dx$$ 

Essa é a integral da 1ª equação. Como essa integral não tem solução analítica, então é preciso simplifcar a equação (padronizar) e usar de tabelas (z-score) pra calcular.

### Explicação da equação

$\frac{x-media}{desvio}$ é a alma da equação

$\frac{1}{desvio\sqrt{2\pi}}$ garante que a área total da curva dê 1

$-\frac{1}{2}(\frac{x-media}{desvio})^2$ controla o formato da curva. O sinal faz a curva ser virada pra baixo com pico na média

- Quanto mais x se afasta da média maior o valor de ${(\frac{x-media}{desvio})}^2$, e como ele tem sinal negativo, menor o valor, garantindo que o maior valor é a média
- O fato da base ser o nº de euler (e) faz a função cair vertiginosamente a medida que x se afasta da média
- O desvio ajuda a segurar a queda da função, tornando a queda mais suave caso ele seja maior

## Infos Importantes

- moda = esperança = média 
- variância = cálculo normal 

Se for a variância da **população** divide por N e se for da **amostra** divide por N-1

- 68,26% fica dentro do 1º desvio padrão
- 95,44% fica dentro do 2º desvio padrão
- 99,72% fica dentro do 3º desvio padrão

## NORMAL PADRONIZADA

- É uma simplificação da distribuição normal, aonde a média é convertida pra 0 e o desvio pra 1
- Para isso, ao invés de calcular x, calculamos z

$$z = \frac{x - media}{desvio}$$ é a parte principal da equação da normal

- z diz quantos desvios padrões o x está acima ou abaixo da média
- Valores acima da média são positivos e abaixo da média negativos
- Desvio padrão = 1, 10% acima do desvio padrão é 1.1, metade do caminho entre o 1º e 2º desvio é 1.5

$$f(z) = \frac{e^{-\frac{1}{2}z^2}}{\sqrt{2\pi}}$$

- Mesmo simplificando usando z, a integral de $e^{z^2}$ ainda não tem solução analítica, então precisa usar as tabelas ou softwares
- Não precisa usar essa fórmula, só procurar a resposta na tabela z-score
- Ao padrozinar os valores eliminamos diferenças de escala, permitindo a comparação entre 2 distribuições mesmo que usem escalas diferentes.

Quando P(z) > 3 (quando tiver + de 3 desvios padrão) é certeza de ser **outlier**. Chance de 0,27% de chance de acontecer.

Quando P(z) > 2 (quando tiver + de 2 desvios padrão) pode ou não ser **outlier**, tem de analisar o seu contexto. Chance de 4,55% de acontecer.

### Intervalo de Confiança

- Intervalo de confiança diz quantos % de certeza eu tenho que a média **populacional** está em um intervalo
- Só me informa a **média** verdadeira, não consigo estimar outros valores.
- Faço isso a partir de uma amostra (da qual tenho média e desvio)
- Quanto maior a amostra, maior o intervalo de confiança (maior minha certeza)

$$intervalo = mediaAmostra \pm Z * \frac{desvioAmostra}{\sqrt{n}}$$

`Z vem da tabela z-score (não é o z da equação)!`

---

## Exercícios

**1. O teste de QI a média é 100 e o desvio padrão 15. Qual a probabilidade:**

media=100 e desvio=15

**a)** alguem ter QI abaixo de 110?

$z = \frac{x-media}{desvio} = \frac{110-100}{15} = \frac{10}{15} = 0,67$

P(x<110) = P(z<0,67) = 0,7486

**b)** alguém ter QI entre 100 e 140?

P(100 < x < 140) = P(x<140) - P(x<100)

$z = \frac{140 - 100}{15} = \frac{40}{15} = 2,67$

P(x<140) = P(z<2,67)

$z = \frac{100 - 100}{15} = 0$

P(x<100) = P(z<0)

P(z<2,67) - P(z<0) = 0,9962 - 0,5 = 0,4962 

**c)** alguém ter QI acima de 80?

$z = \frac{80 - 100}{15} = \frac{-20}{15} = -1,33$

P(z > -1,33) = P(z < 1,33) -> como é simétrico a partir do 0, podemos inverter o sinal e o comparador

P(z < 1,33) = 0,9082

**2. computadores são vendidos com valores na média de 750 dolares e devio de 60 dólares. Quantos são vendidos entre 624 e 768?**

P(624 < x < 768) = P(x<768) - P(x<624)

$z768 = \frac{768 - 750}{60} = 0,3$

$z624 = \frac{624 - 750}{60} = -2,1$

$P(z<0,3) - P(z < -2,1) = P(z<0,3) - P(z > 2,1)$ trocamos o sinal e o comparador pra ficar todos os z positivos

$P(z<0,3) - (1 - P(z < 2,1) )$ pegamos o complementar para ficar com todos os sinais negativos

$P(z<0,3) - 1 + P(z < 2,1) = 0,6179 - 1 + 0,98214 = 0,60004 = 60%$
