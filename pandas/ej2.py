"""Escribir una función que reciba un diccionario con las notas de los alumno de un curso y 
devuelva una serie con la nota mínima, la máxima, media y la desviación típica."""

import pandas as pd

class DiccionarioNotas:
    def __init__(self):
        self.notas_alumnos = {}
    def informar_notas(self):
        while True:
            alumno = input("Cual alumno va a informar la nota? (o si desea terminar digite 'salir')\n")
            if alumno == "salir":
                break
            else:
                nota = float(input("Cual es la nota del alumno informado?\n"))
                self.notas_alumnos[alumno] = nota
    def serie_notas(self):
        convirte_nota = pd.Series(self.notas_alumnos)
        return convirte_nota
    def informe_datos(self):
        estadisticas = self.serie_notas().describe()
        return estadisticas
    
            
dic_nota = DiccionarioNotas()
dic_nota.informar_notas()
print(dic_nota.serie_notas())
print(dic_nota.informe_datos())