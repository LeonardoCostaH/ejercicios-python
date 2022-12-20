"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectágulo como el de más abajo.
"""
while True:
    entero = input("informe un número entero: ")
    if not entero.isdigit():
        print("ese no es un numero entero.")
        continue
    else:
        entero = int(entero)
        for i in range(1,entero+1,2):
            for j in range(i,0,-2):
                print(j,end=" ")
            print()

