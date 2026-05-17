import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# ANOVA de 1 Via Pareado (quando as mesmas amostras são testados em diferentes condições)

# Ex: Quero checar a pressão de um grupo de pacientes antes, durante e depois de fazer um tratamento. 
# Todos os pacientes são medidos nos 3 momentos, ou seja, as amostras são dependentes.
# Queremos saber se há diferenças na pressão entre os momentos

antes = [85, 88, 92, 90]
durante = [78, 82, 86, 80]
depois = [92, 95, 89, 94]

tamanho_amostra = len(antes)

df = pd.DataFrame({
    'Momento': ['Antes']*tamanho_amostra + ['Durante']*tamanho_amostra + ['Depois']*tamanho_amostra,
    'Pressao': antes + durante + depois
})

# Ajuste o modelo Linear (OLS) - Variável Dependente ~ Variável Independente
# Pressao é a var dependente e Momento é a var independente/categórica
modelo = ols('Pressao ~ Momento', data=df).fit()

# Gere a tabela de ANOVA
tabela_anova = sm.stats.anova_lm(modelo, typ=2)
print(tabela_anova)

p_value = tabela_anova.iloc[0]['PR(>F)']
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("Há diferenças significativas entre os momentos")
else:
    print("Não há diferenças significativas entre os momentos")
