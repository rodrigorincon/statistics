import numpy as np
from scipy.stats import norm, chi2
import matplotlib.pyplot as plt

gl = 50
x = np.linspace(0, gl*2, 1000)

qui_square_prob_5 = chi2.pdf(x, 5)
qui_square_prob_inf = chi2.pdf(x, gl)

plt.figure(figsize=(10, 6))
plt.plot(x, qui_square_prob_5, label=f'Qui-Quadrado Data gl=50')
plt.plot(x, qui_square_prob_inf, label=f'Qui-Quadrado Data gl=100')
plt.title('Distribuição Qui-Quadrado tendendo a normal com muitos graus de liberdade')
plt.legend()
plt.show()