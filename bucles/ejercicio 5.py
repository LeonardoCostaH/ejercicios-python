"""
escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
while True:
    inversion = int(input("Cuanto queres invertir? "))
    interes = int(input("Cual sería el interés anual? "))
    interes = interes * 1.01
    ano = int(input("por cuantos años querés invertir? "))
    for i in range(1,ano+1):
        inversion_anual = ((i*12) * inversion) * interes
        print(f"tu capital obtenido en el {i}º año de inversión fue {inversion_anual}")