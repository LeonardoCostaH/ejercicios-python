"""
los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
nombre = input("informe su nombre.")
sexo = input("informe se seu sexo é (M)asculino o (F)eminino.")
sexo = sexo.lower()
nombre = nombre.lower()
if sexo == "m":
    if nombre[0] < "m":
        print("grupo A")
    else:
        print("grupo B")
else:
    if sexo == "f":
        if nombre[0] > "n":
            print("grupo A")
        else:
            print("grupo B")