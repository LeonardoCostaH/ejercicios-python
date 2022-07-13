"""Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

numeros_loteria = []

n = 0
while n < 5:
    n+=1
    numero = input(f"Cuales son los numeros ganadores de la lotería? \n")
    numeros_loteria.append(numero)
else:
    numeros_loteria.sort()
    print(str(numeros_loteria))