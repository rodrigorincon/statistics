import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal

# Criando uma série temporal senoidal com uma pitada de aleatoriedade. Cada valor representa 1 mes
datas = pd.date_range(start="2020-01-01", end="2024-12-01", freq="MS")
valores = np.sin(np.linspace(0, 20 * np.pi, len(datas))) + np.random.normal(0, 0.2, len(datas))
serie = pd.Series(valores, index=datas)
print(serie)
plt.plot(serie)
plt.show()


# Organizando os dados em um DataFrame para separar por mês
df = pd.DataFrame({"valor": serie, "mes": serie.index.month})

# Separando os valores em listas para cada grupo (ex: de 1 a 12 para os meses)
grupos = [grupo["valor"].values for _, grupo in df.groupby("mes")]

# Aplicando o teste de Kruskal-Wallis
estatistica, p_valor = kruskal(*grupos)

print(f"\nEstatística: {estatistica:.2f}, P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("Rejeito H0, há sazonalidade")
else:
    print("Rejeito H0, NÃO há sazonalidade")
