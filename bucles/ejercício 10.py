"""
escribir un programa que pida al usuario un número entero y muestre por pantalla si es
un número primo o no.
"""
while True:
    entero = input("escriba un numero entero: ")
    if not entero.isdigit():
        print(f"{entero} no es un numero entero.")
    else:
        entero = int(entero)
        for i in range(2,entero):
            if entero % i == 0:
                print(f"{entero} no es un numero primo.")
                break
            elif i == entero-1:
                if not entero % i == 0:
                    print(f"{entero} es un numero primo")
