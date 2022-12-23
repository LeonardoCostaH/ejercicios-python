"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla."""


asignaturas = []
while True:
    asignatura = input("escriba una asignatura: ")
    asignaturas.append(asignatura)
    for i in asignaturas:
        print(i)
