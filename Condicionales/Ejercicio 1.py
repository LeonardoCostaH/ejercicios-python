"""
escribir un programa que pregunte al usuario su edad y muestre por pantalla si
es mayor de edad o no
"""

edad = input("Cuantos años tienes? ")
if not edad.isdigit():
    print("valor errado")
else:
    edad = int(edad)
    if edad <= 18:
        print("sos menor de edad!")
    else:
        print("sos mayor")