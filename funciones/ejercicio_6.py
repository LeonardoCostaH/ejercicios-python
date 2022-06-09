"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

def media_numeros(*args):
    lista = list(args)
    media = lista.__len__()
    suma = sum(lista)
    return suma / media
print(media_numeros(1,2,3,4,5))