import numpy as np
import statsmodels.api as sm
import scipy.stats as stats

preco = [840000, 822000, 713000, 689000, 685000, 645000, 625000, 620000, 587500, 585000, 583000, 569000, 546000, 540000, 537000, 
516000, 511000, 510000, 495000, 463000, 457000, 451000, 435000, 431700, 414000, 401500, 399000, 380000, 380000, 375900, 372000, 367500,
356500, 330000, 330000, 307500]

m2 = [257, 232, 222, 204, 252, 234, 253, 226, 195, 180, 206, 303, 166, 138, 270, 181, 162, 160, 157, 159, 153, 156, 139, 176, 109, 107, 
128, 124, 118, 211, 93, 118, 132, 126, 136, 78]

# REGRESSÃO LINEAR SIMPLES

# Por algum motivo, o statsmodels não adiciona o intercepto automaticamente, então precisamos fazer isso manualmente.
X = sm.add_constant(m2) # Adicionar intercepto (A0 da equação y = A0 + A1*x)
y = preco
regressao = sm.OLS(y, X).fit() # OLS = Ordinary Least Squares (Mínimos Quadrados Ordinários). 

# RESPOSTA DA REGRESSÃO: COEFICIENTES
coef_ang = round(regressao.params[1], 2) # 1925.13
coef_lin = round(regressao.params[0], 2) # 172,690.60

# INTERVALO DE CONFIANÇA PARA OS COEFICIENTES
intervalos = regressao.conf_int() # recalcula o intervalo de confiança (por padrão com alfa=0.05)
margem_erro_m2 = np.round((intervalos[1][1] - intervalos[1][0])/2, 2)
margem_erro_preco = np.round((intervalos[0][1] - intervalos[0][0])/2, 2)

print('-------Resultados dos Coeficientes-------')
print(f'Coeficiente Angular (A1): {coef_ang} +- {margem_erro_m2}')
print(f'Coeficiente Linear (A0): {coef_lin} +- {margem_erro_preco}')

# INTERVALO DE REGRESSÃO
# calcula o valor para cada ponto da amostra seguindo a linha de regressão, com intervalo de confiança
previsoes = regressao.get_prediction( sm.add_constant(m2, has_constant='add') )
# calcula os intervalos de regressão para cada ponto da amostra
intervalo_reg = previsoes.conf_int(obs=True)

index_x = 0 # índice do imóvel com 257 m²
intervalo_inf = intervalo_reg[index_x][0]
intervalo_sup = intervalo_reg[index_x][1]
margem_erro = (intervalo_sup - intervalo_inf)/2

print(f'\n-------Intervalo de Regressão para m2 = {m2[0]} -------')
x_teste = m2[index_x]
valor_previsto = regressao.predict( sm.add_constant([x_teste], has_constant='add') )[0]
print(f'{round(valor_previsto, 2)} +- {round(margem_erro, 2)}')

# RESULTADO DOS TESTES DE HIPÓTESE PARA OS COEFICIENTES
p_values = regressao.pvalues
print('\n-------Teste T dos Coeficientes-------')
print(f'P-Value para A1 (m2): {p_values[1]}')
print(f'P-Value para A0 (const): {p_values[0]}')

# PREVER O VALOR PARA UM IMÓVEL DE 200 M²
area_nova = 200
X_novo = sm.add_constant([area_nova], has_constant='add') # Adicionar intercepto
previsao = regressao.predict(X_novo)
preco_previsto = previsao[0]

print(f'\n-------Previsão para Imóvel de {area_nova} m² -------')
print(f'Preço previsto: R$ {round(preco_previsto, 2)}')
