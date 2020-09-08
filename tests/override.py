class Animal:
    @property
    def terrestre(self):
        return True

class Mascota:
    nombre = ''

    def mostrar_nombre(self):
        print(self.nombre)

class Felino(Animal): # clase padre
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino está cazando")


class Gato(Felino, Mascota):
    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self): # este metodo sobreescribe al de la superclase. 
        print("El nombre del gato es: {}".format(self.nombre))

gato = Gato()
gato.nombre = 'Tigro'
gato.mostrar_nombre()
