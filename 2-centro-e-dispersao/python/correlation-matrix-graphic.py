import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# calculating all Pearson correlations between the pandas columns
df = pd.DataFrame({
    'Study_Hours': [10, 20, 30, 40, 50],
    'Test_Scores': [55, 65, 80, 85, 98],
    'Gaming_Hours': [5, 4, 3, 2, 1],
    'Names': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'] # Non-numeric (ignored)
})

# Compute the correlation matrix
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)

# Plot the correlation matrix
scatter_matrix(df, alpha=0.3, figsize=(10, 10), diagonal='kde')
plt.show()

# Plot the heat map
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()
