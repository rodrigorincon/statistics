import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.DataFrame({
  "salario": [5625, 4459, 4170, 9323, 5306, 6296, 5458, 5086, 5358, 4865, 7357, 7384, 4352, 4970, 5290, 4979, 7315, 5233, 9560, 5267, 5129, 9516, 5877, 4915, 5742, 5433, 4630, 4729, 6844, 8005, 5634, 4766, 4949, 4560, 5353, 8211, 5534, 6814, 6474, 5175, 5120, 6088],
  "experiencia": [14, 6, 2, 34, 21, 35, 14, 3, 20, 4, 28, 26, 6, 16, 22, 7, 32, 14, 29, 15, 6, 36, 33, 15, 30, 26, 7, 2, 26, 28, 24, 6, 13, 8, 17, 25, 28, 36, 23, 19, 8, 35],
  "sexo": ["M", "M", "F", "M", "M", "F", "M", "M", "F", "M", "M", "M", "F", "F", "F", "M", "F", "M", "M", "M", "M", "M", "F", "F", "F", "F", "M", "M", "M", "M", "M", "F", "M", "F", "F", "M", "F", "F", "M", "F", "F", "F"],
  "idade60": ["Abaixo", "Abaixo", "Abaixo", "Acima", "Abaixo", "Acima", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Acima", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Acima", "Acima", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Acima", "Acima", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Abaixo", "Acima", "Abaixo", "Abaixo", "Abaixo", "Acima"]
})

# Forma 1
modelo = smf.ols('salario ~ experiencia + C(sexo, Treatment(reference="F")) + C(idade60, Treatment(reference="Abaixo"))', data = df).fit()
print(modelo.summary(), "\n")

# estimando valores
novo_valor_exp = 5
novo_valor_sexo = 'M'
novo_valor_idade = 'Abaixo'

novo_X = pd.DataFrame({'const': [1], 'experiencia': [novo_valor_exp], 'sexo': [novo_valor_sexo], 'idade60': [novo_valor_idade]})
salario_previsto = modelo.predict(novo_X)
print(f'Previsão para {novo_valor_exp} anos de experiência, sexo {novo_valor_sexo} e idade {novo_valor_idade} de 60 anos:')
print(f'Salário previsto: R$ {salario_previsto[0]:.2f}\n\n\n')

# Forma 2
sexo = (df['sexo'] == 'M').astype(int) # M=1, F=0
idade60 = (df['idade60'] == 'Acima').astype(int) # Acima=1 Abaixo=0

list_x = pd.DataFrame({
    'experiencia': df['experiencia'],
    'sexo': sexo,
    'idade60': idade60
}) # usa dataframe para passar os dados pq a função espera os dados onde cada linha é um ponto. Passar como um array vai dar erro
# em outras palavras, como array passaria uma matriz 3x42 e o métodos espers 42x3
x = sm.add_constant(list_x)
modelo = sm.OLS(df['salario'], x).fit()
print(modelo.summary(), "\n")

# estimando valores
novo_valor_exp = 5
novo_valor_sexo = 1 # 'M'
novo_valor_idade = 0 #'Abaixo'
# como estamos usando os valores 0 e 1 direto, precisamos passar os valores pra pedição do mesmo modo, pois o método não foi informado que há vars categóricas

novo_X = pd.DataFrame({'const': [1], 'experiencia': [novo_valor_exp], 'sexo': [novo_valor_sexo], 'idade60': [novo_valor_idade]})
salario_previsto = modelo.predict(novo_X)
print(f'Previsão para {novo_valor_exp} anos de experiência, sexo {novo_valor_sexo} e idade {novo_valor_idade} de 60 anos:')
print(f'Salário previsto: R$ {salario_previsto[0]:.2f}')
