"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
por el usuario."""
import ejercicio_1
lista_asignaturas = []
lista_notas = []
lista_mista = []
def asignaturas_nota(nota,lista):
    lista.append(nota)
    return nota

def mostra_nota(lista_mista, nota_maxima=0):
    if nota_maxima != 0:
        for asignatura, nota in lista_mista:
            if nota <= nota_maxima:
                print(f"La nota en {asignatura} es {nota}")
    else:
        for asignatura, nota in lista_mista:
            print(f"La nota en {asignatura} es {nota}")
if __name__ == "__main__":
    while True:
        cual_asignatura = input(f"escriba tus asignaturas para almacenarlas: \n")
        if cual_asignatura == "x":
            lista_mista = zip(lista_asignaturas,lista_notas)
            mostra_nota(lista_mista)
            break
        else:
            cual_nota = input(f"Cual es tu nota en {cual_asignatura}: \n")
            ejercicio_1.asignaturas_curso(cual_asignatura,lista_asignaturas)
            asignaturas_nota(cual_nota,lista_notas)
            print(lista_asignaturas,lista_notas)