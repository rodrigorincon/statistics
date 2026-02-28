import matplotlib.pyplot as plt
import statistics as stats
import numpy as np

data = list(range(1,1000))

cumulative_hmeans = []
cumulative_ameans = []
cumulative_gmeans = []
cumulative_qmeans = []

# Calculate the harmonic mean cumulatively
for i in range(1, len(data) + 1):
    current_data = data[:i]
    # The statistics module's harmonic_mean() function is easy to use
    hmean = stats.harmonic_mean(current_data)
    amean = np.mean(current_data)
    gmean = stats.geometric_mean(current_data)
    qmean = np.sqrt(np.mean(np.square(current_data)))
    cumulative_hmeans.append(hmean)
    cumulative_ameans.append(amean)
    cumulative_gmeans.append(gmean)
    cumulative_qmeans.append(qmean)

# Create the graphic
plt.figure(figsize=(10, 6))
plt.plot(data, cumulative_hmeans, marker='o', linestyle='-', color='b', label='Média Harmonica')
plt.plot(data, cumulative_ameans, marker='o', linestyle='-', color='g', label='Média Aritimetica')
plt.plot(data, cumulative_gmeans, marker='o', linestyle='-', color='r', label='Média Geometrica')
plt.plot(data, cumulative_qmeans, marker='o', linestyle='-', color='purple', label='Média Quadratica')

# Add titles and labels
plt.title('Cumulative Means')
plt.xlabel('Elements Considered')
plt.ylabel('Means Value')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()