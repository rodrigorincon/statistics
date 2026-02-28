import pandas as pd
import statistics
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

print("-------------- calculating variance using statistics package")
lista = [1,2,3,4]
variancia_populacional = statistics.pvariance(lista)
variancia_amostral = statistics.variance(lista)
print("the populational variance is ", variancia_populacional)
print("the sample variance is ", variancia_amostral)

print("-------------- calculating variance using pandas package")
series = pd.Series(lista)
variancia_amostral = series.var() # Pandas default variance is sample variance (ddof=1)
variancia_populacional = series.var(ddof=0)
print("the populational variance is ", variancia_populacional)
print("the sample variance is ", variancia_amostral)

print("-------------- calculating variance using quadratic formula")
variancia_populacional = np.mean(np.square(lista)) - np.mean(lista)**2
print("the populational variance with quadratic formula is ", variancia_populacional)

print("-------------- calculating variance using esperanca formula")
lista = np.array([1,2,3,4])
probs = np.array([0.2, 0.3, 0.4, 0.1])
esperanca = np.sum( lista * probs )
esperanca_para_x_quarado = np.sum( np.square(lista) * probs )
variancia = esperanca_para_x_quarado - esperanca**2 
print("the populational variance with esperanca formula is ", variancia_populacional)

############ DESVIO PADRAO

print("-------------- calculating standart deviation using numpy")

### numpy uses POPULATION as default
desvio_populacional = np.std(lista)
desvio_amostral = np.std(lista, ddof=1)
print("the populational std is ", desvio_populacional)
print("the sample std is ", desvio_amostral)

print("-------------- calculating standart deviation using pandas")
### pandas uses SAMPLE as default
df = pd.DataFrame({'values': lista})
desvio_amostral = df['values'].std()
desvio_populacional = df['values'].std(ddof=0)
print("the populational std is ", desvio_populacional)
print("the sample std is ", desvio_amostral)


############ COEFICIENTE DE VARIAÇÃO
print("-------------- calculating variation coeficient")
heights = [158, 159, 161, 162, 163, 164, 164, 166, 167, 168, 168, 169, 170, 171, 171, 172, 172, 173, 173, 173, 174, 175, 175, 176, 177, 177, 177, 178, 180, 181, 182, 183, 185, 185, 186, 190, 193]
weights = [62,  63,  64,  65,  66,  67,  68,  68,  69,  70,  71,  72,  72,  73,  73,  74,  74,  75,  75,  75,  76,  76,  77,  78,  78,  79,  79,  80,  80,  81,  81,  83,  84,  85,  85,  87,  88]
heigth_std = np.std(heights)
weight_std = np.std(weights)

heigth_cv = heigth_std/np.mean(heights)
weigth_cv = weight_std/np.mean(weights)

print("heigth: mean:", round(np.mean(heights)) ," std: ", round(heigth_std, 2), "variation coeficient: ", round(heigth_cv, 4))
print("weight: mean:", round(np.mean(weights)) ," std: ", round(weight_std), "variation coeficient: ", round(weigth_cv, 4))
