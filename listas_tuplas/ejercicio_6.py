"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el usuario tiene que repetir."""


asignaturas = []
notas = []
while True:
    asignatura = input("almacene aquí tus asignaturas o 'salir' para terminar: \n ")
    if asignatura != "salir":
        nota = int(input(f"informe cual es tu nota en {asignatura}: \n"))
        if nota < 7:
            asignaturas.append(asignatura)
            notas.append(nota)
        else:
            continue
    else:
        for i, j in enumerate(asignaturas):
            print(f"tenes que repetir en {j} ya que sacaste un {notas[i]}")
        break



#
# lista_asignaturas = []
# lista_notas = []
# lista_mista = []
#
# while True:
#     asignatura = input(f"almacente aquí tus asignaturas o 'x' para terminar: \n")
#     if asignatura == "x":
#         lista_mista = zip(lista_asignaturas,lista_notas)
#         break
#     else:
#         lista_asignaturas.append(asignatura)
#         nota = int(input(f"Cual es tu nota en {asignatura}: \n"))
#         lista_notas.append(nota)
# for i in lista_mista:
#     if i[1] >= 7:
#         continue
#     else:
#         print(f"tienes que repetir en {i[0]}")