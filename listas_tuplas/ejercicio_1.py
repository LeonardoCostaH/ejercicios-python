"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla."""


def asignaturas_curso(lista):
    poner_asignatura = input(f"escriba tus asignaturas para almacenarlas: \n")
    lista.append(poner_asignatura)
    print(lista)
    
    
lista = []
while True:
    asignaturas_curso(lista)