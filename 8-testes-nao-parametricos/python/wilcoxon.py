import numpy as np
from scipy.stats import wilcoxon
import matplotlib.pyplot as plt
import pandas as pd

x = [-7.34, 18.33, 33.35, 59.45, 8.09, 43.79, 34.3, 36.13, -56.02, 76.45]
y = [4.07, 6.52, 9.38, 18.62, 9.44, 3.12, 8.15, 5.44, -11.37, 31.77]

#### wilcoxon para 1 amostra
valor_referencia = 5

# teste de hipótese: H0: a mediana é menor ou igual a 5, H1: a mediana é maior que 5
statistic, p_value = wilcoxon( np.array(x) - valor_referencia, alternative='greater')
# a funcao wilcoxon por padrão verifica teste bicaudal, mas aqui queremos teste unilateral a direita, por isso o alternative='greater'
# a função wilcoxon por padrão compara os valores da amostra com zero, mas aqui queremos comparar com o valor de referência, por isso subtraímos o valor de referência dos valores da amostra
# a estatistica retornada é a soma dos rankings positivos (W+)
print(f"Comparando X com {valor_referencia}: Valor de W+: {statistic}, p-value: {p_value:.4f}")
print("------")

#### wilcoxon para 2 amostras
statistic, p_value = wilcoxon(x, y)
print(f"Valor de W+: {statistic}, p-value: {p_value:.4f}")

#### Plot boxplot of both variables
df = pd.DataFrame({'x': x, 'y': y})

x_q1 = df['x'].quantile(0.25)
x_q3 = df['x'].quantile(0.75)
lower_x = x_q1 - 1.5*(x_q3 - x_q1)
upper_x = x_q3 + 1.5*(x_q3 - x_q1)

y_q1 = df['y'].quantile(0.25)
y_q3 = df['y'].quantile(0.75)
lower_y = y_q1 - 1.5*(y_q3 - y_q1)
upper_y = y_q3 + 1.5*(y_q3 - y_q1)

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))
axs[0].boxplot(x)
axs[1].boxplot(y)
axs[0].axhline(y=valor_referencia, color='red', linestyle='--')
axs[0].set_title(f"Mediana de X {df['x'].quantile(0.5):.2f} com bigodes indo de {lower_x:.2f} a {upper_x:.2f}")
axs[1].set_title(f"Boxplot de Y {df['y'].quantile(0.5):.2f} com bigodes indo de {lower_y:.2f} a {upper_y:.2f}")
plt.show()
