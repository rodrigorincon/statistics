import numpy as np
import matplotlib.pyplot as plt

# z = 1.96 (95% confident) error = 0.03
n_init = round((1.96/(2*0.03))**2)
print("n_init: ", n_init)

population_size_list = np.arange(20_000, 1_000_000, 10_000)

sample_size_list = [ (pop_size*n_init)/(pop_size+n_init) for pop_size in population_size_list]
x_axis = [pop_size/100_000 for pop_size in population_size_list]


plt.figure(figsize=(14, 6))
plt.plot(x_axis, sample_size_list)
plt.xticks( np.arange(0.2, 10, 0.4) )
plt.xlabel("Population Size (in 100_000)")
plt.ylabel("Sample Size (in units)")
plt.grid()
plt.show()
