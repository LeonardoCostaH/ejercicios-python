"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

palabra = input("Informe una palabra que sé un palíndromo")
pali = [i for i in palabra]
cont = len(pali)
reve_pali = [i for i in pali.__reversed__()]
if pali == reve_pali:
    print(f"La palabra {palabra} es un palíndromo.")
else:
    print(f"La palabra {palabra} no es un palíndromo.")
