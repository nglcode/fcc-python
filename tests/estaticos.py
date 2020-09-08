class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self): # Metodos de instancia (tiene la palabra self), es decir, lo puede llamar un objeto
        return self.radio * self.radio * self.pi()

    @staticmethod
    def pi(): # Metodos estáticos (NO tiene la palabra self), le pertenecen a la clase y no a la instancia
        return 3.1416

print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())
