"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista."""

import ejercicio_1

def mostrar_lista(lista):
    for i in lista:
        print(f"Yo estudio {i}")
nueva_lista = []
while True:
    ejercicio_1.asignaturas_curso(nueva_lista)
    mostrar_lista(nueva_lista)
