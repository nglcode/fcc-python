'''def suma(valor_uno, valor_dos):
    return valor_uno + valor_dos
'''

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos

resultado = mi_funcion(10,20)
print(resultado)

# lambda + argumentos + accion a ejecutar (no es necesario indicar return)
formato = lambda sentencia : '¿{}?'.format(sentencia)

resulto = formato('Puedes hacer esto una pregunta')
print(resulto)

# si no regresan nada, al menos deben ejecutar una accion
no_resultado = lambda : print('Lambdas')
res = no_resultado()
print(res)
