nombre = input("Cual es tu nombre? \n")
altura = float(input("Cual es tu altura? \n"))
print(altura)
peso = float(input("Cual es tu peso? \n"))
print(peso)
imc = peso / altura ** 2
print(f"{nombre} tiene {altura} de altura, pesa {peso}, y su IMC es de {imc:.2f}")