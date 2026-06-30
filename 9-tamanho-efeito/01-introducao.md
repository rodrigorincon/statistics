# TAMANHO DO EFEITO

**Nos diz se o efeito encontrado pelo p-valor é pequeno ou grande**.

O p-valor nos diz se um efeito existe, mas não diz sua magnitude. Não sabemos se essa relevância é pequena ou alta. Um p-valor 0,15 não significa que o efeito é mais intenso que um p-valor 0,3. O número não indica sua grandeza!

Isso é especialmente importante quando comparamos médias, pois o p-valor diz que há diferença significativa entre as médias, mas não se ela é pouca ou muita. Principalmente porque o p-valor é enviesado pelo tamanho da amostra (**amostras grandes alteram o p-valor mesmo que todas as médias e desvios se mantenham iguais**)

Ex: Um grupo que recebe massagem antes de dormir dorme mais que um que não recebeu, mas dorme apenas 8 segundos a mais.

OBS: apesar dele ser especialmente importante quando comparamos médias, ele deve ser feito em todo teste para dar maior clareza ao resultado do p-valor.

Cada tipo de teste exige um cálculo diferente do seu tamanho do efeito.

`O tamanho do efeito ignora o tamanho da amostra`

## Relação com P-Valor

Se N é baixo: O foco é em ambos (P-valor e Tamanho do Efeito). Como o P-valor é afetado pelo tamanho da amostra as vezes pode-se rejeitar ou aceitar H0 erroneamente. Para ter mais certeza nesses casos verifica o tamanho do efeito para ter certeza se a resposta do P-Valor é real ou apenas acaso.

Se N é alto: O foco é no Tamanho do Efeito e no Intervalo de Confiança. O P-valor será quase sempre baixo. A tua pergunta passa a ser: "Esta diferença real é grande o suficiente para importar?"

## Como Interpretar

A depender da família da equação usada, nos dá uma dessas duas informações:

- Nos diz quantos desvios padrões um grupo é diferente do outro (família D)
  - Ex: um grupo é X desvios padrões maior/menor que o outro
- Nos diz a força da relação entre as variáveis (família R)
  - Ex: os grupos são X% correlacionados

## Qual Calculo Usar

- Teste T: D de Cohen (para amostras grandes) ou G de Hedges (para amostras pequenas)
- Friedman: D de Cohen ou Correlação de Kendall 
- Anova: eta-quadrado
- Levene: eta-quadrado
- Correlação e Regressão: Coeficiente de determinação R²
- Teste Z, Mann-Whitney ou Wilcoxon: R de Cohen
- Kruskal-Wallis: eta-quadrado
- Qui-Quadrado: V de Cramér (para independência), Razão de chances (para aderência) ou Coeficiente phi (somente para tabelas 2x2)
- Fisher: Coeficiente phi
- Shapiro: O próprio valor do teste
- McNemar: Razão de chances

## Grupos

O tamanho do efeito pode ser dividido em 2 grupos:

- Família D
  - Estimam magnitude de diferença entre médias
  - Diz quantas vezes uma é maior que outra
  - Exemplos:
    - D de Cohen
    - G de Hedges
    - Delta de Glass
- Família R
  - Mede a correlação entre as variáveis
  - Diz quanto da variância que é explicada pelas variáveis
  - Dá a % da relação
  - Exemplos:
    - R² (coeficiente de determinação)
    - Eta-quadrado
    - R de Pearson (correlação padrão)
    - V de Cramér 
    - Coeficiente phi

## Medindo a Magnitude

Cada medida tem uma faixa de valores diferente. Uns vão de -1 a 1, outros de 0 a 1, outros de 0 a infinito. Portanto não existe uma interpretação única para todos. Somente analisando seu contexto pode-se saber quanto é um valor baixo ou alto para o tamanho do efeito. Não tem como definir um valor fixo único para todos os contextos. Procure saber qual o valor usado na sua área. 

Por exemplo, se você está testando o impacto do uso de coletes salva-vidas e encontra um tamanho de 0,02 pode soar baixo, mas isso significa redução em 2% no número de mortes, que pode salvar milhares de vidas.

Porém, caso não possua essa informação, algumas equações tem uma base pré-definida que serve de avaliação inicial. Lembrando que esses valores podem mudar de um autor pra outro.

- Família D (Cohen, Hedges e Glass)
  - Irrisório: até 0,2 
  - Pequeno: entre 0,2 até 0,5
  - Médio: entre 0,5 e 0,8
  - Grande: acima de 0,8
- R de Pearson
  - Irrisório: até 0,1
  - Pequeno: até 0,1
  - Médio: entre 0,1 e 0,5
  - Grande: acima de 0,5
- Coeficiente phi
  - Irrisório: até 0,1
  - Pequeno: entre 0,1 e 0,2
  - Médio: entre 0,2 e 0,6
  - Grande: acima de 0,6
