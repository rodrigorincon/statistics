# TESTE DE LEVENE

O teste de Levene verifica se **um grupo de variâncias são iguais/similares** (homogêneas). Ele checa se todos os grupos tem variância similar ou se ao menos 1 deles é diferente. Ele é igual a Anova de 1 via porém aonde usa a média e a média dos grupos tem-se a possibilidade de trocar pela mediana ou a média aparada (removido os 10% mais extremos).

## CARACTERÍSTICAS

- Funciona com 2 ou + grupos
- Grupos não precisam seguir a distribuição normal
- Pode ser feito com base na média ou na mediana (senda essa mais robusta ara dados não normais)

OBS: Caso os grupos sigam a distribuição normal, o teste F é mais preciso (mas apenas nesse cenário).

## HIPÓTESES

H0: As variâncias de todos os grupos são similares.

H1: Pelo menos uma variância é diferente.

## COMO CALCULAR

O cálculo é exatamente o mesmo da Anova de 1 via (até o passo 3). Porém aonde tem média dos grupos e média geral pode trocar por mediana caso esteja calculando a versão com mediana (versão para dados não normalizados).

Ao final, Levene usa o teste F para chegar a conclusão de rejeitar ou não, fazendo-o idêntico ao teste F, porém podendo trocar as médias por medianas.

## TAMANHO DO EFEITO

Por ser muito similar a Anova, podemos fazer o mesmo cálculo de tamanho do efeito, usando o **eta-quadrado**.