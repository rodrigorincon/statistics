import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

numerador = 10
denominador = 10
x = np.arange(0.0, 3.0, 0.1)
valores1 = stats.f.pdf(x, dfn=numerador, dfd=denominador)

numerador = 10
denominador = 50
valores5_den = stats.f.pdf(x, dfn=numerador, dfd=denominador)

numerador = 50
denominador = 10
valores5_num = stats.f.pdf(x, dfn=numerador, dfd=denominador)


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, valores1, label='valores iguais', color='red')
plt.plot(x, valores5_num, label='numerador maior', color='green')
plt.plot(x, valores5_den, label='denominador maior', color='blue')
plt.legend()
plt.title('Comportamento da Distribuição F quando numerador ou denominador é maior')
plt.show()

