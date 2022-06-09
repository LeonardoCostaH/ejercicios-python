"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectágulo como el de más abajo.
"""
numero_entero = int(input("informe un número entero: "))
for i in range(1, numero_entero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")