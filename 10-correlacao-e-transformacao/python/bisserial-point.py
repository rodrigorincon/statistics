import scipy.stats as stats

# Category var
categories = {
  "success": [10, 15, 16, 18],
  "failure": [9, 12, 17, 21]
}

# to run bisserial we need to join all categories in a single array
# sort them by value to match them correctly with the continuous var
# and set all values in a category = 1 and the values in another = 0
# (success values = 1 and failure values = 0)
category_vars = [ {"value": value, "cat": "success"} for value in categories["success"] ] + [ {"value": value, "cat": "failure"} for value in categories["failure"] ]
category_vars.sort(key=lambda var: var['value'])
category_vars = [1 if var["cat"] == "success" else 0 for var in category_vars]
# category_vars = [0, 1, 0, 1, 1, 0, 1, 0]


# Continuous variable
continuous_var = [55, 85, 60, 90, 80, 50, 95, 65]

# Calculate Point-Biserial Correlation
# Ensure the category data is encoded numerically (0 and 1)
corr, p_value = stats.pointbiserialr(category_vars, continuous_var)

print(f"Point-Biserial Correlation: {corr:.4f}")
print(f"P-value: {p_value:.4f}")