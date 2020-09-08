class Circulo:

    _pi = 3.1416 # variable de clase, no le pertenece a los objetos.
    # Una convencion para indicar que es una constante, es añadir un guion. Python no tiene constantes

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * Circulo._pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

# print(circulo_uno.radio)
# print(circulo_dos.radio)
# print(circulo_uno.pi)
# print(circulo_dos.pi)

print(circulo_uno.__dict__) # nos va a mostrar las variables del objeto

print(circulo_uno.area())
