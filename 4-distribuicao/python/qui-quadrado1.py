import numpy as np
from scipy.stats import norm, chi2
import matplotlib.pyplot as plt

x = np.linspace(0, 8, 100)

normal_prob = norm.pdf(x, loc=0, scale=1)
qui_square_prob3 = chi2.pdf(x, 3)
qui_square_prob5 = chi2.pdf(x, 5)

plt.figure(figsize=(10, 6))
plt.plot(x, normal_prob, label=f'Normal Data')
plt.plot(x, qui_square_prob3, label=f'Qui-Quadrado Data gl=3')
plt.plot(x, qui_square_prob5, label=f'Qui-Quadrado Data gl=5')
plt.title('Comparação entre Distribuição Normal e Qui-Quadrado')
plt.legend()
plt.show()