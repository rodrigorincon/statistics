from collections import Counter
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

lista = [1,1,1,1,2,2,2,3,3,4,4,4,5,5,6] # 4 1s, 3 2s, 2 3s, 3 4s, 2 5s and 1 6. Decrease until 3, growns on 4 and back to down

# using counter
counter = Counter(lista) # {1: 4, 2: 3, 4: 3, 3: 2, 5: 2, 6: 1}
for value, quantity in counter.items():
	print("the quantity of ", value, "is", quantity)

print("-----------------")

# using pandas
frequency_table = pd.Series(lista).value_counts()
for value, quantity in frequency_table.items():
	print("the quantity of ", value, "is", quantity)

print("----------------- grouping by sqare root rule")
# racers time in seconds
lista = [98, 99, 101, 101, 102, 102, 103, 103, 103, 104, 104, 105, 105, 105, 106, 106, 106, 106, 106, 107, 107, 108, 108, 111, 111, 112, 116]

qtt_unique_items = len(Counter(lista).keys())
number_groups = math.ceil(math.sqrt(qtt_unique_items))
amplitude = max(lista) - min(lista)
dist = math.ceil(amplitude / number_groups)

frequency = {}
min_value = min(lista)
for index in range(number_groups):
	init_time = min_value + index*dist
	final_time = init_time+dist
	name = 'from '+str(init_time)+' to '+str(final_time)

	# calculate the amount in this group
	frequency[name] = sum(1 for time in lista if init_time <= time < final_time)

print(frequency)

print("----------------- grouping by sturges rule")
qtt_unique_items = len(Counter(lista).keys())
number_groups = math.ceil(1 + 3.3 * math.log(qtt_unique_items,10))
amplitude = max(lista) - min(lista)
dist = math.ceil(amplitude / number_groups)

frequency = {}
min_value = min(lista)
for index in range(number_groups):
	init_time = min_value + index*dist
	final_time = init_time+dist
	name = 'from '+str(init_time)+' to '+str(final_time)

	# calculate the amount in this group
	frequency[name] = sum(1 for time in lista if init_time <= time < final_time)

print(frequency)

print("----------------- ploting using sturges")
#df = pd.DataFrame(lista, columns=['value'])
#plt.hist(df['value'], bins='sturges')
#plt.title("Histogram with Sturges' Rule")
#plt.show()

print("----------------- ploting using square")
df = pd.DataFrame(lista, columns=['value'])
plt.hist(df['value'], bins='sqrt')
plt.title("Histogram with Square Root' Rule")
plt.show()