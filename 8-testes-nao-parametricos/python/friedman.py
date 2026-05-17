from scipy import stats

# Example data: reaction times for 5 patients on 3 different drugs
drug1 = [5, 5, 5.4, 7.4, 8.5, 7.2, 6.5, 6]
drug2 = [5.5, 6.6, 5.8, 8, 9, 8.3, 6.1, 7]
drug3 = [5.4, 7.8, 6, 8.5, 9.4, 9, 6.5, 6.8]

# Run the Friedman Test
res = stats.friedmanchisquare(drug1, drug2, drug3)

print(f"F: {res.statistic}")
print(f"P-value: {res.pvalue}")
