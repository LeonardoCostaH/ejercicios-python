"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

def media_numeros(*args):
    lista = list(args)
    media = lista.__len__()
    suma = 0
    for l in lista:
        suma += l
    return suma / media
print(media_numeros(1,2,3,4,5))