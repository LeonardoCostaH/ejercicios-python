"""
escribir un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5
y si es mayor de 18 años, 10.
"""

edad = input("Cual es tu edad? ")
if not edad.isdigit():
    print("valor inválido.")
else:
    edad = int(edad)
    if edad < 4:
        print("PUEDE ENTRAR GRATIS.")
    elif edad < 18:
        print("tienes que pagar 5,00 ")
    else:
        print("tienes que pagar 10,00 ")