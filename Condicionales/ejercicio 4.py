"""
escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
"""

numero_entero = input("escriba un número entero: ")
if not numero_entero.isdigit():
    print("valor invalido")
else:
    numero_entero = int(numero_entero)
    if numero_entero % 2 == 0:
        print("número par")
    else:
        print("número ímpar")