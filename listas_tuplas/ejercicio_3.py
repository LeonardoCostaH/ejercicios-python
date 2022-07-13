"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
por el usuario."""


asignaturas = []
notas = []
contador = 0

while True:
    asignatura = input("Cual asignatura quieres almacenar?\n")
    if asignatura == "salir":
        break
    asignaturas.append(asignatura)
    nota = input(f"Cual nota has sacado en {asignatura}\n")
    notas.append(nota)
    print(f"en {asignaturas[contador]} has sacado {notas[contador]}")
    contador+=1
for n, i in enumerate(asignaturas):
    print(f"En {i} has sacado {notas[n]}")