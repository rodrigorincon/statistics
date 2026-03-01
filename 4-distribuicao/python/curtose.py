import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate x-axis
x = np.linspace(-5, 5, 1000)
# 1. Mesokurtic (Normal Distribution, Kurtosis = 0)
meso = stats.norm.pdf(x, 0, 1)
# 2. Leptokurtic (High Peak, e.g., Laplace Distribution)
lepto = stats.laplace.pdf(x, 0, 0.7)
# 3. Platykurtic (Flat, e.g., Uniform Distribution or low-kurtosis dist)
platy = stats.cosine.pdf(x, 0, 1.5)


# Calculating the kurtosis manually
print("--------- Calculating the kurtosis manually")
def kurtosis(my_list):
	average = np.mean(my_list)
	quadratic_deviation_list = [(value - average)**4 for value in my_list]
	momentum = sum(quadratic_deviation_list)/len(my_list)
	std_value = np.std(my_list) # standart deviation for POPULATION
	pearson_kurtosis = momentum/(std_value**4)
	regular_kurtosis = pearson_kurtosis - 3 # as the arrays was created by methods that uses Pearson method, subtract 3 for normal be = 0
	return round(regular_kurtosis, 3)
	
kurstosis_meso = kurtosis(meso)
kurstosis_lepto = kurtosis(lepto)
kurstosis_platy = kurtosis(platy)
print("kurstosis lepto: ", kurstosis_lepto) 
print("kurstosis normal: ", kurstosis_meso) # the value is not perfect 0 because the array was not created to be a perfect normal
print("kurstosis platy: ", kurstosis_platy)

# Calculating the kurtosis by scipy
print("--------- Calculating the kurtosis by scipy")
kurstosis_meso = stats.kurtosis(meso)
kurstosis_lepto = stats.kurtosis(lepto)
kurstosis_platy = stats.kurtosis(platy)
print("kurstosis lepto: ", round(kurstosis_lepto, 3))
print("kurstosis normal: ", round(kurstosis_meso,3))
print("kurstosis platy: ", round(kurstosis_platy,3))


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, lepto, label='Leptokurtic (High Peak, >0)', color='red')
plt.plot(x, meso, label='Mesokurtic (Normal, =0)', color='blue')
plt.plot(x, platy, label='Platykurtic (Flat, <0)', color='green')
plt.legend()
plt.title('Leptokurtic, Mesokurtic, and Platykurtic Distributions')
plt.show()