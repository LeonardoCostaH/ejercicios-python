"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducito.
*
**
***
****
"""

entero = input("escriba un numero entero: ")
if not entero.isdigit():
    print("Ese no es un numero entero! ")
else:
    entero = int(entero)
    for i in range(entero+1):
        print(i*"*")