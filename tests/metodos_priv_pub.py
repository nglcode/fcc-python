class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) # __password es un atributo privado
        self.email = email

    def __generar_password(self, password): # Con esto convertimos el metodo en privado
        return password.upper()

    def get_password(self):
        return self.__password # desde aqui si podemos acceder al atributo privado password

eduardo = Usuario('eduardo', 'abc123', 'eduardo@mail.com')
print(eduardo.username)
# print(eduardo.password)
print(eduardo.get_password())
print(eduardo.email)
