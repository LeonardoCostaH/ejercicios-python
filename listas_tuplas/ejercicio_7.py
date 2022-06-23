"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""

def lista_alfabeto():
    alfabeto = [chr(i) for i in range(ord("a"),ord("z")+1)]
    return alfabeto

for i in lista_alfabeto():
    if ord(i) % 3 == 0:
        continue
    else:
        print(i)