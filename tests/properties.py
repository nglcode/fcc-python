class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) # __password es un atributo privado
        self.email = email

    def __generar_password(self, password): # Con esto convertimos el metodo en privado
        return password.upper()

    @property
    def password(self):
        return self.__password # con esto podemos retornar el atributo privado

    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)

eduardo = Usuario('eduardo', 'abc123', 'eduardo@mail.com')
print(eduardo.password)
eduardo.password = "XYZ789"
print(eduardo.password)
