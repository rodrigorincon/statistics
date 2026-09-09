# TRANSFORMAÇÕES

Se seus dados não forem normais ou não se encaixarem na regressão desejada, você pode realizar uma transformação neles para tentar fazê-los encaixar no formato desejado. Importante lembrar que ao final é preciso fazer a operação inversa.

OBS: também posso fazer transformação só dos resíduos.

## TIPOS DE TRANSFORMAÇÕES

- Logaritmo
  - Usa log na base 10 ou ln
  - **Quando usar**: cauda forte da direita
  - **Onde é usado**: finanças, população, salários, preço, contagem
- Padronização Z-score
  - Organiza os para ficarem com média 0 e desvio 1
  - **Quando usar**: Regressões e quando houver pressuposto de normalidade
  - **Onde é usado**: SVM, regressão linear e logística, redes neurais
- Box-Cox
  - Encontra o expoente que torna os dados mais próximos possível da normal
  - **Quando usar**:  Quando você não tem certeza de qual transformação utilizar. Só serve **se todos os valores forem positivos**
  - **Onde é usado**: Econometria
- Mini-Max
  - Bota em uma escala, geralmente de 0 a 1
  - **Quando usar**: Quando precisa de um limite máximo e mínimo fixo, algoritmos baseado em distâncias
  - **Onde é usado**: Jogos de tabuleiro por turnos, mapeamento de terreno, KNN
- Proporção
  - Apenas divide um dado pelo outro (Y/X ou o contrário)
  - **Dê preferência por esse**. 
  - Mais simples e mais fácil de interpretar seus resultados

## QUANDO USAR

- Dados não seguirem a normal
- Dados/resíduos não se encaixam na regressão desejada
- Variância heterogênea
- Eliminar influência de outliers


## TRANSFORMAÇÃO DE DADOS CATEGÓRICOS EM NUMÉRICOS

As vezes você precisará transformar dados categóricos em numéricos. Para que categorias independentes e não relacionadas (como cores, marcas ou cidades) possam virar números existem 2 formas principais. Mas apenas use isso se for estritamente necessário.

- **One-Hot encoding**: Define um valor binário (0 ou 1) para se o dada é da categoria X. Todas as outras categorias se tornam 1 e essa categoria específica se torna 0. A cateogria 0 é o nosso balizador (como se fosse um grupo controle ou H0). Usado quando as categorias são totalmente não relacionadas (como cores, marcas ou cidades). Cria 1 variável para cada categoria existente.
  - Ex: var1: é azul=0, não é azul=1. Var2: é verde=0, não é verde=1. Var3: é vermelho=0, não é vermelho=1
- **Ordinal encoding**: Atribui números inteiros sequenciais quando os dados tem alguma ordem natural (ruim, neutro, bom...). É ideal para dados com uma ordem lógica
  - Ex: Escolaridade: "Ensino Médio" = 1, "Graduação" = 2, "Mestrado" = 3