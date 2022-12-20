"""
escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
"""

for i in range(1,11):
    tabla = [j*i for j in range(1,11)]
    print(tabla)