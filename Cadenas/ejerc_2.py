"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después 
muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras 
minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre
 y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas
 y minúsculas como quiera."""

def nombre_3(nombre_completo):
    nombre_completo = input("Cuál es tu nombre completo? ")
    repet = 3

    for i in repet:
        if i == 1:
            return upper(nombre_completo)
        elif i == 