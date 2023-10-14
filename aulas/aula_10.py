import threading

def imprimir_numeros():
    for i in range(1, 6):
        print(i)

thread = threading.Thread(target=imprimir_numeros)
thread.start()
