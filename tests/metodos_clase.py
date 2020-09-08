class Animal:
    volador = True

class Cocodrilo(Animal):

    def __init__(self,nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):  # la ventaja de usar metodos de clase, es que pueden acceder a los atributos/metodos de la clase y de la superclase
        cls.volador = False
        return Cocodrilo(nombre)

cocodrilo = Cocodrilo.new('Coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)
