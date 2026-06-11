# TAMANHO DO EFEITO

**Nos diz se o efeito encontrado pelo p-valor é pequeno ou grande**.

O p-valor nos diz se um efeito existe, mas não diz sua magnitude. Não sabemos se essa relevância é pequena ou alta.

`Um p-valor 0,15 não significa que o efeito é mais intenso que um p-valor 0,3. O número não indica sua grandeza!`

Isso é especialmente importante quando comparamos médias, pois o p-valor diz que há diferença significativa entre as médias, mas não se ela é pouca ou muita. Principalmente porque o p-valor é enviesado pelo tamanho da amostra (**amostras grandes alteram o p-valor mesmo que todas as médias e desvios se mantenham iguais**)

Ex: Um grupo que recebe massagem antes de dormir dorme mais que um que não recebeu, mas dorme 8 segundos a mais.

OBS: apesar dele ser especialmente importante quando comparamos médias, ele deve ser feito em todo teste para dar maior clareza ao resultado do p-valor.

Cada tipo de teste exige um cálculo diferente do seu tamanho do efeito.

## Qual Calculo Usar

- Teste T: D de Cohen (para amostras grandes) ou G de Hedges (para amostras pequenas)
- Friedman: D de Cohen ou Correlação de Kendall 
- Anova: eta-quadrado
- Correlação e Regressão: Coeficiente de determinação R²
- Teste Z, Mann-Whitney ou Wilcoxon: R de Cohen
- Kruskal-Wallis: eta-quadrado
- Qui-Quadrado: V de Cramér (mais comum) ou Coeficiente phi (somente para tabelas 2x2)
- Fisher: Coeficiente phi
- Shapiro: O próprio valor do teste
- McNemar: Razão de chances