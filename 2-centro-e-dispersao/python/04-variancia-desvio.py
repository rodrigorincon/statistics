import pandas as pd
import statistics
import numpy as np
from math import sqrt

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
heights = [161, 163, 163, 164, 164, 164, 166, 167, 169, 169, 170, 172, 172, 173, 174, 174, 174, 177, 178, 178, 180, 180, 180, 181, 181, 181, 182, 183, 183, 185, 185, 188, 190, 194]
weights = [55, 57, 58, 58, 49, 60, 61, 61, 62, 62, 63, 66, 66, 69, 71, 73, 76, 77, 77, 78]
heigth_std = np.std(heights)
weight_std = np.std(weights)

heigth_cv = heigth_std/np.mean(heights)
weigth_cv = weight_std/np.mean(weights)

print("heigth: std: ", heigth_std, "variation coeficient: ", heigth_cv)
print("weight: std: ", weight_std, "variation coeficient: ", weigth_cv)