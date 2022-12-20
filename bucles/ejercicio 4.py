"""
escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por coma.
"""
while True:
    entero = input("escriba un numero entero: ")
    if not entero.isdigit():
        print("por favor, el numero tiene que ser un entero! ")
    else:
        entero = int(entero)
        # for i in range(entero,-1,-1):
        #     print(i,end=",")

        regresivo = [i for i in range(entero,-1,-1)]
        print(regresivo)