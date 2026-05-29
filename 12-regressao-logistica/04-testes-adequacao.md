# TESTES DA REGRESSÃO LOGÍSTICA

quais os h0 e h1 de cada um? p-valor tem de ser menor ou maior q alfa?

Box-Tidwell

teste de Wald 

z = a_i / erroPadrao(a_i)

# MEDIDAS DE ADEQUAÇÃO

Além dos testes de hipótese das premissas (que veem se os dados cumprem os requisitos do algoritmo) e do teste dos coeficientes (que testa se as variáveis afetam o resultado final de fato) podemos testar o **quão bem a sigmoide se ajusta aos dados**. Usada tanto para validar a regressão como para **comparar diferentes regressões**.

Importante perceber que uma reta bem ajustada aos dados **pode ser sinal de overfitting**! 

## PSEUDO R²

É uma variação do R² da regressão linear, mas como y é categórico a gente não pode usar correlação normalmente aqui. Mas também **informa quantos porcento da variância de Y é explicada pelo modelo**.

Existem diversas variações dele (McFadden, Cox-Snell, Nagelkerke), mas o mais comum é o McFadden.

$$R2 = 1 - \frac{ln(reg)}{ln(A_0)}$$

????