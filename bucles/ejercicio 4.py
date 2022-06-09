"""
escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por coma.
"""
numero_entero = input("informe un número entero positivo: ")
if not numero_entero.isdigit():
    print("número inválido.")
else:
    numero_entero = int(numero_entero)
    for i in range(numero_entero,0,-1):
        print(f"{i}",end=",")