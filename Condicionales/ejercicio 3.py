"""
escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

numero1 = input("informe un número: ")
numero2 = input("informe otro número: ")
if not numero1.isdigit() and not numero2.isdigit():
    print("no fue informado un numero")
else:
    numero2 = int(numero2)
    numero1 = int(numero1)
    division = numero1 / numero2
    if division == 0:
        print("error")
    else:
        print(f"{division}")