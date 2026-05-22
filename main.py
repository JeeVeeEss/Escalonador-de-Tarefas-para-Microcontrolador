# Fila de Prioridade. Gerenciador de Tarefas em fila
# first in, First out.

from collections import deque
from random import randint

elementos = ["Controle de PWM", "Watchdog Timer", "Leitura de ADC", "Log de Dados", "Protocolo de UART"]

Gerenciador = deque()
Log = [[], []]


'''
for i in range(1, 6):
    Gerenciador.append(randint(1, 1000))
    print(f"- Elemento Adicionado {i}, valor do elemento: {Gerenciador[i-1]}")
'''
def inicializar():
    print("Tarefas: ")
    for i in range(len(elementos)):
        Gerenciador.append(elementos[i])
        Log[0].append(Gerenciador[i])
        print(f" - - {i}, {Gerenciador[i]}")

    
    

if __name__ == "__main__":
    inicializar()



