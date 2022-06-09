"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducito.
*
**
***
****
"""

numero_entero = int(input("informe um número inteiro: "))
arbol = "*"
for i in range(numero_entero):
    print(arbol * i)


