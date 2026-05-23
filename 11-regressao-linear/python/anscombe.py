import matplotlib.pyplot as plt
import statsmodels.api as sm

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]

x3 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]

eixo_x1 = sm.add_constant(x1, has_constant='add')
regressao1 = sm.OLS(y1, eixo_x1).fit()
residuos1 = regressao1.resid

eixo_x2 = sm.add_constant(x2, has_constant='add')
regressao2 = sm.OLS(y2, eixo_x2).fit()
residuos2 = regressao2.resid

eixo_x3 = sm.add_constant(x3, has_constant='add')
regressao3 = sm.OLS(y3, eixo_x3).fit()
residuos3 = regressao3.resid

eixo_x4 = sm.add_constant(x4, has_constant='add')
regressao4 = sm.OLS(y4, eixo_x4).fit()
residuos4 = regressao4.resid

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 5))
axes[0,0].scatter(x1, residuos1)
axes[0,1].scatter(x2, residuos2)
axes[1,0].scatter(x3, residuos3)
axes[1,1].scatter(x4, residuos4)
for i in range(2):
  for j in range(2):
    axes[i,j].set_title("Gráficos dos resíduos")
plt.tight_layout()
plt.show() 