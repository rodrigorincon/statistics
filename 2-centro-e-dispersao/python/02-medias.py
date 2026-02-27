import numpy as np
import math
import statistics

##### 1: MEDIA ARITIMETICA
lista = [1,2,3,4]
media = np.mean(lista) # sum all values and divide by the length
print("the average is ", media) # 2.5

##### 2: MEDIA PONDERADA
# multiply the elements by its weight and divide by the sum of the weights
values = np.array([1,3,5])
weights = np.array([1,2,1])
media = np.sum(values * weights)/sum(weights)
print("the ponderated average is ", media) # 3

# another way to calculate when the value comes in a single dict
lista = {1: 1, 3: 2, 5: 1}
values_with_weights = sum([value * weight for value, weight in lista.items()])
media = values_with_weights / sum(lista.values())
print("the ponderated average is ", media) # 3

##### 3: MEDIA GEOMETRICA
# multiply all elements and take the n-root
lista = [1,2,3,4]
multiplied_values = math.prod(lista)
media = multiplied_values ** (1/len(lista))
print("the geometric average is ", media) # 2.21

# another way to calculate
media = statistics.geometric_mean(lista)
print("the geometric average is ", media) # 2.21

##### 4: MEDIA HARMONICA
# the quantity divided by the sum of the inverses
lista = [1,2,3,4]
total_inversed_values = sum(1/value for value in lista)
media = len(lista) / total_inversed_values
print("the harmonic average is ", media) # 1.92

# another way to calculate
media = statistics.harmonic_mean(lista)
print("the harmonic average is ", media) # 1.92


##### 5: MEDIA QUADRATICA
# the root of average (but with the values powered by 2)
lista = [1,2,3,4]
media = sum(value**2 for value in lista) / len(lista)
media = math.sqrt(media)
print("the quadratic average is ", media) # 2.74

# another way to calculate
media = np.sqrt(np.mean(np.square(lista)))
print("the harmonic average is ", media) # 2.74


########### variancia das medias
# variancia da media ponderada e da quadratica são iguais a da aritimetica
print("----------------")

# variancia aritimetica
lista = [1,2,3,4]
media = np.mean(lista)
variancia = sum(math.pow(value - media, 2) for value in lista) / len(lista)
print("the variance is ", variancia) # 1.25

# variancia geometria
media_logs = sum(math.log(value) for value in lista) / len(lista)
variancia = sum(math.log(value) - media_logs**2 for value in lista) / len(lista)
print("the geometric variance is ", variancia) # 0.16

# variancia harmonica
lista = [1,2,3,4]
media = len(lista) / sum(1/value for value in lista)
variancia = sum((1/value - 1/media)**2 for value in lista) / len(lista)
print("the harmonic variance is ", variancia) # 0.08
