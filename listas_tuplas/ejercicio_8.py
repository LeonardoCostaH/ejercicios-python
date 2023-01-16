"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

while True:
    palabra = input("escriba acá una palabra: \n")
    palabra_lista = [i for i in palabra]
    palabra_invertida = list(palabra_lista.__reversed__())
    if palabra_lista == palabra_invertida:
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")
