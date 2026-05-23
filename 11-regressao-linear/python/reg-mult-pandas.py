import pandas as pd
import statsmodels.api as sm

preco = [840000, 822000, 713000, 689000, 685000, 645000, 625000, 620000, 587500, 585000, 583000, 569000, 546000, 540000, 537000, 
516000, 511000, 510000, 495000, 463000, 457000, 451000, 435000, 431700, 414000, 401500, 399000, 380000, 380000, 375900, 372000, 
367500, 356500, 330000, 330000, 307500]

area = [257, 232, 222, 204, 252, 234, 253, 226, 195, 180, 206, 303, 166, 138, 270, 181, 162, 160, 157, 159, 153, 156, 139, 176, 109, 
107, 128, 124, 118, 211, 93, 118, 132, 126, 136, 78]

banheiros = [3.5, 2.5, 3, 2.5, 3.5, 2, 2.5, 3.5, 1.5, 1.5, 2.5, 2, 2, 1.5, 2.5, 2, 1.5, 2, 2, 2, 2, 2, 1.5, 1.5, 1.5, 1, 1, 2, 1, 1, 1, 
1, 2, 1, 1, 1]

quartos = [4, 4, 3, 3, 3, 3, 4, 4, 3, 3, 3, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 4, 4, 3, 5, 2, 3, 2, 3, 3, 1]

casas = pd.DataFrame({
  'area': area,
  'banheiro': banheiros,
  'quarto': quartos,
  'preco': preco
})

x = casas[['area', 'banheiro', 'quarto']]
x = sm.add_constant(x)
y = casas['preco']
regressao = sm.OLS(y, x).fit()
print(regressao.summary(), "\n\n")
print(f'A equacao eh {regressao.params['quarto']:.0f}*Quartos + {regressao.params['banheiro']:.0f}*Banheiros + {regressao.params['area']:.0f}*Area + {regressao.params['const']:.0f}')

### fazendo a previsao de um novo valor
novo_valor_area = 100
novo_valor_quartos = 3
novo_valor_banheiros = 2
novo_X = pd.DataFrame({'const': [1], 'area': [novo_valor_area], 'quarto': [novo_valor_quartos], 'banheiro': [novo_valor_banheiros]})

preco_previsto = regressao.predict(novo_X)
print(f"Previsão para {novo_valor_area} m2, {novo_valor_banheiros} banheiros e {novo_valor_quartos} quartos:")
print(f"Preço previsto: R$ {preco_previsto[0]:.2f}")