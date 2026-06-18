import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf # yahoo-finance. Biblioteca para baixar dados de mercado

# Criando dados de exemplo (ex: preços de fechamento)
df = yf.download('BTC-USD', start='2025-01-01', end='2026-01-01')['Close']

# Média Móvel Simples com janela de 7 dias
df['simples'] = df['BTC-USD'].rolling(window=7).mean().round(2)
# Média Móvel Exponencial com janela de 7 dias
df['expo'] = df['BTC-USD'].ewm(span=7, adjust=False).mean().round(2)

print(df.head(10))

### Grafico com medias simples
eixo_x = range(1,len(df['BTC-USD'])+1)
plt.figure(figsize=(10, 6))
plt.bar(eixo_x, df['BTC-USD'])
plt.plot(eixo_x, df['simples'], color='black', label='media simples')
plt.plot(eixo_x, df['expo'], color='red', label='media exponencial')
plt.xlabel('Dias')
plt.ylabel('Valor do dia')
plt.title("Médias Móveis simples e exponencial")
plt.legend()
plt.show()
