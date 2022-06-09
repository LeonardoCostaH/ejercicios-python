"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def factorial(n):
    fac = 1
    for i in range(1,n):
        fac += (i*fac)
    return fac
print(factorial(1))