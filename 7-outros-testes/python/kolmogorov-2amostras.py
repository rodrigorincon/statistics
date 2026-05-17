import numpy as np
from scipy import stats

#### TESTE DE 2 AMOSTRAS, verifica se os 2 dados seguem a mesma distribuição ####

# Duas amostras normais iguais
amostra_norm1 = np.random.normal(loc=0, scale=1, size=5000)
amostra_norm2 = np.random.normal(loc=0, scale=1, size=5000)
amostra_norm_dif = np.random.normal(loc=0.5, scale=1, size=5000) # normal com outros parametros
amostra_unif1 = np.random.uniform(low=0, high=1, size=5000)
amostra_unif2 = np.random.uniform(low=0, high=1, size=5000)
amostra_unif_dif = np.random.uniform(low=3, high=4, size=5000)

# Amostras a serem comparadas
comparacoes = [
    ("Amostra Normal vs Mesma Normal", amostra_norm1, amostra_norm2),
    ("Amostra Normal vs Normal Diferente", amostra_norm1, amostra_norm_dif),
    ("Amostra Normal vs Amostra Uniforme", amostra_norm1, amostra_unif1),
    ("Amostra Uniforme vs Uniforme Diferente", amostra_unif1, amostra_unif_dif),
    ("Amostra Uniforme vs Mesmo Uniforme", amostra_unif1, amostra_unif2)
]

# Comparando as duas amostras
for descricao, amostra1, amostra2 in comparacoes:
    estatistica_ks, p_valor = stats.ks_2samp(amostra1, amostra2)

    print(f"Comparando: {descricao}")
    print(f"Estatística D: {estatistica_ks:.4f}")
    print(f"P-valor: {p_valor:.4f}")

    if p_valor < 0.05:
        print("Resultado: As amostras vêm de distribuições diferentes.")
    else:
        print("Resultado: As amostras vêm da mesma distribuição.")
    print("-----------------")
