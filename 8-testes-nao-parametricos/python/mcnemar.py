import numpy as np
from statsmodels.stats.contingency_tables import mcnemar

# [ A e B certos,       A certo e B errado]
# [ A errado e B certo, A e B errados     ]
tabela = np.array([[20, 5], 
                   [15, 10]])

# Realiza o teste de McNemar Qui-Quadrado
statistic = mcnemar(tabela, exact=False, correction=True)

print('Teste de McNemar (Qui-Quadrado)')
print('Estatística do teste: %.3f' % statistic.statistic)
print('P-valor: %.3f' % statistic.pvalue)

# Interpretação
if statistic.pvalue < 0.05:
    print('As proporções são diferentes (rejeito H0)')
else:
    print('As proporções são semelhantes (não rejeito H0)')

print("-----------")
# Realiza o teste de McNemar Binomial
statistic = mcnemar(tabela, exact=True)

print('Teste de McNemar (Binomial)')
print('Estatística do teste: %.3f' % statistic.statistic)
print('P-valor: %.3f' % statistic.pvalue)

# Interpretação
if statistic.pvalue < 0.05:
    print('As proporções são diferentes (rejeito H0)')
else:
    print('As proporções são semelhantes (não rejeito H0)')
