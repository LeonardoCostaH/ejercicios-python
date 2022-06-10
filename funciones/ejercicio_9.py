"""Escribir una función que calcule el máximo común divisor de dos números
y otra que calcule el mínimo común múltiplo."""

def mcd(n1,n2):
    resultado_mcd = 0
    for i in range(1,n1,-1):
        if i % n1 == 0 and i % n2 == 0:
            resultado_mdc = i
            break
    return resultado_mdc

print(mcd(9,27))
