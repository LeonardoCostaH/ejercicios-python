"""
escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

inversion = input("informe un valor para invertir: ")
interes = float(input("informe el interés anual: "))
anos = input("informa cuantos años dura la inversión: ")
if not inversion.isdigit() or not anos.isdigit():
    print("valor informado errado")
else:
    inversion = int(inversion)
    anos = int(anos)
    i = 1
    for i in range(anos):
        inversion = inversion + inversion*interes
        print(f"el capital obtenido en el año {i} fue de {inversion}")

