"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""
import math
def area_circulo(rayo):
    #rayo = int(input("escriba el rayo del circulo que quieres saber el area:\n "))
    area = math.pi * rayo**2
    return area

def volumen_cilindro(r,h):
    #r = int(input("escriba el rayo del cilindro que quieres saber el volumen del cilindro:\n "))
    #h = int(input("escriba la altura del numero que quieres saber el volumen del cilindro:\n "))
    volumen = area_circulo(r) * h
    return volumen

print(volumen_cilindro(10,30))


