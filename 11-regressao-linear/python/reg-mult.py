import numpy as np
import statsmodels.api as sm

y = np.array([12, 15, 18, 22, 25])
x = np.array([
    [1, 2],  # Observação 1: X1=1, X2=2
    [2, 3],  # Observação 2: X1=2, X2=3
    [3, 4],  # Observação 3: X1=3, X2=4
    [4, 5],  # Observação 4: X1=4, X2=5
    [5, 8]   # Observação 5: X1=5, X2=8
])

x = sm.add_constant(x) # X tem de ser uma matriz, onde cada linha é um ponto
regressao = sm.OLS(y, x).fit()
print(regressao.summary(), "\n\n")
print(f'A equacao eh {regressao.params[1]:.0f}*X1 + {regressao.params[2]:.0f}*X2 + {regressao.params[0]:.0f}')

