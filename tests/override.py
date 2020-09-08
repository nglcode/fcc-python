class Animal:
    @property
    def terrestre(self):
        return True

class Mascota:

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Felino(Animal): # clase padre
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino está cazando")


class Gato(Felino, Mascota):

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)  # para que funcione el de mascota, sino se crea solo el nombre en Gato y nunca llega a crearse en la superclase
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self): # este metodo sobreescribe al de la superclase.
        Mascota.mostrar_nombre(self) # con esto llamamos especificamente al metodo de la clase padre
        print("El nombre del gato es: {}".format(self.nombre))

gato = Gato('Tigro')
# gato.nombre = 'Tigro'
gato.mostrar_nombre()
