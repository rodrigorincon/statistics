import pandas as pd
import matplotlib.pylab as plt
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, root_mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import os
import threading
from multiprocessing import Process, Manager
import psutil
import warnings
warnings.filterwarnings("ignore")

def loop_arima_and_forecast(train_data, test, p, start_q, end_q, shared_mem):
  aic_stats = {"p": 0, "q": 0, "d": 0, "aic": 999_999_999, "previsoes": [], "rmse": 999_999_999, "mae": 999_999_999, "mape": 1}
  err_stats = {"p": 0, "q": 0, "d": 0, "aic": 999_999_999, "previsoes": [], "rmse": 999_999_999, "mae": 999_999_999, "mape": 1}

  max_d = 30
  for q in range(start_q, end_q, 2):
    for d in range(2, max_d+1):
      try:
        model = ARIMA(train_data, order=(p, d, q)).fit(method='innovations_mle') 
        # prevê os proximos valores
        previsoes = model.forecast(steps= test.shape[0] )
        mae = mean_absolute_error(test['close'], previsoes)
        mape = mean_absolute_percentage_error(test['close'], previsoes)
        rmse = root_mean_squared_error(test['close'], previsoes)
        if(model.aic < aic_stats['aic']):
          aic_stats['aic'] = model.aic
          aic_stats['p'] = p
          aic_stats['d'] = d
          aic_stats['q'] = q
          aic_stats['previsoes'] = previsoes
          aic_stats['rmse'] = rmse
          aic_stats['mae'] = mae
          aic_stats['mape'] = mape
        if(rmse < err_stats['rmse']):
          err_stats['aic'] = model.aic
          err_stats['p'] = p
          err_stats['d'] = d
          err_stats['q'] = q
          err_stats['previsoes'] = previsoes
          err_stats['rmse'] = rmse
          err_stats['mae'] = mae
          err_stats['mape'] = mape
      except ValueError:
        pass
  shared_mem.append({'aic': aic_stats, 'err': err_stats})
  print('Concluido ', len(shared_mem), 'de 120')

def funcao_do_processo(core_id, shared_mem, p, train_data, test):
  # Identifica o processo atual (pega o PID)
  proc = psutil.Process(os.getpid())
  # Define que o processo corrente vai rodar apenas no núcleo especificado
  proc.cpu_affinity([core_id])

  lista_threads = []
  # Criando e iniciando 10 threads
  start_q = 4 # testa de 4 a 282 (pulando de 2 em 2)
  for i in range(10):
    start_q = start_q + i*28
    end_q = start_q + 28 # cada um processa 14

    # Cria o objeto da Thread apontando para a função
    thread = threading.Thread(target=loop_arima_and_forecast, args=(train_data, test, p, start_q, end_q, shared_mem))
    lista_threads.append(thread)
    thread.start() # Inicia a execução da thread

  # Aguardando todas as threads terminarem antes de avançar o código principal
  for t in lista_threads:
    t.join()


# isso é obrigatoio quando usa Process
if __name__ == "__main__":
  # PEGA OS DADOS A SEREM ANALISADOS
  df = pd.read_csv('../all_stocks_5yr.csv')
  df = df[df.Name == 'AAPL'].set_index('date')

  # SEPARA OS DADOS EM TREINO E TESTE
  ponto_corte = int(df.shape[0] * 0.8)
  train = df[:ponto_corte]
  test = df[ponto_corte:]

  # Apenas o numero de núcleos logicos do processador
  num_processadores = psutil.cpu_count(logical=True)

  # cria o gerenciador de memoria compartilhada
  with Manager() as manager:
    # cria uma memoria compartilhada entre todos os processos
    shared_mem = manager.list([])

    # Inicia um subprocesso em cada nucleo fisico
    lista_procs = []
    start_p = 4 # testa de 4 até 28
    # cria 1 processo em cada processador. Cada um executa só 1 P (só P par)
    for core_id in range(num_processadores):
      proc = Process(target=funcao_do_processo, args=(core_id, shared_mem, start_p, train['close'], test))
      proc.start()
      lista_procs.append(proc)
      start_p += 2

    # Aguardando todos os processos terminarem antes de avançar o código principal
    for proc in lista_procs:
      proc.join()

    print('\n\n\n\n\n=====================')
    print('CALCULADO ', len(shared_mem), 'ARIMAs')

    aic_stats = {'aic': 999_999_999}
    err_stats = {'rmse': 999_999_999}
    for stat in shared_mem:
      if(stat['aic']['aic'] < aic_stats['aic']):
        aic_stats = stat['aic']
      if(stat['err']['rmse'] < err_stats['rmse']):
        err_stats = stat['err']

    print('MELHOR MODELO SEGUNDO AIC -------------')
    print(f'P= {aic_stats['p']:.4f}, Q={aic_stats['q']:.4f}, D={aic_stats['d']:.4f}, AIC={aic_stats['aic']:.4f}, RMSE={aic_stats['rmse']:.4f}, MAE={aic_stats['mae']:.4f}, MAPE={(100*aic_stats['mape']):.2f}%', '\n')
    print('MELHOR MODELO SEGUNDO RMSE -------------')
    print(f'P= {err_stats['p']:.4f}, Q={err_stats['q']:.4f}, D={err_stats['d']:.4f}, AIC={err_stats['aic']:.4f}, RMSE={err_stats['rmse']:.4f}, MAE={err_stats['mae']:.4f}, MAPE={(100*err_stats['mape']):.2f}%', '\n')

    ## plotando os valores previstos pro AIC com os reais
    plt.plot(df.index, df['close'], label='Original', color='blue')
    plt.plot(test.index, aic_stats['previsoes'], label='Teste', color='orange')
    plt.legend(loc="upper left")
    plt.title('Melhor Previsão segundo AIC')
    plt.show()

    # plotando só a parte comum aos 2 para ver mais de perto quão próximo foi
    plt.plot(test.index, test['close'], label='Original', color='blue')
    plt.plot(test.index, aic_stats['previsoes'], label='Teste', color='orange')
    plt.legend(loc="upper left")
    plt.title('Zoom na parte do teste segundo AIC')
    plt.show()


    ## plotando os valores previstos pro ERRO com os reais
    plt.plot(df.index, df['close'], label='Original', color='blue')
    plt.plot(test.index, err_stats['previsoes'], label='Teste', color='orange')
    plt.legend(loc="upper left")
    plt.title('Melhor Previsão segundo RMSE')
    plt.show()

    # plotando só a parte comum aos 2 para ver mais de perto quão próximo foi
    plt.plot(test.index, test['close'], label='Original', color='blue')
    plt.plot(test.index, err_stats['previsoes'], label='Teste', color='orange')
    plt.legend(loc="upper left")
    plt.title('Zoom na parte do teste segundo RMSE')
    plt.show()