import pandas as pd
from scipy.stats import pearsonr

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

# calculating by scipy method
corr, p_value = pearsonr(df['Study_Hours'], df['Test_Scores'])
print("-------------")
print(f"Valor da correlação de Pearson: {corr:.4f}")
print(f"P-valor de Pearson: {p_value}")

# checking if changing the order the result is the same
corr, p_value = pearsonr(df['Test_Scores'], df['Study_Hours'])
print("-------------")
print(f"Valor da correlação de Pearson: {corr:.4f}")
print(f"P-valor de Pearson: {p_value}")