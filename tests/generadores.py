# Generadores: crear objetos sin necesidad de almacenarlos en memoria, como enumerate, range, etc.
'''
def return_valores():
    print("Hola Mundo 1")
    return True
    # True -> Termina la función y regresa ese valor. Todo lo que va después no lo toma en cuenta.
    print("Hola Mundo 2")
    print("Hola Mundo 3")
'''

def generador(*args):
    for valor in args:
        yield valor * 10, True # toma el valor y lo regresa para su posterior iteración. No funcionaría con el return ya que solo regresa 1 valor.

for valor_uno, valor_dos in generador(1,2,3,4,5,6,7,8,9):
    print(valor_uno, valor_dos)
