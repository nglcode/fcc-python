def decorador(is_valid = True): # valor por defecto

    def _decorador(func):
        def before_action():
            print("Inicia funcion")

        def after_action():
            print("Finaliza funcion")

        def nueva_funcion(*args, **kwargs): # n cantidad de argumentos
            if is_valid:
                before_action()

            resultado = func(*args, **kwargs)

            after_action()
            return resultado

        return nueva_funcion

    return _decorador

@decorador()
def saluda():
    print("Hola mundo")

@decorador()
def suma(num_uno, num_dos):
    return num_uno + num_dos

saluda()

res = suma(80, 17)
print(res)
