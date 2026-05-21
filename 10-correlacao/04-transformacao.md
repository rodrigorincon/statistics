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
  - **Quando usar**: algoritmos baseado em distâncias e posso ter um dado muito maior que os demais, quebrando todo o cálculo
  - **Onde é usado**: KNN, SVM, regressão logística, redes neurais
- Box-Cox
  - Encontra o expoente que tornar os dados mais próximos possível da normal
  - **Quando usar**:  Quando você não tem certeza de qual transformação utilizar. Só serve **se todos os valores forem positivos**
  - **Onde é usado**: Econometria
- Mini-Max
  - Bota em uma escala, geralmente de 0 a 1
  - **Quando usar**: Quando precisa de um limite máximo e mínimo fixo
  - **Onde é usado**: Jogos de tabuleiro por turnos, mapeamento de terreno
- Proporção
  - Apenas divide um dado pelo outro (Y/X ou o contrário)
  - **Dê preferência por esse**. 
  - Mais simples e mais fácil de interpretar seus resultados

### Relembrando

**Padronização Z-score**

$z = \frac{x-media}{desvio}$

Aonde desvio é calculado com N-1.

## QUANDO USAR

- Dados não seguirem a normal
- Dados/resíduos não se encaixam na regressão desejada
- Variância heterogênea
- Eliminar influência de outliers

