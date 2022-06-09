"""
escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números ímpares desde 1 hasta ese número separados por comas.
"""
numero_entero = input("informe um número inteiro positivo: ")
if not numero_entero.isdigit():
    print("o número informado não é inteiro positivo")
else:
    numero_entero = int(numero_entero)
    i = 1
    while i <= numero_entero:
        if not i % 2 == 0:
            print(f"{i}",end=",")
        i+=1