import pandas as pd
import numpy as np
from math import floor
from math import ceil

base = pd.read_csv('iris.csv')
print(base.head())

print('Num de registros', base.shape[0]) # 134 linhas

### AMOSTRAGEM SIMPLES

# Seleciona 5 dados SEM repetição
amostra = base.sample(n=5, random_state=42)
print(amostra)

# Seleciona 5 dados COM repetição
amostra = base.sample(n=5, random_state=42, replace=True)
print('\n', amostra)

### AMOSTRAGEM ESTRATIFICADA

# pega quantas classes diferente existem e quantos registros tem de cada
classes = base.groupby(['class']).size()
print('\nEstado:', classes)

# define o tamanho da amostra de cada classe
size_amostra_setosa = floor(classes['Iris-setosa'] / 10)
size_amostra_versicolor = floor(classes['Iris-versicolor'] / 10)
size_amostra_virginica = floor(classes['Iris-virginica'] / 10)
print('Num de amostras do tipo setosa: ', size_amostra_setosa)
print('Num de amostras do tipo versicolor: ', size_amostra_versicolor)
print('Num de amostras do tipo virginica: ', size_amostra_virginica)

# pega as amostras de cada classe de acordo com seu tamanho
amostra_setosa = base[base['class'] == 'Iris-setosa'].sample(n=size_amostra_setosa)
amostra_versicolor = base[base['class'] == 'Iris-versicolor'].sample(n=size_amostra_versicolor)
amostra_virginica = base[base['class'] == 'Iris-virginica'].sample(n=size_amostra_virginica)

print('amostras do tipo setosa. Tamanho: ', len(amostra_setosa))
print(amostra_setosa, '\n')
print('amostras do tipo versicolor. Tamanho: ', len(amostra_versicolor))
print(amostra_versicolor, '\n')
print('amostras do tipo virginica. Tamanho: ', len(amostra_virginica))
print(amostra_virginica)

### AMOSTRA SISTEMATICA

# define o tamanho da nossa amostra e de quanto em quanto irá pegar alguém da população
size_amostra = 20
size_populacao = base.shape[0]
size_salto = ceil(size_populacao / size_amostra)
print('\nselecionar um dado a cada: ', size_salto)

# define aleatoriamente a posicao do primeiro selecionado (de 0 até tamanho do salto)
inicio = np.random.randint(0, size_salto)
print('posicao do primeiro valor: ', inicio)

# define os indices (posicoes) dos dados a serem selecionados 
indices = np.arange(inicio, size_populacao, size_salto)
print('indices a serem selecionados na amotra', indices)

# seleciona os dados a partir dos indices
amostra_sistematica = base.iloc[indices]
print(amostra_sistematica)