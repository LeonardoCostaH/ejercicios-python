"""
para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 mensuales. Escribir un programa que pregunte al
usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
que tributar o no.
"""

edad = input("escriba su edad: ")
ingreso = input("escriba sus ingresos: ")
if not edad.isdigit() or not ingreso.isdigit():
    print("valor incorrecto.")
else:
    edad = int(edad)
    ingreso = int(ingreso)
    if ingreso < 1000 or edad < 16:
        print("no es necesario tributar")
    else:
        print("es necesario tributar")