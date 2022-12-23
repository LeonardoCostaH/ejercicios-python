"""Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

numeros_loteria = []
contador = 0
while contador < 5:
    numeros_ganadores = input("Cuales son los numeros ganadores de la lotería primitiva? \n")
    numeros_loteria.append(numeros_ganadores)
    contador += 1
numeros_loteria.sort()
print(numeros_loteria)

