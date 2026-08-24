import os
import threading
from multiprocessing import Process, Manager
import psutil
import random

# cria diversos processos e threads dentro desses processos
# especifica em qual processador quer que o processo rode
# todas as threads escrevem na mesma memoria compartilhada
# ESCREVE SÓ SE O VALOR CALCULADO FOR MAIOR QUE O DA MEMORIA
# USA LOCK PARA GARANTIR ESCRITA CORRETA (EVITAR RACE CONDITION)

def funcao_da_thread(shared_mem, shared_lock):
    # escreve na memoria compartilhada
    valor_calc = random.randint(1, 365)
    print('Valor calculado: ', valor_calc)
    if(valor_calc > shared_mem['maior']):
        # o bloco with bloqueia a memoria compartilhada e a libera automaticamente quando o bloco termina
        with shared_lock:
            shared_mem['maior'] = valor_calc


def funcao_do_processo(core_id, shared_mem, shared_lock):
    # Identifica o processo atual (pega o PID)
    p = psutil.Process(os.getpid())
    # Define que o processo corrente vai rodar apenas no núcleo especificado
    p.cpu_affinity([core_id])

    lista_threads = []
    # Criando e iniciando 2 threads
    for i in range(2):
        # Cria o objeto da Thread apontando para a função
        # Use 'args' em formato de tupla para passar os parâmetros
        thread = threading.Thread(target=funcao_da_thread, args=(shared_mem, shared_lock))
        lista_threads.append(thread)
        thread.start() # Inicia a execução da thread

    # Aguardando todas as threads terminarem antes de avançar o código principal
    for t in lista_threads:
        t.join()


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

        # cria uma memoria compartilhada entre todos os processos
        shared_mem = manager.dict({'maior': 0})
        # cria um objeto a ser compartilhado que dá o lock
        shared_lock = manager.Lock()
        
        # Inicia um subprocesso em cada nucleo fisico
        lista_procs = []
        for core_id in range(fisicos):
            proc = Process(target=funcao_do_processo, args=(core_id, shared_mem, shared_lock))
            proc.start()
            lista_procs.append(proc)

        # Aguardando todos os processos terminarem antes de avançar o código principal
        for proc in lista_procs:
            proc.join()

        print("\nACABOU TUDO")
        print('Maior numero: ', shared_mem)
