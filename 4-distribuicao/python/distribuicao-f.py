import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

numerador = 1
denominador = 1
x = np.arange(0.0, 5.0, 0.1)
valores1 = stats.f.pdf(x, dfn=numerador, dfd=denominador)

numerador = 10
denominador = 10
valores10 = stats.f.pdf(x, dfn=numerador, dfd=denominador)

numerador = 20
denominador = 20
valores20 = stats.f.pdf(x, dfn=numerador, dfd=denominador)

numerador = 40
denominador = 40
valores40 = stats.f.pdf(x, dfn=numerador, dfd=denominador)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, valores1, label='num=1 e den=1', color='red')
plt.plot(x, valores10, label='num=10 e den=10', color='green')
plt.plot(x, valores20, label='num=20 e den=20', color='blue')
plt.plot(x, valores40, label='num=40 e den=40', color='black')
plt.legend()
plt.title('Distribuição F se tornando próxima a normal')
plt.show()

