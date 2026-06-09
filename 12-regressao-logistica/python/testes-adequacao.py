import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import sklearn.metrics as skl

idades = [45, 50, 30, 60, 55, 40, 35, 70, 65, 50, 42, 36, 53, 58, 62, 39, 48, 33, 66, 41, 57, 49, 34, 61, 47, 38, 54, 63, 32, 46]
glicose = [85, 120, 75, 140, 110, 90, 80, 160, 150, 100, 95, 82, 115, 135, 145, 87, 102, 78, 155, 98, 128, 106, 81, 138, 104, 89, 118, 148, 77, 112]
diabetes = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]

X = pd.DataFrame({'idade': idades, 'glicose': glicose})
y = pd.DataFrame({'diabetes': diabetes})

X = sm.add_constant(X)
modelo = sm.Logit(y, X)
resultado = modelo.fit()
print(resultado.summary(), '\n\n')

##### CRIA COLUNAS NOVAS COM A PROB E A CLASSE PREVISTA

todos_dados = pd.DataFrame({'idade': idades, 'glicose': glicose, 'diabetes': diabetes})

todos_dados['probabilidade'] = resultado.predict(X)
todos_dados['classe_predita']= (todos_dados['probabilidade']>0.5).astype(int) #converter para 0 ou 1
print(todos_dados.head(10), '\n\n')

##### AVALIACAO DE PEFORMANCE

real = diabetes
previsto = todos_dados['classe_predita']

cm = skl.confusion_matrix(real, previsto)
print('Matriz de Confusão: \n', cm) 
# [18, 1]
# [3,  8]
# Isso significa que a maioria dos dados eram positivos (19 em 30) e quase todos foram corretamente previstos (só 1 falso negativo)
# Nossa amostra de testes não tava bem balanceada, com poucos negativos pra usar de treino em comparação com positivos
# 5,2% dos positivos foram previstos errado, enquanto 27% dos negativos foram previstos errado. 
# O que nos diz que nosso modelo prevê bem positivos mas muito mal negativos. Tem uma deficiência nesse lado

# Tivemos baixíssimos falsos positivos (3) e falsos negativos (1). Os corretos foram muito maiores (18 e 8). Mas foram altos os suficiente?
# falso negativo = 0,033 (3,3%) abaixo do beta. ÓTIMO
# falso positivo = 0,1 (10%) acima do alfa. RUIM. Precisa ser menor

# visualizando a matriz de confusão de forma mais bonita, com heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Positivo", "Negativo"], yticklabels=["Positivo", "Negativo"])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

# Podemos calcular nossas métricas a partir da matriz, mas o scikit learn nos dá funções pra pegar os dados direto, 
# Sem nem precisar calcular a matriz de confusão antes

#Acurácia
acc = skl.accuracy_score(real, previsto)
print(f'Acurácia: {acc:.2f}') # 87% de previsões corretas

#Precisão
prec = skl.precision_score(real, previsto)
print(f'Precisão: {prec:.2f}') # 89% de precisão no positivo (coluna)

#Sensibilidade
rec = skl.recall_score(real, previsto)
print(f'Sensibilidade: {rec:.2f}') # 73% de assertividade no positivo (linha)

#F1-score
f1 = skl.f1_score(real, previsto)
print(f'F1-score: {f1:.2f}') # 80%

## CURVA ROC
print('\n\n')

eixo_x, eixo_y, _ = skl.roc_curve(real, todos_dados['probabilidade'])
print("Curva ROC: eixo X: ", eixo_x)
print("Curva ROC: eixo Y: ", eixo_y)

#AUC

roc_auc = skl.auc(eixo_x, eixo_y)
print("AUC ROC: ", roc_auc) # QUANTO MAIS PROXIMO DE 1 MELHOR. 0.5 É IGUAL A UM CHUTE. Res: 0,97

#Gráfico

plt.figure(figsize=(7, 5))
plt.plot(eixo_x, eixo_y, color='navy', lw=2, label=f'AUC = {roc_auc:.2f}') # nossa curva
plt.plot([0, 1], [0, 1], color='darkorange', linestyle='--') # diagonal
plt.xlim([-0.05, 1.05]) # Bom add essa margem no gráfico pra curva não ficar colada nos limites do gráfico
plt.ylim([-0.05, 1.05])
plt.xlabel('Taxa de Falsos Positivos (FRP)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.show()