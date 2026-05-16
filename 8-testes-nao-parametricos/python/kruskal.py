from scipy.stats import kruskal
import scikit_posthocs as sp
import pandas as pd

blacks = [1246, 1148, 1300, 1404, 1396, 1450]
hispanics = [1267, 1228, 1450, 1351, 1280]
whites = [1581, 1649, 9811, 8771, 629, 1800, 1423]
asians = [1623, 1550, 1936, 1800, 1750]

h_stat, p_value = kruskal(blacks, hispanics, whites, asians)
print(f"Kruskal-Wallis H-statistic: {h_stat}")
print(f"P-value: {p_value}")

# Teste post-hoc de dunn
df = pd.DataFrame({
  'Etnia': ['black'] * len(blacks) + ['hispanic'] * len(hispanics) + ['white'] * len(whites) + ['asian'] * len(asians),
  'Notas': blacks + hispanics + whites + asians
})

dunn_test = sp.posthoc_dunn(df['Notas'], val_col='Notas', group_col='Etnia', p_adjust='bonferroni')

# encontrar todos os valores p < 0.05
significant = []
for i in dunn_test.index:
  for j in dunn_test.columns:
    # evitar duplicatas e diagonal
    if i >= j:
      continue
    p = dunn_test.loc[i, j]
    if pd.notna(p) and p < 0.05:
      significant.append((i, j, p))

if significant:
  for a, b, p in significant:
    print(f"Significant: {a} vs {b} (p={p:.4f})")
else:
  print("No significant pairs (p<0.05).")
