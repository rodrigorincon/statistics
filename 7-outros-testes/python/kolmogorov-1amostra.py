import numpy as np
import scipy.stats as stats

#### TESTE DE 1 AMOSTRA, verifica se os dados seguem uma distribuição específica ####
# Vamos verificar se os dados seguem uma distribuição normal, exponencial e uniforme.

# Gerando dados normais
dados_normal = np.random.normal(loc=0, scale=1, size=5000)
media_normal = np.mean(dados_normal)
desvio_normal = np.std(dados_normal)

# Gerando dados exponenciais
dados_expon = np.random.exponential(scale=1, size=5000)
media_expon = np.mean(dados_expon)
desvio_expon = np.std(dados_expon)

# Gerando dados uniformes
dados_unif = np.random.uniform(low=0, high=1, size=5000)
media_unif = 0
desvio_unif = 1


todos_dados = [
    {"tipo": "Normal", "dados": dados_normal, "media": media_normal, "desvio": desvio_normal},
    {"tipo": "Exponencial", "dados": dados_expon, "media": media_expon, "desvio": desvio_expon},
    {"tipo": "Uniforme", "dados": dados_unif, "media": media_unif, "desvio": desvio_unif}
]

for dados in todos_dados:
    print("--------- Teste para os dados: ", dados["tipo"])
    distributions_to_test = ['norm', 'expon', 'uniform']
    for dist in distributions_to_test:
        if dist ==  'expon' and dados["tipo"] == "Exponencial":
            resultado = stats.kstest(dados["dados"], dist)
        else:
            resultado = stats.kstest(dados["dados"], dist, args=(dados["media"], dados["desvio"]))

        print(f"Teste KS com dados {dados['tipo']} numa distribuição {dist}")
        print(f"Estatística D = {resultado.statistic:.4f}, P-valor = {resultado.pvalue:.4f}")
    
        if resultado.pvalue < 0.05:
            print("Resultado: Rejeitamos a H0. Os dados NÃO seguem a distribuição especificada.")
        else:
            print("Resultado: Não rejeitamos a H0. Os dados seguem a distribuição especificada.")
        print("\n")
