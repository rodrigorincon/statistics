import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import kpss, adfuller
from arch.unitroot import PhillipsPerron # not usual lib, need to install it first
np.random.seed(123)

dados_estaionarios = np.random.normal(size=100)
dados_nao_estaionarios = np.cumsum( np.random.normal(scale=2, size=100) ) + np.linspace(0, 30, 100)

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.plot(dados_estaionarios)
plt.title('Dados estacionários')

plt.subplot(1, 2, 2)
plt.plot(dados_nao_estaionarios)
plt.title('Dados Não estacionários')
plt.show()

def analise_kpss(dados):
  statistic, p_value, lags, _ = kpss(dados)
  print(f"Estatsitica KPSS: {statistic:.2f}, P-valor: {p_value:.4f}, Defasagem: {lags:.2f}")
  if(p_value <= 0.05):
    print('Rejeito H0: Dados NÃO SÃO estácionários\n')
  else:
    print('aceito H0: Dados SÃO estácionários\n')

analise_kpss(dados_estaionarios)
analise_kpss(dados_nao_estaionarios)

def analise_adf(dados):
  # LAG = defasagem = num de dados passados a serem considerados (tamanho da janela)
  # se for pequeno, tudo é considerado ruído e ñ pega a correlação entre valores passados e futuros
  # se for grande, consome os graus de liberdade e reduz poder do teste (maior chance de erro tipo 2 - aceitar H0 quando ela é falsa)
  # DF = N-1
  # autolag = define qual métrica será usada para escolher o valor do lag (no caso usa o lag que der o menor AIC)
  statistic, p_value, lags, df, _, _ = adfuller(dados, maxlag=12, autolag='AIC') # maxlag default = 12*raiz_quarta(DF/100)
  print(f"Estatsitica ADF: {statistic:.2f}, P-valor: {p_value:.4f}, Defasagem: {lags:.2f}, Graus de Liberdade: {df:.2f}")
  if(p_value <= 0.05):
    print('Rejeito H0: Dados SÃO estácionários\n')
  else:
    print('aceito H0: Dados NÃO SÃO estácionários\n')

analise_adf(dados_estaionarios)
analise_adf(dados_nao_estaionarios)


def analise_pp(dados):
  pp_test = PhillipsPerron(dados, trend="c")
  print(f"Estatsitica PP: {pp_test.stat:.2f}, P-valor: {pp_test.pvalue:.4f}, Defasagem: {pp_test.lags:.2f}")
  if(pp_test.pvalue <= 0.05):
    print('Rejeito H0: Dados SÃO estácionários\n')
  else:
    print('aceito H0: Dados NÃO SÃO estácionários\n')

analise_pp(dados_estaionarios)
analise_pp(dados_nao_estaionarios)