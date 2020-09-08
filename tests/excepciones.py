# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
#
# print("Fin del script")


try:
    lista = [1,2]
    print(lista[1])
except ZeroDivisionError:
    print("No se puede dividir por cero")
except IndexError:
    print("No es posible obtener ese valor")
finally:
    print("Fin del try-except")

print("Fin del script")
