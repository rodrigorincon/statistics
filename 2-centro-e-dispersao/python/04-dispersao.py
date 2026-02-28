import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib.ticker import PercentFormatter

print("-------------- calculating athletes and families weight")
athletes = [74, 77, 78, 78, 79, 80, 80, 80, 81, 81, 82, 82, 85, 87, 89]
families = [45, 54, 59, 64, 67, 68, 70, 72, 73, 75, 77, 81, 82, 86, 96]

ath_mean = np.mean(athletes)
ath_vari = statistics.pvariance(athletes)
ath_std  = np.std(athletes)
ath_cv   = ath_std/ath_mean

fam_mean = np.mean(families)
fam_vari = statistics.pvariance(families)
fam_std  = np.std(families)
fam_cv   = fam_std/fam_mean


print("athletes: mean:", round(ath_mean) , " vari: ", round(ath_vari, 3), " std: ", round(ath_std, 2), "vari coef: ", round(ath_cv, 4))
print("families: mean:", round(fam_mean) , " vari: ", round(fam_vari, 3), " std: ", round(fam_std, 2), "vari coef: ", round(fam_cv, 4))

# Plotting the arrays ----------------------------------------------------------------
def plot_wheight():
	df = pd.DataFrame({"athletes": athletes, "families": families})
	df.plot(kind='hist', bins=10, alpha=0.5) # alpha adds transparency for overlaid histograms
	plt.xlabel('weight')
	plt.ylabel('Frequency')
	plt.show()

#plot_wheight()

####### Read all Mega Sena results until 2026-02-28 ----------------------------------------------------------------
file_path = '../images/Mega-Sena.xlsx'
df_excel = pd.read_excel(file_path)

bolas_list_nested = df_excel[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']].values.tolist()
bolas_list = list(itertools.chain.from_iterable(bolas_list_nested))

# Plotting the Mega Sena results ----------------------------------------------------------------
def plot_lotery_with_decimal_y_axis():
	df = pd.DataFrame({"Lottery_Results": bolas_list})
	df.plot(kind='hist', bins=10)
	plt.xlabel('Bolas')
	plt.ylabel('Frequency')
	plt.show()

#plot_lotery_with_decimal_y_axis()

# The same graphic, but with Y-axis in percentage ----------------------------------------------------------------
def plot_lotery_with_percent_y_axis():
	df = pd.DataFrame({"Lottery_Results": bolas_list})
	plt.hist(df['Lottery_Results'], weights=np.ones(len(df)) / len(df))
	plt.gca().yaxis.set_major_formatter(PercentFormatter(1)) # change the Y-axis from decimal (0.1) for percentage format (10%)
	plt.xlabel('Bolas')
	plt.ylabel('Frequency')
	plt.show()

#plot_lotery_with_percent_y_axis()

# get the 6 most drawn numbers ----------------------------------------------------------------
print("----------------- printing lotery percents")
counts = np.bincount(bolas_list) # count how much times which value appears
sorted_indices = np.argsort(counts)[::-1] # Get a sorted list of indices of the most frequent values
top_frequent_idx = sorted_indices[:6]

top_frequent_values = {}
for index in top_frequent_idx:
	top_frequent_values[index] = round(100*6*counts[index]/len(bolas_list), 2) # change to percent and round with 2 decimal
print("6 most common numbers: ", top_frequent_values)

# get the 6 less drawn numbers ----------------------------------------------------------------
less_frequent_idx = sorted_indices[-7:-1]

less_frequent_values = {}
for index in less_frequent_idx:
	less_frequent_values[index] = round(100*6*counts[index]/len(bolas_list), 2) # change to percent and round with 2 decimal
print("6 less common numbers: ", less_frequent_values)
print("Lotery amplitude percentage: "+ str(round(100*6*(counts[sorted_indices[0]] - counts[sorted_indices[-2]])/len(bolas_list),2))+ "%" )
