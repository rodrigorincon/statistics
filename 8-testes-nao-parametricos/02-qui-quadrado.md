# TESTE QUI-QUADRADO

- Serve para testar a **independência entre vars categóricas** (não numéricas) 
  - Checa se elas são relacionadas 
    - Ex: existe relação entre tipo de filme e consumo de pipoca? Existe relação entre volume muscular e flexibilidade?
    - OBS: não confundir esse relacionada com terem distribuição similar. É só ver se uma afeta a outra.
  - Também chamado de teste qui-quadrado de Pearson
- Também testa se uma **amostra segue uma determinada distribuição**
  - Também chamado de bondade do ajuste (goodness of fit em inglês) ou aderência
  - `Aderência = se comporta como uma certa distrbuição`

Logo **existem 2 tipos de testes** Qui-Quadrado: **independência e aderência**.

## COMO FUNCIONA

`Em ambos os casos ele compara a amostra com uma outra amostra que segue um comportamento/distribuição ideal.` 

Em suma, ela sempre **compara 2 distribuições**.

![](images/amostras-qui-quadrado.png)

## TIPOS DE QUI-QUADRADO

### TESTE DE INDEPENDÊNCIA

- Conta quantas vezes as categorias de 2 variáveis aparecem juntas
- Cada **variável só pode pertencer a 1 grupo de cada variável** (mutuamente exclusivas)
  - Ex: vendas de camisa pelo tamanho (P, M e G) e tipo da camisa (polo, botão ou regata). Uma camisa não pode ser polo e regata.
- **NÃO FUNCIONA para porcentagens**

Exemplo: Quero ver quais camisas foram mais vendidas. Cada camisa tem um tamanho e um tipo.

![](images/exemplo-categorias.png)

Uma forma muito boa de visualizar as combinações de 2 variáveis com várias categorias é o gráfico mosaico.
- É o gráfico de barras empilhado, só que colorido
- Separamos as categorias de uma das variáveis no eixo X (colunas) 
- Empilhamos as categorias da outra variável no eixo Y (formando linhas)
- Todos os valores da mesma categoria da variável do eixo Y tem a msm cor

![](images/grafico-mosaico.png)

### TESTE DE ADERÊNCIA


## PREMISSA 

### Premissas Gerais

- Os dados devem ser independentes
- Os dados devem ser categóricos

### Premissas de Independência

- As variáveis devem pertencer unicamente a 1 combinação de categoria (os grupos são mutuamente exclusivos)
- Para graus de liberdade < 4, a quantidade mínima em cada combinação de categorias deve ser 10. 
- Para graus de liberdade $\ge$ 4, a quantidade mínima em cada combinação de categorias deve ser 5. 

### Premissas de Aderência

## HIPÓTESES

Para o **teste de independência**:

H0: Variáveis independentes (Não há associação entre elas).
- P(Categoria1 da Var1) = P(Categoria2 da Var1) = ... P(CategoriaN da Var1)

H1: Variáveis dependentes (Há associação significativa entre elas).
- Ao menos 1 categoria da var1 tem probabilidade diferentes

Para o **teste de aderência**:

H0: .

H1: .

## CÁLCULO

## RESÍDUOS

Assim como a Anova, o Qui-Quadrado nos diz se há ou não relação entre os grupos (minha amostra e a amostra esperada). Caso haja (rejeite H0) devo fazer um teste post-hoc para verificar quais combinações de categorias fogem do esperado. Esse teste post-hoc analisa os residuos.

**Caso rejeite H0, verifique os resíduos para ver quais grupos fogem do esperado.**

Cada combinação terá um resíduo. Se o resíduo for maior que $\pm$ 2 significa que ele foge um pouco do esperado e pode ou não ser considerado um desvio. Se o resíduo for maior que $\pm$ 3 significa que ele foge muito do esperado e com certeza é um desvio.

Esses valores de $\pm$ 2 e 3 vem diretamente do desvio padrão da distribuição normal padrão (da onde a distribuição qui quadrado deriva). Aonde 2 significa que o valor está a 2 desvios padrões da média e 3 está a 3 desvios padrões. E lembrando que 3 desvios padrões distante da média é a definição de outlier e 2 pode ou não já ser considerado um outlier.

Ou seja, **a combinação de categorias foge do esperado quando ela é um outlier**. Se pensar um pouco "fugir do esperado" é a própria definição de outlier, então tudo se encaixa.

`O cálculo de resíduo nada mais é que calcular o desvio padrão de cada grupo em relação ao esperado (média).`

### CÁLCULO DOS RESÍDUOS

### asuntos

ver a respota da ia pra "existe diferença no teste qui quadrado de independência e de aderência"

pesquisar calculo do teste para independencia 
  - ver a resposta da ia pra "cálculo teste qui quadrado aderência" e "cálculo teste qui quadrado independência"
pesquisar calculo dos residuos

pesquisar oq é o tipo teste de aderencia (quão diferente é do outro)
pesquisar quais as premissas dele (ver se muda pra do outro)
ver H0 e H1 desse tipo
ver se o cálculo dele e de seus resíduos mudam pro outro

### assuntos 2

estudar a relação da distribuição com o teste

ver como o  Viés Estatístico é usado no qui-quadrado
como usar o qui quadrado pra comparar 3 ou + proporções numéricas
teste de independência do Qui-Quadrado (é igual ao Teste Z para 2 proporções)
  z = (propA - propB)/sqrt{ propTotal(1-propTotal)(1/n_a + 1/n_b) }
