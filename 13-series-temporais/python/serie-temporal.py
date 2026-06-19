import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dados = [10, 12, 15, 14, 13, 15, 18, 16, 15, 16, 17, 17, 16, 15, 12, 11, 10, 11, 10, 11, 12, 13, 15, 14, 17]

# Decompondo a série temporal
# Supondo uma frequência mensal (período = 12)
decomposicao = seasonal_decompose(dados, period=12, model='additive')

# Plotando os componentes
decomposicao.plot()
plt.show()
