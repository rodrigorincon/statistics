import numpy as np

lista = [10,2,4,13,5,8,11,12,7,1,6,9,3]

##### AMPLITUDE
amplitude = max(lista) - min(lista) # subtract the biggest and the smallest values
print("the amplitute is", amplitude) # 12


##### MEDIA ARITIMETICA
media = np.mean(lista) # sum all values and divide by the length
media2 = sum(lista)/len(lista) # another way to calculate the average
print("the average is ", media) # 7
print("the average is ", media2) # 7


##### MEDIANA
mediana = np.median(lista) # sort the elements and gets the middle element. if the array has a even quantity, returns the average of the 2 middle elements
print("the median is", mediana)
# test median with even elements
print("the median is", np.median([1,2,3,4])) # 2.5
# test median with odd elements
print("the median is", np.median([1,2,3])) # 2


##### MODA
lista = [1,1,1,1,2,2,2,3,3,4,4,4,5,5,6] # 4 1s, 3 2s, 2 3s, 3 4s, 2 5s and 1 6. Decrease until 3, growns on 4 and back to down

from collections import Counter
counter = Counter(lista)
moda = counter.most_common(1)[0][0] # gets the most repeated element (1)
print("the moda is ", moda) # 1

import statistics
moda2 = statistics.mode(lista) # another way to calculate the moda
print("the moda is ", moda2) # 1

import pandas as pd
df = pd.DataFrame({'values' :lista})
moda3 = df['values'].mode()[0] # another way to calculate the moda
print("the moda is ", moda3) # 1


##### ESPERANCA
from collections import Counter
counter = Counter(lista) # {1: 4, 2: 3, 4: 3, 3: 2, 5: 2, 6: 1}
esperanca = 0
for value, quantity in counter.items():
	esperanca += value * quantity/len(lista)
print("the esperanca is ", esperanca) # 2.9

values = np.array([1,2,3,4,5,6])
probs = np.array([4/15, 3/15, 2/15, 3/15, 2/15, 1/15])
esperanca = np.sum(values * probs) # another way to calculate esperanca, using 2 arrays
print("the esperanca is ", esperanca) # 2.9
