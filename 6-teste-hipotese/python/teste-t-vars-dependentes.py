import numpy as np
from scipy.stats import ttest_rel

# teste T para vars dependentes, exemplo do doc
antes = [1.1, 3.9, 3.1, 5.3, 5.3, 3.4, 5]
depois = [0, 1.2, 2.1, 2.1, 3.4, 2.2, 3.2]

# executando o teste
t_stat, p_valor = ttest_rel(antes, depois) # P(T < t)
print(f'Estatística t: {t_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')
