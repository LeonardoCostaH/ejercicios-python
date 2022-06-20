"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla."""


def asignaturas_curso(asignatura,lista):
    lista.append(asignatura)
    return asignatura

 
 
if __name__ == "__main__":
        
    lista = []
    while True:
        poner_asignatura = input(f"escriba tus asignaturas para almacenarlas: \n")
        asignaturas_curso(poner_asignatura,lista)
        print(lista)