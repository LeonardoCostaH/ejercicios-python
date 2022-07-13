"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista."""


lista = []
contador = 0
while True:
    asignatura = input("Cual asignatura quieres almacenar?\n")
    lista.append(asignatura)
    print(f"Yo estudio {lista[contador]}")
    contador += 1