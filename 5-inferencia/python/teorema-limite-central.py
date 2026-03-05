import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Teorema com distribuicao uniforme
uniform_population = np.random.uniform(0, 10, 100_000) # População não-normal
n_simulacoes = 10_000
tamanhos_amostra = [1, 5, 30, 100]

# Criar os plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for index, sample_size in enumerate(tamanhos_amostra):
    # Gera as médias amostrais
    medias = [np.mean(np.random.choice(uniform_population, sample_size)) for _ in range(n_simulacoes)]
    desvio = round(np.std(medias, ddof=1), 2)
    
    # Plotar histograma
    axes[index].hist(medias, color='skyblue', label="density")
    axes[index].set_title(f'Tamanho da amostra (n) = {sample_size} e desvio={desvio}')
    axes[index].set_xlabel('Média Amostral')
    axes[index].set_ylabel('Densidade')

plt.tight_layout()
plt.show()


# Teorema com distribuicao assimetrica
assimetric_population = np.random.exponential(scale=2.0, size=100_000)
n_simulacoes = 10_000
tamanhos_amostra = [1, 5, 30, 100]

# Criar os plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for index, sample_size in enumerate(tamanhos_amostra):
    # Gera as médias amostrais
    medias = [np.mean(np.random.choice(assimetric_population, sample_size)) for _ in range(n_simulacoes)]
    desvio = round(np.std(medias, ddof=1), 2)
    
    # Plotar histograma
    axes[index].hist(medias, color='skyblue', label="density")
    axes[index].set_title(f'Tamanho da amostra (n) = {sample_size} e desvio={desvio}')
    axes[index].set_xlabel('Média Amostral')
    axes[index].set_ylabel('Densidade')

plt.tight_layout()
plt.show()


# Teorema com distribuicao normal
normal_population = np.random.normal(loc=0.0, scale=1.0, size=100_000)
n_simulacoes = 10_000
tamanhos_amostra = [5, 15, 30, 50]

# Criar os plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for index, sample_size in enumerate(tamanhos_amostra):
    # Gera as médias amostrais
    medias = [np.mean(np.random.choice(normal_population, sample_size)) for _ in range(n_simulacoes)]
    desvio = round(np.std(medias, ddof=1), 2)
    
    # Plotar histograma
    axes[index].hist(medias, color='skyblue', label="density")
    axes[index].set_title(f'Tamanho da amostra (n) = {sample_size} e desvio={desvio}')
    axes[index].set_xlabel('Média Amostral')
    axes[index].set_ylabel('Densidade')

plt.tight_layout()
plt.show()
