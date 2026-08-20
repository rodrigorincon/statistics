import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox

np.random.seed(123)

# Exemplo de dados aleatórios
dados_nao_correlatos = np.random.randn(1000)
dados_correlatos = np.cumsum( np.random.normal(scale=2, size=1000) ) + np.linspace(0, 30, 1000)

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.plot(dados_nao_correlatos)
plt.title('Dados não correlatos')

plt.subplot(1, 2, 2)
plt.plot(dados_correlatos)
plt.title('Dados correlatos')
plt.show()

def analise_ljung_box(dados):
  resultado = acorr_ljungbox(dados, auto_lag=True) # eu posso especificar a quantidade de lags passando lags=X
  print(resultado)
  lag_usado = int(resultado.index[0])
  stat = resultado.lb_stat.iloc[0]
  p_value = resultado.lb_pvalue.iloc[0]
  print(f'Estatistica: {stat:.4f}, P-valor: {p_value:.4f}, Lag: {lag_usado}')
  if(p_value <= 0.05):
    print("Rejeito H0, há autocorrelação\n")
  else:
    print("Mantenho H0, NÃO há autocorrelação\n")

analise_ljung_box(dados_nao_correlatos)
analise_ljung_box(dados_correlatos)
