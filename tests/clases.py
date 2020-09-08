class Lapiz:

    def __init__(self, color = 'Amarillo', contiene_borrador = False, usa_grafito = False): # Constructor
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print("Lapiz dibujando")

    def borrar(self):
        if self.puede_borrar():
            print("Lapiz borrando")
        else:
            print("No es posible borrar")

    def puede_borrar(self):
        return self.contiene_borrador


# lapiz_generico = Lapiz("Verde", True, True)
lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.borrar()
