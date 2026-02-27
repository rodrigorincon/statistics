# Sobre o mundo da Análise de Dados

Seu percurso de fazer uma narrativa com os dados também está ligado à criação dessa **cultura de dados** em sua organização. Embora fazer a **narrativa** seja importante, onde fazê-la também é algo crucial, assegurando que a narrativa seja feita para as **pessoas certas**. Além disso, verifique se as pessoas podem descobrir a narrativa, se elas sabem onde encontrá-la e que ela faz parte das interações regulares.

---

Os componentes principais da análise são divididos nas seguintes categorias:

1. Descritivo 
- **O que aconteceu** com base em dados históricos.
- Bom definir métricas e KPIs pra olhar. 
- Identifica anomalias
- Ex: relatórios com dados financeiros e de vendas
2. Diagnóstico 
- **Por que** eventos aconteceram. 
- É um complemento da descritiva.
3. Preditivo 
- **O que acontecerá** no futuro. 
- ML, BI, árovres de decisão e regressão
4. Prescritivo 
- **Quais ações fazer para atingir uma meta**. 
- Usa muito Machine Learning

---

Diferença dos cargos:

1. Analista de negócios
- Interpreta os dados **a partir da visualização**.
- É uma especialista na empresa e nos negócios
- Ele pega os resultados processados pelo analista de dados e toma decisões
- É o último a interagir com os dados

2. Analista de dados
- Interpreta os dados a partir do banco e gera visualizações
- trabalha em tirar respostas da base de dado e criar relatórios a partir disso
- Cria modelos dos tipos descritivos e prescritivos pra ter a informação que precisa
- Precisa entender do negócio e do técnico pra saber quais perguntas fazer e como responde-las
- **Focado no passado e na análise descritivo-preditivo**

RESUMO: retira as informações do banco de dados já todo formatado

PS: pode ocasionalmente trabalhar nos data lakes tbm pra buscar por novos padrões e criar novos relatórios caso precise de algo novo

3. Engenheiro de dados
- Gerencia as bases de dados e o fluxo entre eles (DBA e programa a integração entre as bases)
- Gerenciar as bases exige conhecer de cloud (se a base tiver em uma), segurança (pra só pessoas e programas definidos acessem) e programar (pra fazer as integrações)
- As bases podem ser bancos, repositórios, pasta de imagens, documentos de textos, planilhas... Todo tipo de dado primário
- Responsável pelo ETL
	- Faz a formatação dos dados e gera a base de dados mastigada pro analista/cientista
	- Precisa conhecer um pouco do negócio pra fazer a formatação correta e a limpeza do que com certeza não ajudará
- Constroi e mantém data warehouses e data lake
	- Cuidam de ONDE os dados tão guardados
	- Acesso e Velocidade de acesso e consulta são o ponto chave

4. Cientista de dados
- Igual o analista de dados, porém **mais focado em IA** e estatística e menos em visualização
- **Focado no futuro e na análise preditiva-prescritiva**
- Cria modelos dos tipos preditivo e prescritivo pra ter a informação que precisa
- Tem de entender muito do negócio

RESUMO: retira as informações do banco de dados já todo formatado pra definir o futuro

PS: pode ocasionalmente trabalhar nos data lakes tbm pra buscar por novos padrões e criar novos relatórios caso precise de algo novo

---
## DIFERENÇA ENTRE DATA WAREHOUSE E DATA LAKE

- **WAREHOUSE** armazena dados **processados e estruturados**
- **LAKE** armazena dados **brutos**
- Warehouse para relatórios específicos já definidos
- Lake para manter os dados originais, para análises exploratórias e criar novos relatórios que futuramente irão pro Warehouse
- Warehouse tem de ser acessado com velocidade, Lake tem de ter armazenamento barato

---
## DIFERENÇA ENTRE ANÁLISE EXPLORATÓRIA E EXLPANATÓRIA

- **Exploratória**
	- Está descobrindo algo
	- É feita a partir de hipóteses para ver se são reais ou não
	- Pode examinar o mesmo dado de diversas maneiras diferentes
- **Explanatória**
	- Já descobriu oq quer e vai mostrar para os outros
	- Precisa contar uma história e ser intuitivo