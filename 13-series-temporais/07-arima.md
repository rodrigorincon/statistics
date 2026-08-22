# ARIMA

É uma evolução do ARMA que pode ser usado mesmo em `séries não estacionárias`. Para tanto, ele faz uma transformação nos dados para torná-los estacionários e então usar o ARMA. Essa transformação (chamada de integração) é o I do nome ARIMA.

Essa transformação funciona aplicando subtrações nos dados para remover tendências até torná-la estacionária. Essa subtração é a diferença entre o dado e seu dado anterior. Essa subtração pode ser feita várias vezes, subtraindo a diferença das diferenças. Ao final `nossa série será essas diferenças, descartando os dados originais`. A partir de então aplicamos o ARMA nessa nova série formada pelas diferenças.

O parâmetro da intragração I é o "d" e indica quantas vezes os dados sofreram subtração.

A diferenciação é feita da seguinta maneira para cada d:

$\Delta X_t = X_t - X_{t-1}$

A série resultada no final será passada pelo mesmo processo em um loop até executar D vezes. A cada loop a série fica 1 dado menor, assim o D deve ser um valor pequeno, pois a série encolhe conforme vai sendo integrada.

## EXEMPLOS 

### Exemplo com 1 diferenciação

Dados = [100, 105, 103, 110, 108] e d=1.

$\Delta X_2 = X_2 - X_1 = 105 - 100 = 5$

$\Delta X_3 = X_3 - X_2 = 103 - 105 = -2$

$\Delta X_4 = X_4 - X_3 = 110 - 103 = 7$

$\Delta X_5 = X_5 - X_4 = 108 - 110 = -2$

Nossa série final é [5, -2, 7, -2] e será essa série que será executada pelo ARMA.

### Exemplo com 2 diferenciações

Dados = [100, 105, 103, 110, 108] e d=2.

$\Delta X_2 = X_2 - X_1 = 105 - 100 = 5$

$\Delta X_3 = X_3 - X_2 = 103 - 105 = -2$

$\Delta X_4 = X_4 - X_3 = 110 - 103 = 7$

$\Delta X_5 = X_5 - X_4 = 108 - 110 = -2$

Nossa série ao final da 1ª diferenciação é [5, -2, 7, -2].

**Segunda diferenciação**

Dados = [5, -2, 7, -2].

$\Delta X_2 = X_2 - X_1 = -2 - 5 = -7$

$\Delta X_3 = X_3 - X_2 = 7 - (-2) = 9$

$\Delta X_4 = X_4 - X_3 = -2 - 7 = -9$

Nossa série final é [-7, 9, -9] e será essa série que será executada pelo ARMA.

## INTEGRAÇÃO REVERSA

O ARMA é feito com a série reduzida pela diferenciação, mas para **realizar previsões com o modelo é preciso fazer a integração inversa** para que a **previsões estejam na escala original**.

Como a integração é subtração, a integração inversa é uma soma. Isso só é possível se guardar o último valor de cada etapa. Somamos o valor previsto pelo ARMA com o último número de cada diferenciação para encontrar a verdadeira previsão. Se formo prever vários números devemos guardar os valores previstos para cada etapa e usá-los para fazer a integração reversa das próximas previsões.

Pense nisso como se a previsão feita pelo ARMA estivesse criptografada e para decifrar precisa rodar o processo ao contrário. Outra forma de compreender a necessidade disso é que os dados do ARMA não estão na escala real, mas em uma reduzida para ficar estacionária. Então precisamos voltar à escala original para que o número previsto seja compreensível.

#### Exemplo

Dados = [100, 105, 103, 110, 108] e d=2.

1ª diferenciação = [5, -2, 7, -2].

2ª diferenciação = [-7, 9, -9].

Supondo que o ARMA tenha previsto que os próximos valores são 4, 2, 3. Precisamos somar o último valor de todas as etapas.

$PREV_4 = 4 + \Delta^2 X_4 + \Delta X_5 = 4 + (-2) + 108 = 2 + 108 = 110$

Ou seja, nosso primeiro **valor previsto real é 110**.

Armazenamos os valores previstos para cada diferenciação (2 para a 1ª diferenciação e 110 para a série original). Iremos usá-los no passo seguinte para des-escalar o próximo valor previsto.

$PREV_5 = 2 + \Delta^2 X_5 + \Delta X_6 = 2 + 2 + 110 = 4 + 110 = 114$

Ou seja, nosso segundo **valor previsto real é 114**.

Armazenamos os valores previstos para cada diferenciação (4 para a 1ª diferenciação e 114 para a série original).

$PREV_6 = 3 + \Delta^2 X_6 + \Delta X_7 = 3 + 4 + 114 = 7 + 114 = 121$

Ou seja, nosso terceiro **valor previsto real é 121**.