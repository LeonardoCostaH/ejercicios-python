"""Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y 
devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor."""

import pandas as pd

class NotasAlumnos:
    def __init__(self):
        dic_notas = {}
    def informar_notas(self):
        while True:
            alumno = input("informe un alumno: (o 'exit' para salir) \n")
            if alumno == "exit":
                break
            else:
                nota = float(input(f"Cuál es la nota de {alumno}?\n"))
                self.dic_notas[alumno] = nota
    def mostrar_notas(self):
        serie = pd.Series(self.dic_notas)
        return serie
    def aprobados(self):
        self.mostrar_notas()[mostrar_notas >= 5].sort_values(ascending=False)
        return nota_ord

nota = NotasAlumnos()
nota.informar_notas()
print(nota.mostrar_notas())
print(nota.aprobados())
