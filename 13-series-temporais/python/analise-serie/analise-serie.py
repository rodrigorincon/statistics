import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
#registro de converters para uso do matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Carregamento da base de dados
base = pd.read_csv('../AirPassengers.csv')
print("Tamanho da base: ", base.shape)
print('\n', base.head(20), '\n')
print("Tipo de dados das colunas", base.dtypes) # Visualização do tipo de dados dos atributos

# Conversão dos atributos que estão no formato string para formato de data: ANO-MÊS
dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
base['Month'] = base['Month'].apply(dateparse)
print("\n Mes apos conversao: ", base['Month'], '\n')
print("\n", base.head(10), "\n")

#### Filtra valores por data SEM INDEX ---------------------------------------------

# Visualização por ano e mês
print("Filtrando por uma data especifica: ")
print(base.loc[base['Month'] == '1949-02', '#Passengers'])
# como convertemos month pra date podemos filtrar passando um objeto data tanto como string
print(base.loc[base['Month'] == datetime(1949,2,1), '#Passengers'])
print(base.loc[base.Month == datetime(1949,2,1), '#Passengers']) # podemos usar nome da coluna como atributo

# Visualização de intervalos
print(base.loc[base['Month'].between('1950-01-01', '1950-07-31'), '#Passengers'])
print(base.loc[base.Month.between('1950-01-01', '1950-07-31'), '#Passengers']) # podemos usar nome da coluna como atributo

###### Transforma data no index e filtra PELO INDEX ------------------------------------
base = base.set_index('Month')

print('\nFiltro por index por uma data especifica: ', base.loc['1949-02-01'])
print('\nFiltro por index por uma data especifica: ', base.loc[datetime(1949,2,1)])
print('\nFiltro por index por uma faixa de tempo: ', base.loc['1950-01-01':'1950-07-31'])
print('\nFiltro por index até uma data específica: ', base.loc[:'1950-07-31'], '\n')

###### Serie Temporal ------------------------------------------
#criação da série temporal (ts)
ts = base['#Passengers']
print(ts, '\n')
print("Data maxima: ", ts.index.max())
print("Data Mínima: ", ts.index.max())

###### PLOTAR GRÁFICOS DA SERIE --------------------------------
# Visualização da série temporal completa
plt.plot(ts)
plt.title('Serie Temporal')
plt.show()

# Visualização por mês (reune todos os janeiros num valor só, todos os fevereiros num valor... para comparar os meses de maior fluxo independente do ano)
ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)
plt.title('Soma dos passageiros em cada mês de 1949 até 1960')
plt.show()

# Visualização por ano
ts_ano = ts.groupby([lambda x: x.year]).sum()
plt.plot(ts_ano)
plt.title('Quantidade de passageiros em cada ano')
plt.show()

# Visualização entre datas específicas
ts_datas = base.loc['1960-01-01':'1960-12-01']
plt.plot(ts_datas)
plt.title('Quantidade de passageiros de Jan 1960 até Dez 1960')
plt.show()

####### DECOMPOSIÇÃO DA SÉRIE ----------------------------------------
from statsmodels.tsa.seasonal import seasonal_decompose

# Decomposição da série temporal, criando uma variável para cada formato
decomposicao = seasonal_decompose(ts, model="additive") # modelo default é additive
print(decomposicao) # retorna um objeto, só chamando seus atributos para visualizar algo

### TENDENCIA
tendencia = decomposicao.trend
print('\ntendencia:', tendencia)
# no inicio e no fim os dados tão todos NAN, mas no meio não
print("Tamanho: ", len(tendencia), "Numero de NAN: ", np.isnan(tendencia).sum())
print(tendencia.describe())
print('Imprimindo mais tendencias pra ver um valor nao NAN:')
print(tendencia.head(10))

### SAZONALIDADE
sazonal = decomposicao.seasonal
print('\nsazonal: ', sazonal)

### RUÍDO, ERRO OU RESÍDUOS (tudo que não é ciclo sazonal nem tendencia)
ruido = decomposicao.resid
print('\nruido: ', ruido)
# mesmo caso da tendencia, tem muitos valores NAN nas pontas, mas no meio tem valores reais
print("Tamanho: ", len(ruido), "Numero de NAN: ", np.isnan(ruido).sum())
print(ruido.describe())
print('Imprimindo mais ruídos pra ver um valor nao NAN:')
print(ruido.head(10))

# Visualização de gráfico para cada formato da série temporal
plt.plot(sazonal)
plt.title('Mostrando ciclos das compras de passagens')
plt.show()

plt.plot(tendencia)
plt.title('Mostrando tendencia das compras de passagem')
plt.show()

plt.plot(ruido)
plt.title('Mostrando ruído das compras de passagem')
plt.show()


plt.subplot(4,1,1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

# Visualização somente da tendência
plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

# Visualização somente da sazonalidade
plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

# Visualização somente do elemento aleatório
plt.subplot(4,1,4)
plt.plot(ruido, label = 'Ruído')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()