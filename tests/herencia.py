class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal): # clase padre
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino está cazando")

    # un metodo privado no puede heredarse

class Gato(Felino):
    pass

class Jaguar(Felino):
    pass


gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)
print(jaguar.terrestre)
