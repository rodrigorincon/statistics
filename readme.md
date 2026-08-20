# Anotações sobre o curso de estatística

Cada pasta contém um módulo do curso, que aborda estatística descritiva e inferêncial, probabilidade básica, análise combinatória, transformação de dados, regressões e exercícios em python. Cada pasta tem uma série de arquivos .md com as anotações do conteúdo, além de pasta com imagens ilustrativas para ajudar no entendimento e uma pasta de exercícios python quando fizer sentido.

Os textos aqui não são aulas ou apostilas, apenas minhas anotações enquanto estudava o assunto, podendo ser confuso para outros.

# Conteúdo

1. Estatística descritiva
2. Análise exploratória de dados
3. Probabilidade, análise combinatória e distribuições
4. Estatística inferencial
5. Testes de hipóteses paramétricos e não paramétricos
6. Tamanho do efeito
7. Correlações e transformações de dados
8. Regressão linear e mínimos quadrados
9. Regressão logística e gradiente descendente
10. Séries temporais
11. Dicas de apresentação e como apresentar gráficos

# Exercícios em python

Para rodar os códigos, pode-se rodar diretamente no terminar via `python3 nome-programa.py` ou através do Anaconda caso possua ambientes específicos para cada projeto. Para os notebooks presente, pode abrir pelo Jupyter Notebook.

## Como rodar Anaconda e Jupyter

Para rodar o Anaconda e o Jupyter Lab para ter acesso aos notebooks e rodar os códigos em um ambiente de teste, use os seguintes comandos:

Para rodar o Anaconda:

```
anaconda-navigator
```

Para rordar o Jupyer Lab:

```
jupyter lab
```

### Instalação do Anaconda e Jupyter Lab

Para instalar o Anaconda, siga os passos abaixo:

1: Rode `curl -O https://repo.anaconda.com/archive/Anaconda3-2026.07-1-Linux-x86_64.sh`

2: Rode `bash ~/Anaconda3-2026.07-1-Linux-x86_64.sh`

3: Aperte enter e yes para continuar a instalação. Quando pedir para escolher a pasta onde o Anaconda ficará instalado, digite o caminho que deseja (uma opção é /home/<USER>/.anaconda3).

4: Quando perguntar se quer iniciar o Anaconda sempre que iniciar uma nova instância do terminal, escolha "yes" caso queira evitar trabalho de lembrar de iniciá-lo sempre e caso vá usar com frequência.

Para instalar o Jupyter, siga os passos abaixo:

`pip install jupyterlab` ou `conda install -c conda-forge jupyterlab` 