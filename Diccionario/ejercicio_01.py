"""Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una
divisa y muestre su símbolo o un mensaje de aviso si la divisa no
está en el diccionario."""

moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
while True:
    cual_moneda = input("Cual es la moneda que deseas que muestre el símbolo? \n")
    cual_moneda = cual_moneda.capitalize()
    if cual_moneda in moneda:
        print(moneda[cual_moneda])
    else:
        print(f"la moneda que eligista no está en el diccionario!")
        continue