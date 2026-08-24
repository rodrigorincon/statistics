import os
import threading
from multiprocessing import Process, Manager
import psutil
import time
import random

# cria diversos processos e threads dentro desses processos
# especifica em qual processador quer que o processo rode
# TODOS AS THREADS ESCREVEM NA MESMA MEMORIA COMPARTILHADA

def funcao_da_thread(nome, tempo, shared_mem):
    print(f"{nome} iniciada.")
    time.sleep(tempo)
    # escreve na memoria compartilhada
    shared_mem.append(random.randint(1, 365))    
    print(f"{nome} finalizada.")


def funcao_do_processo(core_id, shared_mem):
    # Identifica o processo atual (pega o PID)
    p = psutil.Process(os.getpid())
    # Define que o processo corrente vai rodar apenas no núcleo especificado
    p.cpu_affinity([core_id])

    lista_threads = []
    # Criando e iniciando 2 threads
    for i in range(2):
        nome_thread = 'Proc '+str(core_id)+' thread '+str(i)
        # Cria o objeto da Thread apontando para a função
        # Use 'args' em formato de tupla para passar os parâmetros
        thread = threading.Thread(target=funcao_da_thread, args=(nome_thread, 10, shared_mem))
        lista_threads.append(thread)
        thread.start() # Inicia a execução da thread

    # Aguardando todas as threads terminarem antes de avançar o código principal
    for t in lista_threads:
        t.join()

    print(f"----- Processo FINALIZADO no núcleo: {p.cpu_affinity()}")


# isso é obrigatoio quando usa Process
if __name__ == "__main__":
    # cria o gerenciador de memoria compartilhada
    # de todas as opções de memoria compartilhada é a mais lenta, pois por debaixo dos panos faz a comunicação via sockets
    # ele cria um servidor no processo pai e os filhos se comunicam com ele via socket (ou seja, não é bem uma memoria compartilhada)
    # vantagem: não precisa definir o tamanho da memoria nem gerencia-la byte a byte
    # o bloco já fecha a memoria compartilhada ao encerrar, fazendo todo o processo de liberar a memoria só de encerrar o bloco
    with Manager() as manager:
        # Apenas o numero de núcleos físicos do processador
        fisicos = psutil.cpu_count(logical=False)
        # Todos o numero de núcleos lógicos (com hyper-threading)
        logicos = psutil.cpu_count(logical=True)
        print(f"Núcleos físicos: {fisicos}")
        print(f"Núcleos lógicos: {logicos}")

        # cria uma memoria compartilhada entre todos os processos
        shared_mem = manager.list([])
        
        # Inicia um subprocesso em cada nucleo fisico
        lista_procs = []
        for core_id in range(fisicos):
            proc = Process(target=funcao_do_processo, args=(core_id, shared_mem))
            proc.start()
            lista_procs.append(proc)

        # Aguardando todos os processos terminarem antes de avançar o código principal
        for proc in lista_procs:
            proc.join()

        print("\nACABOU TUDO")
        print('Quantidade de dados: ', len(shared_mem), 'Dados gerados: ', shared_mem)
        print('Maior numero: ', max(shared_mem))
