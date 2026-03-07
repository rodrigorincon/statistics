import numpy as np
import scipy.stats as stats 

# valores do exemplo da pizzaria
expected_value = 30
t_stat = 1.346
n = 30
# 30 dados, com media 32 e desvio 8 (como no exemplo)
dados = np.array([24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]) 


# teste unicaucal a direita  P(T > t)
p_value = 1 - stats.t.cdf(t_stat, n-1) # complementar para ficar P(T < t)
print("------------ \nunicaudal a direita: ", round(p_value, 4) )

t_stat2, p_value2 = stats.ttest_1samp(dados, expected_value, alternative='greater') # Teste t Unicaudal à Direita (alternative='greater')
print("Atraves do pacote: t=", round(t_stat2, 3), " p-value=", round(p_value2, 4) )

# teste unicaucal a esquerda  P(T < t)
p_value = stats.t.cdf(-t_stat, n-1) # T negativo por estar do lado esquerdo
print("------------ \nunicaudal a esquerda: ", round(p_value, 4) )

t_stat2, p_value2 = stats.ttest_1samp(dados, expected_value, alternative='less') # Teste t Unicaudal à Direita (alternative='less')
print("Atraves do pacote: t=", round(t_stat2, 3), " p-value=", round(p_value2, 4) )

# teste bicaudal  P(T = t)
p_value = 2*stats.t.cdf(-t_stat, n-1) # 2x a medida do lado esquerdo
print("------------ \nbicaudal: ", round(p_value, 4) )

t_stat2, p_value2 = stats.ttest_1samp(dados, expected_value, alternative='two-sided') # Teste t Unicaudal à Direita (alternative='two-sided')
print("Atraves do pacote: t=", round(t_stat2, 3), " p-value=", round(p_value2, 4) )

