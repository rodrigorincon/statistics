from scipy.stats import norm, t
import numpy as np

print("------------ IC proporção")
proprocao_amostra = 0.14
tamanho_amostra = 1000
confianca = 0.95

alfa = 1 - confianca
meio_alfa = alfa/2

z = norm.ppf(1-meio_alfa) # usa uni-caudal e recebe a confianca atualizada pro unicaudal

erro_padrao = np.sqrt(proprocao_amostra * (1-proprocao_amostra)/tamanho_amostra)

intervalo_inf = round(proprocao_amostra - z*erro_padrao, 4)
intervalo_sup = round(proprocao_amostra + z*erro_padrao, 4)
print("Intervalo de confianca de", intervalo_inf, " e ", intervalo_sup)


print("------------ IC média")

media = 1990.5
desvio = 2833.33
tamanho_amostra = 140
confianca = 0.95

erro_padrao = desvio/np.sqrt(tamanho_amostra)

intervalo_inf, intervalo_sup = t.interval(confianca, tamanho_amostra-1, media, erro_padrao)
print("Intervalo de confianca de", round(intervalo_inf, 2), " e ", round(intervalo_sup, 2))