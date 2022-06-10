"""Escribir una función que calcule el máximo común divisor de dos números
y otra que calcule el mínimo común múltiplo."""

def mcd(n1,n2):
    rest = 0
    while (n1 > 0):
        rest = n1
        n1 = n2 % n1
        n2 = rest
    return n2
resultado = mcd(9,27)
print(resultado)

def mcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while (greater % n1 != 0) or (greater % n2 != 0):
        greater += 1
    return greater

resultado = mcm(9,27)
print(resultado)