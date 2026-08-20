# TESTES DE HIPÓTESE

Usamos testes de hipótese para garantir que os dados podem ser analisados via série temporal e qual seu tipo. Testamos 4 coisas numa série temporal:

## 1. Se é estacionário ou não.

### Teste de Dickey Fuller Aumentado (ADF)

- H0: não é estacionário
- H1: é estacionário

O principal parâmetro do ADF é a defasagem (lag em inglês). A `defasagem (lag) é quantos dados anteriores serão considerados`, em resumo é o **tamanho do quadro da média móvel**. Um valor baixo faz com que tudo seja considerado ruído e não pega a correlação entre valores passados e futuros. Um valor grande consome os graus de liberdade do teste (gl = n-lags-1) e reduz poder do teste (maior chance de erro tipo 2 - aceitar H0 quando ela é falsa).

Em resumo um lag pequeno faz olhar poucos dados antigos e não capta a relação entre passado e futuro corretamente. Um lag grande faz perder precisão, podendo considerar tudo válido. Para encontrar o lag ideal é calculado diversas opções de lag e fica com aquele que as métricas de comparação de séries (AIC e BIC) derem o melhor valor.

Graus de liberdade: N - lags - 1.

### KPSS

Testa se uma série é estacionária ao redor de alguma tendência. É usada junto com o ADF para dar mais robustês na análise. Importante ficar atento que ela testa o oposto do ADF.

- H0: é estacionário
- H1: não é estacionário

### Teste PP

Corrige de forma não paramétrica autocorrelações nos resíduos. Se diferencia do ADF por não precisar escolher um valor de defasagens (lag) na equação de regressão. 

- H0: não é estacionário
- H1: é estacionário

## 2. Se é autocorrelato ou não.

Avaliam se os valores passados influenciam os valores futuros. Caso não influenciem nem precisa executar mais nada ligado a séries temporais.

### Durbin-Watson

Detecta se os resíduos do valor atual tem correlação com os resíduos do dado diretamente anterior. A janela de comparação é sempre 1, portanto só compara com o último dado. Importante ressaltar que esse teste **analisa resíduos**. 

Retorna um valor entre 0 e 4, aonde:

- De 0 à 2: correlação positiva
- Próximos a 2 (entre 1,5 e 2,5): não há correlação (não faz sentido usar série temporal)
- De 2 à 4: correlação negativa

### Ljung-Box

Verifica se há autocorrelação significativa em uma série dado o tamanho da janela de observação (defasagens ou lags). Assim verifica se a diferença dentro dessa janela é aleatória (ruído) ou se os dados são dependentes temporalmente. Para estudar séries temporais queremos rejeitar H0 (p-valor < alfa).

É muito usado para validar resíduos de modelos como ARIMA.

- H0: sem autocorrelação, dados independentes
- H1: há autocorrelação

Assim como no ADF, é preciso testar com vários tamanhos de janela diferente e ficar com aquele com menor métrica (AIC ou BIC) e levar em consideração as consequências de uma janela muito pequena e muito grande.

## 3. Quebra Estrutural

Identifica mudanças abruptas nos dados em algum momento do tempo. 

### Teste de Chow

Serve para ver se há algum ponto que houve alguma mudança brusca que mudou tudo e não possamos analisar toda a série junta, devendo dividir. Ex: Covid foi um ponto de ruptura em dados de viagens ao exterior, o que exige que faça uma análise pré-covid e outra pós covid.

Ótimo para identificar se um evento histórico ou econômico importante mudou o comportamento de uma série temporal. Também pode checar se subgrupos de uma população reagem de forma diferente a uma mesma variável independente.

- H0: não há quebra estrutural
- H1: há quebra estrutural

OBS: o teste de Chow **não fornece** onde o ponto de corte acontece! Ele pressupõe que você já saiba onde quer cortar os dados para comparar os 2 lados. Porém é possível encontrar o ponto de ruptura por outros meios. Ele usa o tete F por debaixo dos panos, calculando o numerador e denominador de acordo com graus de liberdade e soma dos resíduos de cada pedaço da série dividida. Portanto primeiro se escolhe um ponto de corte, calcula as somas dos resíduos e os graus de liberdade de cada parte e então faz o cálculo do numerador e denominador para o teste F.

Para encontrar os pontos de ruptura é usado o algoritmo de programação dinâmica PELT.

## 4. Se tem sazonalidade

Identifica se tem comportamentos cíclicos nos dados.

### Kruskal-Wallis / Friedman

Verifica se há sazonalidade suficiente nos dados. Informam se a sazonalidade existe E se ela é significativa. Caso exista sazonalidade mas seja tão pequena que nem muda nada o teste diz que não há.

Porém é preciso conhecer o contexto dos dados e saber qual deve ser a sazonalidade esperada (mensal, anual, trimestral...). O teste espera que você separe os dados nos períodos a serem analisados.

Para descobrir os pontos de corte de sazonalidade e passar esses subgrupos pro teste de hipótese use a Função de Autocorrelação Parcial (PACF). Ele irá identificar lags com picos isolados relevantes.

- H0: não tem efeitos sazonais
- H1: tem efeitos sazonais