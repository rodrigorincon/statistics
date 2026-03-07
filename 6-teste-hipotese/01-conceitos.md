# TESTE DE HIPÓTESE

- Teste de Hipótese começa com uma suposição sobre a população e usa uma amostra para validá-la
- Busca responder se uma afirmação é verdadeira ou não
- Hipótese = afirmação sobre a algum parâmetro da população
- Usado em tomada de decisões a partir dos dados

## O que eu posso testar:

- Relação entre valores	
	- Relação entre 2 vars categóricas (ex: existe relação entre tipo de filme e compra de pipoca? Há relação entre um treino e ganho de massa muscular?)
	- Relação entre 2 ou mais vars numéricas (ex: mais número de horas trabalhadas significa mais produtividade?)
	- Análise de regressão
- Comparar valores
	- Medida com um valor específico (ex: a média de tempo de entrega é menor que 30 minutos?)
	- Comparar 2 ou mais medidas entre si (ex: há diferença significativa de preços entre o mercado A e B? Um curso/ação melhorou a produtividade dos funcionários?)
- Distribuição da população

OBS: mostraremos como fazer testes para a média e a proporção. Outras medidas exigem técnicas mais avançadas (como simulações ou bootstrap) não abordadas aqui.

## Tipos de Teste

Exitem centenas de testes. Eles se dividem em 2 grupos: paramétricos e não paramétricos.

- Testes Paramétricos:
	- Assumem que os dados seguem uma distribuição específica (geralmente normal)
	- Bons para amostras grandes e dados contínuos
	- São mais precisos, porém exigem amostras maiores
	- Por serem mais robustos, tem menos chances de erro tipo 2
	- São mais sensíveis a outliers
	- Exemplos:
		- Teste z
		- Teste t
		- Anova
		- Pearson
- Testes Não Paramétricos:
	- Não assumem que os dados sigam alguma distribuição
	- Bons para dados categóricos ou discretos e para amostras pequenas
	- São resistentes a outliers
	- São mais flexíveis, porém com menor poder estatístico.
	- `Adequado quando as premissas do paramétrico são quebradas`
	- Exemplo:
		- Qui Quadrado
		- Wilcoxon
		- Spearman
- Alguns testes tem seu equivalente no outro grupo

## Passos de um teste

1. Definir as hipóteses

- Define as hipóteses nula e alternativa (Ho e H1)
- Comece definindo a hipótese alternativa para depois formular a nula
- Definir o que significa rejeitar e não rejeitar Ho

2. Escolher o nível de significância

- Nível de significância = alfa
- Definir o que acontece ao cair no erro tipo 1 e 2
- Ver qual é menos desejado e ajustar alfa de acordo

3. Calcular as probabilidades

- Escolher o teste que melhor se encaixa no seu contexto
- Calcular o p-valor
- Calcula beta
- Cada teste calcula de um jeito diferente

4. Interpretar o resultado

- Rejeitar Ho (confirmar nossa afirmação, H1)
- Não rejeitar Ho (confirmar Ho)
- Toma a decisão comparando p-valor com alfa
