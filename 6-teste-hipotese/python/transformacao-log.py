import numpy as np
import matplotlib.pyplot as plt

# Compare data with your log based version
data = [10,11,11,12,12,12,13,13,13,14,14,14,15,15,16,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
ln_data = np.log(data) # this is ln, not log in 10 base
# ln_data = [2.3, 2.4, 2.4, 2.48, 2.48, 2.48, 2.56, 2.56, 2.56, 2.64, 2.64, 2.64, 2.71, 2.71, 2.77, 
#            2.77, 2.83, 2.89, 2.94, 3.0, 3.04, 3.09, 3.14, 3.18, 3.22, 3.26, 3.3, 3.33, 3.37, 3.4]
print("log data:", [round(num,2) for num in ln_data] ) # round the log data to read easily
print("-----------")

print("regular std: ", np.std(data), "log data std: ", np.std(ln_data))

# Plot side by side both data to show as log data is more normalized
fig, axes = plt.subplots(1, 2, figsize=(12, 8))
axes[0].boxplot(data)
axes[0].set_title('Regular Data')
axes[1].boxplot(ln_data)
axes[1].set_title('Log Data')

plt.tight_layout()
plt.show()
