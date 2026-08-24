import os
import threading
import multiprocessing
import psutil
import time

# cria diversos processos e threads dentro desses processos
# especifica em qual processador quer que o processo rode

def funcao_da_thread(nome, tempo):
    print(f"{nome} iniciada.")
    time.sleep(tempo)
    print(f"{nome} finalizada.")

def funcao_do_processo(core_id):
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
        thread = threading.Thread(target=funcao_da_thread, args=(nome_thread, 10))
        lista_threads.append(thread)
        thread.start() # Inicia a execução da thread

    # Aguardando todas as threads terminarem antes de avançar o código principal
    for t in lista_threads:
        t.join()

    print(f"----- Processo FINALIZADO no núcleo: {p.cpu_affinity()}")


# isso é obrigatoio quando usa Process
if __name__ == "__main__":
    # Apenas o numero de núcleos físicos do processador
    fisicos = psutil.cpu_count(logical=False)
    # Todos o numero de núcleos lógicos (com hyper-threading)
    logicos = psutil.cpu_count(logical=True)
    print(f"Núcleos físicos: {fisicos}")
    print(f"Núcleos lógicos: {logicos}")

    # Inicia um subprocesso em cada nucleo fisico
    lista_procs = []
    for core_id in range(fisicos):
        proc = multiprocessing.Process(target=funcao_do_processo, args=(core_id,))
        proc.start()
        lista_procs.append(proc)

    # Aguardando todos os processos terminarem antes de avançar o código principal
    for proc in lista_procs:
        proc.join()

    print("\nACABOU TUDO")
