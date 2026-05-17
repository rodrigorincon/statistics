import numpy as np
from statsmodels.stats.contingency_tables import mcnemar

# [ dor antes e depois, dor só antes]
# [ dor só depois     , sem dor     ]
tabela = np.array([[16, 34], 
                   [20, 30]])

# Realiza o teste de McNemar de acordo com tamanho da amostra
if tabela[0, 1] + tabela[1, 0] < 25:
    statistic = mcnemar(tabela, exact=True)
    tipo_teste = 'binomial exato'
else:
    statistic = mcnemar(tabela, exact=False, correction=True)
    tipo_teste = 'qui-quadrado'

print('Teste de McNemar', tipo_teste)
print('Estatística do teste: %.3f' % statistic.statistic)
print('P-valor: %.3f' % statistic.pvalue)

# Interpretação
if statistic.pvalue < 0.05:
    print('As proporções são diferentes (rejeito H0)')
else:
    print('As proporções são semelhantes (não rejeito H0)')
