import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lista = [7, 20, 16, 6, 58, 9 ,20, 50, 23, 33, 8, 10, 15, 16, 104]
lista.sort()

print("-------------- calculating boxplot manually")

def adjust_max_and_min(my_list, value, is_min):
	if value < my_list[0]:
		return my_list[0]
	elif value > my_list[-1]:
		return my_list[-1]
	elif value in my_list:
		return value
	else:
		if is_min:
			for item in my_list:
				if item > value:
					return item
		else:
			for item in my_list[::-1]:
				if item < value:
					return item

average_index = int(len(lista)/2)
mediana = (lista[average_index] + lista[average_index-1])/2 if len(lista)%2 == 0 else lista[average_index]

q1_list = lista[:average_index]
average_q1_list_idx = int(len(q1_list)/2)
q1 = (q1_list[average_q1_list_idx] + q1_list[average_q1_list_idx-1])/2 if len(q1_list)%2 == 0 else q1_list[average_q1_list_idx]

q3_list = lista[average_index+1:]
average_q3_list_idx = int(len(q3_list)/2)
q3 = (q3_list[average_q3_list_idx] + q3_list[average_q3_list_idx-1])/2 if len(q3_list)%2 == 0 else q3_list[average_q3_list_idx]

iqr = q3 - q1
minimum = int(q1 - 1.5*iqr)
maximum = int(q3 + 1.5*iqr)

minimum = lista[0] if minimum < lista[0] else minimum
maximum = lista[-1] if maximum > lista[-1] else maximum

minimum = adjust_max_and_min(lista, minimum, True)
maximum = adjust_max_and_min(lista, maximum, False)

outliers = [item for item in lista if item < minimum or item > maximum]

print("minimum:", minimum, "Q1:", q1, "median:", mediana, "Q3:", q3, "maximum:", maximum)
print("outliers:", outliers)

print("-------------- calculating boxplot by pandas")

df = pd.DataFrame({'values': lista})
data = df.describe()
_, boxplot = pd.DataFrame.boxplot(df, return_type='both')

outliers = boxplot["fliers"][0].get_ydata()
minimum = boxplot["whiskers"][0].get_ydata()[-1]
maximum = boxplot["whiskers"][1].get_ydata()[-1]

print("minimum:", minimum, "Q1:", data.loc['25%']['values'], "median:", data.loc['50%']['values'], "Q3:", data.loc['75%']['values'], "maximum:", maximum)
print("outliers: ", outliers)
# pandas considered the median as part of the subarrays. To have the same results, change the lines 30 and 34 adding +1 q1 subarray and removing the "+1" in q3 subarray