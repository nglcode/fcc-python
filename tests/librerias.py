import random
import datetime
import sys
import time

#valor = random.randint(0,10) #ambos inclusive
lista = [True, "Strings", 23, False]

# valor = random.choice(lista)
# print(valor)

# print(lista)
# random.shuffle(lista)
# print(lista)

# print(datetime.datetime.now())

for i in range(100):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i) # imprime en consola. i se va a imprimir en la misma posicion siempre.
    sys.stdout.flush()
