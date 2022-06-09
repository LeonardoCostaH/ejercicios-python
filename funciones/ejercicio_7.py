"""
Escribir una función que reciba una muestra de números en una
lista y devuelva otra lista con sus cuadrados.
"""

def lista_cuadrados(*args):
    lista = [i**2 for i in args]
    return lista
print(lista_cuadrados(1,2,3,4,5,6,7,8,9))
