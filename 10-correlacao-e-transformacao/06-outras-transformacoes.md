# TRANSFORMAÇÃO MINI-MAX

Nessa transformação padronizamos os dados, deixando eles entre 0 e 1. Assim todos os dado ficam na mesma ordem de grandeza **sem alterar as diferenças relativas entre os dados**. 

Importante ressaltar que isso **NÃO resolve os problemas dos outliers**, pois eles elevam o limite mínimo e máximo e deixam todos os dados convertidos exprimidos juntos.

$$x_i = \frac{x_i - min(x)}{max(x) - min(x)}$$

### QUANDO USAR

- Quando algoritmo exige escalas padronizadas
- Quando algoritmo é baseado em distância (KNN e K-means)
- Quando conhecemos os limites máximos e mínimos que os dados podem alcançar
- Quando quiser acelerar a convergência da rede neural

### QUANDO NÃO USAR

- Quando tivermos outliers
- Quando usar algoritmos baseado em árvores (random forest e XG Boost)

# PADRONIZAÇÃO Z-SCORE

Também padroniza os dados, mas não precisa conhecer os limites máximo e mínimo dos seus dados. Muda seus valores de forma que a média dos novos valores seja 0 e o desvio padrão 1. Os dados podem ser maiores que 1 e menores que zero.

Ele sim **resolve os problemas dos outliers**, pois os deixa mais próxmios mas sem a obrigação de expremer num limite fixo. O outlier ainda pode ficar além de 1 e manter os dados normais mais folgados.

$$x_i = \frac{x_i - media_x}{desvio_x}$$

Aonde desvio é calculado com N-1.

### QUANDO USAR

- Quando tiver outliers
- Regressão linear e logística
- Análise de Componentes Principais (PCA)
- Onde houver pressuposição de normalidade

# TRANSFORMAÇÃO BOX-COX

**Converte dados não normais em uma distribuição próxima à normal**. Ela utiliza um parâmetro lambda ($\lambda$) para estabilizar a variância e corrigir assimetrias, tornando análises como regressões mais confiáveis. É testado vários lambdas (geralmente de -5 a 5) e o que der resultados mais próximos a normal é escolhido.

Usa algum teste de hipótese para verificar se os dados transformados estão próximos o suficiente da normal (Shapiro, Kolmogorov-Smirnov ou Jarque-Bera).

$$x_i = \frac{ x_i^{\lambda} - 1 }{\lambda}$$

Lambda pode assumir valore facionados como 0.5 e negativos. **Lambda só não pode ser 0**. Defina de quanto em quanto os testes devem se incrementar além do ponto inicial e final. Caso nenhuma tentativa passe nos testes de normalidade, tente outra tranformação.

### QUANDO USAR

- Quando os dados não são normais
- Quando tem heterocedasticidade
- Regressão quando não cumpre a homocedasticidade
- Quando não quer usar testes não paramétricos