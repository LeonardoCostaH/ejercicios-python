"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

import ejercicio_1
import ejercicio_3

lista_asignaturas = []
lista_notas = []
lista_mista = []



while True:
    asignaturas = input(f"almacente aquí tus asignaturas: \n")
    if asignaturas == "x":
        lista_mista = zip(lista_asignaturas,lista_notas)
        ejercicio_3.mostra_nota(lista_mista,7)
        break
    else:
        ejercicio_1.asignaturas_curso(asignaturas, lista_asignaturas)
        notas = int(input(f"Cual es tu nota en {asignaturas}: \n"))
        ejercicio_3.cual_nota(notas,lista_notas)
        print(asignaturas,notas)
