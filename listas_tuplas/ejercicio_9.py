"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de
veces que contiene cada vocal."""


palabra = input("escriba una palabra: \n")
vocal = ["a","e","i","o","u"]
for i in vocal:
    c_vocal = palabra.count(i)
    print(f"En la palabra {palabra} aparece {c_vocal} veces la vocal {i}")