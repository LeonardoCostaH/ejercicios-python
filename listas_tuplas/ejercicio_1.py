"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla."""


lista = []
while True:
    asignatura = input(f"Cual asignatura quieres almacenar?\n")
    lista.append(asignatura)
    print(lista)