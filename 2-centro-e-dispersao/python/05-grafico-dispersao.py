import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.array([0, 1, 1.5, 3, 5])
y = np.array([2, 3, 5, 7, 11])

# Calcular a linha de tendência (regressão linear simples)
m, b = np.polyfit(x, y, 1)


# Criar o gráfico
plt.scatter(x, y, color='blue', label='Pontos de Dados')
# Plotar a linha
plt.plot(x, m*x + b, color='red', label='Linha de Tendência')

# Adicionar título e rótulos
plt.title("Gráfico de Dispersão Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()

# Mostrar o gráfico
plt.show()