import pandas as pd
import matplotlib.pyplot as plt

# Criando dados de exemplo (ex: preços de fechamento)
dados = {'preco': [10, 12, 15, 14, 13, 15, 18, 16, 15, 16, 17, 17, 16, 15, 12, 11, 10, 11, 10, 11, 12, 13, 15, 14, 17]}
df = pd.DataFrame(dados)

# Média Móvel Simples com janela de 3 períodos
df['media_simples_3'] = df['preco'].rolling(window=3).mean().round(2)
# Média Móvel Simples com janela de 5 períodos
df['media_simples_5'] = df['preco'].rolling(window=5).mean().round(2)

# Média Móvel Exponencial com janela de 3 períodos
df['media_expo_3'] = df['preco'].ewm(span=3, adjust=False).mean().round(2)
# Média Móvel Exponencial com janela de 5 períodos
df['media_expo_5'] = df['preco'].ewm(span=5, adjust=False).mean().round(2)
print(df)

### Grafico com medias simples
eixo_x = range(1,len(df['preco'])+1)
plt.figure(figsize=(10, 6))
plt.bar(eixo_x, df['preco'])
plt.plot(eixo_x, df['media_simples_3'], color='black', label='simples 3')
plt.plot(eixo_x, df['media_simples_5'], color='red', label='simples 5')
plt.xlabel('Dias')
plt.ylabel('Valor do dia')
plt.title("Médias Móveis simples de 3 e 5 dias")
plt.legend()
plt.show()
# EM AMBOS OS CASOS, A MÉDIA DA JANELA MAIS CURTA ANDA MAIS PROXIMA DOS VALORES ATUAIS, MUDANDO MAIS RAPIDO

### Grafico com medias exponenciais
plt.figure(figsize=(10, 6))
plt.bar(eixo_x, df['preco'])
plt.plot(eixo_x, df['media_expo_3'], color='black', label='exponencial 3')
plt.plot(eixo_x, df['media_expo_5'], color='red', label='exponencial 5')
plt.xlabel('Dias')
plt.ylabel('Valor do dia')
plt.title("Médias Móveis exponencial de 3 e 5 dias")
plt.legend()
plt.show()
# EM AMBOS OS CASOS, A MÉDIA DA JANELA MAIS CURTA ANDA MAIS PROXIMA DOS VALORES ATUAIS, MUDANDO MAIS RAPIDO

### Grafico com media simples e exponencial com mesma janela
plt.figure(figsize=(10, 6))
plt.bar(eixo_x, df['preco'])
plt.plot(eixo_x, df['media_simples_3'], color='black', label='simples 3')
plt.plot(eixo_x, df['media_expo_3'], color='red', label='exponencial 3')
plt.xlabel('Dias')
plt.ylabel('Valor do dia')
plt.title("Médias Móveis simples e exponencial de 3 dias")
plt.legend()
plt.show()
# A EXPONENCIAL ANDA MAIS PROXIMA DOS VALORES ATUAIS, MUDANDO MAIS RAPIDO